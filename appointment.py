class Appointment:
    """
    Represents an appointment scheduled between a patient and a doctor.
    """
    def __init__(self, appointment_id, patient, doctor, date, time):
        # Private attributes (Encapsulation)
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__doctor = doctor
        self.__date = date
        self.__time = time
        self.__status = "Scheduled"
        
    @property
    def appointment_id(self):
        return self.__appointment_id
        
    @property
    def patient(self):
        return self.__patient
        
    @property
    def doctor(self):
        return self.__doctor
        
    @property
    def date(self):
        return self.__date
        
    @property
    def time(self):
        return self.__time
        
    @property
    def status(self):
        return self.__status
        
    def update_status(self, new_status):
        """Updates the status of the appointment."""
        self.__status = new_status
        
    def display_details(self):
        """Returns string representation of the appointment."""
        return f"Appointment ID: {self.appointment_id} | Patient: {self.patient.name} | Doctor: {self.doctor.name} | Date: {self.date} | Time: {self.time} | Status: {self.status}"
