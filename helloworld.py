# Day 1 Exercise - 30DaysOfPython Challenge
# Question 2

print(3 + 4)             # addition(+)
print(3 - 4)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(4 / 3)             # division(/)
print(4 ** 3)            # exponential(**)
print(4 % 3)             # modulus(%)
print(4 // 3)            # Floor division operator(//)

# Question 3
print('Khadijat')
print('Ejide')                           # Your Family Name
print('Nigeria')                         #Your Country
print('I am enjoying 30 days of python') 

# Question 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type({'Name':'Khadijat'}))
print(type({'Family Name':'Ejide'}))
print(type({'Country':'Nigeria'}))


#Exercise: Level 3
# Number(Integer 2,3,0, -7,
         #Float  2.3, 5.2
         #Complex 2-3j), 
#String "Thank you" 
#Boolean T or F, 
#List (3,4,5,6), 
#Tuple ('Red', 'Orange','Yellow', 'Green', 'Blue', 'Indigo','Violet')  Rainbow colours can not be changed or modified once created
#Set {2.3, 8.21, 3.1} 
#Dictionary ({'colour':'blue'}).

# Find an Euclidian distance between (2, 3) and (10, 8)
# Cordinates of the points
import math
point1 = (2,3)
point2 =(10,8)

# Calculating Euclidian distance
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print(f"The Euclidean distance between {point1} and {point2} is: {distance}")