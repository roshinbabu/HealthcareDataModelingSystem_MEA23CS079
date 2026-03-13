# Healthcare Data Modeling System

## Project Title
Healthcare Data Modeling System

## Problem Statement
A system is needed to manage and represent entities within a healthcare environment, such as patients, doctors, medical appointments, prescriptions, and health records. The objective is to efficiently track patient histories and daily hospital interactions using a clean, well-architected Object-Oriented application.

## OOP Concepts Used
1. **Encapsulation**: Used private attributes (e.g., `__age`, `__gender`, `__patients`) with getter and setter properties to restrict direct access to data states.
2. **Inheritance**: The `Patient` and `Doctor` classes inherit shared attributes (`person_id`, `name`, `contact`) from the abstract `Person` class.
3. **Abstraction**: An abstract base class `Person` ensures child classes enforce common configurations, leveraging the Python `abc` module.
4. **Polymorphism**: Overridden abstract method `display_details()` in child subclasses output differing formats explicitly tied to the underlying instances.

## Installation Instructions
1. Ensure you have Python 3.7+ installed.
2. Navigate to the project directory:
   ```bash
   cd HealthcareDataModelingSystem
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: This project strictly relies on standard Python libraries, so no additional downloads are needed).*

## Execution Steps
To run the CLI application with an interactive menu, simply execute:
```bash
python main.py
```

## Output Example
```text
Initializing system with sample data...

========================================
   Healthcare Data Modeling System
========================================
1. Add Patient
2. Add Doctor
3. Schedule Appointment
...
10. Exit
========================================
Enter your choice (1-10): 4

--- Patients List ---
Patient ID: P001 | Name: Charlie Brown | Age: 35 | Gender: Male | Contact: 555-123-4567
```
