class City:
    def __init__(self, name, x_coordinate, y_coordinate, population, distance):
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.population = population
        self.distance = distance

    def __str__(self):
        return (
            f"City: {self.name}\n"
            f"Coordinates: ({self.x_coordinate}, {self.y_coordinate})\n"
            f"Population: {self.population}\n"
            f"Distance: {self.distance} km"
        )
if __name__ == "__main__":
    city1 = City("Kathmandu", 85.324, 27.717, 845767, 12.5)
    print(city1)