#!flask36/bin/python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main()
# Shebang will use whatever python executable appears first in the user's $PATH when set this way vs calling the interpreter explicitly with a defined path --> used to be '#!/usr/bin/env python' in this file
