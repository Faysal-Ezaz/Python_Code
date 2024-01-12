# Write a Random number generator that generates random number between 1 and 6 (simulates a dice)

import random

def roll_dice():
  """
  Simulates a dice roll and returns a random number between 1 and 6.
  """

  # Generate a random integer between 1 and 6 (inclusive) using the randint() function
  dice_value = random.randint(1, 6)

  # Return the generated dice value
  return dice_value

# Example usage:
dice_result = roll_dice()
print(f"You rolled a {dice_result}")
