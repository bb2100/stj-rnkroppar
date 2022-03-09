class Planet:
    def __init__(self, name : str, size : int):
        self.name = name
        self.size = size
        self.moons = []

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_moons(self):
        return self.moons
        
    def add_moon(self, moon):
        self.moons.append(moon)

    def print_moons(self):
        for moon in self.moons:
            print(moon.get_name())

    def certain_size(self, size : int):
        print(f"The following moons around {self.get_name()} larger than {size} sqkm:")
        for moon in self.moons:
            if moon.get_size() > size:
                print(moon.get_name())

class Moon:
    def __init__(self, name : str, size : int):
        self.name = name
        self.size = size
        self.orbit = None

    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_orbit(self):
        return self.orbit
    def add_orbit(self, orbit):
        self.orbit = orbit


def main():
    tellus = Planet("Tellus", 510100000)
    mars = Planet("Mars", 144800000)
    jupiter = Planet("Jupiter", 61420000000)
    luna = Moon("Luna", 37930000)
    europa = Moon("Europa", 19613)
    ganymedes = Moon("Ganymedes", 33101)

    tellus.add_moon(luna)
    mars.add_moon(ganymedes)
    jupiter.add_moon(europa)

    luna.add_orbit(tellus)
    ganymedes.add_orbit(mars)
    europa.add_orbit(jupiter)

    tellus.print_moons()
    jupiter.print_moons()

    mars.certain_size(1000)

if __name__ == "__main__":
    main()