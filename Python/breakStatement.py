import random
dishwasher=['spoon','plate','tongs','small spoon','bowl']

for dish in list(dishwasher):
    if not random.randint(0,19): # if random==0
        print('Out of space!')
        break
    else:
        print(f'Putting {dish} in the cabinet')
        dishwasher.remove(dish)

        # break pure program ko khatam kar deta hai
        # continue current iteration ko skip kar deta hai