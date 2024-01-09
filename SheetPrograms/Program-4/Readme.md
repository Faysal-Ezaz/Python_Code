# Changes have to be made to the code as it doesnot fullfill the given problem statement.

# Create a binary file with name and roll number. Search for a given rollNumber abd display the name, if not found display appropriate message. 
##Replit Link: https://replit.com/@FaysalEzaz/Program-4#main.py
## Explanation:   
<ol>
  <li>Import pickle
    <ul>
      <li>This module is used for serializing and deserializing Python objects for binary file storage.</li>
    </ul>
  </li>  
  
  <li>create_file() function:
    <ul>
      <li>Opens the file 'student_records.dat' in binary write mode ('wb').</li>
      <li>Loops to get name and roll number from the user.</li>
      <li>Uses pickle.dump() to write student data as a dictionary to the file.</li>
    </ul>
  </li>  
  
  <li>search_record(roll_number) function:
    <ul>
      <li>Opens the file in binary read mode ('rb').</li>
      <li>Uses a while True loop and try-except block to handle potential EOFError.</li>
      <li>Reads student data from the file using pickle.load().</li>
      <li>Compares the roll number with the search input.</li>
      <li>Returns the name if found, otherwise returns None.</li>
    </ul>
  </li>  
  
  <li>Main Part: 
    <ul>
      <li>Calls create_file() to create the file and initially add student records.</li>
      <li>Loops to get roll number input for searching.</li>
      <li>Calls search_record() to find the matching name.</li>
      <li>Prints the name if found, otherwise prints a "not found" message.</li>
    </ul>
  </li>
</ol>

