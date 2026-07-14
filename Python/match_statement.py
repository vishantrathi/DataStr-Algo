#compair the value of an expression to a series of case patterns
#executes the first case that matches the pattern

def order_pizza(day):
    match day:
        case 'Sunday':
            return 'spnitch pizza'
        case 'Monday':
            return'mushroom pizza'
        case 'Tuesday':
            return'mushroom + corn pizza'
        case 'wednesday':
            return 'peproni pizza'
        case 'thrusday':
            return 'cheese pizza'
        case 'friday':
            return 'sausage pizza'
        case 'Saturday':
            return 'Hawaiian pizza'
        #match Default case
        #serve as a final catch all pattern
        #defined using the wildcard_sym
        case _:
            print(f'There is no {day} special')
            return None
        
today='Tuesday'
special=order_pizza(today)
print(f'\n Today is {today}, and the special is {special}.\n')

#None Object --> a special python object denoting the lack of a value
 