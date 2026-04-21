a = 10
b = 10

try:
  c = a / b
  print("last")
except Exception as e:
  #print(e)
  print("some exception")

finally:
  print("at last")  

