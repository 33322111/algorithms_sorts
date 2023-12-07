import random


def generate_points(num_points):
    points = []
    for _ in range(num_points):
        points.append((random.uniform(-1, 1), random.uniform(-1, 1)))
    return points


def estimate_pi(points):
    points_inside_circle = 0
    for i in points:
        x = i[0]
        y = i[1]
        if x ** 2 + y ** 2 <= 1:
            points_inside_circle += 1
    pi_estimate = 4 * points_inside_circle / len(points)
    return pi_estimate


num_points = int(input("Введите количество случайных точек: "))
points = generate_points(num_points)
pi_estimate = estimate_pi(points)
print(f"Приблизительное значение числа π: {pi_estimate}")
