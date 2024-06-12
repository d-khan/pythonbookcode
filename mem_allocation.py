def variable_mem():
    address = set([])
    var1 = 10
    print("var1 value is", var1, "and the memory address is", hex(id(var1)), end="")
    if hex(id(var1)) not in address:
        print(" - New memory address")
    else:
        print(" - Memory reused")

    address.add(hex(id(var1)))
    var2 = 20
    print("var2 value is", var2, "and the memory address is", hex(id(var2)), end="")
    if hex(id(var2)) not in address:
        print(" - New memory address")
    else:
        print(" - Memory reused")

    address.add(hex(id(var2)))
    var3 = 10
    print("var3 value is", var3, "and the memory address is", hex(id(var3)), end="")
    if hex(id(var3)) not in address:
        print(" - New memory address")
    else:
        print(" - Memory reused")

    address.add(hex(id(var3)))
    var4 = 20
    print("var4 value is", var4, "and the memory address is", hex(id(var4)), end="")
    if hex(id(var4)) not in address:
        print(" - New memory address")
    else:
        print(" - Memory reused")

    address.add(hex(id(var4)))
    var1 = 20
    print("var1 value is", var1, "and the memory address is", hex(id(var1)), end="")
    if hex(id(var1)) not in address:
        print(" - New memory address")
    else:
        print(" - Memory reused")

    address.add(hex(id(var1)))
    var1 = 30
    print("var1 value is", var1, "and the memory address is", hex(id(var1)), end="")
    if hex(id(var1)) not in address:
        print(" - New memory address")
    else:
        print(" - Memory reused")

    address.add(hex(id(var1)))
    var1 = "Hello"
    print("var1 value is", var1, "and the memory address is", hex(id(var1)), end="")
    if hex(id(var1)) not in address:
        print(" - New memory address")
    else:
        print(" - Memory reused")

    address.add(hex(id(var1)))
    var1 = 30
    print("var1 value is", var1, "and the memory address is", hex(id(var1)), end="")
    if hex(id(var1)) not in address:
        print(" - New memory address")
    else:
        print(" - Memory reused")


variable_mem()
