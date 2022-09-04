from Labirinto import Labirinto
from Agente import Agente
import random

#
#(line, column)

def aptidao(agente:Agente) -> float:

    global foodie
    foodie = 0
    # foodie = 0
    for i in range(len(agente.movimentos)): 

        moviment = agente.movimentos[i]
        agente.set_position_by_moviment(moviment=moviment)
        agente.feet += 1
        if lab.mapp[agente.posicao[0]][agente.posicao[1]] == "c":
            # print(agente.posicao)
            lab.mapp[agente.posicao[0]][agente.posicao[1]] = 0
            foodie += 1
            # print("comi")
            agente.foodie += 1
            # print(agente.foodie)
        else:
            # print("Não achei comida")
            ...
        agente.aptidao += (agente.feet**(agente.feet - foodie))
        if foodie == 5:
            break


def torneio(population:list) -> tuple:

    new_pop = sorted(population, key=lambda x: x.aptidao, reverse=False)
    return tuple(new_pop[0:2])


def crossover(parents:tuple) -> Agente:

    child = Agente()
    child.movimentos = parents[0].movimentos[0:50] + parents[1].movimentos[50:100]
    return child


def mutation(child:Agente) -> Agente:

    if random.random() < child.mutation_probability:
        child.movimentos[random.randint(0,99)] = random.randint(0,8)
    return child



individuos:int = 100
geracoes:int = 100
mutation_factor:float = 0.1
mutation_probability:float = 0.5

for p in range(geracoes):
    
    population = []
    
    for individuo in range(individuos):
        
        lab = Labirinto()
        with open("test.txt") as f:
            text = f.read()
            f.close()
        lab.make_mapp(text)
        # lab.get_mapp()

        if p == 0:
            agente = Agente(id=individuo, mutation_factor=mutation_factor, mutation_probability=mutation_probability)
            agente.set_random_moviments(100)
            # print()
            # print(agente.movimentos)
            aptidao(agente)
            # print(foodie)
            # print(agente.aptidao)
            population.append(agente)
        
        else:
            agente = crossover(bests)
            agente = mutation(agente)
            aptidao(agente)
            # print(agente.movimentos)
            
            population.append(agente)

    bests = torneio(population)
    # print(bests[0].feet, bests[1].feet)
    if bests[0].foodie > 0 or bests[1].foodie > 0:
        print(bests[0].foodie, bests[1].foodie)