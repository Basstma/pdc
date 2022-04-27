from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import re

from .models import FileObject, EmbededObject
from .forms import *


def cloud_main(request, *args, **kwargs):
    context = {
        'public_files': list(FileObject.objects.filter(owner=None)) + list(EmbededObject.objects.filter(owner=None))
    }

    if request.user.is_authenticated:
        context['private_files'] = list(
            FileObject.objects.filter(owner=User.objects.get(id=request.user.id)))
        context['private_files'] += list(
            EmbededObject.objects.filter(owner=User.objects.get(id=request.user.id)))

    return render(request, 'cloud.html', context)


def showfile(request, id: str):
    file = get_object_or_404(FileObject, id=id)
    context = {
        'file': file
    }

    return render(request, 'showfile.html', context=context)


def cloud_show_content(request, id: int):
    file = get_object_or_404(FileObject, id=id)
    context = {
        'file': file
    }

    return render(request, 'showfile.html', context=context)


def cloud_show_embedded(request, id: int):
    file = get_object_or_404(EmbededObject, id=id)
    context = {
        'file': file
    }

    return render(request, 'showembedded.html', context=context)


def cloud_download_content(request, id: int):
    file = get_object_or_404(FileObject, id=id)
    response = FileResponse(file.file)
    return response


@login_required
def cloud_add_content(request):
    if request.method == 'POST':
        new_file = FileObjectForm(request.POST, request.FILES)
        if new_file.is_valid():
            new_file.save()
            return redirect('cloudmain')
    add_file_form = FileObjectForm()
    context = {
        'form': add_file_form
    }

    return render(request, "add_content.html", context=context)


@login_required
def cloud_add_embedded_content(request):
    if request.method == 'POST':
        new_file = EmbeddedObjectForm(request.POST)
        if new_file.is_valid():
            file = new_file.save(commit=False)
            file.content = re.sub(r'(?<=width=").*?(?=[\?"])"', '100%', new_file.cleaned_data['content'])
            file.content = re.sub(r'(?<=height=").*?(?=[\?"])"', '700px', new_file.cleaned_data['content'])
            file.save()
            return redirect('cloudmain')
    add_file_form = EmbeddedObjectForm()
    context = {
        'form': add_file_form
    }

    return render(request, "add_embedded.html", context=context)


@login_required
def cloud_delete_file(request, id: int):
    file = get_object_or_404(FileObject, id=id)
    file.delete()
    return redirect('cloudmain')


@login_required
def cloud_delete_embedded(request, id: int):
    file = get_object_or_404(EmbededObject, id=id)
    file.delete()
    return redirect('cloudmain')
