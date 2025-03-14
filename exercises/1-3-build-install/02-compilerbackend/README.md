# Interactions between Frontend and Backend

There are some special purpose backends, mainly to support distributing python extensions written in compiled languages.

## About this example

This example uses [meson-python](https://mesonbuild.com/meson-python/) to demonstrate how one might package an extension written in C++ using the [nanobind](https://nanobind.readthedocs.io/en/latest/index.html) library.

The example content is only slightly adapted from the following tutorials:

- [meson-python tutorial](https://mesonbuild.com/meson-python/tutorials/introduction.html)
- [Building extensions using Meson (nanobind)](https://nanobind.readthedocs.io/en/latest/meson.html)
- [Creating your first extension (nanobind)](https://nanobind.readthedocs.io/en/latest/basics.html)

### See the Backend in action

#### install in editable mode:

```bash
$ uv venv venv-comp
$ source venv-comp/bin/activate
(venv-comp)$ uv pip install meson ninja
(venv-comp)$ uv pip install -e .
(venv-comp)$ python -c "import cppext; print(cppext.add(2, 2))"
4
```

Change the extension in `src/cpp_extension.cpp`, for example: make the "add" function be one off (always return +1 of what it should).

Test the changes, automatically recompiles.

```bash
(venv-comp)$ python -c "import cppext; print(cppext.add(2, 2))"
5
```

### Does this work with every frontend?

#### Let's build with a few of them:

Make sure the build system picks up a C++17 capable compiler
```bash
(venv-comp)$ export CXX=<path-to-c++17-capable GCC>
```

With pip or the "build" frontends:

```bash
(venv-comp)$ pip wheel --wheel-dir dist .
# you should see compiler output here
(venv-comp)$ ls dist
# you should see a .whl file here, specifig to your arch, os and python version
(venv-comp)$ pip install dist/compilerbackend-0.1.0-<pyversion-os-arch>.whl
```

Replace the first line with the following to use "build":

```bash
(venv-comp)$ pip install build
(venv-comp)$ python -m build
```

With `uv` or `hatch`:

```bash
(venv-comp)$ rm -r dist
(venv-comp)$ pip install uv # if you don't have it installed
(venv-comp)$ uv build
(venv-comp)$ pip install hatch # unless you already have hatch installed
(venv-comp)$ hatch build 
# compiler output
(venv-comp)$ ls dist
# .whl file
(venv-comp)$ pip install dist/compilerbackend-0.1.0-<pyversion-os-arch>.whl
```
Note that the install might fail, because if `hatch` / `uv` are installed standalone, they might decide to use a different python version. This is because we don't tell them what to use in the "pyproject.toml" file. In this case `pip` will complain that there was no version found for your system.

Also note that, (at least on MacOS) while `hatch` picks up exported "CC"/"CXX" env variables, `uv` does not. You might have to explicitly call `$ CC=... CXX=... uv build` to make it use the compiler you want!

## Bonus: building for multiple python versions

The easiest way is with `uv`

```bash
(venv-comp)$ uv build --wheel -p pypy-3.9
# installs PyPy-3.9 for you and runs build inside an ad-hoc environment
(venv-comp)$ ls dist
# this should have built a wheel for version 3.9 of the PyPy interpreter
```

With `hatch` you would configure the project for a range of python versions / implementations and hatch build should build for all of them.

With other build frontends you basically have to create an environment per version and run the build inside that. Thankfully there are tools to automate this process like `tox` and `nox`, if you are stuck with one of those frontends.

## Known special purpose backends

Prominent examples are

- [scikit-build](https://scikit-build.readthedocs.io/en/latest/) (compile with CMake)
- [meson-python](https://mesonbuild.com/meson-python/) (compile with Meson)
- [maturin](https://www.maturin.rs/) (compile rust code with cargo, for example using [PyO3](https://pyo3.rs/v0.23.5/))
- [setuptools] (compile native C-extensions for python, run arbitrary code during build)

## Why not CMake for the example?

There are already some complete working examples using [scikit-build](https://scikit-build.readthedocs.io/en/latest/) within CSCS.

- [arbor](https://github.com/arbor-sim/arbor)
- [serialbox](https://github.com/GridTools/serialbox)
