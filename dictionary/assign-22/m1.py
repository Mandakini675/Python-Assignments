# 1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

# A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

# The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

# Key → Patient ID
# Value → Dictionary containing patient details

# Each patient record should contain:

# Patient Name
# Age
# Gender
# Disease
# Doctor Name
# Sample Data Structure
# {
# 101:{
#     "name":"Ajay",
#     "age":35,
#     "gender":"Male",
#     "disease":"Fever",
#     "doctor":"Dr. Sharma"
# },
# 102:{
#     "name":"Ravi",
#     "age":42,
#     "gender":"Male",
#     "disease":"Diabetes",
#     "doctor":"Dr. Gupta"
# }
# }
# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# =====================================
#  HOSPITAL PATIENT MANAGEMENT SYSTEM
# =====================================

# 1. Add New Patient
# 2. Search Patient
# 3. Update Patient Disease
# 4. Delete Patient Record
# 5. Display All Patients
# 6. Count Total Patients
# 7. Display Patients By Disease
# 8. Display Oldest Patient
# 9. Display Youngest Patient
# 10. Exit

# Functional Requirements
# 1. Add New Patient

# Accept the following information from the user:

# Patient ID
# Patient Name
# Age
# Gender
# Disease
# Doctor Name

# Store the record in the nested dictionary.

# Validation:
# If the Patient ID already exists, display:

# Patient ID already exists.

# 2. Search Patient

# Accept Patient ID from the user.

# If the patient exists, display complete information.

# Sample Output

# Patient ID : 101
# Name       : Ajay
# Age        : 35
# Gender     : Male
# Disease    : Fever
# Doctor     : Dr. Sharma

# If Patient ID is not found:

# Patient Record Not Found

# 3. Update Patient Disease

# Accept Patient ID.

# If found:

# Ask for new disease.
# Update the disease information.

# Sample Output

# Disease Updated Successfully
# 4. Delete Patient Record

# Accept Patient ID.

# If found:

# Remove the patient record.

# Sample Output

# Patient Record Deleted Successfully

# Otherwise:

# Patient Not Found
# 5. Display All Patients

# Display all patient records in a formatted manner.

# Sample Output

# --------------------------------
# Patient ID : 101
# Name       : Ajay
# Age        : 35
# Disease    : Fever
# Doctor     : Dr. Sharma
# --------------------------------

# Patient ID : 102
# Name       : Ravi
# Age        : 42
# Disease    : Diabetes
# Doctor     : Dr. Gupta
# 6. Count Total Patients

# Display the total number of patients currently stored.

# Sample Output

# Total Patients : 25
# 7. Display Patients By Disease

# Accept a disease name from the user.

# Display all patients suffering from that disease.

# Sample Output

# Enter Disease : Fever

# 101  Ajay
# 108  Aman
# 115  Neha

# If no patient is found:

# No Patient Found
# 8. Display Oldest Patient

# Find and display the patient having the highest age.

# Sample Output

# Oldest Patient Details

# Patient ID : 110
# Name       : Ravi
# Age        : 68
# Disease    : Diabetes
# Doctor     : Dr. Gupta
# 9. Display Youngest Patient

# Find and display the patient having the minimum age.

# Sample Output

# Youngest Patient Details

# Patient ID : 121
# Name       : Riya
# Age        : 4
# Disease    : Viral Fever
# Doctor     : Dr. Mehta
# 10. Exit

# Terminate the application.

# Sample Output

# Thank You For Using Hospital Patient Management System

#~~~~~~~~~~~~~~~~~~~~~~~~~~
patients={}
def addpatient():
    
        pat_no = int(input("enter the patient id"))
        
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        disease = input("Enter disease: ")
        doctor = input("enter doctors name:")

        details ={
            "name" : name,
            "age":age,
            "disease":disease,
            "doctor":doctor
        }
        patients[pat_no] = details
        return

print("=====================================")
print("HOSPITAL PATIENT MANAGEMENT SYSTEM")
print("=====================================")

while True:
   
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")

    ch = int(input("enter your choice:"))
    match ch:
        case 1:
              addpatient()
              
        case 2:
             pat_id = int(input("enter patient id for search :"))

             if pat_id in patients:
                print("~~~~~~~~~~~~")
                print("Patient ID =",pat_id)
                for k,v in patients[pat_id].items():
                    print(k ,":",v)
                print("~~~~~~~~~~~~")
             else:
                print("Patient not found")

        case 3:
            pat_id = int(input("enter patient id you wanna updatw :"))

            if pat_id in patients:
                newdisease = input("enter updated disease:")
                patients[pat_id]["disease"] = newdisease
                print("Disease Updated Successfully")
            else:
                print("id not found")
        
        case 4:
            pat_id = int(input("enter patient id to delete :"))

            if pat_id in patients:
                patients.pop(pat_id)
                print("Patient Record Deleted Successfully")
            else:
                print("")
                print("Patient Not Found")

        case 5:
            print("---------------------------")
            for pat_id in patients:
                print("Patient ID ",pat_id)

                for k,v in patients[pat_id].items():
                    print(k,":",v)
                print("~~~~~~~~~~~~~")
            print("---------------------------")
            
        case 6:
            
            print("Total Patients :",len(patients))
            

        case 7:
             dis = input("enter the disease: ")        
             for pat_id in patients:
                if patients[pat_id]["disease"]==dis:
                   print("Patient ID -",pat_id,dis)
                 


        case 8:
             print("Oldest Patient Details ")
             
             highest =0
             for pat_id in patients:
                if patients[pat_id]["age"]>highest:
                    highest = patients[pat_id]["age"]
                    idyy = pat_id
             
             print("Patient id :",idyy)
             print("Name :",patients[idyy]["name"])
             print("Age",patients[idyy]["age"])
             print("Disease :",patients[idyy]["disease"])

        case 9:
             print("Oldest Patient Details ")
             
             lowest =float("inf")
             for pat_id in patients:
                if patients[pat_id]["age"]<lowest:
                    lowest = patients[pat_id]["age"]
                    idyy = pat_id
             
             print("Patient id :",patients[idyy])
             print("Name :",patients[idyy]["name"])
             print("Age",patients[idyy]["age"])
             print("Disease :",patients[idyy]["disease"])

        case 10:
           
            print("Thank You For Using Hospital Patient Management System")
            break
        case _:
           print("entered wrong tryyy again")