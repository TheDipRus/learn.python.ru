# TODO list
# .append("Элемент") - Добавление элементов в список
# .count("Элемент") - Находим количество элементов 
# .index("элемент") - Возвращает индекс элемента
# .sort() - Сортирует список 

#del *list*[index] - удаление по интексу
#.remove('элемент') - удаление элемента по названию


# my_list = [3, 5, 7, 9, 10.5]
# print(my_list)
# my_list.append("Python")
# print(len(my_list))


# print(my_list[0])
# print(my_list[-1])
# print(my_list[2:5])
# my_list.remove("Python")
# print(my_list)


#TODO dict 
#.get('ключ', значение по умолчанию) - запрос по ключу 
#del dict['Ключ']

# phones = ["iphone Xs", "Samsung Galaxy S10", "Xiaomi Mi8"]

# product = {
#     "name": "iPhone xs", 
#     "stock": 5, 
#     "price":65000.0,
#     "recomend": phones,
# }

# print(product["recomend"])
# print(product["recomend"][1])

# product['recomend'].append('iPhone 6')
# print(product)

m_dict = {
    "city": "Москва",
    "temperature": "20"
}
print(m_dict["city"])
m_dict["temperature"] = int(m_dict["temperature"]) - 5
print(m_dict)
print(m_dict.get('country', "Россия"))

m_dict['date'] = '27.05.2019'

print(m_dict)
