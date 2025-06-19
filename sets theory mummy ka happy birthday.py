#all about set theory
#The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False.
cities={"tokyo","berlin","madagascar","new jersey","tokyo"}
print(cities)
cities.discard("madagascar")
print(cities)
gals={"1","2","3","4"}
p=cities.union(gals)
print(p)
cities2={"tokyo","berlin","seoul","newjercsey"}
q=cities.difference(cities2)
print(q)
r=cities.pop()
print(r)
