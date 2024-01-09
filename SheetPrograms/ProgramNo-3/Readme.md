# Remove all the lines that contain the character 'a' in a file and write it to another file.  

## Replit Link: https://replit.com/@FaysalEzaz/Program-3#main.py 

<ol>
  <li>Opening Files:
    <ul>
      <li>with open('input_file.txt', 'r') as input_file, open('output_file.txt', 'w') as output_file:
        <ul>
          <li>This line simultaneously opens two files using the with statement, ensuring proper file closure even if errors occur:
            <ul>
              <li>input_file.txt is opened in read mode ('r') to access its contents.</li>
              <li>output_file.txt is opened in write mode ('w') to create a new file or overwrite an existing one.</li>
              <li>The as keyword assigns these opened file objects to the variables input_file and output_file, respectively.</li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Processing Lines:
    <ul>
      <li>for line in input_file:
        <ul>
          <li>This line initiates a loop that iterates over each line in the input_file. In each iteration, the current line is assigned to the variable line.
</li>
        </ul>
      </li>
      <li>if 'a' in line:
        <ul>
          <li>This conditional statement checks if the character 'a' is present within the current line
            <ul>
              <li>If 'a' is found, the condition evaluates to True, and the code within the if block executes.</li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Writing to Output File:
    <ul>
      <li>output_file.write(line)
        <ul>
          <li>This line, nested within the if block, is executed only when a line containing 'a' is encountered. It writes the current line (which contains 'a') to the output_file.</li>
        </ul>
      </li>
    </ul>
  </li>
</ol>
