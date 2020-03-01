i_have = 0
i_wont = 3
my_money = 100
price = 2
in_stock = 30
while i_wont > 0 and in_stock > 0 and price <= my_money:
    i_have += 1
    i_wont -= 1
    my_money -= price
    in_stock -= 1
    print('in_stock: ', in_stock, 'i_have: ', i_have, end='\n')
    print((i_have < i_wont), (in_stock > 0), (price <= my_money), sep='\t')
print('in_stock: ', in_stock, 'i_have: ', i_have, end='\n')
