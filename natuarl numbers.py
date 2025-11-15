

def is_natural_number(value):
    """
    Checks if the given value is a natural number (1, 2, 3, ...).
    Returns True if yes, False otherwise.
    """
    try:
        num = int(value)  
        return num > 0    
    except ValueError:
        return False  


user_input = input("Enter a number: ").strip()

if is_natural_number(user_input):
    print(f"{user_input} is a natural number.")
else:
    print(f"{user_input} is NOT a natural number.")
