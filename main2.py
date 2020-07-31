nterms = int(input("how many terms?(except 0 and 1) "))
first = 0
second = 1
count = 0

while count < nterms:
       print(first)
       nth = first  + second
       # update values
       first = second
       second = nth
       count += 1
