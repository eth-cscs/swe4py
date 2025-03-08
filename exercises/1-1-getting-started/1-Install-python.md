# 1. Installing a Python interpreter

It is useful to learn different strategies to install the Python interpreter in a system, even if there is already a working Python installation. Here are some options, from the most system-specific to the most Python-specific way:

1. Use your system native package system (e.g. `apt`, `pacman`, ...)
2. Use an alternative package manager available in your system (e.g. `brew`, `conda`, `spack`, ,...)
3. Use a development tool managing different programing tools versions (e.g. `asdf`, ...)
4. Use a Python version manager (e.g. `uv`, `pyenv`) to kickstart a Python installation without an existing Python interpreter.

You will need to decide which strategy works better for your use-case. Here we will only explain option 4, since options 1-3 are not specific to Python.

## Using `uv`

[`uv`](https://docs.astral.sh/uv/) is a modern, very efficient and versatile tool with multiple functionalities, including managing Python versions. There are also many strategies to install `uv` (see [documentation](https://docs.astral.sh/uv/getting-started/installation/)) but here we will use its standalone installer, which is the simplest and most universal way:

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once the `uv` tool is installed (and available in the `$PATH`), you can use it to install and manage different Python versions. The installation is very fast because a precompiled binary is directly downloaded from [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) instead of being built from source (see [CPython distributions](https://docs.astral.sh/uv/concepts/python-versions/#cpython-distributions) section):

```bash
$ uv python list
$ uv python install  # An optional version can be passed. e.g. 3.12
$ python --version
```

------------------------------------------------------------
**EXERCISE:**
Install `uv` in your system and a new Python version of your choice (which is not currently available in your system).

------------------------------------------------------------

## Using `pyenv`

[`pyenv`](https://github.com/pyenv/pyenv?tab=readme-ov-file) is a Python version manager that allows you to install and manage different Python versions in your system. It is more complex tool than `uv`, but it is also more powerful and flexible for dealing with Python versions. For example it supports other  interpreters than cPython (e.g.  `pypy`, `graal`, `pyston`, ...) and allows setting the global Python version, and different version per folder basis.

As in the `uv` case, there are differents ways to install it (see [Getting Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#a-getting-pyenv)), but the simplest one is the standalone installer:

```bash
$ curl -fsSL https://pyenv.run | bash
```

Once it is installed, you can check the list of available versions and pick one:
```bash
$ pyenv install --list  # it also supports other interpreters like pypy
$ pyenv install 3.12
$ pyenv global   # list all installed versions
```

The installation process is slower than `uv` because it builds the Python interpreter from sources. Once the installation is finished, you can set the global version or the local version for a specific directory.

**Note:**
`pyenv` configuration is slightly more tedious (see [B. Set up your shell environment for Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#b-set-up-your-shell-environment-for-pyenv)), therefore, if you are not familiar with `pyenv`, it is recommended to use `uv` on most cases.
