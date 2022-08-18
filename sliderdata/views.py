from django.shortcuts import render
from .models import Slider


def slider(request):
    sliders = Slider.objects.all()
    return render(request, 'Home.html', {'sliders': sliders})
