## Ch3 is about Templates

## Update Template directory
- 'DIRS' specifies location of templates directory
- 'APP_DIRS: True' means each App can use a templates directory

```sh
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates',], # <-- add the location of templates
        'APP_DIRS': True,  # <-- true, app directory is searched for templates dir
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...
```

## Create the view
```python
from django.shortcuts import render

def news(request):
    data = {
        'news': [
            "Riffmates now has a news page!",
            "Riffmates has its first webpage.",
        ],
    }

    return render(request, "news.html", data)

# render(request, template-file, data-to-pass)
```

## create the urls
``` python
...
path('news/', home_views.news, name='news')
...
```

### Create the html file in the templates directory
```html
<!-- riffmates_proj/templates/news.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RiffMates News</title>
</head>
<body>
    <h1>RiffMates News</h1>

    <ul>
        {% for item in news %}
        <li>{{ item }}</li>
        {%  endfor %}
    </ul>
    
</body>
</html>
```