# Week 7, Day 1
Monday, February 27, 2017  

### Rapid Application Development  

The title of Django's homepage reads: "The Web framework for  
perfectionists with deadlines" and I think that it's the perfect maxim  
to describe the quality of the tools that Django provides to developers  
who're subject to materiel constraints. Large-- with regards to the  
sheer size of their source code-- open-source software frameworks, like  
Django, address the two most insidious constraints that developers  
face, namely time and money; by adhering to the advice embedded in the  
age-old adage: "build it and they will come." Django's community of  
contributors compartmentalized *it* into a laundry list of unambigiously  
unglamourous tasks, toiled to publish production-grade Python, and the  
world beat a path to their doors.  

I'm glad that we spent a few days getting our hands dirty with Flask,  
but the underlying utility of *fuller* frameworks, if you will, is that  
the products of the aforementioned "unambigously unglamourous tasks"  
are built-in classes and methods that you won't have to define or  
debug when you're being counted on, to deliver. You have the luxury of,  
to paraphrase Isaac Newton, "standing on the shoulders of giants."  

It's worth taking a moment to reflect on.  

Pragmatically speaking, the following markdown is effectively an ordered  
list of commands, keypress combinations, and naming conventions that  
you're welcome to use to get the ball rolling on your exercises.  

**A word on the syntax of the following markdown:**  

- Lines that start with `>` are keypress combinations  
- Lines that start with `$` are commands  
- Lines that start with `_` are keystrokes  
- Define anything enveloped by percentage signs (`%`)  

### Getting Started  

##### Open a terminal emulator, on *macOS*  

`> Cmd+Shift+u`  
`_ t`  
`> Cmd+Option+o`  

##### Invoke a terminal multiplexer  

`$ tmux`  

##### Install-and-configure autoenv, on *macOS*  

`$ sudo brew install autoenv`  
`$ sudo echo 'source $(brew --prefix autoenv)'/activate.sh' >> ~/.bash_profile`  

##### Build a sandbox 

`$ git clone https://github.com/daeuhl/week7-day1.git`  
`$ cd week7-day1`  
`$ virtualenv --python=``which python3.5`` venv` # Note: this looks funky in the browser, but  
                                                         you should either look at it in nano
                                                         or just note that `which python3.5`
                                                         is enveloped in backticks
##### Set-up an application framework  

`$ django-admin.py startproject %project_name% .`  
`$ tree -I venv` # Checkpoint  

##### Customize its default settings  

`$ nano %project_name%/settings.py`  
`> Ctrl+\`  
`_ UTC`  
`_ America/New_York`  
`_ y`  
`> Ctrl+o, Return`  
`> Ctrl+x`  
`$ echo "STATIC_ROOT = os.path.join(BASE_DIR, 'static')" >> full_frame/settings.py`  
`$ cat full_frame/settings.py` # Checkpoint  

##### Document its dependencies  

`$ pip list --format=columns` # Checkpoint  
`$ pip freeze --local > requirements.txt`  
`$ cat requirements.txt` # Checkpoint  

##### Push  

`$ git checkout -b %branch_name%`  
`$ git status` # Checkpoint  
`$ git add .`  
`$ git commit -m "%commit_message%"`  
`$ git push origin %branch_name%`  
`$ %github_username%`  
`$ %github_password%`  
`$ deactivate`  
`$ exit`  
`$ exit`  
