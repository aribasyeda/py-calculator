from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def muliply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": muliply,
  "/": divide,
}

def calculator():
  print(logo)
  
  num1 = float(input("\n 👉 What's the first number?: "))
  
  for key in operations:
    print(key)
  
  should_continue = True
  
  while should_continue:
    
    selected_operation = input("\n 👉 Pick an operation: ")
    num2 = float(input("\n 👉 What's the next number?: "))
    
    selected_function = operations[selected_operation]
    answer = selected_function(num1, num2) 
    
    print(f"{num1} {selected_operation} {num2} = {answer}")
  
    if input(f"\n 👉 Type 'yes' to continue calculating with {answer}, 'n' to start a new calculation, or type 'e' to exit: ").lower() == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
      
calculator()
