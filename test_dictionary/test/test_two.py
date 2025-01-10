# task to chatgpt to create a python program
# condition of the task
# how to create a dictionary with keys comes from console and values like list of tupels with three element first is str, second float, third element int 




# Initialize an empty dictionary
my_dict = {}

# Get the number of keys you want to input
num_keys = int(input("How many keys do you want to add to the dictionary? "))

# Loop to get each key and its associated values
for _ in range(num_keys):
    # Get the key from the user
    key = input("Enter the key: ")

    # Initialize an empty list to store the tuples for this key
    values_list = []

    # Ask how many tuples you want to add for this key
    num_tuples = int(input(f"How many tuples for the key '{key}'? "))
    
    # Loop to collect each tuple
    for _ in range(num_tuples):
        # Get the elements of the tuple from the user
        str_value = input("Enter a string: ")
        float_value = float(input("Enter a float value: "))
        int_value = int(input("Enter an integer value: "))
        
        # Create a tuple and append it to the list
        values_list.append((str_value, float_value, int_value))

    # Add the list of tuples to the dictionary under the current key
    my_dict[key] = values_list

# Display the final dictionary
print("\nFinal Dictionary:")
print(my_dict)
