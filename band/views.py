from django.shortcuts import render
from band.models import Band
# Create your views here.


def all_bands(request):
    return render(request, 'band/all_band.html')


def band(request, band_id):
    band = Band.objects.get(pk=band_id)

    return render(request, 'band/band.html', {'band': band})