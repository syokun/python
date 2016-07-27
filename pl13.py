# coding: UTF-8
a = 10
b = 1.234234
c = "nakanishi"
d = {"syo":200, "kohei":500}
print "age: %d" % a
print "age: %10d" % a
print "age: %010d" % a
print "price: %f" % b
print "price: %.2f" % b
print "name: %s" % c 

print "sales: %(syo)d" % d
print "%d and %f" %  (a,b)
