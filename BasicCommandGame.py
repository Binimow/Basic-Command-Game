
print ('1- What do you want to do ? \n2- How many building ? \n3- What building ?')
#Défini le premier terme comme étant qqc qui ***ajoute*** la valeur du deuxième terme
def build_something(arg, arg2):
    print("You just executed this function : build")
    all_possible_building[arg] += int(arg2)
#Défini le premier terme comme étant qqc qui ***diminue*** la valeur du deuxième terme
def destroy_something(arg, arg2):
    print('You just executed this function : destroy')
    all_possible_building[arg] -= int(arg2)
#Toutes les choses possibles de construire
all_possible_building = {
    'industry' : 0,
    'house' : 0,
    "potatoe" : 0
    }
all_possible_action = {
    'build' : build_something,
    'destroy' : destroy_something,}
#Melting pot des termes possible
functions = {
    'build': all_possible_action['build'],
    'destroy': all_possible_action['destroy'],
    'industry': all_possible_building["industry"],
    'house' : all_possible_building['house'],
    "potatoe": all_possible_building["potatoe"]
}
#Définition des variables
func1 = 'industry'
func = ""
func2 = 1
test = 1
#Écriture, analyse et mise en action de la commande
while func != 'close':
    try:    
        func = input('What do you want to do ? : ').split()
        func0 = func[0]
        func1 = func[1]
        if (len(func) == 2):
            functions[func0](func1,1)
            print(all_possible_building[func1], func1)
        else:
            func2 = func[2]
            if func[2] in all_possible_building:
                    functions[func0](func2,func1)
                    print (all_possible_building[func2], func2)
    except (ValueError):
            print('Please retry : ValueError')
    except (IndexError):
            print('Please retry : IndexError')
    except (KeyError):
            print('Please retry : KeyError')

