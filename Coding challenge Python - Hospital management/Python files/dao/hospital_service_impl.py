import pyodbc
import sys
import os

# Add parent directory of 'dao' to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.hospital_service import IHospitalService

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.connection_string = self.get_connection_string()
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def get_connection_string(self):
        server_name = "DESKTOP-GM6QDGG\\SQLEXPRESS"
        database_name = "hospitalmanagement"
        trusted_connection = "yes"
        return f'Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};'

    def getAppointmentById(self, appointmentId):
        self.cursor.execute("SELECT * FROM Appointment WHERE appointmentId = ?", (appointmentId,))
        appointment = self.cursor.fetchone()
        return appointment

    def getAppointmentsForPatient(self, patientId):
        self.cursor.execute("SELECT * FROM Appointment WHERE patientId = ?", (patientId,))
        appointments = self.cursor.fetchall()
        return appointments

    def getAppointmentsForDoctor(self, doctorId):
        self.cursor.execute("SELECT * FROM Appointment WHERE doctorId = ?", (doctorId,))
        appointments = self.cursor.fetchall()
        return appointments

    def scheduleAppointment(self, appointment):
        self.cursor.execute("INSERT INTO Appointment (patientId, doctorId, appointmentDate, description) VALUES (?, ?, ?, ?)",
                            (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description))
        self.connection.commit()
        return True

    def updateAppointment(self, appointment):
        self.cursor.execute("UPDATE Appointment SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ? WHERE appointmentId = ?",
                            (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description, appointment.appointmentId))
        self.connection.commit()
        return True

    def cancelAppointment(self, appointmentId):
        self.cursor.execute("DELETE FROM Appointment WHERE appointmentId = ?", (appointmentId,))
        self.connection.commit()
        return True
    
    def __del__(self):
        # Close database connection when the object is destroyed
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'connection'):
            self.connection.close()
