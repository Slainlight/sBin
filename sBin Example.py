# Neat function to shove into your program!
# By Matthew Periut

def sBin(number, arr = 0):
  binary = []
  while number > 0:
    binary = [number % 2] + binary
    number = int(number / 2)
  
  if arr == 0:
    binString = ""
    for x in range(0, len(binary)):
      binString += str(binary[x])
    return binString
  else:
    return binary

# Introduction Instruction
print("Input an decimal integer to convert to binary: ", end='')
# Print the binary conversion of the integer input:
print(sBin(int(input())));

input()