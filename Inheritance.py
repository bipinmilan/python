class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi I am"+self.name)


class PhysicalRobot(Robot):
    pass


x = Robot("Marvin")
y = PhysicalRobot("James")
y.say_hi()
x.say_hi()
