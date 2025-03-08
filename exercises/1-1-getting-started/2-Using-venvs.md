# 2. Using Python virtual environments

A Python _virtual environment_ (AKA _virtualenv_ or _venv_) is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages that can be installed using Python package managers. Virtual environments allow us to isolate the Python packages in the system Python installation from the Python packages used in different projects.

------------------------------------------------------------
**IMPORTANT:** the isolation provided by Python virtual environments is only at the level of what is contained the virtual environments, that is the Python interpreter and Python packages. If a Python package uses directly system libraries which are not part of venv, the venv will not help to deal with those. In summary, Python venvs are are **not** a substitute for user environment isolation technologies like containers or uenvs, but a convenient, idiomatic and lightweight complement to them.

------------------------------------------------------------

A virtual environment can be also created using different tools. Here we will explain how to use the most common ones: `venv`, `virtualenv` and `uv`.

## Using `venv`

[`venv`](https://docs.python.org/3/library/venv.html) is a executable standard Python library module to create virtual environments. It is basically a stripped down version of `virtualenv` (which was the precursor of this kind of tools). To use it, you need to have a Python interpreter installed in your system and then execute the module:

```bash
$ python -m venv --help   # Get help and see the options
$ python -m venv myenv    # Create a new virtual environment
```

Once the venv is created, you need to "activate it", which is just changing the shell's PATH to make the Python interpreter and the installed packages available with higher priority than the system's Python interpreter and packages ("deactivating" it restores tp the previous state):

```bash
$ which python            # Get the current Python interpreter
$ source myenv/bin/activate  # Activate the virtual environment
(myenv) $ which python       # Get the current Python interpreter
(myenv) $ pip list           # List the packages installed by default
(myenv) $ deactivate         # Deactivate the virtual environment
$ which python            # Get the current Python interpreter
```

## Using `virtualenv` (optional)

[`virtualenv`](https://virtualenv.pypa.io/en/latest/) has many extra featuers on top of `venv`, but it is not part of the Python standard library. It is a standalone package that needs to be installed first (check [virtualenv installation](https://virtualenv.pypa.io/en/latest/installation.html)), or use `uv` like:
```bash
$ uv tool install virtualenv
```

Creating and activating virtual environments works very much like `venv`, but it features many other options:

```bash
$ virtualenv venv --help       # Get help and see the options
$ which python                 # Get the current Python interpreter
$ virtualenv myvirtualenv      # Create a new virtual environment
$ source myvirtualenv/bin/activate  # Activate the virtual environment
(myvirtualenv) $ which python       # Get the current Python interpreter
(myvirtualenv) $ pip list           # List the packages installed by default
(myvirtualenv) $ deactivate         # Deactivate the virtual environment
$ which python                      # Get the current Python interpreter
```

## Using `uv venv`

Using [`uv`](https://docs.astral.sh/uv/) to create virtual environments is as straightforward as expected:

```bash
uv venv --help       # Get help and see the options
uv venv myuvenv      # Create a new virtual environment
source myuvenv/bin/activate    # Activate the virtual environment
(myuvenv) $ which python       # Get the current Python interpreter
(myuvenv) $ uv pip list        # List the packages installed by default
(myuvenv) $ deactivate         # Deactivate the virtual environment
```

------------------------------------------------------------
**IMPORTANT:** Creating and activating Python virtual environments using `venv`, `virtualenv` or `uv` is quite similar and straightforward. However, note that the default packages installed in the newly created virtual environment may vary depending on the Python version, the creation options and the tool used to create the virtual environment. For example, `venv` and `virtualenv` install `pip` by default, while `uv` doesn't.

In virtual environments using `pip` as package manager, it is recommended to always install the latest versions of `pip`, `setuptools` and `wheel` before any other package, to avoid installation problems.

```bash
$ python -m pip install --upgrade pip setuptools wheel
```

------------------------------------------------------------
**EXERCISES:**

1. Use `venv` to create a virtual environment in the `.venv-1.26` folder, install NumPy version 1.26 on it with `pip`, and run a python command with an inlined script argument to import `numpy` and print its version.

2. Use `uv` to create a virtual environment in the `.venv-2.2` folder, install NumPy version 2.2 on it with `uv pip`, and run a python command with an inlined script argument to import `numpy` and print its version.

------------------------------------------------------------
