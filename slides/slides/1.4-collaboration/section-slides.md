---
layout: section
---

# Python Skills for Collaboration

<v-click>

## Or How To Kill Project Velocity
</v-click>

<v-click>

### And How To Get It Back
</v-click>

---

## What We Will Learn

<style>
.slidev-vclick-hidden.animate-strike {
  text-decoration: line-through;
  opacity: 1 !important;
}
.slidev-vclick-hidden.animate-vanish {
  display: none;
}
</style>
- How to create 
<span v-click.hide="2" class="animate-vanish">
  <span v-click.hide="1" class="animate-strike">
    terrible
  </span>
</span>
<span v-click="2" class="animate-vanish">
  **great**
</span> dev experience

- How to keep focus and velocity

---
layout: center
---

## 1. Dependency Management

---

## Dependency Management Nightmare

What's the DevEx here?

<v-click>

```toml
# pyproject.toml
[project]
name = "mytool"
dependencies = []
```
</v-click>
<v-click>
```python
# src/analysis.py
import numpy as np
```
</v-click>
<v-click>

```python
# src/main.py
import typer
from . import analysis
```
</v-click>

<v-click>

Rince and repeat:
```bash
$ mytool
ImportError: typer
$ pip install typer && mytool
ImportError: numpy
```
</v-click>

---
layout: fact
---

Contributions to "mytool" welcome!

<v-click>

Excited to get started?
</v-click>

---

## Could Have Been Worse

````md magic-move
```python
# src/analysis.py
import numpy

def calclate():
  ...
```

```python
# src/analysis.py
def calculate(*args, **kwargs): # <- cli entry point
  try:
    import cupy # <- use GPU acceleration if possible
    from ._cupy_calc import run
  except ImportError:
    from ._numpy_calc import run # <- fallback

  return run(*args, **kwargs)
```
````

<v-click at="2">you can</v-click>
<v-click at="3"> &ne; you should</v-click>
<v-click at="5"> (but sometimes you have to)</v-click>
<v-click at="4">

-- The Motto of every true Professional
</v-click>

---
layout: fact
---

## Let's Fix This

<a href="https://github.com/eth-cscs/swe4py">https://github.com/eth-cscs/swe4py</a>

`exercises/1-4-collaboration/01-dependency-management`

---
layout: center
---

## 2. Packaging & Distributing

Packaging: "pip installable"

Distributing: from a registry

---
layout: two-cols
---

### Libraries: Without Packaging

<v-click>
Only ways to use:
</v-click>
<v-click>

- copy the code (and the dependencies)
</v-click>
<v-click>

- submodules
</v-click>
<v-click>

Who wouldn't want that?
</v-click>

::right::
### Libraries: Packaged But Not Distributed
<v-click>

Doable, however:
</v-click>
<v-click>

- Supply chain security concerns anyone?
</v-click>
<v-click>

- Not as pretty
</v-click>

---

### Easy To Try Out CLI App

````md magic-move
```bash
$ git clone git+https://github.com/DropD/mytool
$ cd mytool
$ uv venv .venv && source .venv/bin/activate
$ uv pip install -r requirements.txt
$ python run main.py
```

```bash
$ git clone git+https://github.com/DropD/mytool
$ cd mytool
$ uv run -s main.py # <- automatically installs deps
```

```bash
$ uvx run mytool-main --from "mytool @ https://github.com/DropD/mytool"
```

```bash
$ uvx run mytool-main --from mytool
```

```bash
$ uvx run mytool
```
````

<v-click at="1">

1. move dependencies to `pyproject.toml`
</v-click>
<v-click at="2">

2. Package (using `[project.script]`)
</v-click>
<v-click at="3">

3. Upload to PyPi
</v-click>
<v-click at="4">

4. Rename CLI to match distro
</v-click>

---

### Easy To Try Out & Deploy Web App

````md magic-move
```bash
$ git clone git+https://github.com/DropD/myapp
$ cd myapp
$ uv venv .venv && source .venv/bin/activate
$ uv pip install -r 
$ python manage.py collectstatic
$ python manage.py migrate
$ python manage.py loaddata example/fixtures.yml
$ python manage.py runserver
```

```bash
$ git clone git+https://github.com/DropD/myapp
$ cd myapp
$ uv run -s manage.py collectstatic # <- automatically installs deps
$ uv run -s manage.py migrate
$ uv run -s manage.py loaddata example/fixtures.yml
$ uv run -s manage.py runserver
```

```bash
$ git clone git+https://github.com/DropD/myapp
$ cd myapp
$ hatch run init # <- first time setup
$ hatch run dev # <- runs the dev server
```
````
<v-click at="1">

1. move dependencies to `pyproject.toml`
</v-click>
<v-click at="2">

2. use `hatch` tasks (or `pdm` or `uv` + a task runner)
</v-click>
<v-click at="3">

3. deploy expects "requirements.txt"?

`$ uv export > requirements.txt`
</v-click>
<v-click at="4">

No need to package or upload to PyPi
</v-click>

---
layout: fact
---

<div class="text-5xl">
Packaging Reference: 
<a href="https://www.pypa.io/en/latest/">
 pypa.io
</a>
</div>


---
layout: center
---

## 3. File Layout

---

### Default: "src layout"

````md magic-move
```
hpc-sim
├── README.md
├── pyproject.toml
├── src
│   └── hpc_sim
│       ├── __init__.py
│       ├── bar.py
│       ├── foo.py
│       └── py.typed
└── tests
    ├── conftest.py
    ├── test_bar.py
    └── test_foo.py
```

```{12-14}
hpc-sim
├── README.md
├── pyproject.toml
├── src
│   └── hpc_sim
│       ├── __init__.py
│       ├── bar.py
│       ├── foo.py
│       └── py.typed
└── tests
    ├── conftest.py
    └── hpc_sim_tests
        ├── __init__.py
        ├── utils.py
        ├── test_bar.py
        └── test_foo.py
```

```{4-5,10-11}
hpc-sim
├── README.md
├── pyproject.toml
├── src
│   └── hpc_sim
│       ├── __init__.py
│       ├── bar.py
│       ├── foo.py
│       └── py.typed
└── tests
    ├── conftest.py
    └── hpc_sim_tests
        ├── __init__.py
        ├── utils.py
        ├── test_bar.py
        └── test_foo.py
```
````

<v-click at="1">Note: no `__init__.py` in src or tests</v-click>

---

### No Ambiguity

Compare, without `src`:

```bash
$ cd hpc-sim
$ source .venv/bin/activate
$ pip install hpc_sim
(.venv)$ python
>>> import hpc_sim
```

<v-click>

⚡ Are you importing `.venv/.../site-packages/hpc_sim`?
</v-click>

<v-click>

  or `./hpc_sim`?
</v-click>
<v-click>

  ➯ `.` has priority
</v-click>
<v-click>

Which one are your tests importing?
</v-click>

---

### Defend "src" From IDEs

Put this in your `.gitignore`
```
## Stop IDEs From Destroying Benefits Of Src Layout
src/__init__.py
tests/__init__.py
```
---

### Alternative layouts

````md magic-move
```
# script with inline metadata

single_script.py
```

```
# when it's ok to break site-packages installs
# AND it's the standard for your framework

hpc-app
├── README.md
├── pyproject.toml
├── manage.py
└── hpc_app
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── settings.py
```

```{1,3,5,6-7,12-13}
# monorepo (with uv workspaces)

hpc-collection
├── README.md
├── pyproject.toml
├── hpc-app
│   ├── pyproject.toml
│   ├── manage.py
│   └── hpc_app
│       ├── __ini__.py
│       └── ...
├── hpc-lib
│   ├── pyproject.toml
│   └── src
│       └── hpc_lib
...
└── ...
```
````

---
layout: center
---

## 4. Interactivity

Exercise time:

<a href="https://github.com/eth-cscs/swe4py">https://github.com/eth-cscs/swe4py</a>

`exercises/1-4-collaboration/04-interactivity`

---

### Interactivity: Interfaces

Which would you prefer?

````md magic-move
```python
class Foo:
  def __init__(self, path: pathlib.Path):
    config = parse_yaml_string(path.read_text())
    self.bar = config["bar"]
    ...
```
```python
@dataclasses.dataclass
class Foo:
  bar: int
  ...

  @classmethod
  def from_file(cls: type[Self], path: pathlib.Path) -> Self:
    config = parse_yaml_string(path.read_text())
    return cls(
      bar=config["bar"],
      ...
    )

```
```python
@dataclasses.dataclass
class Foo:
  bar: int
  ...

  @classmethod
  def from_yaml_sring(cls: type[Self], yaml_string: str) -> Self:
    config = parse_yaml_string(yaml_string)
    return cls(
      bar=config["bar"],
      ...
    )
  
  @classmethod
  def from_file(cls: type[Self], path: pathlib.Path) -> Self:
    return cls.from_yaml_sring(path.read_text())
```
````

---

### Interactivity: Got It? Keep It!

1. Encode supported interactivity in Jupyter notebooks
2. Use <a href="https://github.com/treebeardtech/nbmake">https://github.com/treebeardtech/nbmake</a>
3. Check <a href="https://github.com/GridTools/gt4py">https://github.com/GridTools/gt4py</a> for an example


---
layout: center
---

## 5. Focus On Code

<v-click>

**Not** on whitespace
</v-click>
<v-click>

**Not** on chores
</v-click>

---

### Focus: Code Formatting

Which looks better?
````md magic-move
```python
long_list = [foo, bar, baz,
             apple, banana, cranberry,
             ...]
```
```python
long_list = [
  foo,
  bar,
  baz,
  apple,
  banana,
  cranberry,
  ...
]
```
````

<v-click>

Do you want to discuss this on every PR?
</v-click>
<v-click>

Aren't we each defending the choice our IDE made for us anyway?
</v-click>

---

### Code Formatting: Solution

<v-click>

- Run a formatter (Ruff): <a href="https://docs.astral.sh/ruff/">https://docs.astral.sh/ruff/</a>
</v-click>
<v-click>

- On every commit locally (pre-commit): <a href="https://pre-commit.com">https://pre-commit.com</a>
</v-click>
<v-click>

- And on CI (mandatory before merge)
</v-click>
<v-click>

Let your IDEs run wild!
</v-click>

---

### Focus: Linting

- Eliminate basic mistakes from PR reviews!
- Catch them even before the tests run
- Not just syntax errors

<br/>
<br/>
<v-click>

- Run a linter (Ruff): <a href="https://docs.astral.sh/ruff/">https://docs.astral.sh/ruff/</a>
</v-click>
<v-click>

- On every commit locally (pre-commit): <a href="https://pre-commit.com">https://pre-commit.com</a>
</v-click>
<v-click>

- And on CI (mandatory before merge)
</v-click>

---

### Focus: Type Hints

Duck-Typing is great! <v-click>However, Type Hints</v-click>

<v-click>

- advertise how to use an interface
</v-click>
<v-click>

- make you code with intent
</v-click>
<v-click>

- speed up PR reviews
</v-click>

---

### Type Hints Can Be Awful

<v-click>

- Go out of Synch
- Super confusing if wrong
</v-click>
<v-click>

<br/>
<br/>

1. Run `mypy` (soon maybe Ruff)
1. Every commit, locally
1. Every push/pr on CI
</v-click>

---

### Focus: Chores

- running the tests right
- checking for secrets
- formatting markdown files
- building & uploading to PyPi
- etc

<v-click>

Chore ➠ pre-commit ➠ CI
</v-click>

---
layout: center
---

## Safe To Fail Environment

Measure your tests this way:

<v-click>

Level 1: I never worry about breaking things
</v-click>
<v-click>

Level 2: My new intern never worries either
</v-click>
<v-click>

Level 3: Tests ≈ Documentation
</v-click>
