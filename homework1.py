#1 вариант
total = sum(range(2, 101, 2))
print(total)

#2 вариант
a = 1
b = 100
res = sum(i for i in range(a, b + 1)
          if i % 2 == 0)
print(res)