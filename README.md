# EffectivePython
Repository created for the purpose of evaluating the work in the class on the subject effective programming in python

### Run lab10 Django application
```cmd
git clone ...repo link...
cd EffectivePython/lab10
python3 -m venv venv
source venv/bin/activate 
pip install django django-extensions django-mptt django-mptt-admin
python3 manage.py makemigrations app
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
To add a user log in to admin panel