limit=int(input('Enter a limit '))
sum=0
for i in range(1,limit+1):
    if i%2 != 0:
        sum+=i
print("Odd sum = "+str(sum))
