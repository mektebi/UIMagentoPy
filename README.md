# Setup Instructions

## Python Setup

You can complete this course using any OS: Windows, macOS, Linux, etc.

This course requires Python 3.8 or higher.
You can download the latest Python version from [Python.org](https://www.python.org/downloads/).

This course also requires [pipenv](https://docs.pipenv.org/).
To install pipenv, run `pip install pipenv` from the command line.

You should also have a Python editor/IDE of your choice.
Good choices include [PyCharm](https://www.jetbrains.com/pycharm/)
and [Visual Studio Code](https://code.visualstudio.com/docs/languages/python).

You will also need [Git](https://git-scm.com/) to copy this project code.
If you are new to Git, [try learning the basics](https://try.github.io/).

## WebDriver Setup

For Web UI testing, you will need to install the latest versions of
[Google Chrome](https://www.google.com/chrome/)
and [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/).
You can use other browsers with Selenium WebDriver, but the course will use Chrome and Firefox.

You will also need to install the latest versions of the WebDriver executables for these browsers: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome
and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox.
Each test case will launch the WebDriver executable for its target browser.
The WebDriver executable will act as a proxy between the test automation and the browser instance.
Please use the latest versions of both the browsers and the WebDriver executables.
Older versions might be incompatible with each other.

ChromeDriver and geckodriver must be installed on the
[system path](https://en.wikipedia.org/wiki/PATH_(variable)).

### WebDriver Setup for Windows

To install ChromeDriver and geckodriver on Windows:

1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.
3. Add this folder to the *Path* environment variable. (See [How to Add to Windows PATH Environment Variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).)

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
2. Run `cd tau-intro-selenium-py` to enter the project.
3. Run `pipenv install` to install the dependencies.
4. Run `pipenv run python -m pytest` to verify that the framework can run tests.
5. Create a branch for your code changes. (See *Repository Branching* below.)

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

