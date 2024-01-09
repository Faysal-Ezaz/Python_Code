# Create a binary file with name and roll number. Search for a given rollNumber abd display the name, if not found display appropriate message.
import pickle

def create_file():
    with open('student_records.dat', 'wb') as file:
        while True:
            name = input("Enter name (or 'done' to finish): ")
            if name.lower() == 'done':
                break
            roll_number = int(input("Enter roll number: "))
            student_data = {"name": name, "roll_number": roll_number}
            pickle.dump(student_data, file)

def search_record(roll_number):
    with open('student_records.dat', 'rb') as file:
        while True:
            try:
                student_data = pickle.load(file)
                if student_data['roll_number'] == roll_number:
                    return student_data['name']
            except EOFError:  # End of file reached
                return None

create_file()

while True:
    roll_number = int(input("Enter roll number to search (or 0 to exit): "))
    if roll_number == 0:
        break
    name = search_record(roll_number)
    if name:
        print("Name:", name)
    else:
        print("Roll number not found.")
