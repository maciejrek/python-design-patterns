"""
Design patterns clasification:
Creational - creating things, in oop: objects
Structural - helps create relationships between objects
Behavioral - helps with objects interactions
"""
"""
Solid principles of OOP:
- Single responsibility,
- Open-closed:
 class should be open for extension but closed for modification,
- Liskov substitution:
 objects of a superclass shall be replaceable with objects of its subclasses without breaking the application,
- Interface segregation:
 many specific interfaces are better than one 'do it all',
- Dependecy inversion:
 high level modules should not depend on low level modules; both should depend on abstractions.
 Abstractions should not depend on details. Details should depend upon abstractions.
"""
"""
Abstract Base Class definition in python

import abc


class MyABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_something(self, value):
        pass

    @abc.abstractproperty
    def some_property(self):
        pass


class MyClass(MyABC):
    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        self._myprop *= 2 + value

    @property
    def some_property(self):
        return self._myprop
"""
