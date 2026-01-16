# Dictionary & Set Comprehensions

"""student = {
    "name": "John",
    "subjects": {
        "Math": 90,
        "Science": 85,
        "History": 88 
    }
}

print(len(student)) # 2
print(student["name"]) # John
print(student["subjects"]["Math"]) # 90
print(student.get("age", 18)) # 18
print(student.keys()) # dict_keys(['name', 'subjects'])
print(student.values()) # dict_values(['John', {'Math': 90, 'Science': 85, 'History': 88}])
print(student.items()) # dict_items([('name', 'John'), ('subjects', {'Math': 90, 'Science': 85, 'History': 88})])
print("name" in student) # True
print("age" in student) # False

print(list(student.keys)) # ['name', 'subjects']

print(student.get)

student.update({"city": "Copenhagen", "name": "Jane"})
 print(student)
 print(type(student))"""

# Sets
"""fruits = {"apple", "banana", "orange", "apple"}"""

#collection1= { 1, 2, 3, 4, 5}
#collection2 = {3, 4, 5, 6, 7}
#emptySet = set() # Correct way to create an empty set

#print(collection) # {1, 2, 3, 4, 5}
#print(type(collection)) # <class 'set'>
#print(len(collection)) # 5
#print(2 in collection) # True
#collection.add("banana")
#print(collection) # {1, 2, 3, 4, 5, 'banana'}
#collection.remove(3)
#print(collection) # {1, 2, 4, 5, 'banana'}
#collection.discard(10) # No error if element not found
#print(collection) # {1, 2, 4, 5, 'banana'}
#collection.pop() # Removes and returns an arbitrary element
#print(collection) # {2, 4, 5, 'banana'}
#collection.clear() # Empties the set
#print(collection) # set()
#print(collection1.union(collection2)) # {1, 2, 3, 4, 5, 6, 7}
#print(collection1.intersection(collection2)) # {3, 4, 5}

subjects = { 
    "Python", "java", "C++", "JavaScript", "c#", "java", "JavaScript", "Python", "java", "C++", "JavaScript", "c#", "java", "Python"
            }
print(subjects) # {'C++', 'c#', 'Python', 'java', 'JavaScript'}
print("We need only", (len(subjects)), "classes") # 5