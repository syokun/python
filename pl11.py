# coding: UTF-8
# セット（集合型）ー重複を許さない

a = set([1, 2, 3, 4, 3, 2])
print a

b = set([3, 4, 5])
print a - b # 差集合
print a | b # 和集合
print a & b # 積集合
print a ^ b # どちらかにしかないもの 
