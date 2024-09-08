#stair problem: can take 1 or 2 steps 
#calculate how many ways can we take n steps

n = int(input("how many steps?: "))
def stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    table = [1, 2]

    for i in range(2, n):
        table.append(table[i-1] + table[i-2])
    return table[n-1]
ans = stairs(n)
print(ans)

#accidental fibonacci sequence generator