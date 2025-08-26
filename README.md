
This is a Space Invaders style game made with Pygame

You have to reach a certain score to win (25 by default), each enemy gives some points based on their hp

Controls:

- Use W,A,S,D to move around, press SPACE to shoot

You can run tests with this command inside the project folder:<br>
coverage run -m pytest tests/ ; coverage  report <br>
// CURRENLTY NOT WORKING DUE TO IMPORT ERROR//

Install the packages using this command: pip install -r .\requirements.txt
Launch the /star_invaders/main.py file to start the game

Pylint html generation command in folder:<br>
pylint star_invaders tests --disable=no-member,too-many-statements,import-error,line-too-long,missing-function-docstring,missing-module-docstring,missing-class-docstring  --output-format=json | pylint-json2html -o pylint.html

Flake8 command in folder:<br>
flake8 ./ --ignore=E501,E226,F841 --format=html --htmldir=flake-report

<img width="800" height="400" alt="space_invaders" src="https://github.com/user-attachments/assets/2dc83908-3ddd-4e25-b791-04183e722316" />
