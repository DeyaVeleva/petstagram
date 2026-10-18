from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from common.forms import CommentForm
from pets.forms import PetForm, PetDeleteForm

from pets.models import Pet


def pet_add_view(request:HttpRequest) -> HttpResponse:
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save()
        return redirect('pets:details', username='username', pet_slug=pet.slug)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context=context)

def pet_detail_view(request:HttpRequest, username:str, pet_slug:str) -> HttpResponse:
    pet = get_object_or_404(Pet, slug=pet_slug)
    comment_form = CommentForm()
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }
    return render(request, 'pets/pet-details-page.html', context)

def pet_edit_view(request:HttpRequest,  username:str, pet_slug:str) -> HttpResponse:
    pet = get_object_or_404(Pet, slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets:details', username=username, pet_slug=pet.slug)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-edit-page.html', context)

def pet_delete_view(request:HttpRequest,  username:str, pet_slug:str) -> HttpResponse:
    pet = get_object_or_404(Pet, slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('common:home_page')
    form = PetDeleteForm(initial=pet.__dict__)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-delete-page.html', context)
