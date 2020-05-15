# randon-pasword-
Random Password generator using python
import random

alphabests = ["A","B","C","D","E","F"]

small = ['a','b','c','d','e','f']

numbers =[1,2,3,4,5,6,7,8,9,0]

chars = ['!','@','#','$']

ran_1 = random.choice(alphabests) + random.choice(small) + str(random.choice(numbers)) + random.choice(chars)
ran_2 = random.choice(alphabests) + random.choice(small) + str(random.choice(numbers)) + random.choice(chars)
print('Yor Random paswword is:  ',ran_1 + ran_2)
