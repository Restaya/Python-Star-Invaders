Hi!

This is a Star Wars themed Space Invaders game made with the Pygame module
Ez a játék egy Star Wars kinézetű Space Invaders játék, ami Pygame modullal készült

You have to reach a score of 25 to win, each enemy has 1-3 health, if an enemy has 3 health, he grants 3 points on death
25 pontot kell elérni a győzelemhez, minden ellenfélnek 1-től 3-ig van véletlenszerű élete, és ez adja a pontot, 3 életű ellenfél 3 pontot ad halálkor

Controls:

W - moves forward/ előre megy
The player can only move to 1/4-th of the screen height
A játékos a pálya magasságának 1/4-ig tud menni

A - moves left / balra megy
D - moves right / jobbra megy
S - moves backwards / hátra megy
SPACE - shoot / lövés

You can run tests with this command inside the project folder:
coverage run -m pytest tests/ ; coverage  report

A tesztek futtathatók ezzel a parancssal a projekt mappán belül:
coverage run -m pytest tests/ ; coverage  report

How to launch from PyCharm:

In the main/main.py run the Current File option

Hogyan inditsd:

main/main.py-ban indítsd el a Current File opcióval
