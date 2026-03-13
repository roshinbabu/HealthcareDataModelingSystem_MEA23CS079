class MedicalRecord:
    """
    Represents a medical record for a patient, summarizing past diagnoses and treatments.
    """
    def __init__(self, record_id, patient, diagnosis, treatment, date):
        # Private attributes (Encapsulation)
        self.__record_id = record_id
        self.__patient = patient
        self.__diagnosis = diagnosis
        self.__treatment = treatment
        self.__date = date
        
    def display_details(self):
        """Returns string representation of the medical record."""
        return f"Record ID: {self.__record_id} | Date: {self.__date} | Diagnosis: {self.__diagnosis} | Treatment: {self.__treatment}"
