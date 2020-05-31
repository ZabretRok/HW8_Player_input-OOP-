class BasketballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


print("Please, enter some balsketball player's data! ")

first_name = input("Player's first name: ")
last_name = input("Player's last name: ")
height = input("Player's height (CM): ")
weight = input("Player's weight (KG): ")
points = input("Player's points: ")
rebounds = input("Player's rebounds: ")
assists = input("Player's assists: ")

new_player = BasketballPlayer(first_name=first_name, last_name=last_name, height_cm=float(height), weight_kg=float(weight), points=int(points), rebounds=int(rebounds), assists=int(assists))

with open("bball_player.txt", "w") as bball_data:
    bball_data.write(str(new_player.__dict__))

print("Player is entered!")
print("Player's data: {0}".format(new_player.__dict__))