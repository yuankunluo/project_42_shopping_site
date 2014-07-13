project_42_shopping_site
========================

Project 42
-----------------------

Universitaet Duesseldorf Infowiss Projectseminar

Authors:
    * Yuankun
    * Tobias
    * Hylee

Install
-----------------------

    You need python 2.7.5, django 1.6.5, South.
    For installing tipps, please read the doc.
    It's so easy with pip or easy_install to install these tools.
    Like:
        pip install django
        pip install south

    But under windows, you must install python, that can be done by downloading the python2.7's exe.
    :_)

    Here are Install Guide from Book Beginner Django E-Commerce*:

        Installing Python

            First things first, make sure you have Python installed on your system. On any system, you can check by jumping into your shell and typing python. If your system responds to the effect of “cannot be found,” you need to download and install Python. If Python is present and installed, you should be dropped into a new prompt that looks like >>>, from which you can start typing in Python code.

            If you’re using a Unix-variant or OS X, chances are very good that it’s already there. If you’re using Windows and need to install it, I highly recommend you download a version of ActivePython, as it takes care of a lot of configuration work for you. The examples in this book are dependent on Python 2.5. If you are running Django on an earlier version (2.3 is the minimum required), you may be forced to change the examples, spelling out the syntactic sugar added in later versions. The most prevalent example in this book is probably the use of Python decorator syntax.

        Installing Django
            Now that you’ve got Python installed, you can download and install the Django framework on your system. Download the latest version available from http://www.djangoproject.com/ and untar it to a directory on your system. Inside this directory, you should see a file called setup.py. From within your shell, navigate to this directory and issue the following command:
            $ python setup.py install
            You’ll probably need to be an administrator, or have sudo-power,8 in order for this to work. After the install is finished running, you can have a look at the Django base code files. They are on your system in your Python directory under site-packages/django. Most of them probably won’t mean a whole lot to you right now, but after working through a few chapters, you’ll have a much better handle on how to make sense of the code in the Django source.
            There is one item in the bin directory that we’re going to take a look at now. It’s a file called django- admin.py, and it’s going to be an important item during the development process. Make note of where
            this file is on your system, because when you go to issue any commands that use this file, you may need to specify the full path to this file. For example, if you’re on a Unix system, you may need to issue this command:
            $ /usr/lib/python2.5/site-packages/django/bin/django-admin.py command_here
            or on Windows:
            C:/Python25/Lib/site-packages/django/bin/django-admin.py command_here
            These may vary depending on your system’s exact configuration. If you plan to use the django- admin.py utility a lot, you can save yourself from having to type this every time by adding it to your
            PATH on Unix, and your Path environment variable on Windows. This isn’t terribly difficult to do on Unix: you can create a symbolic link to this file in your PATH.
            On Windows, it’s a little trickier. Under System Properties, click “Advanced” and click the “Environment Variables” button. In here, in the “System Variables” section, there is a variable called “Path” that should be a semi-colon–delimited list of paths to various utilities you have installed on your system. You can add one at the end. Note that you use backslashes here:
            C:\Python25\Lib\site-packages\django\bin
            If you add this entry to your “Path” variable, you will be able to reference django-admin.py without
            specifying the full path every time.

        ISBN13: 978-1-4302-2535-5
        User Level: Beginner to Intermediate
        Publication Date: October 28, 2009

IDE
-----------------------

    We use PyCharm from JetBrain.Inc, this Community Edition is free to use, and it's very good for codding in python.
    http://www.jetbrains.com/pycharm/download/

Manage
-----------------------

    Everytime change the model, must using python manage.py syncdb to take the effect on db.

Docs to Read
-----------------------

    Django provides the strong and solid platform
    *   Django's Doc: https://docs.djangoproject.com/en/1.6/

    SOUTH will be used to update the dbs schema automatic.
    *   SOUTH's Doc: http://south.readthedocs.org/en/latest/index.html

Django & Python version
-----------------------

    * django 1.6.5

    * Python 2.7.5

How to run
----------------------

    1.  Using command to locate to the project folder
    2.  Input **python manage.py runserver**
    3.  The default admin address is http://127.0.0.1:8000/admin

    Administrators(Account/Password):
        *   yuankunluo 123123
        *   hylee101    123123
        *   tobias  123123


