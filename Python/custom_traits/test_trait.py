from traits.api import *

class CT(HasTraits):
    vara = Str
    
a = CT(vara="abc")
