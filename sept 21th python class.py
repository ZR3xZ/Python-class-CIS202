muffin = 10
cupcake = 10
buy = input("do you want to buy a muffin or cupcake. enter muffin for muffin. enter 0 to exit ")
while buy != "0":
    if buy == "muffin" and muffin >0:
        muffin = muffin - 1
    elif muffin == 0 and buy == "muffin":
        print("muffins are out of stock")
    if buy == "cupcake" and cupcake > 0:
        cupcake = cupcake - 1
    elif cupcake ==0 and buy == "cupcake":
        print("cupcake are out of stock")
    buy = input("do you want to buy a muffin or cupcake")
print("muffin:", muffin, "cupcake:", cupcake)
