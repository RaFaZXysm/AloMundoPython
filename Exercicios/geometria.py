# Crie um script para calcular a área de formas geométricas
#  * Retângulo (area = base * altura)
#  * Triângulo (area = (base * altura)/2 )
#  * Círculo (area = ℼ * r²)

import math

#retangulo

base_retangulo = int(input('Digite a base do retangulo: '))
altura_retangulo = int(input('Digite a altura do retangulo: '))

area_retangulo = base_retangulo * altura_retangulo

print('A area do retangulo é: '+str(area_retangulo))

#triangulo

base_triangulo = int(input('Digite a base do triangulo: '))
altura_triangulo = int(input('Digite a altura do triangulo: '))

area_triangulo = ((base_triangulo * altura_triangulo) / 2)

print('A area do triangulo é: '+str(area_triangulo))

#circulo

raio_circulo = int(input('Digite a raio do circulo: '))

area_circulo = math.pi * (raio_circulo ** 2)

print('A area do circulo é: '+str(area_circulo))
