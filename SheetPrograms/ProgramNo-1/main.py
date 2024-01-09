# Read a text file line by line and display each word separated by a '#'
with open('your_text_file.txt', 'r') as file:  # Open the file in read mode
  for line in file:  # Iterate over each line in the file
    words = line.split()  # Split the line into words
    print("#".join(words))  # Join the words with "#" and print
