class Car:
  def __init__(self):
    self.gas_amount = 0
    self.capacity = 100
class Station:
  def __init__(self, gas_amount: int):
    self.gas_amount = gas_amount
  def refill(self, car):
    self.gas_amount -= car.capacity
    car.gas_amount = car.capacity

if __name__ == "__main__":
  car = Car()
  petrol_station = Station(2_000)
  print(f"Car capacity: {car.capacity}, Car gas amount: {car.gas_amount}")
  print(f"Station gas amount: {petrol_station.gas_amount}")
  petrol_station.refill(car)
  print("Refilled car...")
  print(f"Car capacity: {car.capacity}, Car gas amount: {car.gas_amount}")
  print(f"Station gas amount: {petrol_station.gas_amount}")
