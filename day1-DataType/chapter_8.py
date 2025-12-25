amit=["amit", "rahul", "tota"] 
amit.append("rj")
print(amit)
amit.remove("amit")
print(amit)

fruits=["mango","banana","orange"]
drink=["milk","cold"]
fruits.extend(drink)
fruits.insert(0,"black tea")
print(fruits)


last_added= fruits.pop()
print(last_added)
print(fruits.reverse())
print(fruits)
fruits.sort()
print(fruits)


sugar_level=[1,2,3,4,5,6]
print(max(sugar_level))
print(min(sugar_level))


base_liquid=["water","milk"]
extra=["ginger"]

full= base_liquid+extra
print(full)
strong=["black","water"]*3
print(strong)

raw_spice=bytearray(b"CINAMON")
help=raw_spice.replace(b"CINA",b"CARD")
print(help)