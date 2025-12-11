n=int(input("Enter The number:"))
for i in range(1,11):
    if i==5:
        continue
    j=2*i
    print(f"{n} x {i} = {j}")