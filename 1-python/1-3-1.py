#how we built the function
#normally this foes away
numbers = [5, 2, 3, 10]
total = sum(numbers)
count = len(numbers)
print(total)
print(count)
average = total / count
print(average) 

#and gets replaced with this 
def average(numbers: list) -> float: # <== input
    '''
    This function takes a list of numbers and returns the average of those numbers.'''
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average # <== output


#call the function 
grades = [100,100,100,0]
result = average(grades)
print(result) #5.0

average()