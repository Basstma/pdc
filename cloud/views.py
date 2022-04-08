import os

from django.shortcuts import render
from django.http import HttpResponse


def cloudmain(request, *args, **kwargs):
    p = "C:\\Users\\HarNoa\\test\\FilesToShow"
    context = {
        'files': [file for file in os.listdir(p) if not os.path.isdir(os.path.join(p, file))]
    }

    return render(request, 'cloud.html', context)
