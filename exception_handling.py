
try:
    print(x)
except NameError:
    print("Something went wrong")
else:
    print("Everything went wrong")      
    
      
x = -1

if x <0:
    raise Exception("Sorry, no number below zero")      