import math
import matplotlib.pyplot as plt

G = 6.6743e-11

class Planet:
    def __init__(self, name: str, mass: float, posx: float, posy: float, speedx: float, speedy: float):
        self.name = name
        self.mass = mass

        self.pos = [posx, posy]
        self.speed = [speedx, speedy]

    def update_pos(self, dt: float):
        posx = self.pos[0]
        posy = self.pos[1]

        sx = self.speed[0]
        sy = self.speed[1]

        self.pos = [posx + sx * dt, posy + sy * dt]

    def interact(self, other, dt):
        dx = (-self.pos[0] + other.pos[0])
        dy = (-self.pos[1] + other.pos[1])
        dist2 = dx * dx + dy * dy
        if dist2 == 0:
            dist2 = 100  # 100m minimum; dumb assumption

        if dx == 0:
            alpha = math.pi / 2
        else:
            alpha = math.atan2(dy, dx)


        # Met a jour les vecteur vitesse en fonction d'une autre planete
        f = G * (self.mass * other.mass) / dist2

        f_over_mass = f / self.mass

        fx = math.cos(alpha)
        fy = math.sin(alpha)

        vx = fx * f_over_mass * dt
        vy = fy * f_over_mass * dt

        self.speed = [self.speed[0] + vx, self.speed[1] + vy]

    def __repr__(self):
        return f'<{self.name} - {self.pos} - {self.speed}>'

planets = [
#   Planet('sun', 1.9e30, 0, 0, 0, 0),
#   Planet('earth', 5.9e24, 110_000_000_000, 0, 0, 29_722),

    #Planet('earth', 5.9e24, 150_000_000_000, 0, 0, 29_722)
    Planet('earth', 5.9e27, -11_000_000_000, 0, 10_000, 11_722),
    Planet('earth', 5.9e27, 0, 11_000_000_000,  19_722, 0),
    Planet('earth', 5.9e27, 3_000_000_000, 11_000_000_000,  19_722, 0),
    Planet('earth', 5.9e29,  0, 0, 0, 0),

    #Planet('mercury', 3.2e23, 10_000_000_000, 57_000_000_000, 30_000, 0),
]


dt = 1

scale = 10_000_000_000

dmax = 150_000_000_000 * 0.1 / scale
w = dmax * 2

plt.figure(figsize=(w, w))
#plt.axis([-dmax, dmax, -dmax, dmax])
#plt.xlim(-dmax, dmax)
#plt.ylim(-dmax, dmax)
plt.ion()
plt.show()

i = 0
while True:
    i += 1
    for planet in planets:
        for other_planet in planets:
            if planet != other_planet:
                planet.interact(other_planet, dt)

    fx = []
    fy = []
    for planet in planets:
        planet.update_pos(dt)
        p = planet.pos
        fx.append(p[0]/scale)
        fy.append(p[1]/scale)
#       print(planet)

    if i > 2600:
        print('\n\n\n')
        for planet in planets:
            print(planet)
        plt.scatter(fx, fy)

        plt.draw()
        plt.pause(0.001)
        i = 0

