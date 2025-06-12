#! /usr/bin/python3
print("Content-Type: text/html\n\n")

import matplotlib.pyplot as plt

with open("Accidental_Drug_Related_Deaths_2012-2021.csv", "r") as text:
    text = text.read()
    text = text.split("\n")
    text = text[:len(text)-1]
    for i in range(len(text)):
        text[i] =  text[i].split(",")
    newtext = []
    for i in range(len(text)):
        if len(text[i]) > 5:
            newtext.append(text[i])
    print(newtext)
         

def getagedata():
    all_ages = []
    x_refined_ages = []
    for i in newtext[1:]:
        if i not in all_ages:
            all_ages.append(i[2])
   

    for i in all_ages:
        if i not in x_refined_ages:
            x_refined_ages.append(i)
           
    int_ages = []
    for i in x_refined_ages:
        if i != '':
            int_ages.append(int(i))
               
#    plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
   
    y_num_deaths_age = []
    for i in int_ages:
        y_num_deaths_age.append(all_ages.count(str(i)))
       
    font1 = {'family':'monospace','color':'black','size':15}
    font2 = {'family':'monospace','color':'darkred','size':12}
    plt.title("Age vs. # of Deaths", fontdict = font1, loc = 'center')
    plt.xlabel("Age", fontdict = font2)
    plt.ylabel("Number of Deaths", fontdict = font2)
   
    colors = []
    for i in range(len(int_ages)):
        avg = (int_ages[i] + y_num_deaths_age[i]) / 2
        colors.append(avg)
    plt.scatter(int_ages,y_num_deaths_age, c=colors, cmap='twilight')
    ax = plt.gca()
    ax.set_facecolor("#faf5f2")
    plt.colorbar() 
    plt.grid()
    plt.savefig("ageData1.png")
    plt.show()
print(getagedata())