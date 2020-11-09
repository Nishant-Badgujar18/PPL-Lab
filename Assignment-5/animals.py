class animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes


class wild_animals(animals):
    def place(self):
        print("Lives in Jungle")

class carnivores(wild_animals):
    def food(self):
        print("Eat a Meat")
    
        
class tiger(carnivores):
    def speak(self):
        print("Speaks : Roar, Growl. etc")
    def colour(self):
        print("Color : Orange")
        
class lion(carnivores):
    def speak(self):
        print("Speaks : Roar, Growl. etc")
    def colour(self):
        print("Color : Yellow")
        
class bear(carnivores):
    def speak(self):
        print("Speaks : growl")
    def colour(self):
        print("Color : Black, White. etc")
                       
class herbivores(wild_animals):
    def food(self):
        print("Eats Plant based food.")

class deer(herbivores):
    def speak(self):
        print("Speaks : bell")
    def colour(self):
        print("Color : Brown")
        
class elephant(herbivores):
    def speak(self):
        print("Speaks : Trumpet, Roar. etc")
    def colour(self):
        print("Color : Grey")
        
class zebra(herbivores):
    def speak(self):
        print("Speaks : Whinny")
    def colour(self):
        print("Color : Black and white")

class domestic_animals(animals):  
    def place(self):
        print("Areas habitated by human beings")

        
class dog(domestic_animals):
    def speak(self):
        print("Speaks : Bark")
    def colour(self):
        print("Color : brown, black, white, golden. etc")
        
class cat(domestic_animals):
    def speak(self):
        print("Speak : Meow")
    def colour(self):
        print("Color : Grey,brown, black, white. etc")
        
class cow(domestic_animals):
    def speak(self):
        print("Speaks : Low, Moo. etc")
    def colour(self):
        print("Color : white, brown. etc")
        
class goat(domestic_animals):
    def speak(self):
        print("Speaks : Bleat")
    def colour(self):
        print("Color : black, brown, white. etc")

print("Animal details :")
p1 = animals()
Var = tiger()
Var.speak()
Var.place()
Var.colour()
print("No. of legs are :")
print(Var.legs)
print("No. of eyes are :")
print(Var.eyes)


