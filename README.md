# AirBnB clone
This repository contains **Holberton School's** AirBnB clone project, which is the final project of the second trimester of **Holberton School's** curriculum.

## Table of contents
* [About](#about)
* [Resources](#resources)
* [Project requirements](#project)
* [Files](#files)
* [Usage](#usage)
* [Authors](#authors)

## About

The purpose of this project is that us students are able to apply all the knowledge we got from Holberton's higher lever proggraming track in a much bigger scope than we are used to. The project itself its divided in five parts scattered around the span of four months:
-   A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
-   A website (the front-end) that shows the final product to everybody: static and dynamic.
-   A database or files that store data (data = objects).
-   An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).

## Resources
* [Python's cmd module](https://docs.python.org/3.4/library/cmd.html)
* *Holberton's Pyhton Packages concept page*
* [Python's uuid module](https://docs.python.org/3.4/library/uuid.html)
* [Python's datetime module](https://docs.python.org/3.4/library/datetime.html)
* [Python's unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Project requirements

* Ubuntu 20.04 LTS.
* Follow the pycodestyle (version 2.7.*) documentation style guide.
* Use the unittest module for testing.

## Files

* **models:** contains all the classes used in the full project
	* **engine:** contains classes used for console working purposes
		* file_storage.py
	* amenity.py
	* base_model.py
	* city.py
	* place.py
	* review.py
	* state.py
	* user.py 
* **tests:** contains all test files
	* **test_models:** unittest for classes
		* test_amenity.py
		* test_base_model.py
		* test_city,py
		* test_file_storage.py
		* test_place.py
		* test_review.py
		* test_state.py
		* test_user.py
* console.py

## Usage
### Instalation
In order to use the AirBnB clone: first you will need to clone this repository:
```bash
git clone https://github.com/4mmZ/holbertonschool-AirBnB_clone.git
```
### The console
In order to use the console, go inside the directory and run the executable:
```bash
cd holbertonschool-AirBnB_clone
./console.py
```
#### How the console works
 * The console will display a prompt, and then wait for a command.
 * The 'help' command will display a list of all avaliable commands. Use 'help + \<command>' to get a description of the specified command.

 ![Console Help](https://i.imgur.com/fjLXHUP.gif)
 ![Console Empty file](https://i.imgur.com/wxQ8Ap7.gif)
 ![objects](https://i.imgur.com/1TZcPsu.gif)

 ### Runing testfiles
To run tests for the project, just run the following command on the root of the repository:
```bash
python3 -m unittest discover tests
```
## Authors
Andrés Maciel: [@4mmZ](https://github.com/4mmZ)
Gonzalo Pedernera: [@gonzalopedernera](https://github.com/gonzalopedernera)
