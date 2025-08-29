# Function to convert string to snake_case format (ex. first_name)
def snake_case(s):
    
    print("snake_case: ", end="")
    
    # For each character (c) in string (s)
    for c in s:
        
        # Checks if the current character in the string is uppercase
        if c[:].isupper() is True:
            # If true then converts it to lowercase and it adds a "_" before the character
            c = c.lower()
            c = "".join(["_", c])

        # Prints the remaining letters 
        print(c, end="")
    
    # New line purposes
    print()

def main():
    # User input for string and strips any blank spaces
    camelCase = input("camelCase: ").strip()

    snake_case(camelCase)
    
main()