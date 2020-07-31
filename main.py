nterms = int(input("how many terms? "))
first = 0
second = 1
x = 0
fibonacci = [first , second]
for i in range(0 , nterms):
        x = fibonacci[i] + fibonacci[i+1]
        fibonacci.append(x)
print(fibonacci)
