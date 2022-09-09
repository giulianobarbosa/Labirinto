from Labirinto import Labirinto
from Agente import Agente
import random
from time import sleep
import math

#To do:
#Ultimo passo Sem travar
#(line, column)

def aptidao(agente:Agente, lab:Labirinto, validate:bool) -> float:
    
    food = 0
    dif_places = 0

    for i in range(len(agente.movimentos)):

        if lab.mapp[agente.posicao[0]][agente.posicao[1]] != "1":


            if lab.mapp[agente.posicao[0]][agente.posicao[1]] != "A":
                agente.last_good_feet = i
                dif_places +=1
            
            if lab.mapp[agente.posicao[0]][agente.posicao[1]] == "c":
                food += 1
            
            lab.mapp[agente.posicao[0]][agente.posicao[1]] = "A"
            agente.posicao = agente.set_position_by_moviment_DEMO(agente.movimentos[i])

        if food == 5:
            agente.food = food
            break
    
    agente.posicao = (0,0)
    agente.food = food
    agente.aptidao = 10*food + dif_places
    agente.lab = lab.mapp

    if validate == True:
        print("APTIDAO DO MIO", agente.aptidao)


def torneio(population:list) -> tuple:

    new_pop = sorted(population, key=lambda x: x.aptidao, reverse=True)
    return tuple(new_pop[0:2])


def crossover(parents:tuple, id:int) -> Agente:

    child = Agente(id=id, mutation_probability=parents[0].mutation_probability)
    child.movimentos = parents[0].movimentos[:50] + parents[1].movimentos[50:]

    return child

def crossover_and_mut(parents:tuple, id:int) -> Agente:

    child = Agente(id=id, mutation_probability=parents[0].mutation_probability)
    child.movimentos = parents[0].movimentos
    child.movimentos[:parents[0].last_good_feet] += [random.randint(0,7) for i in range(0,50)]

    return child


def mutation(child:Agente) -> Agente:

    r = random.randint(0,10)

    if r < (child.mutation_probability*10):
        cromossomo_de_mutacao = random.randint(0,99)
        child.movimentos[cromossomo_de_mutacao] = random.randint(0,7)

    return child


0

individuos:int = 1000
geracoes:int = 1000
mutation_factor:float = 0.1
mutation_probability:float = 0.8
covers_do_pai = 0
first_population = []


for individuo in range(0, individuos):
        
    lab = Labirinto()
    with open("test.txt") as f:
        text = f.read()
        f.close()
    lab.make_mapp(text)
              
    agente = Agente(id=individuo, mutation_factor=mutation_factor, mutation_probability=mutation_probability)
    agente.set_random_moviments(100)
    aptidao(agente, lab, False)
    first_population.append(agente)


bests = torneio(first_population)
print("MELHOR APTIDAO", bests[0].aptidao, bests[0].food)


for geracao in range(1, geracoes):
    
    population = []
    print()

    for individuo in range(0, individuos):
        
        lab = Labirinto()
        with open("test.txt") as f:
            text = f.read()
            f.close()
        lab.make_mapp(text)

        if individuo == 0:
            covers_do_pai += 1
            population.append(bests[0])
            #NO MUTATION

        elif individuo == 1:
            agente = Agente(id=individuo+geracao, mutation_factor=mutation_factor, mutation_probability=mutation_probability)
            agente.set_random_moviments(100)
            aptidao(agente, lab, False)
            population.append(agente)

        elif individuo == 2:
            agente = crossover_and_mut(bests, id=individuo+geracao)
            aptidao(agente, lab, False)
            population.append(agente)

        else:
            agente = crossover(bests, id=individuo+geracao)
            agente = mutation(agente)
            aptidao(agente, lab, False) 
            population.append(agente)

    bests = torneio(population)
    print("MELHOR APTIDAO", bests[0].aptidao, bests[0].food)
    if bests[0].food == 5:
        print("ACHOU AS COMIDAS")
        print(bests[0].lab)
        break
    del population

print("QUANTIDADE DE IDENTICOS", covers_do_pai)