import random

# elif
b = random.randrange(1,7)
print('b = ', b)
if b < 3:
  print('Lower number')
elif b < 5:
  print('Average')
else:
  print('High')