from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def credits(request):
    content = "Manning DIA\nJeff"

    return HttpResponse(content, content_type="text/plain")

def about(request):
    content = '''<h1>About</h1>
    <p>Website that connects musicians, band and venues together</p>
    <p>Version: 1.0</p>'''

    return HttpResponse(content, content_type="text/html")

def version(request):
    return JsonResponse({
        'about':'Website that connects musicians, band and venues together',
        'version':'1.0.0',
        'creator':'Jeff Ballinger'
        })

def news(request):
    data = {
        'news': [
            "Riffmates now has a news page!",
            "Riffmates has its first webpage.",
        ],
    }
    return render(request, "news.html", data)

def news2(request):
    data = {
        'news': [
            "Riffmates now has a news page!",
            "Riffmates has its first webpage.",
        ],
    }
    return render(request, "news2.html", data)

def news3(request):
    data = {
        'news': [
            "Riffmates now has a news page!",
            "Riffmates has its first webpage.",
        ],
    }
    return render(request, "news3.html", data)

def news_bootstrap(request):
    import datetime
    d = datetime.date
    data = {
        'news': [
            (d(2024, 9, 28), "Latest news"),
            (d(2024, 9, 25), "Yesterday's news"),
            (d(2023, 9, 28), "Last year's news"),
        ]
    }
    return render(request, "news_bootstrap.html", data)

def news_advanced(request):
    import datetime
    d = datetime.date
    dd = datetime.datetime.now()
    data = {
        'news': [
            (d(2024, 9, 28), "Latest news"),
            (d(2024, 9, 25), "Yesterday's news"),
            (d(2023, 9, 28), "Last year's news"),
        ],
        'today': dd
    }
    return render(request, "news_adv.html", data)
