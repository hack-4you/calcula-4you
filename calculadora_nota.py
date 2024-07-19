class CalculadoraNotaFinal:
    def __init__(self, incluye_taller):
        self.incluye_taller = incluye_taller
        self.ejercicio1 = 0.0
        self.ejercicio2 = 0.0
        self.taller = 0.0
        self.catedra = 0.0
        self.nota_deseada = 40.0  # Se aprueba con nota 40 en escala de 1 a 70
        self.peso_ej1 = 0.15  # 30% dividido entre dos
        self.peso_ej2 = 0.15  # 30% dividido entre dos
        self.peso_taller = 0.05 if incluye_taller else 0.0
        self.peso_catedra = 0.30
        self.peso_examen = 0.35 if incluye_taller else 0.40  # Dependiendo de si incluye taller o no

    def ingresar_notas_ejercicios(self):
        self.ejercicio1 = float(input("Ingrese la nota del Ejercicio 1: "))
        self.ejercicio2 = float(input("Ingrese la nota del Ejercicio 2: "))
        self.catedra = float(input("Ingrese la nota de Cátedra: "))

        if self.incluye_taller:
            self.taller = float(input("Ingrese la nota del Taller: "))

        self.calcular_notas_minimas()

    def calcular_notas_minimas(self):
        # Calcular el puntaje acumulado de ejercicios, taller y cátedra
        puntaje_acumulado = (self.ejercicio1 * self.peso_ej1) + (self.ejercicio2 * self.peso_ej2) + (self.taller * self.peso_taller) + (self.catedra * self.peso_catedra)

        # Calcular la nota necesaria en el examen final
        nota_examen_necesaria = (self.nota_deseada - puntaje_acumulado) / self.peso_examen
        nota_examen_necesaria = max(nota_examen_necesaria, 0)  # Asegurar que no sea negativa si ya se alcanzó la nota deseada

        self.mostrar_resultado(nota_examen_necesaria)

    def mostrar_resultado(self, nota_examen_necesaria):
        print(f"\nPara aprobar el ramo con un promedio de {self.nota_deseada}, necesitas obtener al menos:")
        print(f"  - {nota_examen_necesaria:.2f} en el examen final.")

def main():
    try:
        incluye_taller = input("Naaak!naaak!¿El ramo incluye el taller de acompañamiento? (s/n): ").strip().lower() == "s"
        calculadora = CalculadoraNotaFinal(incluye_taller)
        calculadora.ingresar_notas_ejercicios()
    except KeyboardInterrupt:
        print("\nProceso de cálculo de notas interrumpido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()