========================
Safari-Do
========================

A Todo manager from Safari

Working Environment
===================

How to configure your virtual environment:

Virtualenv with virtualenvwrapper
------------------------------------

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
which will take care of managing your virtual environments and adding the
project path to the `site-directory` for you::

    $ mkvirtualenv safarido

Configuring the project
=================

To install Django in the new virtual environment, run the following command::

    $ git clone
    $ pip install -r requirements/local.txt
    $ ./manage.py syncdb --migrate

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Service expect a requirements.txt file in the root of projects.*
