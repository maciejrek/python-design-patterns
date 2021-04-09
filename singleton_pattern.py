"""
The singleton pattern (also known as):
Classification: Creational
Description:
Can be used to ensure a class has only one instance.
Controls access to limited resuorce, provide a global point of access and
is responsible for its one instance.

"""
import datetime

# Classic singleton pattern


class Singleton(object):
    ans = None

    @staticmethod
    def instance():
        if "_instance" not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instance


s1 = Singleton.instance()
s2 = Singleton.instance()

assert s1 is s2
s1.ans = 42
assert s1.ans is s2.ans
print("Passed")


class Logger(object):
    log_file = None

    @staticmethod
    def instance():
        if "_instance" not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance

    def open_log(self, path):
        self.log_file = open(path, mode="w")

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f"{now} {log_record}"
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()


logger = Logger.instance()
logger.open_log("my.log")
logger.write_log("Logging with classic Singleton pattern")
logger.close_log()

with open("my.log", "r") as f:
    for line in f:
        print(line)
"""
Downsides:
- Violates Single Responsibility Principle:
look after own instantiation, then hold and proccess that state,
- Non-standard class access,
- Harder to test (hard to mock for example),
- Carry global state,
- Hard to sub-class,
- Singletons are considered harmful
"""
"""
What'll we do now:
- Fix the Single Responsibility problem,
- Build a base class for all singletons,
- Inherit from the base class for each one,
- Fix non-standard instance access
- Other problems remain
"""
# Singleton pattern with a base class


class Singleton2(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger2(Singleton2):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode="w")

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f"{now} {log_record}\n"
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()
        self.log_file = None


logger = Logger2("my_second.log")
logger.write_log("Logging with classic Singleton pattern")
logger2 = Logger2("**ignored**")
logger2.write_log("Another log record")
logger.close_log()

with open("my_second.log", "r") as f:
    for line in f:
        print(line, end="")


# Singleton pattern with metaclass
"""
Metaclass controls building of a class
(inherits from type not object)
"""


class Singleton3(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances.update({cls: instance})
        return cls._instances.get(cls)


class Logger3(metaclass=Singleton3):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode="w")

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f"{now} {log_record}\n"
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()
        self.log_file = None


logger = Logger3("my_third.log")
logger.write_log("Logging with classic Singleton pattern")
logger2 = Logger3("**ignored**")
logger2.write_log("Another log record")
logger.close_log()

with open("my_third.log", "r") as f:
    for line in f:
        print(line, end="")


# The MonoState pattern


class MonoState(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__dict__ = cls._state
        return self


class Logger4(MonoState):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode="w")

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f"{now} {log_record}\n"
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()
        self.log_file = None


logger = Logger4("my_fourth.log")
logger.write_log("Logging with classic Singleton pattern")
logger2 = Logger4("**ignored**")
logger2.write_log("Another log record")
logger.close_log()

with open("my_fourth.log", "r") as f:
    for line in f:
        print(line, end="")

"""
Summary:
- Controlled access to a single instance,
- Reduces the global namespace,
- Subclassible for extended uses,
- Variable number of instances (base class and meta class variants),
- More flexible than a static class (class with no instances),
- MonoState shares all state,
- Can also use a python module,
- Use sparingly. It is Antipattern

"""
