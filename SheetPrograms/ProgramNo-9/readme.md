# Python code to implement the push operation in a stack using a list: 

## Explanation: 
<ol>
  <li>Creating the Stack: 
    <ul>
      <li>The Stack class uses a list named self.items to store the stack's elements. This list acts as the underlying data structure for the stack.</li>
      <li>When a Stack object is created, self.items is initialized as an empty list, ready to hold the stack items.</li>
    </ul>
  </li>
  <li>Push Operation:
    <ul>
      <li>The push(self, item) method is responsible for adding an item to the stack.</li>
      <li>It leverages the list's append() method to efficiently add the item to the end of the self.items list.</li>
      <li>This effectively mimics the "push" operation in a stack, where new elements are added to the top.</li>
    </ul>
  </li>
  <li>Handling Empty Stacks: 
    <ul>
      <li>The is_empty(self) method checks if the stack is empty by comparing self.items to an empty list ([]).</li>
      <li>This is essential for validating operations that require a non-empty stack, preventing potential errors</li>
    </ul>
  </li>
</ol>  

## Replit Link: https://replit.com/@FaysalEzaz/Program-9#main.py
