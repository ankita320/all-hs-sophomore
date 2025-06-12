#! /usr/bin/python3
print("Content-Type: text/html\n\n")


page = '''
<!DOCTYPE html>
<html>
    <head>
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
    </body>
</html>
'''
  
def average(text):
   
    avg_list = []
    names_list = []
    student_list = text.split("\n")
    for slist in student_list:
        grade_avg = 0
        grades = slist.split(" ")
        for grade in grades[2:]:
            grade_avg += int(grade)
        avg = grade_avg / len(grades[2:])
        avg_list.append(avg)
        for name in grades[1:2]:
            names_list.append(name)
    
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
    td = tab + "<tr><td>_TDATA1_</td><td>_TDATA2_/td></tr>\n" + (tab * 2)
    
    th = th.replace("_TTITLE1_", "Name")
    th = th.replace("_TTITLE2_", "Average")
    
    table_page = table_page.replace("_THEADER_", th)
    
    data = ""
    
    for i in range(len(avg_list)):
        tdata = td.replace("_TDATA1_", str(names_list[i]))
        tdata = tdata.replace("_TDATA2_", str(avg_list[i]))
        data += td.replace(td, tdata)
    data = data[:len(data)-1]
    table_page = table_page.replace("_TBODY_", data)
   
    return table_page
  
def generateBody():
    body = "<h1>Average Table</h1>\n"
    body += average('''period1 Krystal 90 45 32 65 66
period1 Tau 59 65 93 88 22 78
period1 Chang 40 97 90 28 31 99
period1 Shan 30 26 35 73 77 99
period1 Bryn 79 93 30 29 23 79 20
period1 Maggie-Rae 78 54 64 50 77
period1 Tiwlip 22 28 54 26 93
period1 Refugio 75 36 83 88 93
period2 Floro 91 74 38 79 20 88 93
period2 Sharilyn 81 76 22 88 73
period2 Alaine 43 56 39 26 71 93
period2 Paula 33 36 24 65 50
period2 Andera 38 90 38 44 24
period2 Onyeka 74 49 32 48 83
period3 Gaia 87 63 82 83 47 74 49
period3 Samira 93 76 84 41 73
period3 Mikaela 84 43 88 22 45
period3 Farrah 75 73 85 42 79
period3 Tiara 62 31 69 53
period3 Valeriy 61 52 86 82 41'''
)
    return body

page = page.replace("_BODY_", generateBody())
print(page)



