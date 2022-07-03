import random


class Elevator:

    def __init__(self):
        self.current_floor = 1
        self.list_of_people_in_elevator = []
        self.number_of_floors = random.randint(10, 20) # рандомная колво генерация этажей
        self.capacity = 5
        self.max_floor = 1
        self.min_floor = 1
        self.direction = "Up"

        print("Сгенерированное количество этажей", self.number_of_floors)

    def log_lift(self):
        print("Список людей в лифте с целевыми этажами", self.list_of_people_in_elevator)

    def set_direction(self, direction): # определение направления лифта
        self.direction = direction
        print("Направление изменилось на", self.direction)

    def lift_up(self): # движение лифта на 1 этаж вверх
        self.current_floor += 1
        print("Лифт поехал на этаж", self.current_floor)

    def lift_down(self): # движение лифта на 1 этаж вниз
        self.current_floor -= 1
        print("Лифт поехал на этаж", self.current_floor)

    def remove_people(self, person_with_floor): # удаление людей вышедших из лифта
        while person_with_floor in self.list_of_people_in_elevator:
            self.list_of_people_in_elevator.remove(person_with_floor)
        print("Вышли люди на этаже", person_with_floor)
        self.calculate_max_floor() # расчет максимального этажа после выхода людей
        self.calculate_min_floor() # расчет минимального этажа после выхода людей

    def add_people_list(self, list_of_ppl): # добавление списка людей в список людей лифта
        empty = self.get_empty_space() # расчет свободных мест в текущем состоянии лифта
        self.list_of_people_in_elevator.extend(list_of_ppl[:empty]) # добавление людей в лифт с учетом свободных мест
        print("Сели", list_of_ppl[:empty], "на этаже", self.current_floor)
        self.calculate_max_floor()
        self.calculate_min_floor()

    def get_empty_space(self):
        empty = self.capacity - len(self.list_of_people_in_elevator)
        return empty

    def calculate_max_floor(self):
        if len(self.list_of_people_in_elevator) != 0:
            self.max_floor = max(self.list_of_people_in_elevator)
        else:
            self.max_floor = self.current_floor

    def calculate_min_floor(self):
        if len(self.list_of_people_in_elevator) != 0:
            self.min_floor = min(self.list_of_people_in_elevator)
        else:
            self.min_floor = self.current_floor
