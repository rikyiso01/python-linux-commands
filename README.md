# python-linux-commands
Reimplementation of the subprocess module

## Installation

You can install it from [Pypi](https://pypi.org/project/linux-commands) or from the [release section](https://github.com/RikyIsola/python-linux-commands/releases)

## Usage

Simply import the command you want to use
```python3
from linux_commands import ps
print(ps())
```
it will automatically raise any error and it will convert the result into the appropriate python type like a tuple, int or string

Supports commands with subcommands like
```python3
from linux_commands import pip
pip.install('wheel')
```

Supports command piping
```python3
from linux_commands import cat,grep
grep(input=cat('file.txt'))
```

Supports arguments
```python3
from linux_commands import gcc
gcc('file.c',g=True,o='run')
```
