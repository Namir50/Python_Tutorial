info = {"Namir": 10,"Ibaad": 11,"Armaan": 20}

while True:
  x = (input("Enter a key: "))

  if x in info.keys():
     print("Key present")
     continue
  else:
     print("Key absent")
     break