class VirtualDog:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.happiness = 100

    def bark(self):
        print(f"{self.name} barks: Woof! Woof!")

    def eat(self, food):
        print(f"{self.name} eats {food}.")
        self.energy += 10
    def run(self,hold):
        print(f"{self.name} runs and  {hold}.")
        self.energy -= 10
    def sit(self,rollover):
        print(f"{self.name} sit and {rollover}.")
        self.energy +=10
    def stand(self):
        print(f"{self.name} stands and barks: Woof! Woof!")
    

# Example usage
dog = VirtualDog("Caeser")
dog.bark()
dog.eat("pedigree")
dog.run("")
dog.sit("")
dog.stand()
def interact_with_dog(dog):
    while True:
        command = input("Enter a command (e.g., bark, feed,run,sit,stand,quit): ").lower()
        if command == "bark":
            dog.bark()
        elif command == "feed":
            food = input("Enter the food to feed the dog: ")
            dog.eat(food)
        elif command == "run":
            hold = input("Enter the thing to hold by the dog: ")
            dog.run(hold)
        elif command == "sit":
            rollover = input("Enter the activity to be done by the dog: ")
            dog.sit(rollover)
        elif command == "stand":
            dog.stand()
        elif command == "quit":
            print("Goodbye! WOOF!")
            break
        else:
            print("Invalid command. Try again.")
interact_with_dog(dog)
