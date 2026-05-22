# QUE 1 
""" 1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
 """
#SOLUTION 1 
        
""" us=input("Enter user name: ").lower()

l=len(us)
if l>=5 and l<=12:
    if "a"<=us[0] and us[0]<="z":
        i=0
        while i<l:
            ch=us[i]
            if ch==" ":
                print("Invalid")
                break
            i=i+1
        else:
            print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid Username") """


# QUE 2
""" 
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12 """
#SOLUTION 2
""" us=input("Enter Number: ")
i=0
c=0
while i<len(us):
    ch=us[i]
    if ch>="0" and ch<="9":
        c=c+1
    i=i+1
print("Total digits:",c) """

# QUE 3
""" 3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5 """
#SOLUTION 3
""" us=input("Enter complaint: ")
i=0
c=0
result=us.split(" ")
print(result)
while i<len(result):
    c=c+1
    i=i+1
print("Total words:",c)
print("Total words:",len(result)) """

#OR

""" us=input("Enter complaint: ")

c=0
for i in us:
    if i==" ":
        c=c+1
print("Total words:",c+1)  """      

# QUE 4
""" 
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID """
#SOLUTION 4

""" ed=input("Enter Employee Id: ")
c=0
for i in ed:
    c=c+1
if c==8:
    if ed[0]=="E" and ed[1]=="M" and ed[2]=="P":
        for i in range(3,c):
             ch=ed[i]
             if ch>="0" and ch<="9":
                 pass
             else:
                print("Invalid Employee Id3")
        else:
            print("Valid Employee Id")
            
    else:
        print("Invalid Employee Id")
else:
    print("Invalid Employee Id 1") """

# QUE 5
""" 5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code """
#SOLUTION 5
""" p=input("Enter Product Name: ").lower()
l=0
for i in p:
   l=l+1
re=""
for i in range(l-1,-1,-1):
    ch=p[i]
    re=re+ch
if re==p:
    print("Palindrome")
else:
    print("Not Palindrome") """
#or
""" 
p=input("Enter Product Name: ").lower()
b=p[::-1]

if b==p:
    print("Palindrome")
else:
    print("Not Palindrome") """
# QUE 6
""" 
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching """
#SOLUTION 6
""" s1=input("enter the first product: ").lower()
s2=input("enter the second product: ").lower()

if len(s1)!=len(s2):
     print("Both Product COdes are not matching")
else:
    f=1
    for i in s1:
        if s1.count(i)!=s2.count(i):
           f=0
           break
    if f==1:
        print("Both Product COdes are  matching")
    else:
        print("Both Product COdes are not matching") """
#or
""" s1=input("enter the first product: ").lower()
s2=input("enter the second product: ").lower()

if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Both Product COdes are  matching")
    else:
        print("Both Product COdes are not matching")
else:
    print("Both Product COdes are not matching") """

# QUE 7
""" 7.
Smart City Citizen Information Formatter

The Smart City Management Department is developing a digital portal to store citizen information in a professional format. Many citizens enter their details using small letters, uppercase letters, mixed casing, or numbers, which creates problems while generating official documents like ID cards, electricity bills, tax records, certificates, and address proofs.

To solve this issue, the department wants a program that automatically converts only the first character of every word into uppercase while keeping the remaining characters unchanged.

The input may contain:
- Words already written in uppercase
- Mixed-case words
- Numbers
- Address details
- Department names
- City names

Task:
Read a complete string from the user and convert the first character of every word into uppercase.

Conditions:
- Words may contain spaces between them
- Do not use built-in title() function
- Digits should remain unchanged

Input:
Enter citizen information:
deepika padukone from smart city raisen madhya pradesh

Output:
Formatted Information:
Deepika Padukone From Smart City Raisen Madhya Pradesh


Test Case 2:
Input:
Enter citizen information:
DEEPIKA pADukone ward number 12

Output:
Formatted Information:
DEEPIKA PADukone Ward Number 12


Test Case 3:
Input:
Enter citizen information:
government engineering college bhopal zone 3

Output:
Formatted Information:
Government Engineering College Bhopal Zone 3


Test Case 4:
Input:
Enter citizen information:
python FULL stack developer batch 18

Output:
Formatted Information:
Python FULL Stack Developer Batch 18 """
#SOLUTION 7
""" info=input("Enter citizen information: ")

l=len(info)
i=0
re=""
while i <l:
    
    ch=info[i]
    if i==0 or info[i-1]==" ":
        if ch>="a" and ch<="z":
            upper=ord(info[i])-32
            re=re+chr(upper)
        else:
            re=re+ch
    else:
        re=re+ch
    i=i+1
            
print(re) """  
               #OR
""" info=input("Enter citizen information: ")
re=info.title()
print(re) """



# QUE 8
""" 
8.
Airport Passenger Name Formatting System

An international airport is developing an automated passenger management system. Many passengers enter their details in different formats such as lowercase, uppercase, mixed-case letters, and numbers while booking flight tickets online.

Due to inconsistent formatting, problems occur while generating boarding passes, security verification records, and passenger identity reports.

To solve this issue, the airport authority wants a program that automatically converts only the first character of every word into uppercase while keeping all remaining characters unchanged.

The input may contain:
- Passenger names
- Passport details
- Terminal names
- Seat numbers
- City names
- Mixed uppercase/lowercase letters
- Digits

Task:
Read a complete string from the user and convert the first character of every word into uppercase.

Conditions:
- Words may contain spaces
- Digits should remain unchanged
- Do not use built-in title() function

Input:
Enter passenger details:
deepika padukone flight ai202 terminal 3 mumbai

Output:
Formatted Details:
Deepika Padukone Flight Ai202 Terminal 3 Mumbai


Test Case 2:
Input:
Enter passenger details:
DEEPIKA pADukone gate number 12

Output:
Formatted Details:
DEEPIKA PADukone Gate Number 12


Test Case 3:
Input:
Enter passenger details:
international departure terminal delhi airport

Output:
Formatted Details:
International Departure Terminal Delhi Airport


Test Case 4:
Input:
Enter passenger details:
business class passenger seat b12

Output:
Formatted Details:
Business Class Passenger Seat B12 """
#SOLUTION 8
""" info=input("Enter citizen information: ")

l=len(info)
i=0
re=""
while i <l:
    
    ch=info[i]
    if i==0 or info[i-1]==" ":
        if ch>="a" and ch<="z":
            upper=ord(info[i])-32
            re=re+chr(upper)
        else:
            re=re+ch
    else:
        re=re+ch
    i=i+1
            
print(re) """  
               #OR
""" info=input("Enter citizen information: ")
re=info.title()
print(re) """