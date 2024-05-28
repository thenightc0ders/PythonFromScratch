# Python From Scratch
<p>Welcome to our Python from Scratch course, designed to guide you through the fundamentals of Python programming. Whether you're a complete beginner or looking to refresh your skills, this course will provide you with the essential knowledge to start writing your own Python scripts and applications.</p>
<br>

## Environment Setup
- [ ] **Python Installation Windows**
  - Download Python Installer
    - https://www.python.org/downloads/windows/
  - Validate Python Installation
       ```sh
      C:\>python
       ```
- [ ] **Python Installation Linux**
  - CLI (Command Line Interface) Installation
       ```sh
      suraj@linuxhost:/$ sudo apt install python3
       ```
  - Validate Python Installation
       ```sh
      suraj@linuxhost:/$ python3
      Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>>
       ```
- [ ] VS Code Setup
- [ ] Pycharm Setup
- [ ] **Virtual Env Setup**
  - ***Windows:*** 
    - Installation:
        ```sh
      C:\>pip install vitrualenv
        ```
    - Creation:
      ```sh
      C:\myprojectfolder>virtualenv myvirtualenv
      ```
    - Activation:
        ```sh
      C:\myprojectfolder>cd myvirtualenv
      C:\myprojectfolder\myvirtualenv>cd scripts
      C:\myprojectfolder\myvirtualenv\scripts>activate.bat
      (myvirtualenv) C:\myprojectfolder\myvirtualenv\scripts>
        ```
    - Deactivation:
        ```sh
        (myvirtualenv) C:\myprojectfolder\myvirtualenv\scripts>deactivate.bat
        C:\myprojectfolder\myvirtualenv\scripts>
        ```
  - ***Linux***
    - Installation:
        ```sh
        $ sudo apt install python3-virtualenv
        $ sudo pip3 install virtualenv
        ```
    - Creation:
       ```sh
        suraj@linuxhost:/myprojectfolder$ python3 -m venv myvirtualenv
      
       ```
    - Activation:
       ```sh
      suraj@linuxhost:/myprojectfolder$ source myvirtualenv/bin/activate
      (myvirtualenv) suraj@linuxhost:/media$ source myvirtualenv/bin/activate
       ```
    - Deactivation:
       ```shell
      (myvirtualenv) suraj@linuxhost:/myprojectfolder$ deactivate
      suraj@linuxhost:/myprojectfolder$
       ```
<br>

## Introduction to Python
- [ ] What is Python and why learn it?
- [ ] Setting up your development environment Repl.it, VSCode, Pycharm
- [ ] Writing your first Python program (a simple print statement or basic calculation).
<br><br>

## Python Fundamentals
- [ ] Variables, data types (numbers, strings, booleans) and operators.
- [ ] Control flow statements (if/else, loops).
- [ ] Functions - defining and using functions.
- [ ] Lists and Tuples - creating, accessing, and manipulating data.
<br><br>

## Intermediate Python
- [ ] Dictionaries - storing and retrieving data with key-value pairs.
- [ ] String Manipulation - using built-in functions and methods.
- [ ] Modules and Packages - importing functionalities for code reuse.
- [ ] Object-Oriented Programming (OOP) basics - classes and objects.
<br><br>

## Projects and Applications
- [ ] Building a small guessing game app.
- [ ] Create a similar app by yourself.

    