from utils import Person

class Doctor(Person):
    """
    Doctor class inheriting from Person.
    Represents a doctor in the hospital.
    """
    def __init__(self, doctor_id, name, contact, specialty, experience_years):
        # Call to superclass constructor (Inheritance)
        super().__init__(doctor_id, name, contact)
        
        # Private attributes (Encapsulation)
        self.__specialty = specialty
        self.__experience_years = experience_years
        
    @property
    def specialty(self):
        """Getter for doctor's specialty"""
        return self.__specialty
        
    @property
    def experience_years(self):
        """Getter for doctor's experience"""
        return self.__experience_years
        
    def display_details(self):
        """Implementation of the abstract method (Polymorphism)"""
        return f"Doctor ID: {self.person_id} | Name: {self.name} | Specialty: {self.specialty} | Experience: {self.experience_years} years | Contact: {self.contact}"
