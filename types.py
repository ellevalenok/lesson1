#a=2
#b = 8
#print(a+b)


#name='лена'.upper()
#b='Привет, {name}!'.format(name=name)
#print (b)

#v=input('Введите число от 1 до 10: ')
#v=int(v)
#a=10
#b=v+a
#print(b) 

#print (v+a)


#v=input('Введите ваше имя: ').capitalize()
#m='привет'.capitalize()
#c='Как дела?'
#print(m+', '+v+'! '+c)

#print(float('1'))
#print(int('2.5'))
#print(float('2.5'))
#print(bool(1))
#print(bool(''))
#print(bool(0))

#задание укажи номер откуда 
#numbers=[int(3),'5', '7', '9', '10.5']
#numbers=['3','5', '7', '9', '10.5']
#numbers.append('Python')
#print(numbers)
#print(len(numbers))
#print(numbers[:1]) #3 первый элемент списка
#print(numbers[:0]) #3 до нулевого элемента
#print(numbers[-1]) #last one - последний элемент списка
#print(numbers[1:5]) #со второго по четвертый
#numbers.remove('Python')
#print(numbers) 

cities= [{"city": "Москва", "temperature": "20"}]
print(cities) #выведеет все строки
print(cities[0]) #выведет строку с москвой

#Выведите на экран значение ключа city 
print(cities[0]["city"]) #для обращения к элементу строки надо указать список, указать строку списк в кв скобках [], в кавычках элемент к которому обращаемся 

#Уменьшите значение "temperature" на 5
# здесь надо преобразовать значение словаря в тип интегер
cities[0]["temperature"]=int(cities[0]["temperature"])-5
print(cities[0])


#Проверьте, есть ли в словаре ключ country - списки со словарями
#print(cities[0]["country"])

#Выведите значение по-умолчанию "Россия" для ключа country
cities[0]["country"]='Russia'

print(cities)
#print(cities[0].get("country", "Russia"))

#Добавьте в словарь элемент date со значением '27.05.2019'
cities[0]["date"]='27.05.2019'
print(cities)
#Выведите на экран длину словаря
#print(len(cities))