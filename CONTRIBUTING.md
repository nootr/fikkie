# Contribution guidelines

First of all, thank you very much for taking the time to contribute! :heart: Whether
it's a feature request, bug/issue or a patch, it's all very much appreciated.

To contribute, just fork this repository and create a Pull Request if you've written a
patch. Create an issue in GitHub if you've found a bug or have a feature request.


## Fikkie philosophy

Fikkie was created to be simple, to be more specific:

**It should be as easy to install and configure as possible.** It should not be much
more work than having set up an SSH connection to a host using a private key or creating
a Telegram bot.

**It should be as lightweight as possible.** Fikkie should be able to run on your
*busybox*-powered toaster without any resource problems.

**It should be able to notify users using the tools they're comfortable with.** This
also means that it should be really easy to write a new notifier.


## Writing a bug report

Bug reports are greatly appreciated! In order to help you as much as possible, please
add the following info:

* The error/traceback
* Fikkie version
* Fikkie configuration
* Python version
* Operating system


## Setting up a development environment

The fikkie documentation contains [a guide on how to set up a development
environment](https://nootr.github.io/fikkie/development).


## Code conventions

Code should always be approved by the `black` linter using its defaults.

Make sure you add as many docstrings to your classes and methods and format them as
follows:

```python
def foo():
    """Single-line docstrings should simply be enclosed by three quotes."""
    pass

class Bar:
    """
    Multi-line docstrings should have the quotes on separate lines.

    Make sure the first line of the docstring summarizes the method or class and is
    followed by an empty newline.
    """
    pass
```

Also, aim to write your code so that it's readable enough to eliminate the need for
comments. When you do write a comment and it's not an instruction for `black` or
`mypy`, prefix it with `TODO:` or `NOTE:`.


## Tests

It might seem a bit neurotic to maintain a 100% code coverage, but it's actually not
that bad. Our goal is not to test all code, but to test all of the code that needs to
be tested.

This means that code that doesn't need to be tested needs to be marked with the
following comment:

```python
def foo(x):  # pragma: no cover - no complexity here
    return bar.baz(x+1)
```


## Version numbers

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
