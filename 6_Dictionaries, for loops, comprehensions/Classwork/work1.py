# calculator
user_input = input('Input the expression as (2+2): ')
index_of_operator = (
                    user_input.find('+')
                    or user_input.find('-') or user_input.find('*')
                    or user_input.find('/')
                    )
a = user_input[(index_of_operator - 1)]
b = user_input[(index_of_operator + 1)]
operator = user_input[index_of_operator]
