class Band:
    bands = []
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.bands.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    def play_solos(self):
        solos = []
        for player in self.members:
            solos.append(player.play_solo())
        #print(f'solos: {solos[0]}')
        return solos

    @classmethod
    def to_list(cls):
        return cls.bands
        
class Musician:
    #DRY code as a parent class
    def __init__(self, name, type, instrument):
        self.name = name
        self.type = type
        self.instrument = instrument
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.type} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    #pass

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'Guitarist', 'guitar')
    
    def play_solo(self):
        return 'face melting guitar solo'

#Refactored this to a superclass
    # def __str__(self):
    #     return f"My name is {self.name} and I play guitar"

    # def __repr__(self):
    #     return f"Guitarist instance. Name = {self.name}"
    #pass

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, 'Bassist', 'bass')

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'Drummer', 'drums')

    def play_solo(self):
        return "rattle boom crash"

if __name__ == '__main__':
    band = Band("Nirvana")
    band1 = Band("CoolBand")
    print(Band.bands)
    