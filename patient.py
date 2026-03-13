from utils import Person

class Patient(Person):
    """
    Patient class inheriting from Person.
    Represents a patient in the hospital.
    """
    def __init__(self, patient_id, name, contact, age, gender):
        # Call to superclass constructor (Inheritance)
        super().__init__(patient_id, name, contact)
        
        # Private attributes (Encapsulation)
        self.__age = age 
        self.__gender = gender
        self.__medical_history = []
        
    @property
    def age(self):
        """Getter for age"""
        return self.__age
        
    @property
    def gender(self):
        """Getter for gender"""
        return self.__gender
        
    def add_medical_record(self, record):
        """Adds a MedicalRecord to the patient's history."""
        self.__medical_history.append(record)
        
    def get_medical_history(self):
        """Returns the patient's complete medical history."""
        return self.__medical_history
        
    def display_details(self):
        """Implementation of the abstract method (Polymorphism)"""
        return f"Patient ID: {self.person_id} | Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Contact: {self.contact}"
