## Day 2 – Variables & Types

### Key Concepts
- Everything in Python is an object
- Dynamic typing
- Importance of understanding types for ML pipelines

### Observations
Written the basics of python to understand the data types present in Python.

### Mistakes
Take special care of the syntax error. One of he mistakes I did was commenting out the name and age variable and it was not defined in the f-string.

## Day 3 – Data Structures

### Key Insights

- Lists are ordered, mutable collections and are heavily used in dataset representation and preprocessing steps.
- Tuples are ordered but immutable, making them safer for fixed structured data (e.g., model outputs).
- Dictionaries are key-value mappings implemented using hash tables, enabling fast lookups.
- Sets store unique elements and are optimized for membership testing and mathematical set operations.

---

### Mutability & References

One critical concept today was understanding reference behavior in Python.

When assigning one list to another variable:

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)

Day 4 – Functions & Control Flow

1. Why Functions Are Critical in AI Systems

Functions are the building blocks of structured systems. In AI pipelines:

- Data preprocessing is done using functions
- Feature engineering steps are modular functions
- Model training is wrapped inside functions
- Evaluation logic is separated into reusable components

Well-designed functions:
- Improve readability
- Enable testing
- Reduce duplication
- Increase modularity
- Improve scalability

Without structured functions, AI systems become tightly coupled and difficult to debug.

---

2. Control Flow Observations

Conditional logic (`if`, `elif`, `else`) is essential for decision-making systems.

In real-world applications:
- Validation rules are implemented using conditionals
- Business rules are enforced using nested logic
- Decision engines rely heavily on structured branching

Proper ordering of conditions is important to avoid logical errors and unreachable states.

---

 3. *args and **kwargs Insight

`*args` allows variable positional arguments.  
`**kwargs` allows variable keyword arguments.

Real-world usage:
- Flexible configuration systems
- API parameter handling
- Logging systems
- Dynamic model parameter passing

They provide flexibility but should be used carefully to maintain readability.

---

4. Scope Understanding

Local variables exist only inside functions.

Global variables exist across the program.

Modifying global variables using `global`:
- Introduces side effects
- Makes debugging harder
- Reduces predictability
- Breaks function purity

In AI systems, uncontrolled global state can lead to non-deterministic behavior.

Pure functions are preferred because they:
- Produce consistent outputs
- Are easier to test
- Improve reproducibility

Reproducibility is critical in ML pipelines.

---

5. Pure vs Impure Functions

Pure Function:
- Depends only on inputs
- Returns output
- Has no side effects

Impure Function:
- Uses input()
- Uses print()
- Modifies global variables
- Writes to files
- Depends on external state

Separation of input handling and business logic improves system architecture.

---

6. Engineering Exercise – Evaluation System

Implemented a structured evaluation system with:
- Input validation
- Attendance rules
- Grade calculation
- Assignment cap logic
- Certification eligibility
- Structured dictionary output

Key design takeaway:
Early returns reduce nesting and improve readability.

---

7. Mistake Made Today

Initially misunderstood that purity depends on covering scenarios.  
Correct understanding: purity depends on absence of side effects and determinism.

---

8. Concept That Required Deeper Thinking

Understanding function parameter ordering:
- Required parameters must come before default parameters.
- This prevents ambiguity in argument binding.

Also gained clarity on how Python binds arguments left-to-right.

---

9. Personal Observation

Variables are simple, but structured function design requires deliberate thinking.

Understanding how to organize logic is more important than memorizing syntax.

Day 5 – OOP Foundations in Python
📌 Overview

Today’s focus was understanding the fundamentals of Object-Oriented Programming (OOP) in Python.

Key concepts covered:

Classes

Objects

Instance variables

Class variables

Instance methods

__init__

__str__

Composition

Defensive programming

🧠 What is OOP?

Object-Oriented Programming organizes code into classes that combine:

Data (attributes)

Behavior (methods)

A class acts as a blueprint, and objects are instances created from that blueprint.

👨‍🎓 Student Class Implementation
class Student:
    school_name = "AI Academy"  # Class variable

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def is_passed(self):
        return self.score >= 60

    def update_score(self, new_score):
        self.score = new_score

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, score={self.score})"

🔎 Concepts Demonstrated
1️⃣ Constructor (__init__)

Initializes object attributes.

Called automatically when object is created.

2️⃣ Instance Variables

Unique to each object.

Defined using self.

3️⃣ Class Variable

Shared across all instances.

Defined at class level.

Only one copy exists.

4️⃣ Instance Methods

Operate on object data.

Must include self.

5️⃣ __str__

Controls how object appears when printed.

Must return a string.

📚 Course Class (Composition Example)
class Course:
    def __init__(self, name, students=None):
        self.name = name
        self.students = students if students is not None else []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added")
        self.students.append(student)

    def average_score(self):
        if not self.students:
            return 0
        total = sum(student.score for student in self.students)
        return total / len(self.students)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.score)

🔗 Concept: Composition

A Course has multiple Student objects.

This is a has-a relationship.

Enables object collaboration.

⚠️ Defensive Programming

To maintain class integrity:

if not isinstance(student, Student):
    raise TypeError(...)


Always protect class invariants.

Never assume inputs are correct — validate them.

🏗 Engineering Insights

This foundation is critical for:

Machine learning model classes

Dataset abstractions

Training pipelines

Configuration systems

API design

OOP enables modular, scalable system design.

📝 Key Learnings

Objects bundle data and behavior.

Class variables are shared across instances.

__str__ improves readability and debugging.

Composition models real-world relationships.

Defensive checks prevent hidden bugs.