class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print(X[12]) # Для X[i] вызывается X.__getitem__(i)

for i in range(13):
    print(X[i])
print("-" * 60)
###
class IndexerTwo:
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def __getitem__(self, index): # Вызывается для нарезания или индексирования
        print("getitem: ", index)
        return self.data[index] # Выполняется индесирование или нарезание

Y =IndexerTwo()
print(Y[0]) # Индексирование отправляет целое число
print(Y[8])
print(Y[-1])
print(Y[::-1]) # Нарезание отправляет __getitem__ объект среза
print(Y[1:])
print(Y[5])
print(Y[::2])
print("-" * 60)
###

class IndexerThree:
    def __getitem__(self, index):
        if isinstance(index, int): # Проверка режима использования
            print("indexing", index)
        else:
            print("slicing", index.start, index.stop, index.step)

M = IndexerThree()
M[99]
M[1:99:2]
M[1:]
print("-" * 60)
###

class StepperIndex:
    def __getitem__(self, index):
        return self.data[index]

H = StepperIndex()
H.data = "spam"
print(H[0]) # Для индексирования вызвается __getitem__
for item in H: # Для циклов for вызывается __getitem__
    print(item) # Цикл for индексирует элементы 0...N

print("p" in H) # Для всех вызывается __getitem__

print([x for x in H]) # Списковое включение

print(list(map(str.upper, H))) # Вызов map

(a, b, c, d) = H # Присваивание
print(c, d)

print(list(H), tuple(H), "".join(H)) # И так далее...
