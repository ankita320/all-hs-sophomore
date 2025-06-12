s = "1=2=3=4"
print(s.split("="))
#divides the stringinto list based on where = is
# makes a list from the characters of what divider is given, divides by =

def makeAList(myString):
    new_list = myString.split(" ")
    total_list = " "
    for i in new_list:
        for j in i:
            j += " "
            j = j.split(" ")
            total_list += total_list.append(j)
    return j

def countOwl(text):
    new_list = text.split(" ")
    count = 0
    for i in new_list:
        if "owl" in i.lower():
            count += 1
    return count

def average(text):
    text = """mariko 90 99 97 89
kobe 91 94 99 89
xiaoxiao 81 94 100 100
david 90 99 79 81
zane 50 79 49 41
amy 90 99 94 94"""
    i = 0
    student_list = text.split("\n")
    print(student_list)
    while i < len(student_list):
        print(student_list[i])
        i += 1
    line = 'mariko 90 99 97 89'
    grades = line.split()
    grade_avg = 0
    for i in line[1:]:
        grade_avg += int(i)
    print(grade_avg)
    
      
      
#    student_avg = ""
 #   for i in student_list:
  #      student = i.split(" ")
   #     for j in student[1:]:
        

def get_index(word):
        ask_index = input("Give an index:")
        if int(ask_index) < 0 or int(ask_index) > len(word) - 1:
            print("Invalid index")
        else:
            return ask_index
        
    
def get_letter(word):
        ask_letter = input("Give a letter:")
        if ask_letter != ask_letter.lower():
            print("must be lowercase")
        elif len(ask_letter) > 1:
            print("must be 1 character!")
        else:
            return ask_letter

def wordLadder():
    initial_word = input("enter a word:")
    for i in range(len(initial_word) - 1):
        new_index = input(get_index(initial_word))
        new_letter = input(get_letter(initial_word))
        initial_word = initial_word.replace(initial_word[int(new_index)], new_letter)
        print(initial_word)
    return initial_word
        

def exclamation(text):
    new_list = []
    new_str = ""
    for letter in text:
        new_list.append(letter)
    for i in range(len(new_list)):
        if new_list[i] == "i":
            new_list[i] = "!"
    for i in new_list:
        new_str += i
    return new_str
    
def exclamation2(text):
    new_str = ""
    for i in text:
        if i == "i":
            new_str += "!"
        else:
            new_str += i
    return new_str

def seq(sqlist):
    sq_list = sq.list.split("\n")
    for i in sq_list:
        print(i, end = "")
        
        