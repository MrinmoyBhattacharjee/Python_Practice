#Nested IF with List Comprehension

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
