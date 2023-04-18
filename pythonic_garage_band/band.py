# ABC class : In Python, an Abstract Base Class (ABC) is a special kind of class that cannot be instantiated
# directly. Instead, it is meant to be subclassed by other classes that will implement its abstract methods.

from abc import abstractclassmethod

class Band:

    instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members or []
        Band.instances.append(self)

    def play_solos(self):
        solos=[]
        for member in self.members:
            solos.append(member.play_solo())
        return solos
        

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def to_list(cls):
        return cls.instances
    
class Musician:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        pass

    
    def __repr__(self):
        pass

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
       return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Drummer(Musician):
    def __init__(self, name):
       super().__init__(name)
        

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
       return "drums"

    def play_solo(self):
      return "rattle boom crash" 

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
       return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
       return "bom bom buh bom"


