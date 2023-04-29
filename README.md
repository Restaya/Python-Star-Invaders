
This is a Space Invaders style game made with Pygame

You have to reach a certain score to win (25 by default), each enemy gives some points based on their hp

Controls:

W - moves forward/ előre megy

The player can only move to 1/4-th of the screen height

A - moves left

D - moves right

S - moves backwards

SPACE - shoot

You can run tests with this command inside the project folder:
coverage run -m pytest tests/ ; coverage  report

How to launch from PyCharm:

In the star_invaders/main.py run the Current File option

Pylint test command in folder:
pylint ./* --recursive=true --disable=no-member,too-many-statements,import-error,line-too-long,missing-function-docstring,missing-module-docstring,missing-class-docstring

Can't generate html for pylint, becuase it is no longer supported

Flake8 command in folder:
flake8 ./ --ignore=E501,E226,F841 --format=html --htmldir=flake-report

