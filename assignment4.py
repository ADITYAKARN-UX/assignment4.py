#task 1
filename = "sample.txt"

try:
    print("Reading file content:")
    with open(filename, "r") as file:
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
#=================================================================
#task 2


filename = "output.txt"
text_to_write = input("Enter text to write to the file: ")

with open(filename, "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

additional_text = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open(filename, "r") as file:
    print(file.read())