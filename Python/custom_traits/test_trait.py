from traits.api import *
from traitsui.api import TextEditor
from api import *
import gc
from PyQt4 import QtGui

class My(object):
    """Base descriptor class"""
    value = None

    def __init__(self, value=None, **kwargs):
        self.value = value

    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        self.value = value

class T(MyTraitClass):
    var = MyStr
    vara = MyStr('abcd')

class A(HasTraits):
    a = Str('hhh')
    b = Int
    c = Float
A.configure_traits()
t = T()
tt = T()
print T.__dict__
print t, tt
print isinstance(A, type)
