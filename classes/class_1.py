x = 0
if x == 3:
        pass
elif x == 4:
        pass
else:
        print(x)

match x: 
        case 1: pass
        case 2: pass
        case 3: pass
        case _: print("test")

for i in range(1, 2, 2):
        print(i)

def function_name(name) -> None:
        return name

name_list = ["Raphael", "Michalis", "CMF"]

name_list.append(5_000)
name_list.remove("Michalis")
popped = name_list.pop(2)
for element in name_list:
        print(element)

while x > 0:
        print(x)
        x -= 1
        
contacts = {"Michalis": 1, "Raphael": 2, "Simon": 3}
contacts["Michalis"] = 11

print(contacts.values)

name_1 = "CMF"
name_2 = "Gmbh"

names_together = name_1 + name_2
print(names_together)
print(f"names_1 = {name_1}")

#len(name_1)


if __name__ == "__main__":
        function_name("hello")
        name = 5_000_000
