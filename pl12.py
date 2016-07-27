# coding: UTF-8
# 辞書 key value
sales = {"nakanishi":200, "kohei":300, "syo":400}
print sales
print sales["nakanishi"]
sales["kohei"] = 800
print sales

# in
print "nakanishi" in sales

# keys, values, items
print sales.keys()
print sales.values()
print sales.items()
