from pprint import pprint
f = open("ex4.txt", mode='wb')
f = open("Толстой.txt", 'w')
data = f.read(20)
print(type(data))
print(data[:1000])
print(f.tell())
f.read(40)
print(f.writable())
print(f.seekable())
print(f.mode)
print(f.closed)
f.close()
print(f.closed)
data = f.readline()

data = ""
for i in range(70):
    data += f.readline()
print(f'Тип данных: {type(data)}',
      f'Размер данных: {len(data)}')
pprint(data[:20])
print(f.tell())

print('ab\n12')
print(r'ab\n12')
print(f.write("123/n456"))
print(f.seek(3))
print(f.write("789"))
f.close()

from math import sin

for i in range(10):
    print("%0.2f" % sin(i))
f.close()

data = [34, 56, 78, 10, 90, 45, 56]
f.write(bytes(data))

f.close()
