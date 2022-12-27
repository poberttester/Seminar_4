
import math    

# Функция вычисляет число π c заданной точностью d. 
# Значение d вводится в формате 0.01, 1, 0.1 и т.д.
def pi_precision():
    d = input('Задайте параметр точности числа π, d = ')

    if len(d) > 1:
        print(round(math.pi, len(d) - 2))
    else:
	    print("π c заданной точностью:", int(math.pi))


# Задаётся натуральное число N.  Функция составит список простых множителей числа N.
def is_a_factor_of_N():

 N = int(input("N = "))
 lst = []

 for i in range(2, N + 1):
  for j in lst:
   if i % j == 0:
    break
  else:       
   if N / i - int(N / i) == 0:
    lst.append(i)
      
 print("Cписок простых множителей числа N", lst)
     

 # Функция выведет список неповторяющихся элементов исходной последовательности заданых чисел.  
def non_repeating_numbers(*params):

    non_repeating = []
    
    for index, value in enumerate(params):
        for index2, value2 in enumerate(params):

            if index != index2 and value == value2:
               break
        else:
            non_repeating.append(value)


    return non_repeating

    