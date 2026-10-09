# Python Assignment 1: Data Structures - Strings & Tuples

# ---------------------------------------------------------
# 1. String Concatenation
# ---------------------------------------------------------
string1 = "Hello "
string2 = input("Enter your Name: ")

greeting = string1 + string2
print(greeting)

string3 = ", welcome to Python programming"
greeting = greeting + string3
print(greeting)

# ---------------------------------------------------------
# 2. String Slicing and Indexing
# ---------------------------------------------------------
s = greeting
print("\n--- String Slicing and Indexing ---")
print("a. First character:", s[0])
print("b. Last character:", s[-1])
print("c. First 5 characters:", s[:5])
print("d. Last 11 characters:", s[-11:])
print("e. Reversed string:", s[::-1])
# "Python programming" is the last 18 characters, so "Python" is s[-18:-12]
# (negative indexes work no matter how long the entered name is)
print("f. Word 'Python':", s[-18:-12])

# ---------------------------------------------------------
# 3. String Methods
# ---------------------------------------------------------
strM = "Python beginner tutorial"
print("\n--- String Methods ---")

upper_str = strM.upper()
print("a. Uppercase:", upper_str)

lower_str = strM.lower()
print("b. Lowercase:", lower_str)

original = upper_str.capitalize()
print("c. Capitalized (original form):", original)

print("d. Occurrences of 't':", strM.count("t"))

print("e. Replaced:", strM.replace("Python", "Machine Learning"))

# ---------------------------------------------------------
# Tuples (Creation, Modification and Access)
# ---------------------------------------------------------
print("\n--- Tuples ---")
t1 = (10, 20, 30)
t2 = (40, 50, 60)

t_combine = t1 + t2
print("a. Concatenated tuple:", t_combine)

print("b. Repeated 3 times:", t_combine * 3)

print("c. 3rd element:", t_combine[2])

print("d. First three elements:", t_combine[:3])

print("e. Last three elements:", t_combine[-3:])
