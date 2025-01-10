# Initialize an empty dictionary
my_dict = {}

# Ask the user for the number of entries they want to add
n = int(input("How many entries do you want to add? "))

# Loop to input data
for _ in range(n):
    # Get the key (string) from the user
    key = input("Enter key (string): ")
    
    # Get the list of tuples (each with three elements) from the user
    value_input = input("Enter list of tuples with three elements (e.g., '1,2,3 4,5,6'): ")
    
    # Split the input string into individual tuple strings
    tuple_strings = value_input.split()
    
    # Convert each tuple string into an actual tuple with three elements and collect them in a list
    value = [tuple(map(str, t.split(','))) for t in tuple_strings if len(t.split(',')) == 3]
    
    # Assign the list of tuples to the dictionary for the given key
    my_dict[key] = value

# Print the final dictionary
print("\nThe dictionary you created is:")
print(my_dict)
