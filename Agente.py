class Agente:

    def __init__(self, id:int, posicao:tuple, movimentos:list, mutation_factor:float, 
                    mutation_probability:float) -> None:
        #1
        self.id = id
        #(0,0)
        self.posicao = posicao
        #[(1,1),(1,2),(1,3),(2,3)...]
        self.movimentos = []
        #Probability of a mutation happen
        self.mutation_probability = mutation_probability
        #How much the agent will mutate
        self.mutation_factor = mutation_factor
