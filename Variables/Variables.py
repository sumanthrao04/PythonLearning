x=6
y="sumanth"

print(x)
print(y)

name = "John"
name= "Doe"  # This will overwrite the previous value of name
print(name)

# Variables can be reassigned to different data types
x = 10      # x is an integer       
x = "Now I'm a string"  # x is now a string
print(x)

#casting
x = str(5)   # '5'
y = int("10")   # 10
z = float("3.14") # 3.14    
print(x)
print(y)    
print(z)

#Get the Type
print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z)) # <class 'float'>

#Single or Double Quotes?
print('Hello')
print("Hello")
print('He said, "Hello!"')
print("It's a beautiful day!")
print("He said, \"It's a beautiful day!\"") 


#Case-Sensitive
myVar = 5
myvar = 10  
print(myVar)  # prints 5
print(myvar)  # prints 10
print(myVar == myvar)  # prints False

#Variable Scope
x = "global"
def my_function():
    x = "local"
    print("Inside function:", x)
my_function()
print("Outside function:", x)

#Using the global Keyword
count = 0
def increment_count():
    global count
    count += 1
    print("Count inside function:", count)
increment_count()
increment_count()
print("Count outside function:", count) 

#Multiple Assignments
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2 
print(c)  # 3

#Assigning the Same Value to Multiple Variables
x = y = z = 0
print(x)  # 0
print(y)  # 0
print(z)  # 0


#Unpacking a Collection
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)  # apple
print(b)  # banana
print(c)  # cherry   



#Variable Naming Rules
#1. A variable name must start with a letter or the underscore character.
#2. A variable name cannot start with a number.
#3. A variable name can only contain letters, numbers, and underscores.
#4. Variable names are case-sensitive.  

#5. Variable names cannot be a reserved keyword in Python. 
# (e.g., if, else, while, for, def, return, etc.)
#6. Variable names should be descriptive and meaningful.
#7. Avoid using single-character variable names except for counters or iterators.
#8. Use lowercase letters with words separated by underscores for better readability (snake_case).  
#9. Avoid using built-in names (e.g., list, str, int) as variable names.
#10. Keep variable names concise but informative.
#11. Use consistent naming conventions throughout your code.
#12. Avoid using special characters (e.g., @, $, %, etc.) in variable
# names.
#13. Avoid using spaces in variable names; use underscores instead.
#14. Use plural names for variables that hold collections (e.g., lists, sets).
#15. Avoid using too many abbreviations; prioritize clarity over brevity.
#16. Use camelCase for variable names if following JavaScript conventions. 
#17. Avoid using leading or trailing underscores unless necessary for specific purposes (e.g., _privateVar).
#18. Document the purpose of complex variables with comments.
#19. Regularly review and refactor variable names for clarity as your code evolves.
#20. Follow the naming conventions of the programming language you are using.
#21. Avoid using non-ASCII characters in variable names to ensure compatibility.    
#22. Use meaningful names for boolean variables (e.g., is_valid, has_data).
#23. Avoid using too many global variables; prefer local scope when possible.
#24. Use constants (e.g., MAX_SIZE) for values that should not change.
#25. Avoid using overly generic names (e.g., data, info) that do not convey meaning.
#26. Use descriptive names for function parameters to clarify their purpose.
#27. Avoid using negations in variable names (e.g., not_valid); prefer positive names (e.g., is_valid).
#28. Use domain-specific terminology for variable names when applicable.
#29. Avoid using variable names that are too similar to each other to prevent confusion.
#30. Regularly seek feedback on your variable naming conventions from peers or mentors.
#31. Use version control comments to track changes in variable names if necessary.
#32. Avoid using variable names that imply a different data type than what they hold.
#33. Use prefixes or suffixes to indicate the type of variable (e.g., str_name, list_items).
#34. Avoid using variable names that are too long; aim for a balance between clarity and brevity.
#35. Use consistent naming conventions for related variables (e.g., user_name, user_age
#36. Avoid using variable names that are too similar to built-in functions or methods.
#37. Use meaningful names for loop counters (e.g., index, count) instead of generic names (e.g., i, j).
#38. Avoid using variable names that are too specific to a particular implementation; prefer more general
# names that can be reused in different contexts.
#39. Use descriptive names for configuration variables to clarify their purpose.
#40. Avoid using variable names that are too similar to each other in the same scope to prevent confusion.
#41. Use meaningful names for temporary variables to clarify their purpose.
#42. Avoid using variable names that are too similar to each other in different scopes to prevent confusion.
#43. Use descriptive names for error handling variables to clarify their purpose.
#44. Avoid using variable names that are too similar to each other in different modules to prevent confusion.
#45. Use meaningful names for return values to clarify their purpose.
#46. Avoid using variable names that are too similar to each other in different classes to prevent confusion.
#47. Use descriptive names for logging variables to clarify their purpose.
#48. Avoid using variable names that are too similar to each other in different functions to prevent confusion.
#49. Use meaningful names for state variables to clarify their purpose.
#50. Avoid using variable names that are too similar to each other in different files to prevent confusion.
