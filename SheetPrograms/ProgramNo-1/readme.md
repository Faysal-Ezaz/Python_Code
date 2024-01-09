# Read a text file line by line and display each word separated by a '#': 

`with open('your_file.txt', 'r') as file:`
<ol>
  <li>with statement: This is a Python construct that ensures proper file handling. It automatically closes the file even if exceptions or errors occur within the block of code, preventing potential resource leaks.</li>
  <li> <b>open('your_file.txt', 'r')</b> : This part opens the specified file, "your_file.txt" in this case, for reading. Here's how it works:
    <ul>
      <li>
        open(): This function is used to open files in Python. It takes <b>two arguments:</b>
          <ul>
            <li>The first argument is the path to the file you want to open (here, 'your_file.txt').</li>
            <li>The second argument is the mode in which you want to open the file.</li>
          </ul>
      </li>
      <li>
        'r': This is the mode argument, indicating that you want to open the file in read mode. It's essential for reading the contents of a file without modifying it.
      </li>
    </ul>  
  </li>
  <li>
    as file: This assigns the opened file object to the variable file. You'll use this variable to interact with the file within the with block.
  </li>
</ol>  

`for line in file`: 
<ul>
  <li>Iterates over each line in the file, assigning the current line to the <b><i>line</i></b> variable.</li>
</ul>  

`words = line.split()`: 
<ul>
  <li>Splits the current line into a list of words using spaces as delimiters.</li>
</ul>  

`print("#".join(words))`: 
<ul>
  <li>Joins the words in the words list with the "#" character as a separator.</li>
  <li>Prints the resulting string to the console.</li>
</ul>
