p1 = int(input("물건 가격은??"))
p2 = int(input("물건 개수는??"))
price = p1*p2

if price >= 100000:
    print("과소비")
elif 100000 > price >= 80000:
    print("적당")
else:
    print("좀 더 써라")