class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print(X[12]) # Для X[i] вызывается X.__getitem__(i)

for i in range(13):
    print(X[i])

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

