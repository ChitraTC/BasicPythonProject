#to print num between 100-400 both included.each digit of a num is even num.
l1 = []
for i in range(100, 401):
        n = str(i)
        if (int(n[0]) % 2 == 0) and (int(n[1]) % 2 == 0) and (int(n[2]) % 2 == 0):
            l1.append(n)
print(",".join(l1))
