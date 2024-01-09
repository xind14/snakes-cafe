# Lab: Class 1 - Intro to Python

## Author: Xin Deng, chatGPT

## Links and Resources

- chatGPT on how to do the stretch goals 

## Overview - snakes-cafe

Today you’ll begin working on a command line utility that will mimic the functionality of a point of sale restaurant system using your basic Python tools and understanding of the basics of the language.

## Feature Tasks and Requirements

- When run, the program should print an intro message and the menu for the restaurant.
- The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
- The program should prompt the user for an order.
- When a user enters an item, the program should print an acknowledgment of their input.
- The program should tell the user how to exit.
- The program’s content should match included sample exactly. Actually, there’s one tiny spot that should be different - see if you can spot it.
- The `>` character represents user input line and should be printed out with a trailing space.

```bash
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
> 
```

## Entering an order
```bash
***********************************
** What would you like to order? **
***********************************
> Cake

** 1 order of Cake has been added to your meal **

> Cake

** 2 orders of Cake have been added to your meal **
```

## Exiting
```bash
> quit
```

## Stretch Goals
- Print out a summary of the complete order.
- Only allow ordering items on the menu.
- Allow ordering items not on the menu but give a custom reply.


## Setup

### Creating Project

```bash
mkdir example-lab
cd example-lab
touch README.md
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

#### Mac/Linux

```bash
source .venv/bin/activate
```

### Git

#### On Local System

#### Initialize local Git repository

```bash
git init
touch .gitignore
```

Add `.venv` folder to `.gitignore`

```bash
git add .
git commit -m "first commit"
```

#### On GitHub site

- Create an EMPTY repository `example-lab` on GitHub. 
  - DO NOT initialize with README, license, or gitignore. Those will be added soon.
  - The next screen will have a "Quick Setup" section with a URL available to copy. Copy it ;)

#### On Local System (again)

```bash
git remote add origin the_url_you_copied_that_ends_with_git
git push -u origin main
```

