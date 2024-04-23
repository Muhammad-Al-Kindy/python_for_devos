# type: ignore

class Agent:
    def __init__(self, name, role, abilities):
        self._name = name               # protected var
        self._role = role               # protected var
        self.__abilities = abilities    # provate var
        
    def get_name(self):         # public method
        return self._name
    
    def get_role(self):         # public method
        return self._role
    
    def get_abilities(self):    # public method
        return self.__abilities
    
class Duelist(Agent):
    def __init__(self, name, abilities, signature_move):
        super().__init__(name,"Duelist", abilities)
        self.signature_move = signature_move # public var
        
    def activate(self):
        print(f"{self.get_name()}, a Duelist, is activating {self.signature_move}")
        
class Controller(Agent):
    def __init__(self, name, abilities, support_ultimate):
        super().__init__(name, "Controller", abilities)
        self.__support_ultimate = support_ultimate
        
    def get_support_ultimate(self):
        return self.__support_ultimate
    
    def activate(self):
        print(f"{self.get_name()}, a Controller, is using their support ultimate {self.get_support_ultimate()}")
        
phoenix_abilities = ["Blaze","Curveball","Hot Hands","Run It Backs"]
phoenix = Duelist("Phoenix",phoenix_abilities,"Run It Back")

brimstone_abilities = ["Incendiary","Stim Beacon","Sky Smoke","Orbital Strike"]
brimstone = Controller("Brimstone", brimstone_abilities, "Orbital Strike")

print("Agent Details: ")
print("Name: ", phoenix.get_name())
print("Role: ", phoenix.get_role())
print("Abilities: ", phoenix.get_abilities())
print("Signature Move: ", phoenix.signature_move)

print("\nAgent Details: ")
print("Name: ", brimstone.get_name())
print("Role: ", brimstone.get_role())
print("Abilities: ", brimstone.get_abilities())
print("Support Ultimate: ", brimstone.get_support_ultimate())

# accesing private variable direclty
print("Acess Private abilities: ", brimstone._Agent__abilities)

# polymorphism
phoenix.activate()
brimstone.activate()