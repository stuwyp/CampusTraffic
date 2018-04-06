import os
import sys

mod = sys.modules.get(__name__)
print mod
print mod.__file__
print os.path.abspath(mod.__file__)
print os.path.dirname(os.path.abspath(mod.__file__))
