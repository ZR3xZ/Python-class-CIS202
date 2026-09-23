import math
family = 4
pizza_slice = 8
person1 = int(input("how many slices do the first person in the family eats "))
person2 = int(input("how many slices do the second person in the family eats "))
person3 = int(input("how many slices do the third person in the family eats "))
person4 = int(input("how many slices do the fourth person in the family eats "))
total = (person1 + person2 + person3 + person4)
whole_pizza = math.ceil(total/pizza_slice)
print(total)
print(whole_pizza)
leftover = total%pizza_slice
leftover = pizza_slice - leftover
print (leftover)
