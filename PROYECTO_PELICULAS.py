import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre

class CatalogoPelicula:
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo

    def agregar(self, pelicula):
        with open(self.ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(pelicula.obtener_nombre() + '\n')

    def listar(self):
        if not os.path.exists(self.ruta_archivo):
            print(f"El catálogo {self.nombre} está vacío.")
            return
        
        with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
            print(f"Catálogo de películas {self.nombre}:")
            for linea in archivo:
                print(linea.strip())

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"Se ha eliminado el catálogo {self.nombre}.")
        else:
            print(f"No existe el catálogo {self.nombre}.")

def menu():
    print("\n*** Gestión de Catálogo de Películas ***")
    print("1- Agregar Película")
    print("2- Listar Películas")
    print("3- Eliminar catálogo de películas")
    print("4- Salir")

def main():
    nombre_catalogo = "Catalogo de Peliculas"
    ruta_archivo = "catalogo_peliculas.txt"

    catalogo = CatalogoPelicula(nombre_catalogo, ruta_archivo)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar(pelicula)
            print(f"Película '{nombre_pelicula}' agregada al catálogo.")
        
        elif opcion == '2':
            catalogo.listar()

        elif opcion == '3':
            catalogo.eliminar()

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()