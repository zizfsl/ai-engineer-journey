def evaluate_candidate(score, attendance, is_assignment_submitted):

    # 1️⃣ Score Validation
    if score < 0 or score > 100:
        return {
            "grade": None,
            "status": "Invalid Score",
            "certified": False
        }
    # 2️⃣ Attendance Rule (Hard Fail)
    if attendance < 75:
        return {
            "grade": "F",
            "status": "Fail - Low Attendance",
            "certified": False
        }
    # 3️⃣ Grade Calculation
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"

    # 4️⃣ Assignment Rule (Cap at C)
    if not is_assignment_submitted and grade in ["A", "B"]:
        grade = "C"

    # 5️⃣ Pass/Fail Status
    status = "Pass" if grade in ["A", "B", "C", "D"] else "Fail"

    # 6️⃣ Certification Eligibility
    certified = (
        grade in ["A", "B", "C"]
        and attendance >= 75
        and is_assignment_submitted
    )

    # 7️⃣ Structured Return
    return {
        "grade": grade,
        "status": status,
        "certified": certified
    }

# Example Usage
result = evaluate_candidate(score=85, attendance=80, is_assignment_submitted=True) 
print(result)

print(evaluate_candidate(92, 80, True)) 
print(evaluate_candidate(85, 60, True))
print(evaluate_candidate(95, 90, False))
print(evaluate_candidate(150, 80, True))

#----------Basic Functions----------

# 1️⃣ Basic Function (No Return)
def greet_user(name):
    """
    Prints a greeting message.
    This function does not return anything.
    """
    print(f"Hello, {name}! Welcome to the certification system.")

greet_user("Faisal")

# 2️⃣ Function With Return Value
def square_number(number):
    """
    Returns the square of a number.
    """
    return number * number

result = square_number(5)
print(result)  # Output: 25

# 3️⃣ Function Returning Multiple Values
def get_min_max(numbers):
    """
    Returns minimum and maximum values from a list.
    """
    return min(numbers), max(numbers)

numbers = [3, 1, 4, 1, 5, 9, 2]
minimum, maximum = get_min_max(numbers) 
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 1, Max: 9

# 4️⃣ Function With Default Parameters
def create_user(name, role="student"):
    """
    Creates a user with a default role of 'student'.
    """
    return f"User: {name}, Role: {role}"

print(create_user("Alice"))  # Output: User: Alice, Role: student
print(create_user("Bob", role="instructor"))  # Output: User: Bob, Role: instructor

# 5️⃣ Function With Variable-Length Arguments
def calculate_average(*scores):
    """
    Calculates the average of a variable number of scores.
    """
    if not scores:
        return 0
    return sum(scores) / len(scores)

average_score = calculate_average(80, 90, 100)
print(average_score)  # Output: 90.0

# 6️⃣ Recursive Function
def factorial(n):
    """
    Returns the factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 5️⃣ Function Called Using Keyword Arguments
def calculate_area(length, width):
    """
    Returns area of a rectangle.
    """
    return length * width

area = calculate_area(width=5, length=10)
print(area)  # Output: 50

# 6️⃣ Positional vs Keyword Argument Difference
def describe_product(name, price, category):
    """
    Describes a product.
    """
    return f"{name} costs {price} and belongs to {category} category."

# Using Positional Arguments
value_01= describe_product("Laptop", 999.99, "Electronics")
print(value_01)  # Output: Laptop costs 999.99 and belongs to Electronics category.   

value_02 = describe_product(category="Books", name="Python Programming", price=29.99)
print(value_02)  # Output: Python Programming costs 29.99 and belongs to Books category.

#--------------*args and **kwargs--------------
def display_info(*args, **kwargs):
    """
    Displays information passed as variable-length arguments.
    """
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

value_03 = display_info("Alice", "Bob", age=30, city="New York")
print(value_03)  # Output: Positional Arguments: ('Alice', 'Bob') Keyword Arguments: {'age': 30, 'city': 'New York'} None

def calculate_sum(*numbers):
    """
    Calculates the sum of a variable number of numbers.
    """
    return sum(numbers)

total_sum = calculate_sum(1, 2, 3, 4, 5)
print(total_sum)  # Output: 15

def print_user_info(**info):
    """
    Prints user information passed as keyword arguments.
    """
    for key, value in info.items():
        print(f"{key}: {value}")

value_04 = print_user_info(name="Alice", age=30, city="New York")
print(value_04)  # Output: name: Alice age: 30 city: New York None

# Global variable
system_status = "Operational"

def check_local_scope():
    """
    Demonstrates a local variable.
    This variable exists only inside this function.
    """
    local_message = "This is a local variable"
    print(local_message)
    
check_local_scope()  # Output: This is a local variable
print(system_status)  # Output: Operational

def read_global_status():
    """
    Reads global variable without modifying it.
    """
    print("System status:", system_status)

read_global_status()  # Output: System status: Operational

"""
⚠️ Risk of Global Variables:

- Makes debugging harder
- Creates hidden side effects
- Reduces predictability
- Breaks function purity
- Causes issues in concurrent systems

In large systems (including AI pipelines),
global state can cause non-deterministic behavior.
Pure functions are preferred for stability and testability.
"""

def update_system_status(new_status):
    """
    Modifies a global variable using 'global'.
    """
    global system_status
    system_status = new_status

update_system_status("Maintenance")
print(system_status)  # Output: Maintenance

def update_system_status(new_status):
    system_status = new_status

update_system_status("Operational")

#------------ Exercises ------------

def analyze_scores(students):
    """
    Analyzes student scores and returns a summary.
    """
    if not students:
        return "No students to analyze."

    total_score = sum(student["score"] for student in students)
    average_score = total_score / len(students)
    highest_scorer = max(students, key=lambda x: x["score"])
    above_average_students = [student for student in students if student["score"] > average_score]

    return {
        "average_score": average_score,
        "highest_scorer": highest_scorer,
        "above_average_students": above_average_students
    }

students = [
    {"name": "A", "score": 78},
    {"name": "B", "score": 92},
    {"name": "C", "score": 85}
]
result = analyze_scores(students)
print(result) 