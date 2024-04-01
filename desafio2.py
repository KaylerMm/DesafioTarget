# Calcula a sequência de Fibonacci até encontrar número igual ou maior ao informado
def in_fibonacci(number):
  x, y = 0, 1
  while y < number:
      x, y = y, x + y
  if y == number:
      return True
  return False

while True:
  number = int(input('Digite um número para verificar se ele pertence a sequência de Fibonacci: '))

  if in_fibonacci(number):
      print(f"{number} pertence a Fibonacci! 😉")
  else:
       print(f"{number} não pertence a Fibonacci... 😵")