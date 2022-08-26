print('mymodule')
print('mymodule-init=', __name__)

from . import m1
from . import m2

# from .sub import *
from .sub import sub1

from .m1 import method_m1

method_m1()
