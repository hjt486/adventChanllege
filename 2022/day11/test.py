def ASCIIadd(num1, num2):
        c = 0
        res = ''
        num1, num2 = num1.strip()[::-1], num2.strip()[::-1]
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        for i in range(len(num1)):
            a = 0
            b = 0
            if i < len(num1):
                a = int(num1[i])
            if i < len(num2):
                b = int(num2[i])
            r = a + b + c
            res += str(r % 10)
            c = r // 10
        if c:
            res += str(c)
        return res[::-1]

print(ASCIIadd("30", "15"))

def ASCIImultiply(num1, num2):
    num1, num2 = num1.strip()[::-1], num2.strip()[::-1]
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    accum = "0"
    for i in range(len(num1)):
        temp_res = "".join(["0" for x in range(i)])
        a = int(num1[i])
        c = 0
        for j in range(len(num2)):
            b = int(num2[j])
            r = a * b + c
            temp_res += str(r % 10)
            c = r // 10
        if c:
            temp_res += str(c)
        accum = ASCIIadd(accum, temp_res)
    return accum[::-1]

def ASCIImod(num1, num2):
    num1 = num1.strip()
    res = 0
    for i in range(len(num1)):
        res = (res * 10 + int(num1[i])) % num2
    return res


print(ASCIImod("10000", 30))

