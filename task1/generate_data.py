import csv
import random
def generate_city_data(filename, number_of_cities):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Name",
            "X_Coordinate",
            "Y_Coordinate",
            "Population",
            "Distance"
        ])

        for i in range(number_of_cities):

            name = f"City_{i + 1}"
            x_coordinate = round(random.uniform(80.0, 89.0), 2)
            y_coordinate = round(random.uniform(26.0, 30.0), 2)
            population = random.randint(10000, 1000000)
            distance = round(random.uniform(1.0, 500.0), 2)

            writer.writerow([
                name,
                x_coordinate,
                y_coordinate,
                population,
                distance
            ])

    print(f"{filename} created successfully.")
generate_city_data("data/cities_100.csv", 100)
generate_city_data("data/cities_1000.csv", 1000)
generate_city_data("data/cities_10000.csv", 10000)
