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
