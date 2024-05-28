# Python From Scratch
<p>Welcome to our Python from Scratch course, designed to guide you through the fundamentals of Python programming. Whether you're a complete beginner or looking to refresh your skills, this course will provide you with the essential knowledge to start writing your own Python scripts and applications.</p>


## [Environment Setup ](https://github.com/thenightc0ders/PythonFromScratch/tree/d12c12533296d4df1d520d1f1c3b33f7b036f08b)

- [x] **Python Installation Windows**
  - Winget: https://winget.run/ (_Optional_)
  - Download Python Installer
    - https://www.python.org/downloads/windows/
    - ```C:\>winget install -e --id Python.Python.3.11```
  - Validate Python Installation
       ```sh
      C:\>python
       ```
- [x] **Python Installation Linux**
  - Installation Steps
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
- [x] **VS Code Setup**
  - _Windows_
    - https://code.visualstudio.com/Download
    - ```C:\>winget install -e --id Microsoft.VisualStudioCode```
  - _Linux_
    - Installation Steps
         ```sh
        suraj@linuxhost:/$ sudo apt install snapd #(if snapd is not present by default)
        suraj@linuxhost:/$ sudo snap install code --classic
         ```
- [x] **Pycharm Setup**
  - Download (Pycharm Early Access Program)
    - https://www.jetbrains.com/pycharm/nextversion/
  - Installation Steps
    - _Windows_
      - Execute downloaded exe file.
    - _Linux_
      ```sh
      suraj@linuxhost:/$ sudo tar -xvf pycharm-professional-242.10180.30.tar.gz
      suraj@linuxhost:/$ sudo mv pycharm-242.10180.30 /opt/pycharm-242.10180.30
      suraj@linuxhost:/$ sudo ln -s /opt/pycharm-242.10180.30/bin/pycharm /usr/local/bin/pycharm
      suraj@linuxhost:/$ nano ~/.local/share/applications/pycharm.desktop
      ```
      Add the below in .desktop file
      ```sh
      [Desktop Entry]
      Name=Pycharm
      Exec=/opt/pycharm-242.10180.30/bin/pycharm
      Icon=/opt/pycharm-242.10180.30/bin/pycharm.png
      Type=Application
      Categories=IDE;Development;
      ```
      <br>
- [x] **Virtual Env Setup**
  - A Python virtual environment is an isolated workspace that allows you to manage dependencies and packages for different projects independently, without conflicts. It ensures that each project can have its own versions of libraries and tools, preventing compatibility issues across projects.<br><br>
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
          suraj@linuxhost:/$ sudo apt install python3-virtualenv
          suraj@linuxhost:/$ sudo pip3 install virtualenv
          ```
      - Creation:
         ```sh
          suraj@linuxhost:/myprojectfolder$ python3 -m venv myvirtualenv
          suraj@linuxhost:/myprojectfolder$ virtualenv myvirtualenv
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

## [Introduction to Python](https://github.com/thenightc0ders/PythonFromScratch/tree/fdbe6aca4c357e785ed0ab88546a56f1fe7dfb47)
- [x] What is Python and why learn it?
  - Python is a high-level, interpreted programming language known for its readability and simplicity, making it ideal for beginners and experienced developers alike. It is widely used in various fields such as web development, data analysis, artificial intelligence, scientific computing, and automation due to its extensive libraries and supportive community. Learning Python can enhance your problem-solving skills, open up diverse career opportunities, and enable you to build versatile and powerful applications efficiently.
- [x] Setting up your development environment Repl.it, VSCode, Pycharm
  - We have seen in the last section how to setup vscode and pycharm, here we will take a look at replt.it.
- [x] Writing your first Python program (a simple print statement or basic calculation).
<br>

## Python Fundamentals
- [ ] Variables, data types (numbers, strings, booleans) and operators.
- [ ] Control flow statements (if/else, loops).
- [ ] Functions - defining and using functions.
- [ ] Lists and Tuples - creating, accessing, and manipulating data.
<br>

## Intermediate Python
- [ ] Dictionaries - storing and retrieving data with key-value pairs.
- [ ] String Manipulation - using built-in functions and methods.
- [ ] Modules and Packages - importing functionalities for code reuse.
- [ ] Object-Oriented Programming (OOP) basics - classes and objects.
<br>

## Projects and Applications
- [ ] Building a small guessing game app.
- [ ] Create a similar app by yourself.

    