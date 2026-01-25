"""
Работа с единичным тензором и матричными операциями
"""
import numpy as np

print("=" * 50)
print("ЕДИНИЧНЫЙ ТЕНЗОР (МАТРИЦА)")
print("=" * 50)

# 1. Создание единичной матрицы
I3 = np.eye(3)
print("1. Единичная матрица 3x3:")
print(I3)

# 2. Свойство единичной матрицы
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("\n2. Свойство A × I = I × A = A")
print("Матрица A:")
print(A)

result1 = np.dot(A, I3)
result2 = np.dot(I3, A)

print("\nA × I (должно быть равно A):")
print(result1)
print("\nI × A (должно быть равно A):")
print(result2)
print(f"\nПроверка: A == A×I? {np.allclose(A, result1)}")
print(f"Проверка: A == I×A? {np.allclose(A, result2)}")

# 3. Единичная матрица в нейросетях
print("\n" + "=" * 50)
print("ПРИМЕР ИЗ НЕЙРОСЕТЕЙ: ИНИЦИАЛИЗАЦИЯ ВЕСОВ")
print("=" * 50)

# Симуляция слоя нейросети
input_size = 4
output_size = 4

# Обычная инициализация
W_normal = np.random.randn(output_size, input_size) * 0.01

# Инициализация единичной матрицей (для Residual Networks)
W_identity = np.eye(output_size, input_size)

print(f"Размерность весов: {W_normal.shape}")
print(f"\nНормальная инициализация (первые 3x3):")
print(W_normal[:3, :3])
print(f"\nЕдиничная инициализация (первые 3x3):")
print(W_identity[:3, :3])

# 4. Собственные значения и векторы
print("\n" + "=" * 50)
print("СОБСТВЕННЫЕ ЗНАЧЕНИЯ ЕДИНИЧНОЙ МАТРИЦЫ")
print("=" * 50)

eigenvalues, eigenvectors = np.linalg.eig(I3)
print("Собственные значения:", eigenvalues)
print("Собственные векторы (столбцы):")
print(eigenvectors)

# 5. Тензорное произведение
print("\n" + "=" * 50)
print("ТЕНЗОРНОЕ ПРОИЗВЕДЕНИЕ С ЕДИНИЧНЫМ ТЕНЗОРОМ")
print("=" * 50)

# Создаём тензор 2x2x2
tensor = np.random.rand(2, 2, 2)
print("Исходный тензор формы", tensor.shape)
print(tensor)

# Тензорное произведение с единичной матрицей
# (в данном случае просто для демонстрации)
print("\nПрименение единичного преобразования к каждому слою:")
for i in range(tensor.shape[0]):
    layer = tensor[i, :, :]
    transformed = np.dot(layer, I3[:2, :2])
    print(f"\nСлой {i} после I×A:")
    print(transformed)
