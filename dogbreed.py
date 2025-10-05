class Dog:


    species = "dog"
    


    def __init__(self, name, lifespan):
        self.name = name      
        self.lifespan = lifespan  



dog1 = Dog("German Shepherd", "9–13 years")
dog2 = Dog("Golden Retriever", "10–12 years")
dog3 = Dog("Pug", "12–15 years")


print("{} is a {}".format(dog1.name, dog1.species))
print("{} is a {}".format(dog2.name, dog2.species))
print("{} is a {}".format(dog3.name, dog3.species))



print("{} has a lifespan of {}".format(dog1.name, dog1.lifespan))
print("{} has a lifespan of {}".format(dog2.name, dog2.lifespan))
print("{} has a lifespan of {}".format(dog3.name, dog3.lifespan))