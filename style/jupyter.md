# Basic notebook structure

The project should include this skeleton

```
root/
 - nb/
   - nb1.ipynb
   - utils.py
 - src/
   - __init__.py
   - module.py
```

Where `nb/utils.py` includes

```
# utils.py
import sys
import os

# This can go in a config file
dir_root = '/home/akhil/example/jupyter'  # Your project root

# Add the project root to the system path
sys.path.insert(0, dir_root)
```

Then notebooks can run modules in `src` such as `module.py`

```
# src/module.py
def a():
    print 'Hello World'
```

## Usage

```
# nb/nb1.ipynb
import utils
from src import module

module.a()
> Hello World
```
