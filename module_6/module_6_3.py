class Horse:
    def __init__(self):
        super().__init__()
        self.x_distance = 0
        self.sound = "Frrr"
        print(self.sound, super())

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        return print(self.sound)


if __name__ == '__main__':
    p1 = Pegasus()
    test_Horse = Horse()
    test_Eagle = Eagle()
    print('Horse: ', test_Horse, 'Eagle: ', test_Eagle.sound, 'Pegasus: ', p1.sound)
    print(Pegasus.mro())
    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()
