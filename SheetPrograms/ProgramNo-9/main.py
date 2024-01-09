# Python code to implement the push operation in a stack using a list:

class Stack:
  def __init__(self):
      self.items = []  # Create an empty list to hold the stack items

  def is_empty(self):
      return self.items == []  # Check if the stack has no items

  def push(self, item):
      """Adds an item to the top of the stack."""
      self.items.append(item)  # Place the item at the end of the list
  # this function can be ignored, this function is to remove the elements from the stack ie the pop() operation: 
  def pop(self): 
    if self.is_empty():
      return "stack is empty"
    return self.items.pop()
# Example usage:
stack = Stack()  # Create a new stack

stack.push(42)  # Add the number 42 to the stack
stack.push("hello")  # Add the string "hello" to the stack

print("Stack items:", stack.items)  # Output: [42, "hello"]

# this part can be ignored: cl
stack.pop()
stack.pop()
print("Stack items:", stack.items)
