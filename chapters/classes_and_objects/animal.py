class Animal:
  def __init__(self):
    self.hunger = 50
    self.thirst = 50
  def eat(self):
    self.hunger -= 1
  def drink(self):
    self.thirst -= 1
  def play(self):
    self.hunger += 1
    self.thirst += 1
if __name__ == "__main__":
  animal = Animal()
  print(f"Thirst: {animal.thirst}, Hunger: {animal.hunger}")
  animal.drink()
  animal.eat()
  print(f"Thirst: {animal.thirst}, Hunger: {animal.hunger}")
  animal.play()
  animal.play()
  print(f"Thirst: {animal.thirst}, Hunger: {animal.hunger}")