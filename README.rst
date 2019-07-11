word-count
==========

A word counter

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Basic Run
--------
This application uses a Django + Docker container. In order to run it, please follow the command list bellow;

Running:
^^^^^^^^^^^^^^^^^^^^^

Build: 

docker-compose -f local.yml build

Run:

docker-compose -f local.yml run

The app will stay listening in the address:

http://0.0.0.0:8000/core/word-count/

Note that this is a development instance. The production setup is placed in the production.yml.



Testing:
^^^^^^^^^^^^^^^^^^^^^

docker-compose -f local.yml run django python manage.py test

docker-compose -f local.yml run django coverage run manage.py test

docker-compose -f local.yml run django coverage html
