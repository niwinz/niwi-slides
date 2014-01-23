Introduction to Clojure
=======================

Lisp
----

Fundamentals
------------

Numbers
~~~~~~~

.. code-block:: clojure

    42
    (+ 1 2 3)
    ;=> 6

- ``java.long.Long`` by default, overflow throws ``java.lang.ArithmeticException``
- Special operators for automatic promotion to ``BigInt`` upon overflow ``+'``, ``-'`` et. al.


.. code-block:: clojure

    (/ 1 3)
    ;=> 1/3

- Represents a ratio between integers

.. todo :: bigint and bigdecimal literals

Strings
~~~~~~~

Maps
~~~~

Keywords
~~~~~~~~

Vectors
~~~~~~~

Lists
~~~~~

Sets
~~~~

Symbols
~~~~~~~

Functions
~~~~~~~~~

Regexes
~~~~~~~

Abstractions
------------

seq
~~~

.. todo :: first, rest, lazy seqs

collection
~~~~~~~~~~

.. todo :: into, conj

function
~~~~~~~~

IFn

.. todo :: apply, partial, complement, comp)

Reference types
---------------

var
~~~

ref
~~~

atom
~~~~

agent
~~~~~

Protocols
---------

Multimethods
------------

Reader
------

Special forms
~~~~~~~~~~~~~

Reader macros
~~~~~~~~~~~~~

Evaluation
~~~~~~~~~~

Macros
~~~~~~

Java Interop
------------
