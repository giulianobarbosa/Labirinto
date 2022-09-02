class Labirinto:

    def __init__(self) -> None:

        self.mapp = []
        self.food = None
        self.start = None


    @property
    def mapp(self) -> list:     
        return self._mapp


    @mapp.setter
    def mapp(self, value) -> None:
        self._mapp = value


    def get_mapp(self) -> None:

        for line in self.mapp:

            print(line)


    def put_in_mapp(self, val:list) -> None:

        temp_mapp = self.mapp
        temp_mapp.append(val)
        self.mapp = temp_mapp


    def make_mapp(self, txt):

        self.mappa = txt.split("\n")

        for content in self.mappa:

            self.put_in_mapp([item for item in content if item != " "])


if __name__ == "__main__":

    lab = Labirinto()
    with open("test.txt") as f:
        text = f.read()
        f.close()
    lab.make_mapp(text)
    lab.get_mapp()