"""Module defining the top-level class and its functions for data-validation 
and event handling"""

from traceback import print_stack

from descriptors import MyTrait


class DescriptorOwner(type):
    def __new__(cls, name, bases, attrs):
        # find all descriptors, auto-set their labels
        for n, v in attrs.items():
            if isinstance(v, MyTrait):
                v.label = n
            elif isinstance(v, type) and MyTrait in v.__bases__:
                attrs[n] = v()
                attrs[n].label = n
        return super(DescriptorOwner, cls).__new__(cls, name, bases, attrs)

class MyTraitClass(object):
    __metaclass__ = DescriptorOwner
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def add_mytrait_attribute(self, name, value, trait_type=None):
        #a.add_mytrait_attribute("varc", 3, MyInt)
        #a.add_mytrait_attribute("vard", MyInt(3))
        #a.add_mytrait_attribute("vare", 4)  ==> Will not check for type
        if isinstance(value, type):
            raise ValueError("Attribute of {name} must be an instance. Instead a type is specified.".format(name=name))
        elif isinstance(value, MyTrait):
            trait_type = value
            value = trait_type.value
        elif isinstance(trait_type, type):
            trait_type = trait_type()
        if trait_type and isinstance(trait_type, MyTrait):
            if not isinstance(value, trait_type.type):
                raise ValueError("Attribute cannot be added as the value and MyTrait type does not match.")
            elif trait_type:
                trait_type.value = value
                trait_type.label = name
                setattr(self.__class__, name, trait_type)
        else:
            setattr(self.__class__, name, value)
