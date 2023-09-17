
name = input("Enter your name: ")

# Open a file for writing
output_file = open("output.txt", "w")

for i in range(1, 11):
    message = f"Iteration {i}: {i} you, {name} are dumb"
    # Print the message to the screen
    print(message)
    
    # Write the message to the output file
    output_file.write(message + "\n")

# Close the output file
output_file.close()

print("Output has been written to 'output.txt'")
