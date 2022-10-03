# Spin example components

This repository contains a list of Spin HTTP components in various
programming languages.
To explore a component, read the accompanying section in this readme,
and the corresponding component in `spin.toml`, and the code directory
associated with the component.

pre-requisites:

1. [tinygo](https://tinygo.org/getting-started/install/)
2. [zig](https://ziglang.org/learn/getting-started/#installing-zig)

To build and run:

```
$ make build serve
```

## `python-hello`: An experimental Python component

This is a very early experiment for running Python as a Spin component.
It is based on the work done in <https://github.com/fermyon/wagi-python> and
<https://github.com/singlestore-labs/python-wasi>:

```python
import cgi

print('Content-Type: text/plain; charset=UTF-8')
print('Status: 200')
print()

print('Hello, from Python!')

params = cgi.parse()
print(params)
```

Sending a request to the Python component, we can see the result of the script
above being executed:

```
$ curl -i 'localhost:3000/python-hello?abc=def'
HTTP/1.1 200 OK
content-type: text/plain; charset=UTF-8
content-length: 37
date: Wed, 30 Mar 2022 13:44:24 GMT

Hello, from Python!
{'abc': ['def']}
```

# Running Python in Spin

This demo is based on https://github.com/fermyon/wagi-python and
https://github.com/singlestore-labs/python-wasi.
