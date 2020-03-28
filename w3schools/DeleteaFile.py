import os


# if os.path.exists("C:/Users/Paul Jo/Desktop/pythonworkspace/w3schools/demofile1.txt"):
#    os.remove("C:/Users/Paul Jo/Desktop/pythonworkspace/w3schools/demofile1.txt")

if os.path.exists("C:/Users/Paul Jo/Desktop/pythonworkspace/w3schools/test"):
   os.rmdir("C:/Users/Paul Jo/Desktop/pythonworkspace/w3schools/test")
else:
  print("The file does not exist")