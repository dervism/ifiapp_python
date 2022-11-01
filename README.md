# ifiapp-python

## How to use PyBuilder

1. Generate a new project:
   `pyb --start-project`
2. List all possible commands:
   `pyb -t`
3. Build, test and analyze the project:
   `pyb` or `pyb -v` for verbose output
4. Install all dependencies:
   `pyb install_build_dependencies`

## Setup a Python project with PyBuilder

1. Make to have Python installed
2. Install PyBuilder: `pip3 install pybuilder`
3. Continue from the section "Creating PyBuilder Project" in the PyBuilder tutorial: https://pybuilder.io/documentation/tutorial

_PS: You do not need to activate virtualenv (venv) for PyBuilder as mentioned in the tutorial. PyBuilder deals with venv itself._

## Setup Python in Intellij

After installing PyBuilder and completing the tutorial. Make sure to correctly set up your editor. Here is how you do with IntelliJ IDEA:

https://www.jetbrains.com/help/idea/configuring-local-python-interpreters.html

_PS: IntelliJ IDEA isn't fully compatible with PyBuilder. You might receive warnings in IDEA on `import` statements in your code. It's safe to ignore those warnings._