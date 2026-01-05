import numpy as np

# Метрический тензор (в данном случае - единичная матрица для евклидова пространства)
g = np.eye(3)
print (g)
# Два вектора
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Вычисляем расстояние
distance = np.sqrt(np.dot(v1 - v2, np.dot(g, v1 - v2)))

print(f"Distance: {distance}")