---
layout: section
---

# Getting started with Python: Basic environment configuration

---

## Content

- Understanding a Python interpreter
- Understanding virtual environments

---

# Python Interpreter

- Python is an *interpreted* language
    - Programs are distributed as source code instead of binary machine code
    - An *interpreter* is required to run the program

- Python interpreters
    - [CPython](https://github.com/python/cpython) is the reference interpreter for the language ([📖](https://en.wikipedia.org/wiki/CPython))
    - [PyPy](https://pypy.org/) is a _just-in-time_ compiler Python with limited support for CPython extensions
    - [RustPython](https://rustpython.github.io/) is a Python interpreter written in Rust
    - [GraalPy](https://www.graalvm.org/python/) is part of [GraalVM](https://www.graalvm.org/)
    - Others/unmaintained: IronPython, Jython, [pyston](https://github.com/pyston/pyston)...
    - [Python Interpreters Benchmarks](https://pybenchmarks.org/)
    - Experimental full Python compiler: [Nuitka](https://nuitka.net/)

<!--
Python (created by Guido van Rossum in 1989-1991) is an interpreted language, which means that Python programs are not directly translated into binary machine code by the programming language processing tool (usually called *compiler*) at *compilation* time. Therefore, Python programs cannot be distributed as independent executable programs but only as source code files, and require the programming language processing tool (usually called *interpreter*) at run-time.

There are several Python interpreters developed in different programming languages, but the interpreter taken as reference implementation is CPython, written in C (originally used the C89 standard with several select C99 features, from version 3.11 it uses C11). CPython works by translating first the source code into bytecode (cached to the filesystem if possible) and then executing it by the Python stack virtual machine. Note that the bytecode is just an implementation detail and thus it's not guaranteed to be compatible across different versions.

RustPython:
    it can be embedded into Rust programs to use Python as a scripting language for your application, or it can be compiled to WebAssembly in order to run Python in the browser.
-->

---

# Anatomy of a Python Interpreter (CPython)

- CPython actually compiles the source code into bytecode (and caches it) before executing it

![cpython](./assets/python-interpreter.svg)

---

# CPython Basics

- `python` | `python3` command
  - `python3` command introduced to avoid conflicts between incompatible versions (Python2 != Python3)
  - Python 2 is end-of-life since 2020
  - Many Linux distributions still use `python3` (e.g. [Ubuntu](https://launchpad.net/ubuntu/focal/+package/python-is-python3)) as default command name
- Importable packages are searched from the list of sources in `sys.path` variable (`python -m site`)
  - usually: `/<prefix>/lib/pythonX.Y/site-packages`
  - some distributions use `dist-packages` instead of `site-packages`
  - if `$PYTHONPATH` (`dir1:dir2:...`) exists, it is prepended to the `sys.path`
  - if user-specific packages are enabled, they are searched first
    - `PYTHONNOUSERSITE`: disable user-specific site-packages directory
    - `PYTHONUSERBASE`: prefix for user-site packages (`$HOME/.local`)

---

# CPython Usage

- Python code can be run in different modes affecting the `sys.path` variable
- Script mode: `$ python [options] script.py`
  - `sys.path.insert(0, basedir(script.py))`
- Module mode (**-m**): `$ python [options] -m package.module_name`
  - `sys.path.insert(0, $PWD)`
- Command mode (**-c**): `$ python [options] -c 'python_statement; python_statement'`
  - `sys.path.insert(0, $PWD)`
- Note that the same file can be run in different modes depending on the command line
  - `python ./my_local_source.py` vs `python -m my_local_source`

---

# CPython Usage Options

- Some useful options:
  - `-u` : unbuffered output (stdout, stderr)
  - `-O` : remove assert and __debug__-dependent statements (`$PYTHONOPTIMIZE=1`)
  - `-OO` : do -O changes and also discard docstrings (`$PYTHONOPTIMIZE=2`)
  - `-s` : don't add user site directory to sys.path (`$PYTHONNOUSERSITE`)
  - `-E` : ignore environment variables like PYTHONPATH
  - `-I` : isolate Python from the user environment (implies `-E` and `-s`)

---

# Python Virtual Environments

- A _virtual environment_ (or _venv_) is a self-contained directory tree:
  - with a Python interpreter
  - with an independent set of Python packages installed inside the venv tree
  - disposable (easy to recreate, not checked in VCS)
  - not movable or copyable
- Virtual environments isolate the Python infrastucture:
  - between different projects with different requirements
  - between the system installation and the project requirements (optional)
- Virtual environments need to be _activated_ by sourcing an activaction script:
  - `source myenv/bin/activate`
  - the activation script usually only changes the shell's environment (e.g. `PATH=myenv/bin:$PATH`)

---

# Python Virtual Environments are **not** Containers

- Virtual environments do **not** replace user environment isolation tools
 (containers, uenvs, ...)
  - System / user resources outside of the venv tree are not isolated
  - Environment variables are not isolated

- Why using venvs if we need another isolation layer anyway?
  - Lightweight and very easy to bootstrap
  - Very well integrated with Python tools
  - Convenient for development and testing with different Python versions
  - Fully cross-platform where Python is available
  - (Opinionated) Except for production, _"sometimes"_ a container _might_ be overkill

<!--

# Other Virtual Environment Tools: Conda, Spack,

- conda ...


-->

---
layout: fact
---

## Exercises

Time to see it in action: Browse to

<br />
<a href="https://github.com/eth-cscs/swe4py">https://github.com/eth-cscs/swe4py</a>

<br />
<br />

Open a code space and head to `exercises/1-1-getting-started`
(need to be logged in)

or

Clone the repo & `cd swe4py/exercises/1-1-getting-started`
