from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
import pyperclip

from common.forms import CommentForm, SearchForm
from common.models import Like, Comment
from photos.models import Photo

def home_page_view(request: HttpRequest) -> HttpResponse:
    photos = Photo.objects.all().order_by('-date_of_publication')
    comment_form = CommentForm()
    search_form = SearchForm(request.GET)
    context = {
        'photos': photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context)

def like_photo(request: HttpRequest, photo_id: int) -> HttpResponse:
    photo = Photo.objects.get(id= photo_id)
    liked_object= Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()
    return redirect(f"{request.META['HTTP_REFERER']}#{photo_id}")

def share_photo(request: HttpRequest, photo_pk: int) -> HttpResponse:
    photo = get_object_or_404(Photo, pk=photo_pk)
    photo_url=request.build_absolute_uri(
        resolve_url('photos:detail', pk=photo_pk)
    )
    pyperclip.copy(photo_url)
    return redirect(
        request.META.get(
            'HTTP_REFERER',
            resolve_url('common:home_page'),
        )
    )

def show_photo_details(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    likes = Like.objects.filter(to_photo=photo)
    comments = Comment.objects.filter(to_photo=photo)
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }
    return render(request, 'photos/photo-details-page.html', context)

def add_comment(request: HttpRequest, photo_id: int) -> HttpResponse:
    photo = get_object_or_404(Photo, pk=photo_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = photo
        comment.save()
    return redirect(f"{request.META['HTTP_REFERER']}#{photo_id}")