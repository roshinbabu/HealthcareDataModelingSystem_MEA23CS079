from patient import Patient
from doctor import Doctor
from appointment import Appointment
from prescription import Prescription
from medical_record import MedicalRecord

class Hospital:
    """
    Main management class for the Healthcare Data Modeling System.
    Demonstrates encapsulation by coordinating among core classes.
    """
    def __init__(self, name):
        self.name = name
        # Encapsulated collections
        self.__patients = {}  # patient_id -> Patient
        self.__doctors = {}   # doctor_id -> Doctor
        self.__appointments = {} # appointment_id -> Appointment
        
        # ID counters to auto-generate IDs
        self.__patient_counter = 1
        self.__doctor_counter = 1
        self.__appointment_counter = 1
        self.__prescription_counter = 1
        self.__record_counter = 1

    def add_patient(self, name, contact, age, gender):
        p_id = f"P{self.__patient_counter:03d}"
        patient = Patient(p_id, name, contact, age, gender)
        self.__patients[p_id] = patient
        self.__patient_counter += 1
        return patient

    def add_doctor(self, name, contact, specialty, experience):
        d_id = f"D{self.__doctor_counter:03d}"
        doctor = Doctor(d_id, name, contact, specialty, experience)
        self.__doctors[d_id] = doctor
        self.__doctor_counter += 1
        return doctor

    def schedule_appointment(self, patient_id, doctor_id, date, time):
        if patient_id not in self.__patients or doctor_id not in self.__doctors:
            return None
        a_id = f"A{self.__appointment_counter:03d}"
        appt = Appointment(a_id, self.__patients[patient_id], self.__doctors[doctor_id], date, time)
        self.__appointments[a_id] = appt
        self.__appointment_counter += 1
        return appt

    def generate_prescription(self, appointment_id, medications, instructions):
        if appointment_id not in self.__appointments:
            return None
        appt = self.__appointments[appointment_id]
        pr_id = f"PR{self.__prescription_counter:03d}"
        prescription = Prescription(pr_id, appt, medications, instructions)
        self.__prescription_counter += 1
        return prescription

    def store_medical_record(self, patient_id, diagnosis, treatment, date):
        if patient_id not in self.__patients:
            return None
        patient = self.__patients[patient_id]
        rec_id = f"MR{self.__record_counter:03d}"
        record = MedicalRecord(rec_id, patient, diagnosis, treatment, date)
        patient.add_medical_record(record)
        self.__record_counter += 1
        return record

    def get_all_patients(self):
        return self.__patients.values()

    def get_all_doctors(self):
        return self.__doctors.values()

    def get_all_appointments(self):
        return self.__appointments.values()

    def display_hospital_data(self):
        print(f"Hospital Name: {self.name}")
        print(f"Total Patients: {len(self.__patients)}")
        print(f"Total Doctors: {len(self.__doctors)}")
        print(f"Total Appointments: {len(self.__appointments)}")
