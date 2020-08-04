# Your code here
lookup = {}


def expensive_seq(x, y, z):
    # Your code here
    if (x,y,z) not in lookup:
        if x <= 0:
            lookup[(x,y,z)] = y+z
        else:
            lookup[(x,y,z)] = sum(expensive_seq(x-i, y+i, z*i) for i in range(1,4))
    return lookup[(x,y,z)]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
