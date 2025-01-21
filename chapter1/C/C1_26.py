def arithmetic(*k):
    # if len(k) != 3:
    #     return False
    length = len(k)
    for i in range(length):
        for x in range(length-i-1,i,-1):
            if k[i]+k[x] in [k[y] for y in range(length)]:
                print(f"{k[i]}+{k[x]}={k[i]+k[x]}")
            if k[i]-k[x] in [k[y] for y in range(length)]:
                print(f"{k[i]}-{k[x]}={k[i]-k[x]}")
            if k[x]-k[i] in [k[y] for y in range(length)]:
                print(f"{k[x]}-{k[i]}={k[x]-k[i]}")
            if k[i]*k[x] in [k[y] for y in range(length)]:
                print(f"{k[i]}*{k[x]}={k[i]*k[x]}")

if __name__ == "__main__":
    arithmetic(1, 2, 3,6,10,20)
