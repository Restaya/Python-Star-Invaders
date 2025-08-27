
This is a Space Invaders style game made with Pygame

You have to reach a certain score to win (25 by default), each enemy gives some points based on their health

Controls:

- Use W,A,S,D to move around, press SPACE to shoot

You can run tests with this command inside the project folder:<br>
coverage run -m pytest star_invaders/tests/ ; coverage  report <br>
python -m unittest

Install the packages using this command: pip install -r .\requirements.txt <br>
Command to start the game: python .\star_invaders\main.py

Pylint html generation command in folder:<br>
pylint star_invaders --disable=no-member,too-many-statements,import-error,line-too-long,missing-function-docstring,missing-module-docstring,missing-class-docstring  --output-format=json | pylint-json2html -o pylint.html

Flake8 command in folder:<br>
flake8 ./ --ignore=E501,E226,F841 --format=html --htmldir=flake-report

<img width="800" height="400" alt="space_invaders" src="https://github.com/user-attachments/assets/2dc83908-3ddd-4e25-b791-04183e722316" />
