# Shebang will use whatever python executable appears first in the user's $PATH when set this way vs calling the interpreter explicitly with a defined path


#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main()
