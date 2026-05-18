#1
""" 1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8 """
#solution 1
""" n=input("Enter the feedback message = ").lower()
vowel="aeiou"
count=1
for i in n:
    if i in vowel:
        count+=1
        
print("Total vowels:",count) """
# 2
""" 2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5 """
#solution 2
""" n=input("Enter the feedback message = ").lower()
space=" "
count=1
for i in n:
    if i in space:
        count+=1
        
print("Total spaces:",count) """
#3
""" 3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times """
#solution 3
""" n=input("Enter the feedback message = ").lower()
ch=input("Enter the character = ")
count=0
for i in n:
    if ch ==i: 
        count+=1
        
print("Total ",ch,"is ",count) """

#4
""" 4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U """
#solution 4 
""" n=input("Enter the feedback message = ").lower()
vowel="aeiou"
count=1
for i in n:
    if i in vowel:
        count+=1
        
print("Total consonants are :",len(n)-count) """

#5
""" 5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password """
#solution 5
password=input("Enter the password : ")
upper=0
lower=0
special=0
space=1
digit=0
enddigit=0
length=0
if 7<len(password)<16:
     length=1
elif 'A'<=password[0]<='Z':
     upper=1
elif 0<=int(password[-1])<=9:
     enddigit=1
for ch in password:
    if 0<=int(ch)<=9:
        count+=1
        if count>1:
            digit=1
    if ch==" ": 
        space=0
    else:
         special=1
if upper==1 and lower==1 and special==1 and space==0 and digit==1 or enddigit==1 or length==1:

      print("done")
else:
      print("Not Done ") 

#6
""" 6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number """
#solution 6
""" password=input("Enter the password : ")
digit=0
start=0
length=0
pnr="PNR"
p=password[:3]
s=password[3:]
if len(password)>=12:
    length=1
if p==pnr:
    start=1
for ch in s:
    if 0<=int(ch)<=9:
        digit=1
    
if length==1 and start==1 and digit==1:                                                                      
    print("VAlid PNR ")
else:
    print("Not valid ") """
    
#7
""" 7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number """
#solution 7 
""" n=input("Enter the vehicle number : ")
A=0
D=0
L=0
special=0
p=n[:2]
s=n[2:4]
if len(n)>=10:
    L=1
    if 'A'<=p<='Z':
        A=1 
        if 0<=int(s)<=9:
           D=1

    
if L==1 and D==1 and A==1 :                                                                      
    print("VAlid vehicle number ")
else:
    print("Not valid ") """