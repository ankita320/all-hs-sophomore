def allPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''

        style = '''

body{
  background: pink;
}

.dropdown {
  display: inline-block;
  position: relative;
}

button{
  border:none;
  border-radius:5px;
  padding:15px 30px;
  font-size:18px;
  cursor:pointer;
}

button:hover{
  background-color:#ddd;
}

.dropdown-options {
  display: none;
  position: absolute;
  background-color:aliceblue;
  border-radius:5px;
  box-shadow: 0px 10px 10px 0px rgba(0,0,0,0.4);
}

.dropdown:hover .dropdown-options {
  display: block;
}

.dropdown-options a {
  display: block;
  color: #purple;
  padding: 15px;
  text-decoration: none;
  padding:40px 40px;
}

.dropdown-options a:hover {
  color: white;
  background-color: gray;
  border-radius:5px;
}
'''
        site = site.replace("?STYLE?", style)
        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Pokemon Reviews</h1>\n"
        p = tab * 2 + "<p>I think pokemans are cool even though I haven't really played with them that much. I heard PIkachu is really popular though, so I think that's my favorite! I also heard of Kirby which is also cool!</p>\n"
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="/style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Dark",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "types.html">Types</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "all.html">All Pokeman</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += p
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
        tdata = td.replace("_TDATA0_", img)
        tdata = tdata.replace("_TDATA1_", str(num[i]))
        tdata = tdata.replace("_TDATA2_", str(name[i]))
        tdata = tdata.replace("_TDATA3_", str(type1[i]))
        tdata = tdata.replace("_TDATA4_", str(type2[i]))
        tdata = tdata.replace("_TDATA5_", str(total[i]))
        tdata = tdata.replace("_TDATA6_", str(hp[i]))
        tdata = tdata.replace("_TDATA7_", str(attack[i]))
        tdata = tdata.replace("_TDATA8_", str(defense[i]))
        tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
        tdata = tdata.replace("_TDATA10_", str(spdef[i]))
        tdata = tdata.replace("_TDATA11_", str(speed[i]))
        tdata = tdata.replace("_TDATA12_", str(gen[i]))
        tdata = tdata.replace("_TDATA13_", str(legend[i]))
        data += td.replace(td, tdata)
        data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(allPage())

alls = open("all.html", "w")
print(allPage(), file = alls)
alls.close()


def typesPage():
    return "hegfhthfgfgfgyo"

types = open("types.html", "w")
print(typesPage(), file = types)
types.close()

def topPage():
    return "hegfhthfgfgfgyo"

top = open("top.html", "w")
print(typesPage(), file = top)
top.close()


