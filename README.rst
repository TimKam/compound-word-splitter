compound-word-splitter
======================

.. image:: https://travis-ci.org/TimKam/compound-word-splitter.svg?branch=master
    :target: https://travis-ci.org/TimKam/compound-word-splitter

Splits words that are not recognized by pyenchant (spell checker) into largest possible compounds.

Installation
------------

::

    pip install compound-word-splitter

Usage
-----

.. code:: python

    import splitter

    splitter.split('artfactory')

returns

.. code:: python

    ['art', 'factory']

If the word cannot be split into compounds pyenchant recognizes as words, the splitter returns an empty string.

