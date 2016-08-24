import json


class User(object):
    count = 0

    def __init__(self, name, salary, car):
        User.count += 1
        self.id = User.count
        self.name = name
        self.car = car
        self.salary = salary

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True)


class Car(object):
    count = 0

    def __init__(self, price, year):
        Car.count += 1
        self.id = Car.count
        self.price = price
        self.year = year

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True)


class CarDao(object):
    def __init__(self):
        self.car_map = {}

    def get_by_id(self, car_id):
        return self.car_map.get(car_id)

    def get_all(self):
        return list(self.car_map.values())

    def delete_by_id(self, car_id):
        del self.car_map[car_id]

    def add_car(self, car):
        self.car_map[car.id] = car


class UserDao(object):
    def __init__(self):
        self.user_map = {}

    def get_by_id(self, user_id):
        return self.user_map.get(user_id)

    def get_all(self):
        return list(self.user_map.values())

    def delete_by_id(self, user_id):
        del self.user_map[user_id]

    def add_user(self, user):
        self.user_map[user.id] = user


def generate_data(user_dao: UserDao, car_dao: CarDao):
    car1 = Car(1, 2000)
    car2 = Car(2, 2016)
    car_dao.add_car(car1)
    car_dao.add_car(car2)

    user1 = User('Ivan', 2, car1)
    user2 = User('John', 10, None)
    user_dao.add_user(user1)
    user_dao.add_user(user2)

