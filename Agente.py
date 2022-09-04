import random


class Agente:

    def __init__(self, id:int=None, posicao:tuple=(0,0), movimentos:list=[], mutation_factor:float=0.5, 
                    mutation_probability:float=0.5) -> None:
        #1
        self.id = id
        #(0,0)
        self.posicao = posicao
        self.feet = 0
        self.foodie = 0
        #[baixo, baixo, esquerda, direita, cima, cima...]
        #[
        # norte = 0
        # nordeste = 1
        # leste = 2
        # sudeste = 3
        # sul = 4
        # sudoeste = 5
        # oeste = 6
        # noroeste = 7
        # ]
        self.movimentos = []
        #Probability of a mutation happen
        self.mutation_probability = mutation_probability
        #How much the agent will mutate
        self.mutation_factor = mutation_factor
        self.aptidao = 0
    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value:int) -> None:
        self._id = value
    
    @property
    def posicao(self) -> tuple:
        return self._posicao

    @posicao.setter
    def posicao(self, value:tuple) -> None:
        self._posicao = value

    @property
    def feet(self) -> int:
        return self._feet

    @feet.setter
    def feet(self, value:int) -> None:
        self._feet = value

    @property
    def foodie(self) -> int:
        return self._foodie

    @foodie.setter
    def foodie(self, value) -> None:
        self._foodie = value

    @property
    def movimentos(self) -> list:
        return self._movimentos

    @movimentos.setter
    def movimentos(self, value:list) -> None:
        self._movimentos = value

    @property
    def mutation_probability(self) -> float:
        return self._mutation_probability

    @mutation_probability.setter
    def mutation_probability(self,value) -> None:
        self._mutation_probability = value

    @property
    def mutation_factor(self) -> float:
        return self._mutation_factor

    @mutation_factor.setter
    def mutation_factor(self,value) -> None:
        self._mutation_factor = value

    @property
    def aptidao(self) -> int:
        return self._aptidao

    @aptidao.setter
    def aptidao(self, value) -> None:
        self._aptidao = value

    def set_random_moviments(self, size:int=100):
        self.movimentos = [random.randint(0,8) for i in range(size)]

    def set_position_by_moviment(self, moviment:int) -> bool:
    
        if moviment == 0:
            if (self.posicao[0] - 1) >= 0:
                self.posicao = (self.posicao[0] - 1, self.posicao[1])
                return True

        elif moviment == 1:
            if ((self.posicao[0] - 1) >= 0) and ((self.posicao[1] + 1) <= 9):
                self.posicao = (self.posicao[0] - 1, self.posicao[1] + 1)
                return True
            

        elif moviment == 2:
            if ((self.posicao[1] + 1) <= 9):
                self.posicao = (self.posicao[0], self.posicao[1] + 1)
                return True

        elif moviment == 3:
            if ((self.posicao[0] + 1 <= 9) and ((self.posicao[1] + 1) <= 9)):
                self.posicao = (self.posicao[0] + 1, self.posicao[1] + 1)
                return True
            
        elif moviment == 4:
            if ((self.posicao[0] + 1) <= 9):
                self.posicao = (self.posicao[0] + 1, self.posicao[1])
                return True

        elif moviment == 5:
            if ((self.posicao[0] + 1) <= 9) and ((self.posicao[1] - 1) >= 0):
                self.posicao = (self.posicao[0] + 1, self.posicao[1] - 1)
                return True

        elif moviment == 6:
            if ((self.posicao[1] - 1) >= 0):
                self.posicao = (self.posicao[0], self.posicao[1] - 1)
                return True

        elif moviment == 7:
            if ((self.posicao[0] - 1) >= 0) and ((self.posicao[1] - 1) >= 0):
                self.posicao = (self.posicao[0] - 1, self.posicao[1] - 1)
                return True

        return False


    def set_position_by_moviment_DEMO(self, moviment:int) -> bool:
    
        if moviment == 0:
            if (self.posicao[0] - 1) >= 0:
                return (self.posicao[0] - 1, self.posicao[1])

        elif moviment == 1:
            if ((self.posicao[0] - 1) >= 0) and ((self.posicao[1] + 1) <= 9):
                return (self.posicao[0] - 1, self.posicao[1] + 1)
            

        elif moviment == 2:
            if ((self.posicao[1] + 1) <= 9):
                return (self.posicao[0], self.posicao[1] + 1)
                

        elif moviment == 3:
            if ((self.posicao[0] + 1 <= 9) and ((self.posicao[1] + 1) <= 9)):
                return (self.posicao[0] + 1, self.posicao[1] + 1)
                
            
        elif moviment == 4:
            if ((self.posicao[0] + 1) <= 9):
                return (self.posicao[0] + 1, self.posicao[1])
                

        elif moviment == 5:
            if ((self.posicao[0] + 1) <= 9) and ((self.posicao[1] - 1) >= 0):
                return (self.posicao[0] + 1, self.posicao[1] - 1)
            

        elif moviment == 6:
            if ((self.posicao[1] - 1) >= 0):
                return (self.posicao[0], self.posicao[1] - 1)
                

        elif moviment == 7:
            if ((self.posicao[0] - 1) >= 0) and ((self.posicao[1] - 1) >= 0):
                return (self.posicao[0] - 1, self.posicao[1] - 1)
                

        return self.posicao