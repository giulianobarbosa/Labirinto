from typing import Tuple
from Labirinto import Labirinto
from Agente import Agente
import random
import time

#Função de aptidao
def aptidao(agente:Agente, lab:Labirinto, saving:bool=False) -> float:

    """
    Essa função irá retornar o quão apto o agente passado para ela está para enfrentar o desafio do labirinto
    O calculo é 10*food + dif_places, sendo food a quantidade de comida que ele comeu ao final do labirinto
    e dif_places a quantidade de lugares novos que ele explorou

    Params:
    agente -> É o agente que será avaliado
    lab -> É o labirinto que o agente será avaliado
    saving -> Para salvar em um txt o trajeto do agente no labirinto
    """
    
    #food e dif_places começam zerados pois o agente ainda não percorreu o labirinto
    food = 0
    dif_places = 0

    #Iteração sobre o vetor de movimentos do agente para gerar seus movimentos no labirinto
    for i in range(len(agente.movimentos)):

        #Aqui vemos se a posição que o agente quer ir é possível, 
        # pois a posicao do agente é dada por uma tupla(linha, coluna)
        if lab.mapp[agente.posicao[0]][agente.posicao[1]] != "1":
            
            # Aqui vemos se o agente quer ir é um lugar novo para guardarmos
            # a quantidade de lugares novos que o agente foi, além de
            #  o last_good_feet que é o ultimo lugar novo que o agente alcançou
            if lab.mapp[agente.posicao[0]][agente.posicao[1]] != "A":
                agente.last_good_feet = i
                dif_places +=1
            
            #Aqui vemos se é comida para que possamos armazenar a quantidade de comidas que o agente comeu
            if lab.mapp[agente.posicao[0]][agente.posicao[1]] == "c":
                food += 1
            
            #Aqui setamos o lugar que o agente passou para "A" no labirinto para guardar a trajetória do agente
            lab.mapp[agente.posicao[0]][agente.posicao[1]] = "A"
            #Aqui atualizamos a posição do agente para sua proxima posição conforme seu vetor de movimentos 
            agente.posicao = agente.set_position_by_moviment_DEMO(agente.movimentos[i])
        
        #Se o agente bater na parede ele sai do loop, ou seja ele morre
        else:
            break

        #Verificando se é para salvar
        if saving:
            #Tenta sobreescrever um arquivo já existente
            try:
                with open("best_agent_maze.txt", "a") as f:
                    f.write(f"\n Movimento {i}\n")
                    for line in lab.mapp:
                        f.write(f"{str(line)}\n")
            # Se falhou a sobreescrever o arquivo não existe, logo nós criamos e escrevemos nele
            except:
                with open("best_agent_maze.txt", "w") as f:
                    f.write(f"\n Movimento {i}\n")
                    for line in lab.mapp:
                        f.write(f"{str(line)}\n")
        
        #Se o agente pegar as 5 comidas ele para o loop, pois pegou todas
        #MUDAR PARA VER SE PEGOU N/2 COMIDAS
        if food == 5:
            agente.food = food
            break

    #Seta a posição do agente de volta para a inicial para que os filhos não surjam na mesma posição que o pai terminou
    agente.posicao = (0,0)
    #Seta a comida do agente para a quantidade de comidas que ele pegou
    agente.food = food
    #Seta a aptidao do agente
    agente.aptidao = 10*food + dif_places
    #Seta o labirinto do agente conforme a sua trajetória
    agente.lab = lab.mapp
    #printa a aptidao e id do agente
    print(agente.aptidao, agente.id)

#Função que ordena o vetor de população e retorna uma tupla com os dois melhores agentes
def torneio(population:list) -> Tuple[Agente]:
    
    #ordenando a população conforme a aptidao
    new_pop = sorted(population, key=lambda x: x.aptidao, reverse=True)
    #retornando uma tupla com os dois melhores agentes
    return (new_pop[0], new_pop[1])

#Função que irá fazer a combinação dos movimentos dos pais (2 melhores agentes do torneio)
def crossover(parents:Tuple[Agente], id:int) -> Agente:

    #Criando um agente com prob de mutação igual ao do pai
    child = Agente(id=id, mutation_probability=parents[0].mutation_probability)
    #Setando o vetor de movimentos do filho como o vetor de movimentos do pai até o seu melhor passo(ultimo lugar diferente visitado)
    # e completando o vetor com os movimentos da mãe
    child.movimentos = parents[0].movimentos[:parents[0].last_good_feet] + parents[1].movimentos[parents[0].last_good_feet:]
    #retornando o filho
    return child

#Função que irá fazer o filho uma copia exata do pai
def parthenogenesis(parent:Agente, id:int) -> Agente:

    #Criando um agente com prob de mutação igual ao do pai
    child = Agente(id=id, mutation_probability=parent.mutation_probability)
    #Setando o movimento do filho para igual ao do pai
    child.movimentos = parent.movimentos
    #Retornando o filho
    return child

#Função que faz a copia do pai e muta os cromossomos a partir do ultimo melhor passo
def crossover_and_mut(parent:Agente, id:int) -> Agente:
    #Criando um agente com prob de mutação igual ao do pai
    child = Agente(id=id, mutation_probability=parent.mutation_probability)
    #Setando o movimento do filho para igual ao do pai até o seu melhor passo(ultimo lugar diferente visitado)
    child.movimentos = parent.movimentos[:parent.last_good_feet]
    #Completando o vetor de movimentos com novos movimentos aleatórios
    child.movimentos += [random.randint(0,7) for i in range(parent.last_good_feet, len(parent.movimentos))]
    #Retornando o filho
    return child

#Função que vai mutar o agente
#MUDAR O 99 PARA O TAMANHO DO LABIRINTO
def mutation(child:Agente) -> Agente:
    
    r = random.randint(0,10)
    #Vendo se o agente irá mutar com se o numero aleatório gerado é melhor do que a taxa de mutação passada
    if r < (child.mutation_probability*10):
        cromossomo_de_mutacao = random.randint(0,99)
        child.movimentos[cromossomo_de_mutacao] = random.randint(0,7)
    #Retornando filho
    return child

#Função que irá resetar a população com novos individuos aleatóriamente gerados sem nenhuma relação com a geração passada
# ESSA FUNÇÃO SÓ SERÁ UTILIZADA EM CASO DE CONVERGENCIA DOS INDIVIDUOS PARA UMA APTIDAO QUE AINDA NÃO É DESEJADA
def reset_generation(individuos, mutation_factor, mutation_probability):
    #gerando a lista de populacao
    population = []
    #Loop que cria os individuos
    for individuo in range(0, individuos):
        #Bloco que cria o labirinto
        lab = Labirinto()
        with open("test.txt") as f:
            text = f.read()
            f.close()
        lab.make_mapp(text)
        
        #Criando agentes totalmente novos e aleatórios
        agente = Agente(id=individuo, mutation_factor=mutation_factor, mutation_probability=mutation_probability)
        #Criando novos movimentos totalmente aleatórios
        #MUDAR ESSE 100 PARA O TAMANHO DO LABIRINTO
        agente.set_random_moviments(100)
        #Vendo a aptidao do agente criado 
        aptidao(agente, lab, False)
        #Colocando o agente na população
        population.append(agente)
    #Retornando a população nova
    return population


#Parametros universais para individuos e geracoes
individuos:int = 100
geracoes:int = 100
mutation_factor:float = 0.1
mutation_probability:float = 0.8

#geracao começa em 0
geracao = 0
#Criando a primeira população
first_population = reset_generation(individuos=individuos, mutation_factor=mutation_factor, mutation_probability=mutation_probability)
#Pegando os melhores da primeira população 
bests = torneio(first_population)
#Printando O MELHOR individuo
print("MELHOR APTIDAO DA GERAÇÃO ", bests[0].aptidao, bests[0].food)

#Loop que gerará as próximas gerações
while True:
    #Contabilizando a geração
    geracao += 1
    print("="*50, f"\n Geração {geracao}\n", "="*50)
    #Criando a população da geração específica
    population = []

    #Loop que criará cada individuo da população
    for individuo in range(0, individuos):
        
        #Cria o labirinto
        lab = Labirinto()
        with open("test.txt") as f:
            text = f.read()
            f.close()
        lab.make_mapp(text)

        #Garantindo que o pai vá para a próxima geração
        if individuo == 0:
            population.append(bests[0])

        #Criando um agente totalmente aleatório
        elif individuo == 1:
            agente = Agente(id=individuo+geracao, mutation_factor=mutation_factor, mutation_probability=mutation_probability)
            #MUDAR PARA O TAMANHO DO LABIRINTO
            agente.set_random_moviments(100)
            aptidao(agente, lab, False)
            population.append(agente)

        #Criando um individuo que seja mistura da mãe e do pai
        elif individuo == 2:
            agente = crossover(bests, id=individuo+geracao)
            agente = mutation(agente)
            aptidao(agente, lab, False) 
            population.append(agente)

        #Criando um individuo parecido com o pai melhorado 
        else:# individuo == 2:
            agente = crossover_and_mut(bests[0], id=individuo+geracao)
            aptidao(agente, lab, False)
            population.append(agente)
            
    #Se passar de 100 gerações por iteração reseta a população pois convergiu
    if geracao%100 == 0:
        population = reset_generation(individuos=individuos, mutation_factor=mutation_factor, mutation_probability=mutation_probability)
    
    #Pegando os melhores individuos
    bests = torneio(population)
    print("MELHOR APTIDAO DA GERAÇÃO ", bests[0].aptidao, bests[0].food)

    #Critérios de parada
    if bests[0].food == 5 or geracao > geracoes:
        print("ACHOU AS COMIDAS")
        #bloco para criar o documento de texto de movimentos do individuo que completou
        lab = Labirinto()
        with open("test.txt") as f:
            text = f.read()
            f.close()
        lab.make_mapp(text)
        aptidao(agente=bests[0], lab=lab, saving=True)
        break
