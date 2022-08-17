"""Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)"""

print("Enter Int type of Data")
a=int(input())
print("Enter bool type of Data")
b=bool(input())
print("Enter string type of Data")
c=str(input())
print("Enter Float type of Data")
d=float(input())
print("Enter complex type of Data")
e=complex(input())
print(type(a),type(b),type(c),type(d),type(e))