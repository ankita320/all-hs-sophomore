#! /usr/bin/python3
print("Content-Type: text/html\n\n")

page = '''<!DOCTYPE html>
<html>
    <head>
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
    </body>
</html>
'''

def favoritePolynomial(start,end):
    tab = " " * 4
    table_page = '''    <table>
            <theader>
                _THEADER_
            </theader>
            <tbody>
            _TBODY_
            </tbody>
        </table>'''
    th = "<tr><th>_TTITLE1_</th><th>_TTITLE2_</th></tr>"
    td = tab + "<tr><td>_TDATA1_</td><td>_TDATA2_</td></tr>\n" + (tab * 3)

    th = th.replace("_TTITLE1_", "X")
    th = th.replace("_TTITLE2_", "y = 3x^3 + 4x + 8")

    table_page = table_page.replace("_THEADER_", th)

    data = ""

    for i in range((end - start) + 1):
        tdata = td.replace("_TDATA1_", str(start))
        tdata = tdata.replace("_TDATA2_", str((3 * (start ** 3)) + (4 * start) + 8))
        start += 1
        data += td.replace(td, tdata)
    data = data[:len(data)-13]
    table_page = table_page.replace("_TBODY_", data)
    return table_page

def generateBody():
    body = "<h1>My favorite polynomial</h1>\n"
    body += "<p>Below is my favorite polynomial. I like this polynomial because it uses different methods to factor rather just being a simple factor. I can use the quadratic formula to solve this, and I can use the quadratic formula song!!</p>\n"
    body += favoritePolynomial(-20,50)
    return body

page = page.replace("_TITLE_", "Favorite Polynomial")
page = page.replace("_BODY_", generateBody())
print(page)
