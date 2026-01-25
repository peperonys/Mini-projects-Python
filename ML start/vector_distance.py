"""
Вычисление различных расстояний между векторами
"""
import numpy as np
from scipy.spatial import distance

print("=" * 50)
print("РАССТОЯНИЯ МЕЖДУ ВЕКТОРАМИ")
print("=" * 50)

# Создаём два вектора
v1 = np.array([1, 2, 3, 4, 5])
v2 = np.array([4, 5, 6, 7, 8])

print(f"Вектор 1: {v1}")
print(f"Вектор 2: {v2}")

# 1. Евклидово расстояние
euclidean = np.linalg.norm(v1 - v2)
print(f"\n1. Евклидово расстояние: {euclidean:.4f}")

# 2. Манхэттенское расстояние
manhattan = np.sum(np.abs(v1 - v2))
print(f"2. Манхэттенское расстояние: {manhattan}")

# 3. Косинусное расстояние
cosine_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
cosine_dist = 1 - cosine_sim
print(f"3. Косинусное сходство: {cosine_sim:.4f}")
print(f"   Косинусное расстояние: {cosine_dist:.4f}")

# 4. Расстояние Чебышева
chebyshev = np.max(np.abs(v1 - v2))
print(f"4. Расстояние Чебышева: {chebyshev}")

# 5. Расстояние Минковского (p=3)
minkowski = np.sum(np.abs(v1 - v2)**3)**(1/3)
print(f"5. Расстояние Минковского (p=3): {minkowski:.4f}")

# 6. Применение в машинном обучении
print("\n" + "=" * 50)
print("ПРИМЕР: K-БЛИЖАЙШИХ СОСЕДЕЙ (K-NN)")
print("=" * 50)

# Создаём небольшой набор данных
np.random.seed(42)
X_train = np.random.rand(10, 5)  # 10 samples, 5 features
y_train = np.random.randint(0, 2, 10)  # binary labels

X_test = np.random.rand(3, 5)  # 3 test samples

print("Обучающие данные (первые 3):")
for i in range(3):
    print(f"  Образец {i}: {X_train[i]}, метка: {y_train[i]}")

print("\nТестовые данные:")
for i in range(3):
    print(f"  Тест {i}: {X_test[i]}")

# K-NN с k=3
k = 3
print(f"\nK-NN предсказания (k={k}):")

for i, test_point in enumerate(X_test):
    # Вычисляем расстояния до всех тренировочных точек
    distances = []
    for j, train_point in enumerate(X_train):
        dist = np.linalg.norm(test_point - train_point)  # Евклидово
        distances.append((dist, y_train[j]))
    
    # Сортируем по расстоянию
    distances.sort(key=lambda x: x[0])
    
    # Берём k ближайших
    k_nearest = distances[:k]
    k_labels = [label for _, label in k_nearest]
    
    # Majority vote
    prediction = max(set(k_labels), key=k_labels.count)
    
    print(f"  Тест {i}: ближайшие расстояния {[d[0]:.3f for d in k_nearest]}")
    print(f"         метки ближайших: {k_labels}")
    print(f"         предсказание: {prediction}")
