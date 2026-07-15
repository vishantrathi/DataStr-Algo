sink=['plate','spoon','cup']

print(f'\n There are {len(sink)} dishes in the sink :{sink}\n')

for dish in list(sink):
    print(f'-put a {dish} in the dishwasher')
    sink.remove(dish)

    print(f'\n there are {len(sink)} dishes in the sink{sink}\n')