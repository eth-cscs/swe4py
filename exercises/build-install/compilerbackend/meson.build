project(
    'compilerbackend',
    'cpp',
    version: '0.1.0',
    default_options: 'cpp_std=c++17'
)

py = import('python').find_installation()
nanobind_dep = dependency('nanobind', static: true)
py.extension_module(
    'cppext',
    sources: ['src/cpp_extension.cpp'],
    dependencies: [nanobind_dep],
    install: true,
)
