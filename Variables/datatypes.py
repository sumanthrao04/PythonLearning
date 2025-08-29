age = 25
price = 19.99
z = 2 + 3j  
name = "Alice"
fruits = ["apple", "banana", "cherry"]
coordinates = (10, 20)
unique_numbers = {1, 2, 3}
person = {"name": "John", "age": 30}


# Data Types
# Python has several built-in data types, including:
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range
# 3. Text Type: str
# 4. Mapping Type: dict
# 5. Set Types: set, frozenset
# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview    
# 
# 
#  
# You can check the type of a variable using the type() function:
print(type(age))          # <class 'int'>   
print(type(price))        # <class 'float'>
print(type(z))            # <class 'complex'>
print(type(name))         # <class 'str'>
print(type(fruits))       # <class 'list'>
print(type(coordinates))  # <class 'tuple'>
print(type(unique_numbers)) # <class 'set'>
print(type(person))       # <class 'dict'>
print(type(True))         # <class 'bool'>
print(type(b"Hello"))     # <class 'bytes'>
print(type(bytearray(5))) # <class 'bytearray'>
print(type(memoryview(b"Hello"))) # <class 'memoryview'>


# You can convert between data types using functions like int(), float(), str(), list(), tuple(), dict(), set(), etc.
# Example:
num_str = "123"
num_int = int(num_str)       # Convert to integer
num_float = float(num_str)   # Convert to float 
print(num_int)    # 123
print(num_float)  # 123.0   

# Note: Python is dynamically typed, so you don't need to declare the type of a variable explicitly. The type is inferred based on the value assigned to it.