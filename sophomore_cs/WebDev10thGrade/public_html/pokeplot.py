import matplotlib.pyplot as plt

f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
poke_file = f.read()
poke_list = poke_file.split("\n")

poke_2dlist = []
name = []
type1 = []
type2 = []
attack = []

for row in poke_list[1:]:
    row = row.split(",")
    poke_2dlist.append(row)


for subList in poke_2dlist[0:len(poke_2dlist) - 1]:
    name.append(subList[1])
    type1.append(subList[2])
    type2.append(subList[3])
    attack.append(subList[6])
    
for subList in poke_2dlist[0:len(poke_2dlist) - 1]:
    name.append(subList[1])
    type1.append(subList[2])
    type2.append(subList[3])
    attack.append(subList[6])

top_name = []
top_attack = []

for i in range(1,151, 15):
    top_name.append(name[i])
    top_attack.append(attack[i])
#check for equal items

font1 = {'family':'serif','color':'green','size':20}
font2 = {'family':'serif','color':'purple','size':15}

plt.bar(top_name, top_attack)
plt.title("Attack Scores of Fire Pokemon", fontdict = font1)
plt.xlabel("Fire Pokemon", fontdict = font2)
plt.ylabel("Attack Scores", fontdict = font2)
plt.grid(axis = "x")
plt.show()