

class Barco:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0

    def recibir_impacto(self):
        if self.golpes_recibidos < self.longitud:
            self.golpes_recibidos += 1

    def esta_hundido(self):
        return self.golpes_recibidos >= self.longitud

    def mostrar_estado(self):
        print(f"Barco: {self.nombre}")
        print(f"Longitud: {self.longitud}")
        print(f"Golpes recibidos: {self.golpes_recibidos}")
        print(f"Hundido: {self.esta_hundido()}")
        print("-" * 20)


# Pruebas:
if __name__ == "__main__":
    # Crear barcos
    submarino = Barco("Submarino", 1)
    buque = Barco("Buque", 3)

    # Prueba Submarino
    print("Pruebas con el Submarino:")
    submarino.mostrar_estado()
    submarino.recibir_impacto()
    submarino.mostrar_estado()

    # Prueba Buque
    print("\nPruebas con el Buque:")
    buque.mostrar_estado()
    buque.recibir_impacto()
    buque.recibir_impacto()
    buque.mostrar_estado()
    buque.recibir_impacto()
    buque.mostrar_estado()
