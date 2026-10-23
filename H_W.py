
# 50 EASY PYTHON FOR LOOP EXAMPLES


# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# 2. Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# 3. Print Hello 5 times
for i in range(5):
    print("Hello")


# 4. Print your name 5 times
for i in range(5):
    print("Sarthak")


# 5. Print numbers from 0 to 9
for i in range(10):
    print(i)


# 6. Print numbers in reverse
for i in range(10, 0, -1):
    print(i)


# 7. Print even numbers
for i in range(2, 21, 2):
    print(i)


# 8. Print odd numbers
for i in range(1, 21, 2):
    print(i)


# 9. Print multiples of 3
for i in range(3, 31, 3):
    print(i)


# 10. Print numbers from 5 to 15
for i in range(5, 16):
    print(i)


# 11. Multiplication table of 2
for i in range(1, 11):
    print(2, "x", i, "=", 2 * i)


# 12. Multiplication table using input
num = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 13. Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum =", total)


# 14. Sum of even numbers
total = 0
for i in range(2, 21, 2):
    total += i
print("Even sum =", total)


# 15. Sum of odd numbers
total = 0
for i in range(1, 21, 2):
    total += i
print("Odd sum =", total)


# 16. Squares of numbers
for i in range(1, 11):
    print(i * i)


# 17. Cubes of numbers
for i in range(1, 6):
    print(i ** 3)


# 18. Factorial of a number
num = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)


# 19. Sum of squares
total = 0
for i in range(1, 6):
    total += i * i
print("Sum of squares =", total)


# 20. Multiples of 5
for i in range(1, 11):
    print(5 * i)


# 21. Print each character in Python
for ch in "Python":
    print(ch)


# 22. Print each character in a name
name = "Sarthak"
for ch in name:
    print(ch)


# 23. Count characters in a string
count = 0
for ch in "Python":
    count += 1
print("Characters =", count)


# 24. Print vowels in a word
word = "education"
for ch in word:
    if ch in "aeiou":
        print(ch)


# 25. Count vowels in a word
word = "education"
count = 0
for ch in word:
    if ch in "aeiou":
        count += 1
print("Vowels =", count)


# 26. Print a word in reverse
word = "Python"
for i in range(len(word) - 1, -1, -1):
    print(word[i])


# 27. Convert characters to uppercase
word = "python"
for ch in word:
    print(ch.upper())


# 28. Count spaces in a sentence
sentence = "I love Python"
count = 0
for ch in sentence:
    if ch == " ":
        count += 1
print("Spaces =", count)


# 29. Print consonants
word = "python"
for ch in word:
    if ch.isalpha() and ch not in "aeiou":
        print(ch)


# 30. Print each word in a sentence
sentence = "Python is very easy"
for word in sentence.split():
    print(word)


# 31. Print all fruits
fruits = ["Apple", "Mango", "Banana"]
for fruit in fruits:
    print(fruit)


# 32. Print all numbers in a list
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)


# 33. Sum of list elements
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print("List sum =", total)


# 34. Find the largest number
numbers = [10, 50, 20, 80, 30]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest =", largest)


# 35. Find the smallest number
numbers = [10, 50, 20, 5, 30]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest =", smallest)


# 36. Count even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("Even count =", count)


# 37. Print odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7]
for num in numbers:
    if num % 2 != 0:
        print(num)


# 38. Multiply all numbers in a list
numbers = [2, 3, 4]
result = 1
for num in numbers:
    result *= num
print("Product =", result)


# 39. Print list items with their index
fruits = ["Apple", "Mango", "Banana"]
for i in range(len(fruits)):
    print(i, fruits[i])


# 40. Search for a number in a list
numbers = [10, 20, 30, 40]
search = 30
found = False

for num in numbers:
    if num == search:
        found = True
        break

if found:
    print("Number found")
else:
    print("Number not found")


# 41. Increasing star pattern
for i in range(1, 6):
    print("*" * i)


# 42. Decreasing star pattern
for i in range(5, 0, -1):
    print("*" * i)


# 43. Square star pattern
for i in range(5):
    print("* * * * *")


# 44. Number pattern
for i in range(1, 6):
    print(str(i) * i)


# 45. Right-aligned star pattern
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)


# 46. Numbers divisible by 3
for i in range(1, 31):
    if i % 3 == 0:
        print(i)


# 47. Numbers divisible by 5
for i in range(1, 51):
    if i % 5 == 0:
        print(i)


# 48. Print positive numbers
numbers = [-5, 10, -2, 20, 0, 8]
for num in numbers:
    if num > 0:
        print(num)


# 49. Check pass or fail
marks = [75, 30, 85, 20, 60]
for mark in marks:
    if mark >= 35:
        print(mark, "Pass")
    else:
        print(mark, "Fail")


# 50. Sum of digits
num = 12345
total = 0
for digit in str(num):
    total += int(digit)
print("Sum of digits =", total)
