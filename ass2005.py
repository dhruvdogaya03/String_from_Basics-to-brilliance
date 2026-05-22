# QUE 1
""" 1. Remove All Special Characters from a String

Online Banking Customer Data Cleaning System

A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.

Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

* Alphabets
* Numbers
* Spaces

The cleaned value should be stored back into the original string variable.

Input:

Deepika@@ Padukone!! 123
Output:
Deepika Padukone 123
Input:
Ajay###Singh$$$
Output:
AjaySingh """
#SOLUTION 1
""" n=input("Enter the string : ")

new=""
for ch in range (len(n)):
    if "a"<=n[ch]<="z" or "0"<=n[ch]<="9" or "A"<=n[ch]<="Z":
        new=new+n[ch]

print(new) """

# QUE 2
""" 2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:
Python is powerful
Output:
lufrewop si nohtyP """
#SOLUTION 2
""" n=input("Enter the string : ")
half=n[::-1]
print(half) """
#or 
""" n=input("Enter the string : ")
rev="" 
for i in n:
 
        rev=i+rev
print(rev)
 """


# QUE 3
""" ```
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:
e
``` """
#SOLUTION 3

""" n = input("Enter the string : ")

for i in n:
    count = 0

    for j in n:
        if i == j:
            count += 1

    if count == 1:
        print(i)
        break
 """
#or
"""n=input("Enter the string : ")
l=len(n)
for i in n:
    if n.count(i)==1:
        print(i) """


# QUE 4
""" 4. Program should work for both uppercase and lowercase letters.

 Find the Shortest Word in a Sentence

Telecom SMS Cost Optimization System

A telecom company charges customers based on the length of words used in bulk SMS campaigns.

The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.

Input:
Python is very easy to learn
Output:
is
``` """
#SOLUTION 4
""" n=input("Enter the string : ")
l=len(n)
s1=n.split()
print(s1)
small=s1[0]
for i in s1:
    if len(i)<len(small):
        small=i
print(small)    """
  
# QUE 5
""" 5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.
Input:
aabbccdde
Output:
5
``` """

#SOLUTION 5
""" n=input("Enter the n:")
count=0
rev=""
for i in n:
    if i not in rev:
        rev=i+rev
print(len(rev)) """



# QUE 6
""" 6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:

```
iphone is good and iphone battery is strong
```

Word:
iphone
Output
2
 """
#SOLUTION 6
""" n=input("Enter the string :")
m=n.split()
word=input("Enter the word :")
count=0
for i in m:
    if word ==i :
        count+=1
print(count) """

# QUE 7
""" 7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System 

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you
```

Output:

```
hello how are you """
#SOLUTION 7
""" n=input("Enter the n ;")
s=n.split()
rev=[]
for i in s:
    if i not in rev:
        rev.append(i)
print(rev) """

# QUE 8
""" 
8.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found """
#SOLUTION 8
n=input("Enter the string :").lower()
highest=""
secondhig=""
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
            s=i
print(s)
print(count)

