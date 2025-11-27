# Print the header row
print("    ", end="")  # Top-left corner empty space
for i in range(1, 11):
    print(f"{i:4}", end="")  # Print column headers
print()

# Print the table rows
for i in range(1, 11):
    print(f"{i:4}", end="")  # Print row header
    for j in range(1, 11):
        print(f"{i * j:4}", end="")  # Print multiplication results
    print()  # Move to the next row
