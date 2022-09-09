from Labirinto import Labirinto
from Agente import Agente
import random
from time import sleep
import math

#
#(line, column)

def aptidao(agente:Agente, lab:Labirinto, p:bool) -> float:

    
    foodie = 0
    print(agente.movimentos)

    for i in range(len(agente.movimentos)):

        
        moviment = agente.movimentos[i]
        # print(i,moviment)
        agente.feet += 1
        if p:
            lab.get_mapp()  
        print("Anterior",agente.posicao)
        new_position = agente.set_position_by_moviment_DEMO(moviment=moviment)
        
        if lab.mapp[new_position[0]][new_position[1]] != "1":# and (not lab.mapp[new_position[0]][new_position[1]] == "A"):
            print("ENTROU")
            lab.mapp[agente.posicao[0]][agente.posicao[1]] = "A"+str(i)
            agente.posicao = new_position
        
            if lab.mapp[agente.posicao[0]][agente.posicao[1]] == "c":
                
                foodie += 1
                agente.foodie += 1
                
            if lab.mapp[agente.posicao[0]][agente.posicao[1]] == "0":
                
                # lab.mapp[agente.posicao[0]][agente.posicao[1]] = "A"
                ...
        else:
            
            ...
        print("Nova",new_position)
        
        if foodie == 5:
        
            agente.aptidao = foodie
            print("DEU BREAK")
            # agente.aptidao = (100*foodie) - i
            break
    
    agente.aptidao = foodie
    # print("APTIDAO FILHO",agente.aptidao)    
    agente.lab = lab
    # if lab:
    #     print(agente.lab.get_mapp())    
    #     agente.lab = lab
        


def torneio(population:list) -> tuple:

    new_pop = sorted(population, key=lambda x: x.aptidao, reverse=True)
    
    return tuple(new_pop[0:2])


def crossover(parents:tuple) -> Agente:

    # print("APTIDAO FATHER", parents[0].aptidao)
    child = Agente(mutation_probability=parents[0].mutation_probability)
    # print(parents[0].movimentos)
    child.movimentos = parents[0].movimentos
    # print("Movimentos dos filhos são iguais aos pai? ",child.movimentos == parents[0].movimentos)
    # sleep(1/10)

    return child


def mutation(child:Agente) -> Agente:

    r = random.randint(0,10)
    # print("MOV FILHO ANTES",child.movimentos)
    # print(r, child.mutation_probability)
    if r < child.mutation_probability:
        print("VIU TEIMOSA")
        cromossomo_de_mutacao = random.randint(0,99)
        child.movimentos[cromossomo_de_mutacao] = random.randint(0,7)
    # print("MOV FILHO DEPOIS",child.movimentos)
    
    return child



individuos:int = 100
geracoes:int = 100
mutation_factor:float = 0.1
mutation_probability:float = 0.01
m = False

for p in range(geracoes):
    
    population = []
    
    for individuo in range(individuos):
        
        lab = Labirinto()
        with open("test.txt") as f:
            text = f.read()
            f.close()
        lab.make_mapp(text)
        
        if p == 0:
            
            agente = Agente(id=individuo, mutation_factor=mutation_factor, mutation_probability=mutation_probability)
            agente.set_random_moviments(100)
            aptidao(agente, lab, m)
            population.append(agente)
        
        else:
            
            agente = crossover(bests)
            agente = mutation(agente)
            aptidao(agente, lab, m) 
            if agente.aptidao < bests[0].aptidao:
                print("AQUI DEU A MERDA")
                m = True
                # bests[0].lab.get_mapp()
                # print(agente.aptidao, bests[0].aptidao)
                # print("MOV",agente.movimentos == bests[0].movimentos)
                # print("FOD",agente.foodie == bests[0].foodie)
                # agente.lab.get_mapp()
            
            population.append(agente)
        
    bests = torneio(population)
    # print("FECHOU")
    # print("FECHOU")
    # print("FECHOU")
    # print("FECHOU")
    # print("FECHOU")
    # print("FECHOU")
    # print(bests[0].foodie)
    # print(bests[0].lab.get_mapp())
    # print("FECHOU")
    # print("FECHOU")
    # print("FECHOU")
    # print("FECHOU")
    if p > 3:
        exit()