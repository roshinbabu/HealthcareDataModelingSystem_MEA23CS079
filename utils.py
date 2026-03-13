from abc import ABC, abstractmethod

class Person(ABC):
    """
    Abstract Base Class representing a Person.
    Demonstrates Abstraction and Inheritance.
    """
    def __init__(self, person_id, name, contact):
        # Protected attributes (Encapsulation)
        self._person_id = person_id
        self._name = name
        self._contact = contact

    @property
    def person_id(self):
        """Getter for person ID"""
        return self._person_id

    @property
    def name(self):
        """Getter for person name"""
        return self._name

    @property
    def contact(self):
        """Getter for person contact"""
        return self._contact

    @abstractmethod
    def display_details(self):
        """Abstract method to display person details (Polymorphism)"""
        pass
