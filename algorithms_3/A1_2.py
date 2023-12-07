import matplotlib.pyplot as plt
import random
import math


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


def calculate_error(estimated_pi):
    error = abs((estimated_pi - math.pi)) / math.pi * 100
    return error


pi_values = []
errors = []
for num_points in range(100, 5001, 100):
    points = generate_points(num_points)
    pi_value = estimate_pi(points)
    pi_values.append(pi_value)
    error = calculate_error(pi_value)
    errors.append(error)

points_range = range(100, 5001, 100)

print("Исходные данные, использованные для построения графиков:")
print(f"Количество точек: {[i for i in points_range]}")
print(f"Приближенное значение числа π: {pi_values}")
print(f"Относительное отклонение (в %): {errors}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(points_range, pi_values, marker='o', linestyle='-', color='b')
plt.axhline(y=math.pi, color='r', linestyle='--', label='Точное π')
plt.title('Приближенное значение числа π от Количества точек')
plt.xlabel('Количество точек')
plt.ylabel('Приближенное значение числа π')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(points_range, errors, marker='o', linestyle='-', color='g')
plt.title('Относительное отклонение (в %) от Количества точек')
plt.xlabel('Количество точек')
plt.ylabel('Относительное отклонение (в %)')

plt.tight_layout()
plt.show()



