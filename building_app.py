import random
from elevator import Elevator


class BuildingApp:

    def __init__(self):
        self.elevator = Elevator()
        self.ppl_num_on_each_floor = {}

    def generate_people_on_floors(self):
        for floor in range(1, self.elevator.number_of_floors + 1):
            list_of_target_floor_ppl = []
            self.ppl_num_on_each_floor[floor] = list_of_target_floor_ppl  # генерация людей с целевыми этажами для каждого этажа

            for i in range(random.randint(0, 10)):  # генерация количества людей на этаж
                target_floor_person = random.randint(1, self.elevator.number_of_floors)
                while target_floor_person == floor:
                    target_floor_person = random.randint(1, self.elevator.number_of_floors) # назначение рандомного этажа человеку с учетом этажа, на котором находится человек
                list_of_target_floor_ppl.append(target_floor_person)

        print("Сгенерированный список людей на этажах", self.ppl_num_on_each_floor)

    def start(self):
        while True:  # выполнение алгоритма пока лифт не развезет всех людей

            self.elevator.remove_people(self.elevator.current_floor)  # выпустить всех людей, которым надо на текущий этаж

            if self.elevator.current_floor == self.elevator.max_floor or self.elevator.current_floor == self.elevator.min_floor: # проверка достиг ли лифт макс или мин этажа
                if len(self.ppl_num_on_each_floor[self.elevator.current_floor]) != 0: # есть ли люди на текущем этаже
                    num_of_ppl_going_up = 0
                    num_of_ppl_going_down = 0
                    for person in self.ppl_num_on_each_floor[self.elevator.current_floor]: # определение направления лифта
                        if person > self.elevator.current_floor:
                            num_of_ppl_going_up += 1
                        else:
                            num_of_ppl_going_down += 1
                    if num_of_ppl_going_up > num_of_ppl_going_down:
                        self.elevator.set_direction("Up")
                    else:
                        self.elevator.set_direction("Down")

                else: # если людей нет на текущем этаже
                    floor_with_people_exists = False
                    for floor in range(1, self.elevator.number_of_floors + 1):
                        if len(self.ppl_num_on_each_floor[floor]) != 0:  # опредение этажа на котором есть люди
                            floor_with_people_exists = True
                            if floor > self.elevator.current_floor:          # определение направления лифта
                                self.elevator.set_direction("Up")
                            else:
                                self.elevator.set_direction("Down")
                            break

                    if not floor_with_people_exists: # если в результате цикла на этажах нет людей
                        print("Людей на этажах не осталось")
                        break

            empty = self.elevator.get_empty_space() # посчитать колво свободных мест в лифте
            checked_list_of_people = []  # отфильтрованный список людей на посадку в лифт

            for person in self.ppl_num_on_each_floor[self.elevator.current_floor]: # цикл по людям на текущем этаже
                if person > self.elevator.current_floor and self.elevator.direction == "Up":
                    checked_list_of_people.append(person)
                elif person < self.elevator.current_floor and self.elevator.direction == "Down":
                    checked_list_of_people.append(person)

            checked_list_of_people = checked_list_of_people[:empty]  # оставляю людей сколько свободно в лифте

            self.elevator.add_people_list(checked_list_of_people) # добавляет отфильтрованный спсико людей в лифт
            for person in checked_list_of_people:
                self.ppl_num_on_each_floor[self.elevator.current_floor].remove(person)  # удаляю с этажа людей которые сели

            if self.elevator.direction == "Up": # исходя из направления движется на один этаж
                self.elevator.lift_up()
            else:
                self.elevator.lift_down()

            print("Людей на этажах осталось", self.ppl_num_on_each_floor)
            self.elevator.log_lift()
            print("--------------------")
