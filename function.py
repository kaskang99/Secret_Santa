import random as random

list_names = ["kang","jenny","antonio","cristina","davi","solomon","jay","jenny","stella","renan","erick","jung sun noh","juliana"]
nome = input("qual seu nome: ")
def choose_name(list,name):
    for i in range(len(list_names)):
        chosen = random.choice(list_names)
        if chosen != name:
            print("Compre um presente para: " + chosen)
            list_names.remove(chosen)
            print(list_names)
            break
        else:
            chosen = random.choice(list_names)
        return chosen

print(choose_name(list_names,nome))