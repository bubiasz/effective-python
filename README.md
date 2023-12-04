# EffectivePython
Repository created for the purpose of evaluating the work in the class on the subject effective programming in python

### Run lab10 Django application
```cmd
git clone ...repo link...
cd lab10
python3 -m venv venv
source venv/bin/activate 
pip install django django-extensions django-mptt
python3 lab10/manage.py makemigrations app
python3 lab10/manage.py migrate
python3 lab10/manage.py runserver
```