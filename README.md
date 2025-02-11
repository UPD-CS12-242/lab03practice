# CS 12 24.2 Lab Exercise 3 Practice

Without modifying `model.py` and/or `project_types.py`, create a text-based _synchronous I/O_ view (`view.py`) and a corresponding controller (`controller.py`) that allows playing of the game _Subtract-a-Square_.

Additionally, create a `main.py` that instantiates the model, view, and controller and starts the game.

## Game mechanics

Instead of searching online on how the game works, you are strongly encouraged to instead infer the rules of the game and how it is played by checking the unit tests in `test_model.py` and cross-checking the logic in `model.py`.

## Input parsing

For this exercise, you may place input parsing logic in the controller.

## I/O specification

For this exercise, you may be in charge of what exactly is printed, in what order they are printed, and when input is taken from the user as long as the game can be _sensibly_ played _(i.e., there is enough information provided to the players)_.

Ensure that the number of players taken from the user prior to instantiating the model and that **exceptions raised are handled gracefully** _(i.e., the exception must be caught with an appropriate error message shown to the user followed by proper termination of the game)_.
