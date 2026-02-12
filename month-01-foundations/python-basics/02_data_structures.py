#**************Lists**************
a = [1, 2, 3, 4]
print(a[-1])  # Output: 3
print(a[1])  # Output: 2
print(a[2])  # Output: 3

x =slice(1, 3)  
print(a[x])  # Output: [2, 3]

nums = [1,4,9,16,25,36,49,64,81,100]

print(nums[0:5])  # Output: [1, 4, 9, 16, 25]
print(nums[5:])   # Output: [36, 49, 64, 81, 100]
print(nums[:5])   # Output: [1, 4, 9, 16, 25]
print(nums[:])    # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
mil = [names,nums]
print(mil)  # Output: [['Alice', 'Bob', 'Charlie', 'David', 'Eve'], [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]]

nums.append(121)
print(nums)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
nums.insert(0, 0)
print(nums)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]

nums.remove(16)
print(nums)  # Output: [0, 1, 4, 9, 25, 36, 49, 64, 81, 100, 121]

nums.pop()
print(nums)  # Output: [0, 1, 4, 9, 25, 36, 49, 64, 81, 100]
nums.pop(0)
print(nums)  # Output: [1, 4, 9, 25, 36, 49, 64, 81, 100]   

del nums[0:3]
print(nums)  # Output: [25, 36, 49, 64, 81, 100]

#**************Tuples**************
t = (1, 2, 3, 4)
print(t[0])  # Output: 1
print(t[1])  # Output: 2

# t[0] = 10  # This will raise a TypeError since tuples are immutable

t.index(3)  # Output: 2
t.count(2)  # Output: 1

person = ("Faisal", 25, "Engineer")

name, age, profession = person
print(name) # Output: Faisal print(age) # Output: 25 print(profession) # Output: Engineer

#**************Dictionaries**************

person = {"name": "Faisal", "age": 25, "profession": "Engineer"} 
print(person["name"]) # Output: Faisal 
print(person["age"]) # Output: 25 
print(person["profession"]) # Output: Engineer
print(person) # Output: {'name': 'Faisal', 'age':26, 'profession': 'Engineer'}

student = {
    "name": "Alice", 
    "age": 20, 
    "courses": ["Math", "Science"], 
    "grades": {"Math": "A", "Science": "B"}
    }

print(student["grades"]) # Output: {'Math': 'A', 'Science': 'B'}

#***************Sets**************
s = {1, 2, 3, 4, 5} 
print(s) # Output: {1, 2, 3, 4, 5} 

s.add(6) 
print(s) # Output: {1, 2, 3, 4, 5, 6} 

s.remove(3) 
print(s) # Output: {1, 2, 4, 5, 6} 

s.discard(10) 
print(s) # Output: {1, 2, 4, 5, 6}

s.pop() 
print(s) # Output: {2, 4, 5, 6}

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

new_list = set(list1) | set(list2)
print(new_list) # Output: {1, 2, 3, 4, 5, 6, 7, 8} 
intersection = set(list1) & set(list2) 
print(intersection) # Output: {4, 5} 
difference = set(list1) - set(list2) 
print(difference) # Output: {1, 2, 3}
unique = set(list1) ^ set(list2)
print(unique) # Output: {1, 2, 3, 6, 7, 8}

# -------------------Exercises-------------------

students = [
    {"name": "A", "score": 78},
    {"name": "B", "score": 92},
    {"name": "C", "score": 85}
]

#Calculate average score
total = sum(student["score"] for student in students)
average = total / len(students)
print(average) # Output: 85.0

#Find highest scorer
highest_scorer = max(students, key=lambda x: x["score"])
print(highest_scorer["name"]) # Output: B

# Return list of students scoring above average
above_average = [student for student in students if student["score"] > average]
print(above_average) # Output: [{'name': 'B', 'score': 92}, {'name': 'C', 'score': 85}]

#Then refactor using Pythonic constructs (list comprehension / max with key)
above_average = [student for student in students if student["score"] > average]
print(above_average) # Output: [{'name': 'B', 'score': 92}, {'name': 'C', 'score': 85}]

