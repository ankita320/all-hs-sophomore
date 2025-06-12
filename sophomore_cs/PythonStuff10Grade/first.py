#def firstHalf(s):
  #  return s[:(len(s) / 2)]
#print(firstHalf("helloo")


def tally(s,letter):
    count = 0
    for i in range(len(s)):
        if s[i] == letter:
            count += 1
    print(count)
tally("abbbbbba!", "b")

def findFirst(s, letter):
    for i in range(len(s)):
        if letter == s[i]:
            return i
        else:
            return -1
findFirst("abba!", "a")

def hello(name):
    return "hello " + name
    
s = "hello world"
for i in range(len(s)):
    print(s[i])
    
def printHail(n):
    while n != 1:
        print(n, end= " ")
        if n % 2 == 0:
            n = int(n / 2)
        elif n % 2 == 1:
            n = 3 * n + 1
    print("1")
printHail(6)

def namesLen(n):
    fullName = ""
    for i in range(n):
        x = input("Enter your next name:")
        fullName += x
    return len(fullName)

        
def countVowels(s):
    count = 0
    for x in s.lower():
        if x in "aeiou":
            count += 1
    return count
    #going character by charcter in the input and seeing if that matches with a vowel, for every charcter that matches +1 --> adds vowel
        
def removeChar(s,c):
    new_string = ""
    for i in s:
        if i != c:
            new_string += i
    return new_string
            
    return(s)
#find and slices work too
        
def countConsonants(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for i in range(len(s)):
        if s[i].lower() in consonants:
            count += 1
    return count
        
def countConsonantsTwo(s):
    consonants = "aeiou"
    count = 0
    for i in range(len(s)):
        if s[i].lower() not in consonants:
            count += 1
    return count
        
print(ord("&"))

def shiftLetterBy1(c):
    return(chr((ord(c))+ 1))

def shiftLetterByN(c,n):
    if n > 0:
        return(chr((ord(c)) + n))
    elif n < 0:
        return((ord(c)) - n)
    
              
def isLowerCase(c):
    for i in range((ord("a")), (ord("z") + 1)):
        if ord(c) == i:
            return True
        else:
            return False

def isLowerCaseCorrect(c):
    return c >= 'a' and c <= 'z'

def uppercaseLetter(c):
    if c >= 'a' and c <= 'z':
        return c.upper()
    else:
        return c
    ##DO NOT USE UPPER
    
def generateTable():
    table = '''
        <table>
            <theader>
                _HEADER_
            </theader>
            <tbody>
                _TBODY_
            </tbody>
            '''
    print(table)
        
def makeStupidTable(n):
        table = table.replace("_THEADER_", "\t\t\t\t Stupid Table")
        for i in range(n):
            line = "<tr><th>" + data + "</th></tr>"
            data -=1
            header += line
        return body

#Declare some variables at the top 
PAGE_TITLE = "The best page!"



#Make a function that generates your content.
#It can be broken up into pieces as needed.
#QUESTION: why are there \n characters here?


def makeLessStupidTable(n):
    full_body = '''\t\t<table>
                        <tr><th>Number</th><th>Square</th></tr>\n'''
    x = 0
    for i in range(n):
        table = ("\t\t\t<tr><td>" + str(x) + "</td>"+ "<td>" + str(i) + "</td></tr>\n")
        table = table.replace(str(i), str(i ** 2))
        table = table.replace(str(x), str(i))
        full_body += table
    full_body += "\t\t</table>"
    return full_body
   
    #add more parts
#page = page.replace("_TITLE_",PAGE_TITLE)




page = '''

'''

import random
def randomList(start,end):
    ulist = '''
        <ul>
            _LBODY_
        </ul>
'''
    data = ""
    for i in range(10):
        l = "\t<li>" + str(i) + "</li>\n\t"
        l = l.replace(str(i), str((random.randint(start,end))))
        data += l.replace(str(i), l)
    ulist = ulist.replace("_LBODY_", data)
   
    return ulist
    print(ulist)
                      
        
   
   

  
def favoritePolynomial(start,end):
    tab = " " * 4
    table_page = '''
    <table>
        <theader>
            _THEADER_
        </theader>
        <tbody>
        _TBODY_
        </tbody>
    </table>
        '''
    th = "<tr><th>_TTITLE1_</th><th>_TTITLE2_/th></tr>"
    td = tab + "<tr><td>_TDATA1_</td><td>_TDATA2_/td><td>_TDATA3_/td><td>_TDATA4_/td></tr>\n" + (tab * 2)
    
    th = th.replace("_TTITLE1_", "X")
    th = th.replace("_TTITLE2_", "y = 3x^2 + 7x + 8")
    
    table_page = table_page.replace("_THEADER_", th)
    
    data = ""
    
    for i in range((end - start) + 1):
        tdata = td.replace("_TDATA1_", str(start))
        tdata = tdata.replace("_TDATA2_", str((3 * (start ** 2))))
        tdata = tdata.replace("_TDATA3_", str(7 * start))
        tdata = tdata.replace("_TDATA4_", str(8))
        start += 1
        data += td.replace(td, tdata)
    data = data[:len(data)-9]
    table_page = table_page.replace("_TBODY_", data)
   
    return table_page
favoritePolynomial(-2, 2)


   
   
def generateBody():
    body = "<h1>My favorite polynomial</h1>\n"
    body = "<p>Below is my favorite polynomial. I like this polynomial because it uses different methods to factor rather just being a simple factor. I can use the quadratic formula to solve this, and I can use the quadratic formula song!!</p>\n"
    body += favoritePolynomial(1,10)
    return body

page = page.replace("_BODY_", generateBody())
print(page)


def makePolyTable(start, end):
    result = "<table>\n<tr><th>x</th><th>y</th></tr>\n"
    for x in range(start, end+1):
        y = x**4 - 2*x**3 + 3*x**2 - 4*x + 5
        result += f"<tr><td>{x}</td><td>{y}</td></tr>\n"
    result += "</table>"
    return result
poly = "2*x**3 + 5*x**2 - 3*x + 1"
table = makePolyTable(-2, 2)
print(table)


##lists

def favoriteNumbersTable():
   table_number = '''
    <!DOCTYPE html>
<html>
    <head>
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
    </body>
</html>'''
   th = "<tr><th>_THEADER1_</th><th>_THEADER2_</th></tr>/n"
   td = "<tr><td>_TDATA1_</th><th>_TDATA2_</th></tr>/n"
   
   th = th.replace("_THEADER1_", "number")
   th = th.replace("_THEADER2_", "why I like it")
    
   table_number = table_number.replace("_THEADER_", th)
   
   tdata = td.replace("_TDATA1_",   "16")
   tdata += td.replace("_TDATA2_",   "16")
   tdata += td.replace("_TDATA1_",   "16")
   tdata += td.replace("_TDATA2_",   "16")
   tdata += td.replace("_TDATA1_",   "16")
   tdata += td.replace("_TDATA2_",   "16")
   tdata += td.replace("_TDATA1_",   "16")
   
   table_number = table_number.replace("_TDATA1_", tdata)
   table_number = table_number.replace("_TDATA2_", tdata)
      
   return table_number


def cleanList(data, thingsToRemove):
    new_list = []
    for i in data:
        if i not in thingsToRemove:
            new_list.append(i)
    return new_list
            

            
   
   
   #passing the adress when list but if regular varibel like x, 5, num2 = num will not make a opy of the list, they're identical, changes tt the same time, to make opy of list, use forloops and for every element, add it