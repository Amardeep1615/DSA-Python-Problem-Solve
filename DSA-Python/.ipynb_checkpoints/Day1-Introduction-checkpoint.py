# DSA -- DataStrucutres and Algorithms
# Big O Notation
# O(n)
# O(1)
# O(n2)

#Square numbers 
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers
    
numbers = [2,4,5,6,7,8,9,10]

print(get_squared_numbers(numbers))



       