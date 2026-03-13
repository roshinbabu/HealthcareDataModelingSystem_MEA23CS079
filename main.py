import sys
from hospital import Hospital

def display_menu():
    print("\n" + "="*40)
    print("   Healthcare Data Modeling System")
    print("="*40)
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Schedule Appointment")
    print("4. View Patients")
    print("5. View Doctors")
    print("6. View Appointments")
    print("7. Generate Prescription")
    print("8. Store Medical Record")
    print("9. Display Hospital Data")
    print("10. Exit")
    print("="*40)

def main():
    hospital = Hospital("City General Hospital")
    
    # Adding initial data for demonstration purposes
    print("Initializing system with sample data...")
    hospital.add_doctor("Alice Smith", "123-456-7890", "Cardiology", 10)
    hospital.add_doctor("Bob Jones", "098-765-4321", "Neurology", 15)
    hospital.add_patient("Charlie Brown", "555-123-4567", 35, "Male")
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-10): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 10.")
            continue

        if choice == 1:
            name = input("Enter Patient Name: ")
            contact = input("Enter Contact Number: ")
            try:
                age = int(input("Enter Age: "))
            except ValueError:
                print("Invalid age!")
                continue
            gender = input("Enter Gender: ")
            patient = hospital.add_patient(name, contact, age, gender)
            print(f"Successfully added {patient.display_details()}")

        elif choice == 2:
            name = input("Enter Doctor Name: ")
            contact = input("Enter Contact Number: ")
            specialty = input("Enter Specialty: ")
            try:
                exp = int(input("Enter Experience (Years): "))
            except ValueError:
                print("Invalid experience!")
                continue
            doctor = hospital.add_doctor(name, contact, specialty, exp)
            print(f"Successfully added {doctor.display_details()}")

        elif choice == 3:
            patient_id = input("Enter Patient ID (e.g., P001): ").upper()
            doctor_id = input("Enter Doctor ID (e.g., D001): ").upper()
            date = input("Enter Date (YYYY-MM-DD): ")
            time = input("Enter Time (HH:MM): ")
            appt = hospital.schedule_appointment(patient_id, doctor_id, date, time)
            if appt:
                print(f"Appointment Scheduled: {appt.display_details()}")
            else:
                print("Error: Invalid Patient ID or Doctor ID.")

        elif choice == 4:
            patients = hospital.get_all_patients()
            print("\n--- Patients List ---")
            if not patients:
                print("No patients found.")
            else:
                for p in patients:
                    print(p.display_details())

        elif choice == 5:
            doctors = hospital.get_all_doctors()
            print("\n--- Doctors List ---")
            if not doctors:
                print("No doctors found.")
            else:
                for d in doctors:
                    print(d.display_details())

        elif choice == 6:
            appointments = hospital.get_all_appointments()
            print("\n--- Appointments List ---")
            if not appointments:
                print("No appointments scheduled.")
            else:
                for a in appointments:
                    print(a.display_details())

        elif choice == 7:
            appt_id = input("Enter Appointment ID (e.g., A001): ").upper()
            meds_input = input("Enter Medications (comma-separated): ")
            medications = [m.strip() for m in meds_input.split(",")]
            instructions = input("Enter Instructions: ")
            prescription = hospital.generate_prescription(appt_id, medications, instructions)
            if prescription:
                print(f"Prescription Generated: {prescription.display_details()}")
            else:
                print("Error: Invalid Appointment ID.")

        elif choice == 8:
            patient_id = input("Enter Patient ID (e.g., P001): ").upper()
            diagnosis = input("Enter Diagnosis: ")
            treatment = input("Enter Treatment: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            record = hospital.store_medical_record(patient_id, diagnosis, treatment, date)
            if record:
                print(f"Medical Record Stored: {record.display_details()}")
            else:
                print("Error: Invalid Patient ID.")

        elif choice == 9:
            print("\n--- Hospital Data ---")
            hospital.display_hospital_data()

        elif choice == 10:
            print("Exiting system. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice, please select from 1-10.")

if __name__ == "__main__":
    main()
