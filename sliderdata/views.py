from django.shortcuts import render
from .models import Slider


def slider(request):
    sliders = Slider.objects.all()
    return render(request, 'index.html', {'sliders': sliders})


def home2(request):
    sliders = Slider.objects.all()
    return render(request, 'Home2.html', {'sliders': sliders})
