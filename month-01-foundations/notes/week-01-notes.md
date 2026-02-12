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

