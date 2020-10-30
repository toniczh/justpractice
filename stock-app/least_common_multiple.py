def lcm(int_1,int_2):
    bigger = max(int_1,int_2)
    product = int_1*int_2
    temp = product - bigger
    while temp>bigger:
        if temp % bigger == 0:
            product=temp
            temp=product-bigger

    return product

print(lcm(24,36))