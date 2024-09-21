# Getting Started with Django

```sh
# setup Django shortcuts - add to .bashrc or type directly to shell
complete -f -d -W "runserver createsuperuser test shell dshell migrate makemigrations loaddata dumpdata" ./manage.py
# now you can press tab for completion
```

## General Workflow
1. Create a project directory
```sh
mkdir riffmates_proj
```
2. CD into that directory
```sh
cd riffmates_proj
```
3. Activate virtual environment
```sh
python -m venv ./venv
source venv/bin/activate
```
4. Install django
```sh
pip install django
```
5. Start a project
```sh
django-admin startproject riffmates .
```
6. Create an app 
```sh
django-admin startapp home 
```
7. Register the new app to settings.py
```python
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]
...
```
8. Migrate to activate django admin
```sh
./manage.py migrate
```
9. Run the server
```sh
./manage.py runserver
```
10. Write views.py
11. map the views to urls.py 
