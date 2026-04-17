from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Galeria

@login_required
def vista_carrusel(request):
    fotos = Galeria.objects.all().order_by('-fecha_subida')[:10]
    return render(request, 'carrusel.html', {'fotos': fotos})