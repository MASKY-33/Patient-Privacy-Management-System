import json



with open("patient.json", "r") as file:
    loaded_data = json.load(file)

del loaded_data['citizenServiceNumber']

with open("patient.json", "w") as file:
    json.dump(loaded_data, file)

with open("privacy_audit.txt", "a") as file:
    file.write("Sensitive data successfully destroyed in accordance with legislation. \n")