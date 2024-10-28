## Ch4 is about ORM models

### Start a new app bands
``` sh
./manage.py startapp bands
```

### Add to settings.py
``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'bands',
]
```

### Define the first ORM models
``` python
# create the first table called Musician
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()

    # overwrite the base class to display a more meaningful object name
    def __str__(self):
        return f"Musician (id={self.id}, last_name={self.last_name})"

```

### Run 'makemigrations' and 'migrate'
``` sh
./manage.py makemigrations bands
./manage.py migrate
```

## Django ORM via CLI
You can interact with the database using the django shell
```sh
# Enter the django shell
./manage.py shell```
```

### .create()
``` python
# import required libraries
from bands.models import Musician
from datetime import date

# insert some data
Musician.objects.create(first_name="Steve", last_name="Vai", birth=date(1960, 6, 6))

Musician.objects.create(first_name="John", last_name="Lennon", birth=date(1940, 10, 9))

Musician.objects.create(first_name="John", last_name="Bonham", birth=date(1948, 7, 31))
```

### .objects Query
``` python
Musician.objects.all() # returns all the records

# Common practice to store the result in a variable
result = Musician.objects.all()
steve = result[0]

# other objects query
Musician.objects.first()  # returns the first record in the table
Musician.objects.last()  # returns the last record
```

### .filter()
This is like using the where clause in SQL
``` python
Musician.objects.filter(first_name="Steve")

# you can chain the methods together
result = Musician.objects.filter(first_name="John").first()
# or
result.first()
```


### Field Lookup
Field look-ups are modifications to a query arguments filter method.  For example to find first_name starting with "J".  
``` python
Musician.objects.filter(first_name__startswith="J")
```
Starting with double underscore (__) and the description of modification. Here are some common look-ups
| Look-up |  Description |
| -------- | ------------ |
| __contains | 	Contains the phrase |
| __icontains | 	Same as contains, but case-insensitive |
| __date  |	Matches a date |
| __day  |	Matches a date (day of month, 1-31) (for dates) |
| __endswith  |	Ends with |
| __iendswith | 	Same as endswidth, but case-insensitive |
| __exact  |	An exact match |
| __iexact  |	Same as exact, but case-insensitive |
| __in  |	Matches one of the values |
| __isnull  |	Matches NULL values |
| __gt  |	Greater than |
| __gte  |	Greater than, or equal to |
| __hour  |	Matches an hour (for datetimes) |
| __lt  |	Less than |
| __lte  |	Less than, or equal to |
| __minute  |	Matches a minute (for datetimes) |
| __month  |	Matches a month (for dates) |
| __quarter  |	Matches a quarter of the year (1-4) (for dates) |
| __range  |	Match between |
| __regex  |	Matches a regular expression |
| __iregex  |	Same as regex, but case-insensitive |
| __second  |	Matches a second (for datetimes) |
| __startswith  |	Starts with |
| __istartswith  |	Same as startswith, but case-insensitive |
| __time  |	Matches a time (for datetimes) |
| __week  |	Matches a week number (1-53) (for dates) |
| __week_day  |	Matches a day of week (1-7) 1 is Sunday |
| __iso_week_day | 	Matches a ISO 8601 day of week (1-7) 1 is Monday |
| __year | 	Matches a year (for dates) |
| __iso_year | 	Matches an ISO 8601 year (for dates) |

### Modifying data
``` python
Musician.objects.create(first_name="Roseanne", last_name="Barr", birth=date(1955, 7, 31))   # Is she a musician?

# use .get() to instantiate an object
roseanne = Musician.objects.get(id=5)
# .get() only returns a single match, so use a unique identifier like the pk 

# use the object to manipulate data: her birthday is actually 11/3/1952; update
roseanne.birth = date(1952, 11, 3)  # this only updates the object

# Have to save() to write to the database
roseanne.save()
```

### Deleting data
``` python
# I hate to classify Roseanne as a singer; remember that butchering of National Anthem?

roseanne.delete()  # Calling delete actually deletes the data in database, but not the class instance -- the variable roseanne still contains the values in the object

```

## Django MVT - Model, View, Template
## URL based views
Django uses URL based argument to query a specific record in the DB

For example:
```python
# proj/bands/urls.py
...
urlpatterns = [
    path('musician/<int:musician_id>/', views.musician, name='musician'),
    path('musicians/', views.musicians, name='musicians'),
]

# http://localhost:8000/bands/musician/1/
```

### function based views 
``` python
# proj/bands/views.py
from django.shortcuts import render, get_object_or_404

from bands.models import Musician

# List all the musicians record
def musicians(request):
    '''View for all the records.'''   
    data = {
        all_musicians = Musician.objects.all().order_by('last_name'),
    }

    return render(request, "musicians.html", data)

# Single, specific record
# using the built in 'get_object_404'
def musician(request, musician_id):
    '''View for single record.'''
    musician = get_object_or_404(Musician, id=musician_id)

    data = {
        "musician": musician,
    }

    return render(request, "musician.html", data)

```

### Templates
```html
<!-- proj/templates/musicians.html -->
{% extends "base.html" %}

{% block title %}
    {{block.super}}: Musician Listing
{% endblock %}

{% block content %}
    <h1>Musicians</h1>
    <ul>
        {% for musician in musicians %}
            <li><a href="{% url 'musician' musician.id %}">
                {{musician.last_name}}, {{musician.first_name}}
            </a></li>
        {% empty %}
            <li> <i>No musicians in the database</i> </li>
        {% endfor %}
    </ul>
{% endblock content %}
```

```html
<!-- proj/templates/musician.html -->
{% extends "base.html" %}

{% block title %}
    {{block.super}}: Musician Details
{% endblock %}

{% block content %}
    <h1>{{musician.first_name}} {{musician.last_name}}</h1>
    <p> Was born {{musician.birth}}. </p>
{% endblock content %}
```

