# Regular Method (well w/o bin()) lmao
# By Matthew Periut

# Introduction Instruction
print("Input an decimal integer to convert to binary: ", end='')

# Variables, Input
number = int(input())
binary = []

# Convert to Binary
while number > 0:
  binary = [number % 2] + binary
  number = int(number / 2)

# Print to Console
print("In Binary: ", end='')
for x in range(len(binary)):
  print(binary[x], end='')
print()
input()
