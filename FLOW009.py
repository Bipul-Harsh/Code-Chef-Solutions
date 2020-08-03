def total(quant,price):
    if(quant<=1000):
        return(quant*price)
    else: 
        total = quant*price
        return(total-(total*0.1))

for _ in range(int(input())):
    (quant,price) = map(int,input().split())
    print("%0.6f"%total(quant,price))