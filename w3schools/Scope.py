def myfunc():
  global x
  x = 200
  def myinnerfunc():
    print(x)
  



x = 400

myfunc()

print(x)
