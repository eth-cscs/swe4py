# Interactivity Exercise

Currently, our project is a bit annoying to try out interactively in IPython or Jupyter. See for yourself!

```
$ uv run ipython
>>> import hpc_lib
>>> hpc_lib<Tab><Tab>
```

Nothing! But look, it's not because it's empty:

```
>>> import hpc_lib.hello
>>> hpc_lib.hello.hello()
"Hello from hpc-lib"
```

1. What can we do to fix that?
2. What more can we do to improve the experience?
