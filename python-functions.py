def sum_to(n):
  sum = 0
  for num in range(0,n+1):
    sum = sum + num
  print(sum)

sum_to(6)

def largest(array):
  placeholder = array[0]
  for idx in range(len(array)):
    if (array[idx] >= placeholder):
      placeholder = array[idx]
  print(placeholder)
  
largest([10, 4, 2, 231, 91, 54])

def occurances(string1, string2):
  print(string1.count(string2))
  
occurances('floop fleep', 'ee')

def product(*args):
  result = args[0]
  for x in args:
    result = result * x
  print(result)
  
product(1, -4)
