# A Peek into a Python Build Backend

This project sets up a custom "in-tree" build backend in order to demonstrate the backend interface. The interface is documented in [PEP-517](https://peps.python.org/pep-0517/) (PEP stands for Python Enhancement Proposal).

## Important Warning

Never do this in actual Python projects unless you have exhausted all other options (see below). There are easier and more maintainable ways of achieving almost anything you could achieve doing this.

While the "in-tree backend" technique is part of the PEP ([here](https://peps.python.org/pep-0517/#in-tree-build-backends)), it is meant for special cases like build backends building themselves (self-hosting).

We do not anticipate anyone in CSCS ever using this technique. Most likely there is already a backend that can do what you need (like compile extensions) or alternatively, there are extensible backends like [hatchling](https://hatch.pypa.io/1.9/plugins/about/), which allow you to register a hook customizing what you want without reimplementing anything.

Here it is used only for illustrative purposes, hence it will not be explained further.

## See it in action

create a virtualenv and install into it

```bash
$ python -m venv .venv
$ source .venv/bin/activate
(venv)$ pip install .
(venv)$ hello # test the installation
(venv)$ ls
# this should have written a "wheel-log.txt" file
(venv)$ cat wheel-log.txt
```

Now, take a look at `src/mybuild.py`. It implements all of the mandatory hooks specified in PEP-517!

Actually for what you just did, only `build_wheel` was used. The other one, `build_sdist`, is used for building source distributions (building a wheel was already implicitly done for you during install).

```bash
(venv)$ pip install build # pip doesn't have an interface for building sdists, only wheels
(venv)$ python -m build --sdist .
(venv)$ cat sdist-log.txt
```

Of course the actual implementation would look a lot more complicated if we didn't just defer to an existing backend. The log files show you everything that is passed to the hooks, now ask yourself:

- How does the backend know what metadata to put into the distribution? It has to read the `pyproject.toml` file itself! Thankfully, the metadata section is standardized.
- How does the backend know which python files to include? There is no standard way of telling a backend, each backend has to make a decision (most read it from a backend specific pyproject.toml section).

If you wonder why there is no standard way of specifying included python modules, remember that some backends compile C/C++/Fortran/Rust code into python modules, so the modules might not exist before the build starts.

How about editable installs?

```bash
(venv)$ pip install -e .
```

That's right, it fails! Editable installs require the optional `build_editable` hook, which we did not wrap in `mybuild.py`. That said, all the popular backends implement this.

## Optional Exercise

Find the implementation of `build_editable` in [hatchling](https://github.com/pypa/hatch/blob/master/backend/src/hatchling/build.py) and wrap it in `mybuild.py`. Check if it works by repeating the editable install commandline call above.
