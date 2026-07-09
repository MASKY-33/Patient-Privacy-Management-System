import json



patient = {"name": "Zack", "citizenServiceNumber": "BSN-123456", "blood_group": "A+"}


with open("patient.json", "w") as file:
    json.dump(patient, file)
    
with open("patient.json", "r") as file:
    loaded_data = json.load(file)
print(f"\n Current database info: {loaded_data} \n")
