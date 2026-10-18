from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from common.forms import CommentForm
from common.models import Like, Comment
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


def photo_add_view(request:HttpRequest) -> HttpResponse:
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('common:home_page')
    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)

def photo_detail_view(request: HttpRequest, pk:int) -> HttpResponse:
    photo = get_object_or_404(Photo, pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'photos/photo-details-page.html', context)

def photo_edit_view(request:HttpRequest, pk:int) -> HttpResponse:
    photo = get_object_or_404(Photo, pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)
    if form.is_valid():
        form.save()
        return redirect('photos:detail', pk=pk)
    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)

def photo_delete_view(request:HttpRequest, pk:int) -> HttpResponse:
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('common:home_page')

        
