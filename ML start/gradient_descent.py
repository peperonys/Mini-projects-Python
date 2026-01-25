"""
Градиентный спуск
"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Шаг 1: Сгенерировать данные
np.random.seed(42)
X = np.random.rand(100, 1).astype(np.float32)  # 100 случайных значений для X
epsilon = np.random.randn(100, 1).astype(np.float32) * 0.1  # Небольшой случайный шум
y_true = 2 * X + 1 + epsilon  # Настоящие значения y = 2*X + 1 + шум

# Шаг 2: Инициализация параметров (theta_0 и theta_1)
theta_0 = tf.Variable(np.random.randn(), dtype=tf.float32, trainable=True)
theta_1 = tf.Variable(np.random.randn(), dtype=tf.float32, trainable=True)

# Шаг 3: Функция потерь (MSE)
def compute_loss(X, y, theta_0, theta_1):
    y_pred = theta_0 + theta_1 * X  # Прогноз модели
    loss = tf.reduce_mean(tf.square(y - y_pred))  # Среднеквадратичная ошибка
    return loss

# Шаг 4: Градиентный спуск
learning_rate = 0.1
epochs = 500

# История для визуализации
loss_history = []

for epoch in range(epochs):
    with tf.GradientTape() as tape:
        # Вычисляем ошибку
        loss = compute_loss(X, y_true, theta_0, theta_1)
    
    # Вычисляем градиенты
    gradients = tape.gradient(loss, [theta_0, theta_1])
    
    # Обновляем параметры с использованием градиентного спуска
    theta_0.assign_sub(learning_rate * gradients[0])
    theta_1.assign_sub(learning_rate * gradients[1])
    
    # Сохраняем значение потерь для отслеживания процесса
    loss_history.append(loss.numpy())

    # Каждые 50 шагов выводим текущие параметры и ошибку
    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss.numpy():.4f}, theta_0: {theta_0.numpy():.4f}, theta_1: {theta_1.numpy():.4f}")

# Шаг 5: Визуализация потерь
plt.plot(loss_history)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Градиентный спуск: изменения функции потерь")
plt.show()

# Финальные параметры модели
print(f"Оптимальные параметры: theta_0 = {theta_0.numpy():.4f}, theta_1 = {theta_1.numpy():.4f}")

# Визуализация результата
plt.scatter(X, y_true, label="Данные")
plt.plot(X, theta_0.numpy() + theta_1.numpy() * X, color='red', label="Прогнозная линия")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Решение линейной регрессии с градиентным спуском")
plt.show()
