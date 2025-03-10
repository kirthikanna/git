# a=[3,0,5,0,4,0]
# a.sort()
# a.sort(reverse=True)
# print(a)

# # Lambda function to calculate the area of a rectangle
# y=lambda l,b:l*b
# print(y(2,3))
# print(f"The area of a rectangle with width {b} and height {l} is {y}")
# # Lambda function to find the maximum of two numbers
# x=lambda a,b :a if a>b else b
# print(x(5,7))


#

# data = [('apple', 3), ('banana', 2), ('cherry', 1)]
# sorted_data = sorted(data, value=lambda x: x[1])
# print(sorted_data)
#
# x=[10,20,30]
# y=map(lambda a:a**2,x)
# print(list(y))

num1=[1,2,3,4]
num2=[5,6,7]
results=map(lambda x,y:x+y,num1,num2)
print(list(results))


# List of temperatures in Celsius
temperatures_celsius = [0, 10, 20, 30, 40]
# Lambda function to convert Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (9/5) * c + 32
# Use map to apply the lambda function to each element in the list
temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))
# Print the result
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)




numbers=[1,2,3,4,5]
results=map(lambda a:a**2,numbers)
print(list(results))

x=[1,2,3,4,5]
results=filter(lambda a:a%2!=0,x)
print(list(results))


a=["Hi","","Hello",""]
b=filter(None,a)
print(list(b))


strings = ["apple", "", "banana", "cherry", "", "date"]
#results=filter(None,strings)
results=filter(lambda x:x!="",strings)
print(list(results))

def generate_squares():
 i = 1
 while True:
  yield i * i
 i += 1
# Create an instance of the infinite square generator
squares = generate_squares()
# Print the first 10 squares
for _ in range(100):
 print(next(squares), end=' ')
