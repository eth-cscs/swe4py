# Example for a special purpose backend

There are some special purpose backends, mainly to support distributing python extensions written in compiled languages.

## About this example

This example uses [meson-python](https://mesonbuild.com/meson-python/) to demonstrate how one might package an extension written in C++ using the [nanobind](https://nanobind.readthedocs.io/en/latest/index.html) library.

The example content is only slightly adapted from the following tutorials:

- [meson-python tutorial](https://mesonbuild.com/meson-python/tutorials/introduction.html)
- [Building extensions using Meson (nanobind)](https://nanobind.readthedocs.io/en/latest/meson.html)
- [Creating your first extension (nanobind)](https://nanobind.readthedocs.io/en/latest/basics.html)

### See it in action

#### install in editable mode:

```bash
$ virtualenv .venv
(venv)$ activate .venv/bin/activate
(venv)$ pip install meson
(venv)$ pip install -e .
(venv)$ python -c "import cppext; print(cppext.add(2, 2))"
4
```

change the extension in `src/cpp_extension.cpp`, for example: make the "add" function be one off (always return +1 of what it should).

recompile and test

```bash
(venv)$ meson compile -C build
(venv)$ python -c "import cppext; print(cppext.add(2, 2))"
5
```

#### build for distribution:

with pip or the "build" frontends

```bash
(venv)$ pip wheel .
# you should see compiler output here
(venv)$ ls dist
# you should see a .whl file here, specifig to your arch, os and python version
(venv)$ pip install dist/compilerbackend-0.1.0-<pyversion-os-arch>.whl
```

replace the first line with the following to use "build":

```bash
(venv)$ pip install build
(venv)$ python -m build --wheel .
```

also try building source distribution as well

```bash
(venv)$ export CXX=<path-to-c++17-capable GCC>
(venv)$ pip install build
(venv)$ python -m build . # without --wheel it will try to build both, wheel and sdist
# you should see compiler output here
# followed by an error
```

That's right, source distributions for compiled extensions don't actually make any sense!

with `uv` or `hatch`

```bash
(venv)$ rm -r dist
(venv)$ hatch build -t wheel  # note the different CLI API
(venv)$ #or uv build --wheel
# compiler output
(venv)$ ls dist
# .whl file
(venv)$ pip install dist/compilerbackend-0.1.0-<pyversion-os-arch>.whl
```
Note that the install might fail, because if `hatch` / `uv` are installed standalone, they might decide to use a different python version. This is because we don't tell them what to use in the "pyproject.toml" file. In this case `pip` will complain that there was no version found for your system.

Also note that, (at least on MacOS) while `hatch` picks up exported "CC"/"CXX" env variables, `uv` does not. You might have to explicitly call `$ CC=... CXX=... uv build` to make it use the compiler you want!

## Bonus: building for multiple python versions

The easiest way is with `uv`

```bash
(venv)$ uv build --wheel -p pypy-3.9
(venv)$ ls dist
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
