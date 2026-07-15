import random

dirty = True
scrub_count = 0

while dirty:
    scrub_count += 1
    print(f"Scrubbed the pan {scrub_count} times")

    print("Rinsing to check if the pan is clean...\n")

    number = random.randint(0, 9)
    print("Random number:", number)

    if number == 0:
        print("All clean")
        dirty = False
    else:
        print("Still dirty")