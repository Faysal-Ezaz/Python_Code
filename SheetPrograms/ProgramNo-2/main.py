# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.
with open('your_file.txt', 'r') as file:  # Open the file in read mode
  text = file.read()  # Read the entire content of the file

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowel_count = 0
consonant_count = 0
uppercase_count = 0
lowercase_count = 0

for char in text:
  if char in vowels:
      vowel_count += 1
  elif char in consonants:
      consonant_count += 1
  if char.isupper():
      uppercase_count += 1
  elif char.islower():
      lowercase_count += 1

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
print(f"Number of uppercase characters: {uppercase_count}")
print(f"Number of lowercase characters: {lowercase_count}")
