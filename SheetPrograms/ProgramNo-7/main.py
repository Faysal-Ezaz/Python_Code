class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to hold the stack items

    def is_empty(self):
        return self.items == []  # Check if the stack is empty

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if self.is_empty():
            return "Stack is empty"  # Handle the case of an empty stack
        return self.items.pop()  # Remove and return the top item

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]  # Return the top item without removing it

    def size(self):
        return len(self.items)  # Return the number of items in the stack

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Popped item:", stack.pop())  # Output: 3
print("Top item:", stack.peek())   # Output: 2
print("Stack size:", stack.size())  # Output: 2
