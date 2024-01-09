with open('input_file.txt', 'r') as input_file, open('output_file.txt', 'w') as output_file:
  for line in input_file:
      if 'a' in line:  # Check if 'a' is not present in the line
        output_file.write(line)  # Write the line to the output file
