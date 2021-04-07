"""
The observer pattern (Dependents pattern, Publish-Subscribe pattern):
Classification: Behavioral
Description:
Provides a way to define a one to many relationship between a set of objects.
When the state of one changes, its dependants are notified.
"""
"""
subject handles the attached obervers (1+) and norifications
observer handles updates received from the subject

Observer Pattern structure

#######################                                 #######################
#     <interface>     #                                 #     <interface>     #
#      AbsSubject     # ----------------------------->  #      AbsObserver    #
#      Attributes     #                                 #      Attributes     #
#      Operations     #                                 #      Operations     #
# - Attach(Observer)  #   ######################        # - Update()          #
# - Detach(Observer)  #   # For each observer  #        #######################
# - Notify()          # - # call it's Update() #                  ^
#######################   # method.            #                  |
            ^             ######################                  |
            |                                                     |
            |                                                     |
#######################                                 #######################
#   ConcreteSubject   #                                 #   ConcreteObserver  #
#      Attributes     #                                 #      Attributes     #
# - Subject State     #                                 # - Observer State    #
#      Operations     # ----------------------------->  #      Operations     #
# - Attach(Observer)  #                                 # - Update()          #   ######################
# - Detach(Observer)  #                                 ####################### - # Observer State =   #
# - GetState()        #                                                           # subject.GetState() #
# - Notify()          #   ########################                                ######################
####################### - # return Subject State #
                          ########################
"""

import abc


class AbsObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, value):
        pass

    def __enter__(self):
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass


class AbsSubject(metaclass=abc.ABCMeta):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError("Observer not derived from AbsObserver")
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._observers.clear()


class KPIs(AbsSubject):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()


class CurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis) -> None:
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print(
            f"Current kpis:\n"
            f"Open tickets: {self.open_tickets}\n"
            f"New tickets: {self.new_tickets}\n"
            f"Closed tickets: {self.closed_tickets}\n"
        )

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)


class ForecastKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis) -> None:
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print(
            f"Forecast kpis:\n"
            f"Open tickets: {self.open_tickets}\n"
            f"New tickets: {self.new_tickets}\n"
            f"Closed tickets: {self.closed_tickets}\n"
        )

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)


with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):

        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(250, 110, 50)
        kpis.set_kpis(22, 32, 63)

print("\nExited context managers \n")
kpis.set_kpis(150, 110, 120)

"""
What have been achieved:
- Implemented the observer pattern,
- Separated the corners of subjects and observer (simplified main program),
- Easy to add new observers and keep them separate,
- Thanks to the context manager we don't need to care about detaching observers

What can be fixed:


Summary:
- Simple way to define a one-to-many relationship,
- When one changes, the many are notified,
- Applicable for example in GUIs,
- MVC pattern uses this pattern (Model = Subject, View = Observer)
- Extra logic in AbsSubcject notify method enables "push" notifications

"""
