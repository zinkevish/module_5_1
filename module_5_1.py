class House:
    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to (self,new_floor):
        if new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        elif new_floor > self.number_of_floors:
                print("Такого этажа не существует")

    def __str__(self):
        return f"Название: {self.name}, Кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 5)
h1.go_to(20)
h2.go_to(4)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))