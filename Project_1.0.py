#print('"Hello" world')
#print('"Hello"'  + ' world')
#print(type("Hello world"))

def duplicate_consonants(word):
    # Создаем шаблон, где все гласные буквы заменяются на пробелы, а согласные остаются на месте
    vowel_mask = ''.join(' ' if letter in 'аеёиоуыэюя' else letter for letter in word)

    # Дублируем каждую согласную букву
    return ''.join(letter * 2 for letter in vowel_mask)


# Применяем функцию к слову "программирование"
result = duplicate_consonants("программирование")
#print(result)
#_________________________________________________________________
import random

# Функция для сравнения суммы элементов двух массивов
def compare_sums(arr1, arr2):
    return sum(arr1) > sum(arr2)

# Генерация четырех случайных массивов из 10 чисел каждый
array1 = [random.randint(1, 100) for _ in range(10)]
array2 = [random.randint(1, 100) for _ in range(10)]
array3 = [random.randint(1, 100) for _ in range(10)]
array4 = [random.randint(1, 100) for _ in range(10)]

# Суммирование элементов каждого массива
sum1 = sum(array1)
sum2 = sum(array2)
sum3 = sum(array3)
sum4 = sum(array4)

# Сравнение суммы первого массива с суммой третьего массива
if sum1 > sum3:
    print("Truth")
else:
    print("Fals")