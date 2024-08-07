Introduction to an example package
##################################

A Python package for example purposes. This package demonstrates basic Python package structure, setup, and documentation using Sphinx and ReadTheDocs.

Installation
------------

Install the package using pip
::
    pip install ksr_example_package


Usage
-----
Here's a simple example of how to use the package:

.. code-block:: python
    
    import package
    result = package.add(5, 3)
    print(f"The result is {result}")

Documentation
-------------

Full documentation is available at `ReadTheDocs <https://about.readthedocs.com/>`_.

Installation
------------

ksr_example_package is currently running on Mac OS. ksr_example_package runs on Python 3.10 and up. We recommend you use the latest version of python 3 if possible.

**pip**

.. code-block:: bash
    
    pip install numpy
    pip install ksr_example_package

Alternatively, install  numpy and run the following

.. code-block:: bash
    
    git clone https://github.com/ketansingharoy/ksr_example_package.git
    cd ksr_example_package
    pip install .

**conda**

.. code-block:: bash
    
    conda create env -n ksr_example_package
    conda install -c conda-forge numpy
    conda install -c ksr22 ksr_example_package

**Manual installation**

    1. Install dependent packages: numpy
    2. Download ksr_example_package. Unzip it.
    3. Add ksr_example_package into your Python path.





Contributing
------------

Contributions are welcome! Please fork the repository and submit a pull request.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Authors
-------

Ketan Singha Roy, ketansingharoy@gmail.com

Acknowledgments
---------------

I thank Dr. ABC for helping me making the project
