# 🐍 Python Basics - PPS Lab (FE Sem 2)

After surviving Semester 1 with C and its pointers, Python felt like a breath of fresh air. Simple syntax, no semicolons, and swapping variables in one line?💅🏻
---
## What's This?

My **First Year Engineering, Semester 2** practicals for **Programming and Problem Solving (PPS)** - where I learned that Python makes coding feel less like work and more like conversation.

**From C to Python:** The journey from `printf` to `print()`, from manual memory to "Python handles it".

---

## 📂 What's Inside
```
PPS-Practicals-FE-2025-USS/
├── armstrong_number.py      # Number theory magic
├── swap_numbers.py          # The no-temp-variable trick
├── even_odd.py              # Modulo basics
├── prime_number.py          # Trial division algorithm
├── string_operations.py     # String manipulation
├── gross_salary.py          # Real-world calculations
└── pyramid_pattern.py       # Nested loops beauty
```

**7 programs** covering Python fundamentals, from basic I/O to pattern printing.
---

## Running These
```bash
python3 program_name.py
# That's it. No compiling. No errors about missing semicolons.
```

### Interactive Mode (for playing around)
```bash
python3 -i program_name.py
# Run it, then mess with the variables afterward
```

---

## 📝The Programs

### 1. **armstrong_number.py** - The Satisfying Number
**What it does:** Checks if a number equals the sum of its digits raised to the power of digit count  
**Example:** 407 = 4³ + 0³ + 7³ = 407 ✨  
**Learned:** List comprehensions make this so elegant

### 2. **swap_numbers.py** - Python's Party Trick  
**What it does:** Swaps two numbers without a temp variable  
**The magic:** `a, b = b, a` (this blew my mind)  
**In C:** Would need 5+ lines and a temp variable

### 3. **even_odd.py** - Modulo Basics
**What it does:** Checks if a number is even or odd using `%`  
**Simple but:** Foundation for understanding divisibility

### 4. **prime_number.py** - Number Theory  
**What it does:** Checks if a number is prime using trial division  
**Algorithm:** Tests divisibility up to √n (efficient!)  
**Learned:** Sometimes simple algorithms are the best

### 5. **string_operations.py** - String Manipulation
**What it does:** Length, reversal, substring checking  
**The beauty:** `"".join(reversed(str))` is so pythonic  
**Also:** The `in` operator for substring search - no loops needed!

### 6. **gross_salary.py** - Real World Math
**What it does:** Calculates gross salary from basic pay  
**Components:** HRA (10%) + DA (5%) - PF (80%)  

### 7. **pyramid_pattern.py** - Nested Loop Art
**What it does:** Prints a symmetric asterisk pyramid  
**Concept:** Spaces + asterisks, controlled by nested loops  
**Satisfaction level:** High when the pattern looks perfect

---

## What Python Taught Me (After C)

### The Python Way
```python
# C way (what I was used to)
int temp = a;
a = b;
b = temp;

# Python way (mind = blown)
a, b = b, a
```

### The "Wait, That's It?" Moments
- **Reversing a string:** `reversed()` function exists
- **String search:** `if substring in string:` (no manual loops!)
- **Exponentiation:** `**` operator (not `pow()`)
- **User input:** `input()` returns a string (simple!)

---

## 🌸Semester Context

**Before this (Sem 1):** C programming - pointers, malloc/free, printf/scanf  
**This semester (Sem 2):** Python - where coding feels human-friendly  
**What changed:** Understanding stayed same, syntax got friendlier

---

## Complexity Check

| Program | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Armstrong | O(d) where d = digits | O(1) |
| Swap | O(1) | O(1) |
| Even/Odd | O(1) | O(1) |
| Prime | O(√n) | O(1) |
| String Ops | O(n) for reversal | O(n) |
| Salary | O(1) | O(1) |
| Pyramid | O(n²) | O(1) |

---

**From C to Python:**
- C taught me how computers work
- Python taught me how to solve problems elegantly
- Both are valuable, different tools for different jobs

---

## 💭Notes to Future Me
```python
# Things to remember:
remember = [
    "Indentation matters (it's not just style)",
    "Everything is an object in Python",
    "Use f-strings for formatting",
    "List comprehensions > explicit loops",
    "Python has batteries included (use them!)"
]
```
First Year Engineering - AI & ML  
Semester 2 (Apr 2023)

[LinkedIn](https://www.linkedin.com/in/umasalunke7) • [GitHub](https://github.com/ivy-1602) • [Email](mailto:umasalunke7@gmail.com)

---

## 📄License

MIT License - Learn, use, share!

---

*Made with 🤍, 🐍 & relief*

*P.S. - If you find a bug, no you didn't. These are foundational programs, they work perfectly.*
