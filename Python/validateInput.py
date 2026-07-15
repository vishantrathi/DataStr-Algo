

class circuitBreaker:
    def __init__(self,max_amps):
        self.capacity=max_amps
        self.load=0

    def connect(self, amps):
        self.load +=amps
        if self.load> self.capacity:
            # print('tripped')
            raise Exception('limit exceeds')

    
cb=circuitBreaker(20)
print(cb.capacity)
print(cb.load)

cb.connect(12)
cb.connect(15)
cb.connect(10)

print(cb.load)
