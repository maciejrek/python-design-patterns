"""
The strategy pattern (also known as the Policy pattern):
Classification: Behavioral
Description:
Provides a way to take a family of algorithms,
encapsulate each one and make them interchangeable
with each other.
"""
"""
Strategy Pattern structure

#######################          #########################
#       Context       #          #       <interface>     #
#      Attributes     #          #        Strategy       #
#      Operations     # -------> #       Attributes      #
# -ContextInterface() #          #       Operations      #
# -__init__(Strategy) #          # -AlgorithmInterface() #
#######################          #########################
                ______________________^__________________________
                |                     |                         |
                |                     |                         |
#########################  #########################  #########################
#    ConcreteStrategy   #  #    ConcreteStrategy   #  #    ConcreteStrategy   #
#       Attributes      #  #       Attributes      #  #       Attributes      #
#       Operations      #  #       Operations      #  #       Operations      #
# -AlgorithmInterface() #  # -AlgorithmInterface() #  # -AlgorithmInterface() #
#########################  #########################  #########################
"""

from abc import ABCMeta, abstractmethod


class Order(object):
    def __init__(self, shipper="missing"):
        self._shipper = shipper

    @property
    def shipper(self):
        return self._shipper


class ShippingCost(object):
    def __init__(self, strategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)


class AbsStrategy(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""
        pass


class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.00


class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 4.00


class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00


order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.00

order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.00

order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.00

"""
What have been achieved:
- Following solid principles,
- Each algorithm can be tested in isolation,
- Easy to test outer code with deterministick mock algorithms,
- No need to use if/elif/else statement for diff costs

What can be fixed:
Order is some kind of object so dependency inversion problem is not fixed yet.
It'll be fixed using factory pattern later

Summary:
- simple way to encapsulate algorithms,
- several techniques available,
- sequences of if/elif are red flag
"""
