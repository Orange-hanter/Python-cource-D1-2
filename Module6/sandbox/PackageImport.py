import sys

from Module6 import SandboxPac
from Module6.SandboxPac import *
import Module6.SandboxPac


if __name__ == '__main__':
    print(list(sys.modules['Module6.SandboxPac'].__dict__['A'].__dict__))
    print(foo)
    B.bar() #Error because of import * (see SandboxPac/__init__.py)
    SandboxPac.B.bar()
