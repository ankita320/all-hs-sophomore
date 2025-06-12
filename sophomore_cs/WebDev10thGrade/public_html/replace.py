def replacio(s,q,r):
    s = s.split(" ")
    new_list = []
    for word in s:
        if q == word:
            new_list.append(r)
        else:
            new_list.append(word)
    new_string = " ".join(new_list)
    return(new_string)
 
def bondify_w(name):
    name = name.split(" ")
    print(name[:len(name)-1])
    name = name[1:]
    return name + "," + name