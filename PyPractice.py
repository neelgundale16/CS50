name=["Harry","Ron","Hermione"]
print(name[1]) #list , is mutable and ordered

coordinates=(4,5)
print(coordinates[0]) #tuple , is immutable and ordered

set1={1,2,3}
print(set1) #set , is mutable and unordered

dict1={"name":"Harry","age":20}
print(dict1["name"]) #dictionary , is mutable and unordered

string1="Hello, World!"
print(string1[7]) #string , is immutable and ordered

#defining a list of names
names_list=["Alice","Bob","Charlie"]
print(names_list)   

names_list.append("Abob")  #adding an element to the list
print(names_list)

names_list.sort()  #sorting the list
print(names_list)

#loops

for i in [0,1,2,3,4,5]:
    print(i)

#built-in functions
for i in range(10): #range 10 means 0 to 9
    print(i)    

for names_list in names_list:
    print(names_list)

houses ={"Gryffindor":"Hufflepuff","Ravenclaw": "Slytherin"}

for house in houses:
    print(house) #prints only keys

#to print values
for house in houses.values():
    print(house)

#to print key and value both
for house, rival in houses.items():
    print(house + " : " + rival) #rival is not a keyword in python
    #it just gets the value of corresponding key

#functions

def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")    

class Point() : 
    def __init__(self, input1, input2):
        self.x=input1
        self.y=input2

p = Point(2,3)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity=capacity
        self.passengers=[]

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True    

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
print(flight.capacity)    

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people :
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

#decorators
# A decorator is a function that takes another function as an argument,
# adds some kind of functionality and then returns another function.

def announce(f):    
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper            

@announce
def hello():
    print("Hello, world!")
hello()

#exceptions
try : 
    x = input("Enter a number x : ")
    y = input("Enter a number y : ")

except ValueError :
    print("Invalid input. Please enter numeric values.")    

try :
    result=int (x)/int (y)
except ZeroDivisionError :
    print("You can't divide by zero!")

print(f"The result is {result}")

