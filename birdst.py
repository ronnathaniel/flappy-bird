
class Bird:
    def __init__(self):
        self.pos = [100, 100]
        self.vel = [0, 0.]
        self.acc = [0, 0.5]
        self.size = (30, 30)

    def jump(self):
        self.vel[1] = -7.5

    def update(self):
        twice = range(2)
        for i in twice:
            self.pos[i] += self.vel[i]
            self.vel[i] += self.acc[i]
