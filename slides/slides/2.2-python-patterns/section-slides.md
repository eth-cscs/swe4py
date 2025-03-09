---
layout: image
image: /public/images/python-patterns.jpg
class: md-auto
---

---
layout: section
---

# Pythonic Patterns

---

# Encapsulation

## Private Modules

Meaning: DO NOT DIRECLTY IMPORT

````md magic-move
```bash
src
└── hpc_sim
    ├── __init__.py
    ├── _utils.py
    ├── _config_parser.py
    ├── _numerics.py
    ├── _compiled_numerics-cp312-aarch64-linux.so
    ├── lib.py
    └── main.py
```
```bash {6-7}
src
└── hpc_sim
    ├── __init__.py
    ├── utils.py
    ├── config_parser.py
    ├── _compiled_numerics-cp312-aarch64-linux.so
    ├── numerics.py
    ├── lib.py
    └── main.py
```
````

Not even in tests

---

# List Comprehensions

## Can help Comprehension

```python {monaco-run} {autorun: false}
numbers = range(15)

def filter(number: int) -> bool:
  return (number % 3 == 0) or (number % 5 == 0)

filtered: list[int] = []

# c-style for loop
for i in range(0, len(numbers)):
  if filter(numbers[i]):
    filtered.append(numbers[i])

print(filtered)
```

---

# List Comprehensions

## Can help Comprehension

```python {monaco-run} {autorun: false}
numbers = range(15)

def filter(number: int) -> bool:
  return (number % 3 == 0) or (number % 5 == 0)

print(
  [] # list comprehension
)
```

---

# Iterators

## Can Help Even More

```python {monaco-run} {autorun: false}
from typing import Sequence, Iterator
numbers = range(1000)

def filter_divisible(numbers: Sequence[int], by: int) -> Iterator[int]:
  for number in numbers:
    if number % by == 0:
      yield number

by_7 = filter_divisible(numbers, by=7)
by_35 = filter_divisible(by_7, by=5)
by_105 = filter_divisible(by_35, by=3)

print(list(by_105))
```

---

# Iterator Comprehensions & Composition

```python {monaco-run} {autorun: false}
from __future__ import annotations

data = {"green mangos": 4, "red apples": 5, "green apples": 2} # ...

green_fruits = ((k, v) for k, v in data.items() if k.startswith("green"))

# def by_color(fruits: Sequence[tuple[str, int]], color: str) -> Iterator[tuple[str, int]]:
#   return ((k, v) for k, v in data.items() if k.startswith(color))

# def total(fruits: Sequence[tuple[str, int]]) -> int:
#   return sum(i[1] for i in fruits)

print(dict(green_fruits))
# print(total_green := sum(i[1] for i in green_fruits))
# print(total(by_color(data, color="green")))
```

---

# Dataclasses

The structs of the Python world: <a href="https://docs.python.org/3/library/dataclasses.html">Dataclasses Docs</a>

````md magic-move
```python
class Fruit:
  __init__(self, fruit_type: str, color: str):
    self.fruit_type = fruit_type
    self.color = color
    if self.color == "brown" and not self.fruit_type == "coconut":
      self.overripe = True
```
```python
import dataclasses

@dataclasses.dataclass
class Fruit:
  fruit_type: str
  color: str
```
```python
import dataclasses

@dataclasses.dataclass
class Fruit:
  fruit_type: str
  color: str
  overripe: bool = dataclasses.field(init=False)

  def __post_init__(self):
    if self.color == "brown" and not self.fruit_type == "coconut":
      self.overripe = True
```
```python
import dataclasses

@dataclasses.dataclass(frozen=True)
class Fruit:
  fruit_type: str
  color: str

  @property
  def overripe(self) -> bool:
    return self.color == brown and self.fruit_type != "coconut"
```
````

Prefer `list[Fruits]` over "JS in Python", `{"fruit_type": "coconut", "color": ...}`

---

# Dataclasses: Extensions

````md magic-move
```python
from typing import Annotated, Literal
from pydantic import BaseModel

class Fruit(BaseModel):
  fruit_type: Literal["banana", "coconut"]
  color: Literal["yello", "brown"]
  overripe: bool
```

```python
import attrs

@attrs.define
class Fruit:
  fruit_type: Literal["banana", "coconut"]
  color: Literal["yello", "brown"]
  overripe: bool
```
````

<v-click>

- pydantic: <a href="https://docs.pydantic.dev/">docs.pydantic.dev</a>
</v-click>
<v-click>

- attrs: <a href="https://www.attrs.org/en/stable/index.html">attrs.org</a> + <a href="https://github.com/python-attrs/attrs/wiki/Extensions-to-attrs">attrs extensions</a>
</v-click>

---

# Protocols

## Extendability Without Subclassing

---

# Protocols

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Renderer(Protocol):
	def title_spacing(self) -> str:
		...
	# more data / methods that are required for renderers

@runtime_checkable
class Document(Protocol):
	def format_title(self, renderer: Renderer) -> str:
		...
	def format_body(self, renderer: Renderer) -> str:
		...
	# more data / methods that define the protocol

def render(document: Document, renderer: Renderer):
	if not isinstance(document, Document):  # optional depending on whether you expect your users to do static type checking in CI or not.
		raise TypeError("'document' needs to implement the 'Document' protocoll documented here: ...")
```
