THIS NEEDS SOME REFACTORING TO USE THE NEW OAUTH2 MECHANISM IN CROP-R

cropr_demo
==========

Crop-R Demo Application for using the Crop-R API v3

==========
Installation
==========

1. set up virtual env
2. install requirements:
  1. pip install Django
  2. pip install requests
3. rename settings.copy to settings.py
4. follow <a href="https://www.crop-r.com/apps/cropletdeveloper/tutorial/">the tutorial</a>
5. copy `client_id` and `client_secret` to settings.py
6. run ./manage.py syncdb
7. run ./manage.py migrate
8. run ./manage.py createsuperuser
9. run ./manage.py runserver
