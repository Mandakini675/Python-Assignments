
# =====================================================================
# QUESTION 3: HOSPITAL PATIENT TRACKER
# ====================================

# A hospital stores patient records for daily monitoring.

# Fields:
# patient_id, patient_name, age, disease

# Requirements:

# 1. Read N patient records from the user and store them in a list of NamedTuples.

# ---

# 2. Display all patient details.

# ---

# 3. Display patients whose age is above 60 years.

# ---

# 4. Search for a patient using Patient ID.

# ---

# 5. Count the number of patients suffering from a particular disease.

# ---

# Test Case:

# Input:
# Enter number of patients: 4

# P101 Rajesh 65 Diabetes
# P102 Suman 45 Fever
# P103 Mohan 70 Diabetes
# P104 Rita 35 Cold

# Enter Patient ID: P103
# Enter Disease: Diabetes

# Expected Output:
# Patient Found:
# P103 Mohan 70 Diabetes

# Patients Above 60:
# P101 Rajesh 65 Diabetes
# P103 Mohan 70 Diabetes

# Patients with Diabetes:
# 2


from collections import namedtuple
print("=================================================================")
print("             HOSPITAL PATIENT TRACKER")
print("==================================================================")
n= int(input("enter no of hospital ="))

Hosp = namedtuple("patienttracker",["patient_id", "patient_name", "age", "disease"])
hospital =[]
for i in range(n):
    patient_id = input("enter patient_id no =")
    name = input("enter name =")
    age = int(input("enter age ="))
    disease = input("enter disease name =")
    h1 = Hosp(patient_id,name,age,disease)
    hospital.append(h1)
print("="*20)
print("details :")
for x in hospital:
    print(*x)
print("="*20)
pat_id = input("enter patients id :")
dis = input("enter the disease name to search:")
print("="*20)
for i in hospital:
    if i.patient_id ==pat_id:
        print("patient found :")
        print(*i)
        break

print("patients Above 60:")
for x1 in hospital:
    if x1.age>60:
       print(*x1)
print("Patients with ",dis,":")
count=0
for x2 in hospital:  
    if x2.disease ==dis:
         count+=1
    #     print(*x2)
print(count)
print("="*20) 