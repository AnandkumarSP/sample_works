"""Module defining the descriptors supported"""

from types import *

class MyTrait(object):
    """Base descriptor class"""
    value = None
    type = None
    label = None

    def __init__(self, value=None):
        if value and isinstance(value, self.type):
            self.value = value
        elif value:
            raise ValueError("{value} is not a valid default for {name}.".format(value=value, name=self.__class__.__name__))

    def update_instance_class_traits(self, instance):
        if '__is_class' in instance.__class_traits:
            cls_traits = {}.update(instance.__class_traits)
            cls_traits.pop('__is_class', None)
            instance.__class_traits = cls_traits

    def set_default_value(self):
        if not isinstance(self.value, dict):
            self.value = {}

    def __get__(self, instance, owner):
        if instance:
            if isinstance(instance, object):
                self.update_instance_class_traits(instance)
                return instance.__class_traits[self.label]
            else:
                return self.value[instance]
        else:
            return self.value[None]
    
    def __set__(self, instance, value):
        if isinstance(value, self.type):
            if instance:
                if isinstance(instance, object):
                    self.update_instance_class_traits(instance)
                    instance.__class_traits[self.label] = value
                else:
                    self.set_default_value()
                    self.value[instance] = value
            else:
                self.set_default_value()
                self.value[None] = value
        else:
            msg = "The '{attr_name}' attribute of '{class_name}' instance " \
                  "must be a {valid_types}. But an instance of {specified_type} " \
                  "is specified.".format(attr_name=self.label,
                                         class_name=instance.__class__.__name__,
                                         valid_types=self.type,
                                         specified_type=type(value))
            raise ValueError(msg)

class MyStr(MyTrait):
    type = StringType
    value = ""

class MyBool(MyTrait):
    type = BooleanType
    value = False

class MyInt(MyTrait):
    type = IntType
    value = 0

class MyFloat(MyTrait):
    type = FloatType
    value = 0.0

class MyComplex(MyTrait):
    type = ComplexType
    value = 0 + 0j

class MyTuple(MyTrait):
    type = TupleType
    value = ()

class MyList(MyTrait):
    type = ListType
    value = []

class MyDict(MyTrait):
    type = DictType
    value = {}

class MyInstance(MyTrait):
    type = None
    value = None

    def __init__(self, trait_types=None, value=None):
        self.type = trait_types
        self.value = value
