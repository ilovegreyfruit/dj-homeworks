import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import os
from pathlib import Path


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = os.path.join(BASE_DIR, 'data-398-2018-08-30.csv')

    with open (path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader)
        page_number = request.GET.get('page', 1)
        paginator = Paginator(stations, 20)
        page = paginator.get_page(page_number)


    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
