#! /usr/bin/python3
print("Content-Type: text/html\n\n")

site = '''
<DOCTYPE HTML>
<html>
  <head>
    <title>
      ?TITLE?
    </title>
    <link rel="stylesheet" href="style.css" type="text/css">
  </head>
  <body>
    ?BODY?
  </body>
</html>'''

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

#generates navbar
def generateNavbar():
    navbar= "<!--code for navbar-->"
    navbar+="\n    <header>\n"
    navbar+="      <nav>\n"
    navbar+="        <ul>"
    for i in ["amy", "ankitapage", "zoey", "victoria"] :
        if i == "amy":
            navbar+="\n          <li><a href=\"" + "dataproject" + ".py\">" + i + "</a></li>"
        else:
            navbar+="\n          <li><a href=\"" + i + ".html\">" + i + "</a></li>"
    navbar+="\n        </ul>"
    navbar += "\n      </nav>"
    navbar+="\n    </header>"
    return navbar

#######################################################################
# Amy Kuang - City vs Number of Deaths
#######################################################################
diction = {}

for i in newtext[1:]:
    if i[9] not in diction:
        diction[i[9]] = 1
    else:
        diction[i[9]] += 1

def getPievalues():
    dictionvalues = sorted(diction.values(), reverse=True)[:15]
    return dictionvalues

def getPiekeys(data):
    dictionkeys = []
    for numbers in data:
        for k in diction:
            if diction[k] == numbers:
                if k not in dictionkeys:
                    dictionkeys.append(k)
                    continue
    return dictionkeys

def piechart(ydata, label):
    font1 = {'family':'serif','color':'blue','size':20}
    plt.pie(ydata, labels = label, startangle = 90, explode = [0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], shadow = True)
    plt.title("Location vs Number of Deaths", fontdict = font1, loc = 'left')
    plt.savefig("myPie.png")
piechart(getPievalues(), getPiekeys(getPievalues()))

def amysbody():
    body=generateNavbar()
    body+= "\n    <h1>Amy's Pie Chart</h1>\n"
    body += "    <p>Here is a pie chart of the top 15 locations where there were the most amoubt if drug-related deaths</p>"
    body += "<img src=\"myPie.png\" alt=\"My pie chart of the top 15 locations\">"
    return body

amysite = site.replace("?BODY?", amysbody())
amysite = amysite.replace("?TITLE?", "Amy's Pie Chart")

print(amysite)

#######################################################################
# Zoey Zhou
#######################################################################
def deaths():
    newdict = {}
    for i in range(len(newtext)):
        if i != 0:
            if newtext[i][19].lower() not in newdict.keys():
                newdict[newtext[i][19].lower()] = 1
            else:
                for j in newdict.keys():
                    if j == newtext[i][19].lower():
                        newdict[j] += 1
    newdict.pop("")
    sortedv = sorted(newdict.values(),reverse=True)
    yvalues = []
    xvalues = []
    for i in range(15):
        yvalues.append(sortedv[i])
    for i in yvalues:
        for j in newdict:
            if newdict[j] == i:
                xvalues.append(j)
    for index, value in enumerate(yvalues):
        plt.text(value,index,str(value))
    for i in range(len(xvalues)):
        xvalues[i] = xvalues[i].replace("\"","")

    plt.figure(figsize=(20,15))
    plt.barh(xvalues,yvalues, height=0.5)
    plt.xlabel("# of Deaths")
    plt.ylabel("Cause of Death")
    plt.title("Top 10 Drug Related Causes of Deaths")
    plt.yticks(fontsize=5)
    plt.savefig("ZoeyGraph.png")
    #plt.show()
#homepage
deaths()
def generatebody():
    body = generateNavbar()
    body += "<h1>Zoey's Bar Graph</h1>\n"
    body += "<p>Here, we compare the top 10 most prominent drug related causes of death in...</p>\n"
    body += "<img src=\"ZoeyGraph.png\" alt=\"Bar Graph\">"
    return body
def makePage(filename):
    html_file = open(filename + ".html", "w")
    zoeysite = site
    zoeysite = zoeysite.replace("?TITLE?","Zoey's webpage")
    zoeysite = zoeysite.replace("?BODY?",generatebody())
    print(zoeysite, file=html_file)
    html_file.close()

makePage("zoey")

#######################################################################
# Ankita Saha - age vs death, death vs date
#######################################################################
def getdatedata():
    yr2012 = []
    yr2013 = []
    yr2014 = []
    yr2015 = []
    yr2016 = []
    yr2017 = []
    yr2018 = []
    yr2019 = []
    yr2020 = []
    yr2021 = []

    yYears = [yr2012, yr2013, yr2014,yr2015,yr2016,yr2017,yr2018,yr2019,yr2020,yr2021]
    yearNum = ["2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
    for i in newtext:
        for j in range(len(yearNum)):
            if yearNum[j] in i[0]:
                yYears[j].append(i[0])

    y_values = []
    for i in yYears:
        y_values.append(len(i))

    x_values = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

    font1 = {'fontname':'monospace','color':'black','size':15}
    font2 = {'family':'monospace','color':'#1b596e','size':12}
    plt.title("Time vs. # of Deaths", fontdict = font1, loc = 'center')
    ax = plt.gca()
    ax.set_facecolor("aliceblue")
    plt.xlabel("Year", fontdict = font2)
    plt.ylabel("Number of Deaths", fontdict = font2 )
    plt.plot(x_values, y_values, '#3ab6c9',  marker = '*')
    plt.grid()
    plt.savefig("dateData.png")

# print(getdatedata())

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
    plt.savefig("ages.png")


def ankitaPage(site):
    tab = " " * 4
    site = site.replace("?TITLE?", "Age & Date")
    head = ""

    h1 = "<h1>Age & Death Data</h1>\n"
    p = tab * 2 + "<p>I think pokemans are cool even though I haven't really played with them that much. I heard Pikachu is really popular though, so I think that's my favorite! I also heard of Kirby which is also cool!</p>\n"

    technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''
#loop for

    data = ""
    data += technical
    data += generateNavbar()
    data += h1
    data += p
    data += "<img src= \"ages.png\">"
    data += "<img src= \"dateData.png\">"
    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)

ankita = open("ankitapage.html", "w")
print(ankitaPage(site), file = ankita)
ankita.close()



