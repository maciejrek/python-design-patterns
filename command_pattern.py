"""
The command pattern (Action Pattern, Transaction Pattern):
Classification: Behavioral
Description:
Provides a way to encapsulate a request as an object.
Parameterize objects with different requests.
Provides simple way to support queues and logs.
"""
"""
What do we get ?
- Commands are encapsulated in separate ConcreteCommand,
- Information is hidden (client can invoke without knowing and details),
- Easy to add new commands.

Command Pattern structure

#######################      ####################               ####################
#        Client       #      #      Invoker     #               #   <interface>    #
#      Attributes     #      #    Attributes    # ------------> #    Attributes    #
#      Operations     #      #    Operations    #               #    Operations    #
#######################      # - set_command()  #               # - execute()      #
    |           |            ####################               # - undo()         #
    |           |                                               ####################
    |           |                                                       ^
    |           |           ####################                        |
    |           |           #     Receiver     #                #####################
    |           ----------> #    Attributes    # <-----------   #  ConcreteCommand  #
    |                       #    Operations    #                #     Attributes    #
    |                       # - action()       #                #     Operations    #         #########################
    |                       ####################                # - execute()       #  -----> # def execute():        #
    |                                                           # - undo()          #         #     receiver.action() #
    --------------------------------------------------------->  #####################         #########################

"""
import abc
import sys


class AbsCommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass


class AbsOrderCommand(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def description(self):
        pass


class CreateOrder(AbsCommand, AbsOrderCommand):
    name = "CreateOrder"
    description = "Create Order"

    def __init__(self, args) -> None:
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        # Simulate db update
        print("Updated Database")

        # Simulate logging the update
        print(f"Logging: Updated qty from {oldqty} to {self.newqty}")


class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = "UpdateQuantity"
    description = "UpdateQuantity number"

    def __init__(self, args) -> None:
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        # Simulate db update
        print("Updated Database")

        # Simulate logging the update
        print(f"Logging: Updated qty from {oldqty} to {self.newqty}")


class ShipOrder(AbsCommand, AbsOrderCommand):
    name = "ShipOrder"
    description = "Ship Order"

    def __init__(self, args) -> None:
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        # Simulate db update
        print("Updated Database")

        # Simulate logging the update
        print(f"Logging: Updated qty from {oldqty} to {self.newqty}")


class NoCommand(AbsCommand):
    """
    Example of null pattern
    """

    def __init__(self, args) -> None:
        self._command = args[0]

    def execute(self):
        print(f"No command named {self._command}")


def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return {cls.name: cls for cls in commands}


def print_usage(commands):
    print("Usage:python -m Command CommandName [arguments]")
    print("Commands:")
    for command in commands.values():
        print(f"    {command.description}")


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()
if len(sys.argv) < 2:
    print_usage(commands)
    exit()

command = parse_command(commands, sys.argv[1:])
command.execute()

"""
What have been achieved:


What can be fixed:


Summary:
- Encapsulate behavior,
- Separate command logic from the client,
- Add additional capabilities (like validation or undo),
- Usefull in building menus

"""
