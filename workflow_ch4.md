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
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
```

### Run 'makemigrations' and 'migrate'
``` sh
./manage.py makemigrations bands
./manage.py migrate
```

## Django ORM
You can do this in django shell
```sh
# Enter the django shell
./manage.py shell```
```

### .create()
``` python
from bands.models import Musician
from datetime import date

Musician.objects.create(first_name="Steve", last_name="Vai", birth=date(1960, 6, 6))

Musician.objects.create(first_name="John", last_name="Lennon", birth=date(1940, 10, 9))

Musician.objects.create(first_name="John", last_name="Bonham", birth=date(1948, 7, 31))
```

### .objects Query
``` python
Musician.objects.first()  # returns the first record
Musician.objects.last()  # returns the last record
Musician.objects.all() # returns all the records

# Common practice to store the result in a variable

result = Musician.objects.all()
steve = result[0]

```

### .filter() 
``` python
Musician.objects.filter(first_name="Steve")

# you can chain the methods together
result = Musician.objects.filter(first_name="John")

result.first()
```

### Field Lookup
Field look-ups are modifications to a query arguments expressed through double underscore (__) 
``` python
Musician.objects.filter(first_name__startswith="J")
```
Here are some common look-ups
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
Musician.objects.create(first_name="Roseanne", last_name="Barr", birth=date(1965, 7, 31))   # Is she a musician?

roseanne = Musician.objects.get(id=5)

# her birthday is actually 11/3/1952
roseanne.birth = date(1952, 11, 3)  # this only updates the object

# Have to save() to write to the database
roseanne.save()

```

### Deleting data
``` python
# I hate to classify Roseanne as a singer; remember that butchering of National Anthem?

roseanne.delete()  # Calling delete actually deletes the data in database, and not the object -- the variable roseanne still contains the values in the object

```
