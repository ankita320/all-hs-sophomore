from tkinter import Tk, simpledialog, messagebox
print('Ask the Expert - Capital cities of the World')
root = Tk()
root.withdraw()
the_world = {}

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            line1 = line.split()
            country = line1[0]
            city = line1[1]
            the_world[country] = city
read_from_file()

while True:
    query_country = simpledialog.askstring("Country", "Type the name of a country:")
    if query_country.capitalize() in the_world:
        result = the_world[query_country.capitalize()]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring("Teach me", "I don\'t know!" + "what is the capital of" + query_country + "?")
        the_world[query_country] = new_city
        write_to_file(query_country,new_city)
root.mainloop()
        

def write_to_file(country_name,city_name):
    with open('capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '  ' + city_name)
    file.close()
                     

