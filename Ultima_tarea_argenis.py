import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def ejercicio_1():
    print("\nEjercicio 1: Maximización de rendimientos con restricciones.")

    # Función objetivo a maximizar (la multiplicamos por -1 porque usaremos minimize)
    def funcion_objetivo(x):
        return -(0.1 * x[0] + 0.08 * x[1])

    # Restricción de presupuesto: x + y = 1
    restriccion1 = {'type': 'eq', 'fun': lambda x: x[0] + x[1] - 1}

    # Restricción de riesgo: 0.02*x^2 + 0.03*y^2 <= 0.05
    restriccion2 = {'type': 'ineq', 'fun': lambda x: 0.05 - (0.02 * x[0]**2 + 0.03 * x[1]**2)}

    x0 = [0.5, 0.5]  # Valores iniciales

    resultado = minimize(funcion_objetivo, x0, constraints=[restriccion1, restriccion2])

    if resultado.success:
        print(f"Inversión óptima en x: {resultado.x[0]:.4f}")
        print(f"Inversión óptima en y: {resultado.x[1]:.4f}")
        print(f"Rendimiento máximo: {-resultado.fun:.4f}")
    else:
        print("No se encontró solución.")

def ejercicio_2():
    print("\nEjercicio 2: Minimización de costos de producción.")

    # Función de costos a minimizar
    def funcion_costos(x):
        return 5 * x[0]**2 + 3 * x[1]**2 + x[2]**2

    # Restricción: x + y + z = 100
    restriccion = {'type': 'eq', 'fun': lambda x: x[0] + x[1] + x[2] - 100}

    x0 = [30, 30, 40]  # Valores iniciales

    resultado = minimize(funcion_costos, x0, constraints=[restriccion])

    if resultado.success:
        print(f"Producción óptima de A: {resultado.x[0]:.2f}")
        print(f"Producción óptima de B: {resultado.x[1]:.2f}")
        print(f"Producción óptima de C: {resultado.x[2]:.2f}")
        print(f"Costo mínimo: {resultado.fun:.2f}")

        # Gráfica de barras
        plt.bar(['Producto A', 'Producto B', 'Producto C'], resultado.x)
        plt.title("Distribución óptima de producción")
        plt.ylabel("Unidades")
        plt.show()
    else:
        print("No se encontró solución.")

def ejercicio_3():
    print("\nEjercicio 3: Descenso del gradiente.")

    # Función a minimizar
    def funcion(x, y, z):
        return x**2 + y**2 + z**2 - 2*x*y + 3*z

    # Derivadas parciales (gradiente)
    def gradiente(x, y, z):
        df_dx = 2*x - 2*y
        df_dy = 2*y - 2*x
        df_dz = 2*z + 3
        return np.array([df_dx, df_dy, df_dz])

    x, y, z = 1.0, 1.0, 1.0
    alpha = 0.1
    valores_funcion = []

    for i in range(15):
        grad = gradiente(x, y, z)
        x -= alpha * grad[0]
        y -= alpha * grad[1]
        z -= alpha * grad[2]
        valor = funcion(x, y, z)
        valores_funcion.append(valor)

    print(f"Valores después de 15 iteraciones:")
    print(f"x: {x:.4f}, y: {y:.4f}, z: {z:.4f}")
    print(f"Valor final de la función: {valor:.4f}")

    plt.plot(range(1, 16), valores_funcion, marker='o')
    plt.title("Evolución del valor de f(x, y, z)")
    plt.xlabel("Iteración")
    plt.ylabel("Valor de la función")
    plt.grid()
    plt.show()

def ejercicio_4():
    print("\nEjercicio 4: Minimización con restricciones.")

    # Función a minimizar
    def funcion(x):
        return x[0]**2 + 4*x[0] + 5

    # Restricciones: x >= 2 y x <= 5
    restricciones = [
        {'type': 'ineq', 'fun': lambda x: x[0] - 2},  # x >= 2
        {'type': 'ineq', 'fun': lambda x: 5 - x[0]}   # x <= 5
    ]

    x0 = [3.0]  # Valor inicial

    resultado = minimize(funcion, x0, constraints=restricciones)

    if resultado.success:
        print(f"Valor óptimo de x: {resultado.x[0]:.4f}")
        print(f"Valor mínimo de la función: {resultado.fun:.4f}")
    else:
        print("No se encontró solución.")

def ejercicio_5():
    print("\nEjercicio 5: Teoría - Puntos estacionarios.")

    print("""
Un punto estacionario es aquel donde la derivada de la función es cero.
Tipos de puntos estacionarios:
- Mínimo local: el valor de la función es menor que el de sus alrededores.
- Máximo local: el valor de la función es mayor que el de sus alrededores.
- Punto de inflexión: la derivada es cero pero cambia la concavidad (ni mínimo ni máximo).

Ejemplo: f(x) = x^3
f'(x) = 3x^2 => f'(0) = 0, pero no es ni mínimo ni máximo. Es punto de inflexión.
    """)

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ DE EJERCICIOS ---")
        print("1. Ejercicio 1: Inversión con restricciones")
        print("2. Ejercicio 2: Minimización de costos")
        print("3. Ejercicio 3: Método de gradiente")
        print("4. Ejercicio 4: Minimización con restricciones")
        print("5. Ejercicio 5: Puntos estacionarios")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ejercicio_1()
        elif opcion == '2':
            ejercicio_2()
        elif opcion == '3':
            ejercicio_3()
        elif opcion == '4':
            ejercicio_4()
        elif opcion == '5':
            ejercicio_5()
        elif opcion == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el menú
menu()
