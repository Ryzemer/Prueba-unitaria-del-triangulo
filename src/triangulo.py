import math


def area_triangulo(a, b, c):
    # Verificar si los lados pueden formar un triángulo
    if a + b <= c or a + c <= b or b + c <= a:
        return "Los lados proporcionados no forman un triángulo válido."

    # Calcular el semiperímetro
    s = (a + b + c) / 2

    # Calcular el área usando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def main():
    # Solicitar los lados del triángulo al usuario
    try:
        a = float(input("Ingrese la longitud del lado a: "))
        b = float(input("Ingrese la longitud del lado b: "))
        c = float(input("Ingrese la longitud del lado c: "))

        # Calcular y mostrar el área del triángulo
        resultado = area_triangulo(a, b, c)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"El área del triángulo es: {resultado:.2f}")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()
