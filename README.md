# Python Loop Assessment

This project contains a collection of Python functions that demonstrate the use of **loops, conditionals, and basic algorithmic thinking**. The project also includes **unit tests using Python's `unittest` framework** to verify that each function works correctly.

## 📌 Project Overview

The goal of this assessment is to practice using loops in Python to solve common programming problems such as:

* Summing numbers
* Counting even numbers
* Calculating factorials
* Generating multiplication tables
* Working with strings
* Finding prime numbers
* Creating patterns
* Building multiplication grids

Each function is implemented in `assessment1.py` and tested using automated unit tests.

---

## 📂 Project Structure

```
project-folder/
│
├── assessment1.py      # Main file containing all loop-based functions
├── test_assessment.py  # Unit tests for the functions
└── README.md           # Project documentation
```

---

## ⚙️ Functions Implemented

### 1. `sum_to_n(n)`

Returns the sum of numbers from **1 to n**.

Example:

```python
sum_to_n(5)
# Output: 15
```

---

### 2. `count_even_numbers(n)`

Counts how many **even numbers** exist between **1 and n (inclusive)**.

Example:

```python
count_even_numbers(10)
# Output: 5
```

---

### 3. `factorial(n)`

Calculates the **factorial of n** using a loop.

Example:

```python
factorial(5)
# Output: 120
```

---

### 4. `multiplication_table(n)`

Returns the **multiplication table of n from 1 to 10**.

Example:

```python
multiplication_table(3)
# Output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

---

### 5. `sum_of_digits(num)`

Returns the **sum of all digits in a number**.

Example:

```python
sum_of_digits(1234)
# Output: 10
```

---

### 6. `count_vowels(text)`

Counts the number of **vowels (a, e, i, o, u)** in a string.

Example:

```python
count_vowels("hello")
# Output: 2
```

---

### 7. `find_primes(n)`

Returns a list of **prime numbers from 2 up to n**.

Example:

```python
find_primes(10)
# Output: [2, 3, 5, 7]
```

---

### 8. `reverse_string(text)`

Reverses a given string.

Example:

```python
reverse_string("hello")
# Output: "olleh"
```

---

### 9. `pyramid_pattern(n)`

Generates a **pyramid pattern of stars**.

Example:

```python
pyramid_pattern(3)
# Output:
["*", "**", "***"]
```

---

### 10. `multiplication_grid(n)`

Creates an **n × n multiplication grid using nested loops**.

Example:

```python
multiplication_grid(3)
# Output:
[
 [1, 2, 3],
 [2, 4, 6],
 [3, 6, 9]
]
```

---

## 🧪 Running the Tests

This project uses Python's built-in **unittest framework**.

To run the tests:

```bash
python -m unittest
```

or

```bash
python test_assessment.py
```

All tests should pass if the functions are implemented correctly.

---

## 🛠 Requirements

* Python 3.x
* No external libraries required

---

## 🎯 Learning Objectives

This project demonstrates:

* Using **for loops**
* Working with **ranges**
* Applying **conditional logic**
* Using **nested loops**
* Performing **string manipulation**
* Writing **unit tests**

---

## 📄 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Author

Created as part of a **Python programming assessment focused on loops and basic algorithms**.
