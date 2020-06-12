# Setup Instructions

### WebDriver Setup for *NIX

To install ChromeDriver and geckodriver on Linux, macOS, and other UNIX variants,
simply move them to the `/usr/local/bin/` directory:

```bash
$ mv /path/to/ChromeDriver /usr/local/bin
$ mv /path/to/geckodriver /usr/local/bin
```

This directory should already be included in the system path.
For troubleshooting, see:

* [Setting the path on macOS](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)
* [Setting the path on Linux](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)

### Test WebDriver Setup

To verify correct setup on any operating system, simply try to run them from the terminal:

```bash
$ ChromeDriver
$ geckodriver
```

You may or may not see any output.
Just verify that you can run them without errors.
Use Ctrl-C to kill them.

## Project Setup

1. Clone this repository.
2. Run `pipenv install` to install the dependencies.
3. Run `pipenv run python -m pytest` to verify that the framework can run tests.

If these steps don't work in your project, then try to run without pipenv:

* Install Python packages directly using `pip`.
* Run tests directly using `python -m pytest`.

Next, install [pytest-xdist](https://docs.pytest.org/en/3.0.1/xdist.html),
the pytest plugin for parallel testing:

```bash
$ pipenv install pytest-xdist
```

Finally, run the tests using the following command:

```bash
$ pipenv run python -m pytest -n 3
```

