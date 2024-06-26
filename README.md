# Tic Tac Toe

![](https://github.com/BaoThan/tictactoe-core/actions/workflows/test-pipeline.yml/badge.svg?branch=main)
![](https://github.com/BaoThan/tictactoe-core/actions/workflows/stylelint-pipeline.yml/badge.svg?branch=main)

A REST API for Tic Tac Toe bot, implemented using the Minimax algorithm.

---

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXZ6OXZodWo0NmV1ZGxzZWp5anFnMWJzemM3YXhpbnBwd3pkeWoxbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT3i1j9j4yMLXPDj5C/giphy.gif" />
</p>

---

#### Base URL: https://e0cb-76-21-119-158.ngrok-free.app

---

### Find best next move
POST `/best_next_move`

##### Body Form-Data Arguments:
- `player`: String (either "X" or "O") representing the player to find the best next move for.
- `board`: The string representation of the game board.

##### Example:
Example calling the API in Python:
```python
import requests

url = "https://e0cb-76-21-119-158.ngrok-free.app/best_next_move"
payload = {
    'player': 'X',
    'board': '[["X", "O", ""], ["", "O", ""], ["", "", ""]]'
}
response = requests.request("POST", url, headers={}, data=payload)
print(response.json()) # {'data': {'next_move': [2, 1]}, 'success': True}
```

---

## Development Setup

A complete guide to setup your development environment :D

#### Requirements

`python 3.10`

Make sure you also already installed `pip` and `venv` for your Python.


#### Create Virtual Environment

Start by creating your isolated Python environment with `venv`:

```bash
$ python3 -m venv .venv
```
In this case, `.venv` is the name of the directory containing your Python executable and other files. You can name it anything you want, but `.venv` is the most common name.

Next, activate your virtual environment:

```bash
$ source .venv/bin/activate
```
You can verify your virtual environment is properly activated by running `python -V` which will either have your regular path (incorrectly activated) or your virutal environment path (correctly activated).

This virtual environment will basically isolate your Python development project from your system installed Python and other Python environements. So you will have full control over your current working project and make it easier to be reproduced on another system. Make sure you activate your virtual environment every time you develop code for this project (You're good if you see `(.venv)` on your terminal or if `which python` returns the virtual environment path instead of the regular path)

To exit your virtual environment, run:

```bash
$ deactivate
```

#### Install Packages

Enter your virtual environment if you exited.

You will notice there are 2 files named `requirements-dev.txt` and `requirements.txt`. These files contain the name of the `pip` packages.

`requirements-dev.txt` contains the packages needed to enhance developer's experience. While `requirements.txt` contains the packages needed for the application to run.

Install all of these by running:

```bash
pip install -r requirements-dev.txt
pip install -r requirements.txt
```

#### Pre-commit

Inorder to make sure the codebase is clean and the style is consistent between many developers, we use a few lint tools to detect and auto-fix (if possible). These can be found in `.pre-commit-config.yaml`.

To install git hooks in your `.git` directory, run:
```
pre-commit install
```

These lint tools will be run when you commit your code and you can only successfully commit if . You can also run it without commiting: `pre-commit run --all-files`


## Run Tests

`test` directory contains all the tests needed to make sure the features are working properly. To run the tests, simple run:
```bash
python3 -m pytest .
```
