
import unittest

from api import *

class TestMyTraitClass(unittest.TestCase):
    def test_01_instance_without_param(self):
        class T(MyTraitClass):
            var = MyStr()
        t = T()
        self.assertRaises(ValueError, lambda: setattr(t, "var", 1))
    
    def test_02_instance_with_param(self):
        class T(MyTraitClass):
            var = MyStr()
        t = T(var="abc")
        self.assertEqual("abc", t.var)
        t.var = "abcd"
        self.assertEqual("abcd", t.var)
        self.assertRaises(ValueError, lambda: setattr(t, "var", 1))

    def test_03_instance_without_param(self):
        class T(MyTraitClass):
            var = MyStr()
        t = T()
        t.var = 'abc'
        self.assertEqual('abc', t.var)
    
    def test_04_instance_with_param(self):
        class T(MyTraitClass):
            var = MyStr()
        t = T(var='abc')
        self.assertEqual('abc', t.var)
    
    def test_05_add_mytrait_attribute(self):
        class T(MyTraitClass):
            var = MyStr()
        t = T()
        t.add_mytrait_attribute("vara", 3, MyInt)
        self.assertEqual(3, t.vara)
        self.assertRaises(Exception, lambda: setattr(t, "vara", "value"))
    
    def test_06_add_mytrait_attribute(self):
        class T(MyTraitClass):
            var = MyStr()
        t = T()
        t.add_mytrait_attribute("vara", MyInt(3))
        self.assertEqual(3, t.vara)
        self.assertRaises(Exception, lambda: setattr(t, "vara", "value"))
    
    def test_07_add_mytrait_attribute(self):
        class T(MyTraitClass):
            var = MyStr()
        t = T()
        t.add_mytrait_attribute("vara", 3)
        self.assertEqual(3, t.vara)
        t.vara = "value"
        self.assertEqual("value", t.vara)
    
    def test_08_instance_with_param(self):
        class T(MyTraitClass):
            var = MyList()
        t = T(var=[1,2,3,4])
        self.assertEqual([1,2,3,4], t.var)
        t.var = [1,2]
        self.assertEqual([1,2], t.var)
        self.assertRaises(ValueError, lambda: setattr(t, "var", 1))
    
    def test_09_instance_with_param(self):
        class T(MyTraitClass):
            var = MyDict()
        t = T(var={})
        self.assertEqual({}, t.var)
        t.var = {'a':1, 'b':2}
        self.assertEqual({'a':1, 'b':2}, t.var)
        self.assertRaises(ValueError, lambda: setattr(t, "var", 1))

if __name__ == "__main__":
    unittest.main()
