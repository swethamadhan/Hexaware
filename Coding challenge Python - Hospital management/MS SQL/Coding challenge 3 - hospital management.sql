create database hospitalmanagement;

use hospitalmanagement;

create table patient (
 patientId INT PRIMARY KEY IDENTITY,
 firstName VARCHAR(255),
 lastName VARCHAR(255),
 dateOfBirth DATE,
 gender VARCHAR(100),
 contactNumber VARCHAR(150),
 address varchar(100)
);

SET IDENTITY_INSERT patient ON;

insert into patient (patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address) values
(1, 'Alice', 'Johnson', '1990-05-15', 'Female', '123-456-7890', '123 Main St, City, Country'),
(2, 'Bob', 'Smith', '1985-09-20', 'Male', '456-789-0123', '456 Elm St, Town, Country'),
(3, 'Charlie', 'Brown', '1978-03-10', 'Male', '789-012-3456', '789 Oak St, Village, Country'),
(4, 'Diana', 'Lee', '1995-12-05', 'Female', '234-567-8901', '234 Maple St, Town, Country'),
(5, 'Eva', 'Martinez', '1982-08-25', 'Female', '567-890-1234', '567 Pine St, City, Country'),
(6, 'Frank', 'Garcia', '1973-07-17', 'Male', '890-123-4567', '890 Cedar St, Village, Country'),
(7, 'Grace', 'Davis', '1998-01-30', 'Female', '345-678-9012', '345 Birch St, City, Country'),
(8, 'Henry', 'Taylor', '1993-06-12', 'Male', '678-901-2345', '678 Oak St, Town, Country'),
(9, 'Ivy', 'Clark', '1980-11-22', 'Female', '901-234-5678', '901 Willow St, Village, Country'),
(10, 'Jack', 'Anderson', '1970-04-03', 'Male', '012-345-6789', '012 Elm St, City, Country');

SET IDENTITY_INSERT patient OFF;

create table doctor (
 doctorId INT PRIMARY KEY IDENTITY,
 firstName VARCHAR(255),
 lastName VARCHAR(255),
 specialization VARCHAR(255),
 contactNumber VARCHAR(150)
);

SET IDENTITY_INSERT doctor ON;

insert into doctor (doctorId, firstName, lastName, specialization, contactNumber)values 
(1, 'John', 'Doe', 'Cardiology', '123-456-7890'),
(2, 'Jane', 'Smith', 'Pediatrics', '456-789-0123'),
(3, 'Michael', 'Johnson', 'Orthopedics', '789-012-3456'),
(4, 'Emily', 'Brown', 'Dermatology', '234-567-8901'),
(5, 'David', 'Lee', 'Neurology', '567-890-1234'),
(6, 'Sarah', 'Taylor', 'Oncology', '890-123-4567'),
(7, 'James', 'Wilson', 'Gastroenterology', '345-678-9012'),
(8, 'Olivia', 'Martinez', 'Psychiatry', '678-901-2345'),
(9, 'Daniel', 'Anderson', 'Endocrinology', '901-234-5678'),
(10, 'Sophia', 'Thomas', 'Rheumatology', '012-345-6789');

SET IDENTITY_INSERT doctor OFF;

create table appointment (
 appointmentId INT PRIMARY KEY IDENTITY,
 patientId INT,
 doctorId INT,
 appointmentDate DATE,
 description varchar(255),
 FOREIGN KEY (patientId) REFERENCES Patient(patientId),
 FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId)
);

SET IDENTITY_INSERT appointment ON;

insert into appointment (appointmentId, patientId, doctorId, appointmentDate, description)
values
(1, 1, 1, '2024-03-22', 'Routine checkup'),
(2, 2, 3, '2024-03-23', 'Consultation for flu symptoms'),
(3, 3, 2, '2024-03-24', 'Follow-up after surgery'),
(4, 4, 4, '2024-03-25', 'Skin condition examination'),
(5, 5, 5, '2024-03-26', 'Headache diagnosis'),
(6, 6, 7, '2024-03-27', 'Colonoscopy procedure'),
(7, 7, 6, '2024-03-28', 'Psychological evaluation'),
(8, 8, 8, '2024-03-29', 'Medication adjustment'),
(9, 9, 9, '2024-03-30', 'Thyroid checkup'),
(10, 10, 10, '2024-03-31', 'Arthritis treatment');

SET IDENTITY_INSERT appointment OFF;