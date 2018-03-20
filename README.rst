compound-word-splitter
======================

.. image:: https://travis-ci.org/TimKam/compound-word-splitter.svg?branch=master
    :target: https://travis-ci.org/TimKam/compound-word-splitter

Splits words that are not recognized by pyenchant (spell checker) into largest possible compounds.

Installation
------------

OS X prerequisites:
For OS X users, you need to install enchant first.

Try installing it with homebrew
::

    brew install enchant


Now run
::

    pip install compound-word-splitter


Note that languages installed by default are: ['en', 'en_CA', 'en_GB', 'en_US']
If you would like to use 'de_de', like in the example below, you will have to install it.

On GNU/Linux run:
::

    sudo apt-get install myspell-de-de


Usage
-----

.. code:: python

    import splitter

    splitter.split('artfactory')

returns

.. code:: python

    ['art', 'factory']
    
.
    
.. code:: python

    split('Glossarelement', 'de_de')
   
   
returns

.. code:: python

    ['Glossar', 'Element']
    
.

If the word cannot be split into compounds pyenchant recognizes as words, the splitter returns an empty string.

