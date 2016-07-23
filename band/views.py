#-*- coding:utf-8 -*-
from django.shortcuts import render
from band.models import Band
from band.serializer import BandSerializer
from rest_framework import generics
from band.form import DetailForm
# Create your views here.


def all_bands(request):
    if request.method == "GET":
        return render(request, 'band/all_band.html', {'form': DetailForm})
    elif request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            print(form)
            return render(request, 'band/all_band.html', {'form': DetailForm})


def band(request, band_id):
    band = Band.objects.get(pk=band_id)

    return render(request, 'band/band.html', {'band': band})


class BandDetail(generics.RetrieveUpdateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer