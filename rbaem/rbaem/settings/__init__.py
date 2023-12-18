import os
from .prod import *
if os.environ.get("DEBUG"):
    print("Local setting")
    from .local import *
