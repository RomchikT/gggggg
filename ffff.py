List1 = [1, 2, 3, 34, 55, 6, 7, 12]
List2 = [2, 7, 8, 99, 10, 11, 12]
List3 = [5, 122, 9, 35, 5, 7, 88, 11, 21002]
List6 = [1, 2, 4]
List7 = [5, 6, 8]
list8 = [123, 455, 5556]
imena = ("Artem", "Roma", "Ceny", "Kirill")
print ("Сумма чисел:", sum(List1))
print ("Наибольший элемент:", max(List2))
spiski = List1 + List2 
print ("Объединенный список:", spiski)
print ("Уникальные элементы:", set(List3))
index = imena.index("Roma")
print("Индекс:", index)
kortedg = List6 + List7 
print("Два кортежа:", str(kortedg)) 
marks = (1, 2, 3, 3, 5, 6, 2, 8, 9)
count = marks.count(2)
print(count)