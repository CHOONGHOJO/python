# demofile.txt

# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

f = open("C:/Users/Paul Jo/Desktop/pythonworkspace/w3schools/demofile.txt", "r")
# print(f.readline())
# print(f.readline())
# f.close()

for x in f:
  print(x, end="")
f.close()

# Return the 5 first characters of the file:
# print(f.read(5))

# f.close()

