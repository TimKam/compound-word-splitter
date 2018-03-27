compound-word-splitter
======================

.. image:: https://travis-ci.org/TimKam/compound-word-splitter.svg?branch=master
    :target: https://travis-ci.org/TimKam/compound-word-splitter

Splits words that are not recognized by *pyenchant* (spell checker) into largest possible compounds.

Installation
------------

Make sure you have `enchant <https://www.abisource.com/projects/enchant/>`_ installed before proceeding.


Now run
::

    pip install compound-word-splitter


Note that languages installed by default are:

.. code:: python

    ['en', 'en_CA', 'en_GB', 'en_US']

If you would like to use 'de_de', like in the example below, you will have to install
`myspell <http://www.openoffice.org/lingucomponent/dictionary.html/>`_
dictionary for it (*myspell-de-de*).


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

