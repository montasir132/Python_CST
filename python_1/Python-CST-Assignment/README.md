````markdown
# 🐍 Python Assignment--

এই অ্যাসাইনমেন্টটি **Python** ভাষার বেসিক প্রোগ্রাম অনুশীলনের জন্য তৈরি করা হয়েছে।  
প্রতিটি প্রশ্নের জন্য আলাদা প্রোগ্রাম লেখা হয়েছে যেখানে **input নেওয়া, output দেওয়া এবং গাণিতিক অপারেশন করা** শেখানো হয়েছে।

> 📖 এই অ্যাসাইনমেন্টটা মূলত খাতায় লিখে জমা দিতে হবে।  
> কোড লেখার সময় নিচে দেওয়া `#` চিহ্ন দিয়ে লেখা **comment** গুলো খাতায় লিখবে না — এগুলো শুধু বোঝার সুবিধার জন্য রাখা হয়েছে।

---

## 🧠 Comment (`#`) কী এবং এর কাজ কী?

Python-এ `#` দিয়ে শুরু হওয়া লাইনগুলোকে **comment** বলা হয়।  ( যিনি কোড করছে সে যাতে বুঝতে পারে কি করতাছে সে তাই একটা মেসেজ আকারে স্টেপ বাই স্টেপ রাখা)
কমেন্ট আসলে **কোড ব্যাখ্যা করার জন্য ব্যবহৃত হয়**, প্রোগ্রাম চালানোর সময় Python এগুলো **ignore করে**।  
মানে এগুলো শুধু মানুষের জন্য—কম্পিউটারের জন্য নয়।

**উদাহরণ:**
```python
# এটি একটি কমেন্ট
print("Hello World")  # এটিও একটি কমেন্ট
````

> 💡 অ্যাসাইনমেন্ট করার সময় কমেন্ট বাদ দিয়ে শুধু প্রোগ্রামের নাম মূল কোড ইনপুট আউটপুট লিখবে।

---

## 📚 Assignment Questions & Code Summary

---

### 🧩 1. [নাম এবং রোল প্রিন্ট কর](assignment_1.py)

**Description:**
এই প্রোগ্রামে ব্যবহারকারীর নাম এবং রোল ইনপুট নিয়ে সেগুলো স্ক্রিনে প্রিন্ট করা হয়েছে।

```python
# Program - 1
n = str(input("Enter Your Name : "))
r = int(input("Enter Your Board Roll : "))
print("Name :-", n, "\nBoard Roll :-", r)
```

**Input:**

```
Montasir
245456
```

**Output:**

```
Name :- Montasir
Board Roll :- 245456
```

---

### ➕➖✖️➗ 2. [দুইটি সংখ্যার যোগ, বিয়োগ, গুণ, ভাগ](assignment_2.py)

**Description:**
দুইটি সংখ্যা ইনপুট নিয়ে তাদের উপর চারটি মৌলিক গাণিতিক অপারেশন (যোগ, বিয়োগ, গুণ, ভাগ) করা হয়েছে।

```python
# Program - 2
a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
sum = a + b
sub = a - b
mul = a * b
div = a / b
print("The sum of", a, "and", b, "=", sum)
print("The subtraction of", a, "and", b, "=", sub)
print("The multiplication of", a, "and", b, "=", mul)
print("The division of", a, "and", b, "=", div)
```

**Input:**

```
10
5
```

**Output:**

```
The sum of 10 and 5 = 15
The subtraction of 10 and 5 = 5
The multiplication of 10 and 5 = 50
The division of 10 and 5 = 2.0
```

---

### 🔲 3. [চতুর্ভুজের ক্ষেত্রফল](assignment_3.py)

**Description:**
দৈর্ঘ্য ও প্রস্থ ইনপুট নিয়ে চতুর্ভুজের ক্ষেত্রফল নির্ণয় করা হয়েছে।

```python
# Program - 3
length = int(input("Enter length: "))
width = int(input("Enter width: "))

area = length * width
print("Area of Rectangle:", area)
```

**Input:**

```
5
2
```

**Output:**

```
Area of Rectangle: 10
```

---

### 🔺 4.  [ত্রিভুজের ক্ষেত্রফল](assignment_4.py)

**Description:**
ভিত্তি (base) ও উচ্চতা (height) ইনপুট নিয়ে ত্রিভুজের ক্ষেত্রফল নির্ণয় করা হয়েছে।

```python
# Program - 4
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print("Area of Triangle:", area)
```

**Input:**

```
2
10
```

**Output:**

```
Area of Triangle: 10.0
```

---

### ⬜ 5. [বর্গক্ষেত্রের ক্ষেত্রফল](assignment_5.py)

**Description:**
একটি বাহুর দৈর্ঘ্য ইনপুট নিয়ে বর্গক্ষেত্রের ক্ষেত্রফল নির্ণয় করা হয়েছে।

```python
# Program - 5
side = int(input("Enter side length: "))

area = side * side
print("Area of Square:", area)
```

**Input:**

```
10
```

**Output:**

```
Area of Square: 100
```

---

### 🌡️ 6. [সেলসিয়াস থেকে ফারেনহাইট রূপান্তর](assignment_6.py)

**Description:**
সেলসিয়াস তাপমাত্রা ইনপুট নিয়ে সেটি ফারেনহাইটে রূপান্তর করা হয়েছে।

```python
# Program - 6
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 1.8) + 32
print("Temperature in Fahrenheit:", fahrenheit)
```

**Input:**

```
88
```

**Output:**

```
Temperature in Fahrenheit: 190.4
```

---
## 7. [তিনটি সংখ্যার মধ্যে ছোট সংখ্যা নির্ণয়](assignment_7.py)
**Description:**
তিনটি সংখ্যার মধ্যে ছোট সংখ্যা নির্ণয়ের প্রোগ্রাম |

### ✔ Program

```python
# Program - 7
a = int(input("Enter a value A =  "))
b = int(input("Enter a value B =  "))
c = int(input("Enter a value C =  "))

if (a < b and a < c):
    print("A =", a, "is the smallest number")
elif (b < a and b < c):
    print("B =", b, "is the smallest number")
else:
    print("C =", c, "is the smallest number")
```

### ✔ Input

```
47
99
72
```

### ✔ Output

```
A = 47 is the smallest number
```

---

## 8. [জোড় এবং বিজোড় সংখ্যা নির্ণয়](assignment_8.py)
**Description:**
জোড় এবং বিজোড় সংখ্যা নির্ণয় প্রোগ্রাম |

### ✔ Program

```python
# Program - 8
a = int(input("Enter a value =  "))
if (a % 2 == 0):
    print(a, "is the Even number")
else:
    print(a, "is the Odd number")
```

### ✔ Input

```
47
```

### ✔ Output

```
47 is the Odd number
```

---

## 9. [স্কোরের উপর ভিত্তি করে লেটার গ্রেড নির্ধারণ](assignment_9.py)
**Description:**
স্কোরের উপর ভিত্তি করে লেটার গ্রেড নির্ধারণের প্রোগ্রাম |

### ✔ Program

```python
# Program - 9
res = int(input("Enter a value =  "))

if (80 <= res):
    print(res, "=", "A+")
elif (70 <= res):
    print(res, "=", "A")
elif (60 <= res):
    print(res, "=", "A-")
elif (50 <= res):
    print(res, "=", "B")
elif (40 <= res):
    print(res, "=", "C")
elif (33 <= res):
    print(res, "=", "D")
else:
    print(res, "=", "F")
```

### ✔ Input

```
47
```

### ✔ Output

```
47 = C
```

---

## 10. [বয়স অনুযায়ী ব্যক্তি Minor / Young / Old নির্ণয়](assignment_10.py)
**Description:**
if-elif-else ব্যবহার করে একজন ব্যক্তি নাবালক (Minor), তরুণ (Young) না বৃদ্ধ (Old) তা নির্ধারণের জন্য প্রোগ্রাম। |

### ✔ Program

```python
# Program - 10
age = int(input("Enter your age: "))

if (age < 19):
    print("Minor")
elif (age < 61):
    print("Young")
else:
    print("Old")
```

### ✔ Input

```
47
```

### ✔ Output

```
Young
```

---


## 📌 Summary

এই ছয়টি প্রোগ্রাম Python-এর সবচেয়ে বেসিক ধারণাগুলো শেখায়:

* **input()** দিয়ে ব্যবহারকারীর কাছ থেকে ডেটা নেওয়া
* **print()** দিয়ে আউটপুট দেখানো
* **গাণিতিক অপারেশন** (+, -, *, /) করা
* **float ও int** টাইপ ব্যবহার করা
* **if–elif–else** ভিত্তিক পাইথন প্রোগ্রাম দেওয়া হলো
* এবং **কমেন্ট** দিয়ে কোড বোঝানো।


---

> ✍️ **Tips:** অ্যাসাইনমেন্ট লেখার সময় কোডের মধ্যে থাকা `#` দিয়ে শুরু হওয়া লাইনগুলো বাদ দিয়ে কেবল মূল প্রোগ্রামটাই লিখবে।

