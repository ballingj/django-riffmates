from django.shortcuts import render, get_object_or_404

from bands.models import Musician
from django.core.paginator import Paginator

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)

    data = {
        "musician": musician,
    }

    return render(request, "musician.html", data)

def musicians_no_paginations(request):
    data = {
        'musicians': Musician.objects.all().order_by('last_name')
    }

    return render(request, "musicians.html", data)

def musicians(request):
    all_musicians = Musician.objects.all().order_by('last_name')
    paginator = Paginator(all_musicians, 2) # Create a Paginator using the query, limiting two objects per page.

    page_num = request.GET.get('page', 1) # Fetch the page key from the GET dictionary, defaulting to 1 if the key does not exist.
    page_num = int(page_num)    # URLs are text, convert any value to an integer.

    if page_num < 1:    # The minimum value for the page number is 1.
        page_num = 1
    elif page_num > paginator.num_pages:  # The maximum value for the page number is the number of pages.
        page_num = paginator.num_pages

    page = paginator.page(page_num)
    
    data = {
        'musicians': page.object_list,
        'page': page,
    }

    return render(request, "musicians.html", data)

