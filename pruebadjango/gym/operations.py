# programaEntrenadores/utils.py
import math

class Usuario:
    def __init__(self, sexo, edad, peso, altura, cintura, cuello, cadera):
        self.sexo = sexo
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.cintura = cintura
        self.cuello = cuello
        self.cadera = cadera

    def calcular_bmr(self):
        if self.sexo == '1':
            return (10 * float(self.peso)) + (6.25 * float(self.altura)) - (5 * self.edad) + 5
        elif self.sexo == '2':
            return (10 * float(self.peso)) + (6.25 * float(self.altura)) - (5 * self.edad) - 161
        else:
            raise ValueError("Sexo no válido. Usa 'hombre' o 'mujer'.")

    def calcular_imc(self):
        altura_m = float(self.altura) / 100
        return float(self.peso) / (altura_m ** 2)

    def calcular_indice_cintura_altura(self):
        return float(self.cintura) / float(self.altura)

    def calcular_porcentaje_graso(self):
        if self.sexo == '1':
            return 495 / (1.0324 - 0.19077 * math.log10(float(self.cintura) - float(self.cuello)) + 0.15456 * math.log10(float(self.altura))) - 450
        elif self.sexo == '2':
            if self.cadera is None:
                raise ValueError("La cadera es necesaria para mujeres.")
            return 495 / (1.29579 - 0.35004 * math.log10(float(self.cintura) + float(self.cadera) - float(self.cuello)) + 0.22100 * math.log10(float(self.altura))) - 450
        else:
            raise ValueError("Sexo no válido. Usa 'hombre' o 'mujer'.")

    def masa_corporal_magra(self, porcentaje_graso):
        return float(self.peso) * (1 - porcentaje_graso / 100)


def calcular_calorias(bmr, actividad):
        return bmr * float(actividad)
