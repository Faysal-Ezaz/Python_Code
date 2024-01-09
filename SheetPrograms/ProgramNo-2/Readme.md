# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file. 

### Explanation: 

<ol>
  <li>Opening and Reading the file: 
    <ul>
      <li>with open('your_file.txt', 'r') as file: opens the file in read mode.</li>
      <li>text = file.read() reads the entire content of the file into the text variable</li>
    </ul>
  </li>
  <li>Counting Characters:
    <ul>
      <li>vowels and consonants strings store vowel and consonant characters, respectively.</li>
      <li>vowel_count, consonant_count, uppercase_count, and lowercase_count variables are initialized to 0 for counting.</li>
      <li>The for loop iterates over each character in the text.
        <ul>
          <li>If a character is in vowels, vowel_count is incremented.</li>
          <li>If a character is in consonants, consonant_count is incremented.</li>
          <li>char.isupper() and char.islower() check for uppercase and lowercase characters, respectively, and increment the corresponding counts.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Printing Results:
    <ul>
      <li>
        The final counts for each category are printed using f-strings.</ul> 
      </li>
  </li>

  # Replit Link: 
  https://replit.com/@FaysalEzaz/Program2#main.py
  
</ol>
