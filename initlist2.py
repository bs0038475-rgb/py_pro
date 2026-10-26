import random

class DynamicExponentialList:
    def __init__(self, length_growth_rate, initial_length=None):
        self.length_growth_rate = length_growth_rate
        self.current_length = 0
        self.values = []
        
        if initial_length is None:
            actual_initial_length = random.randrange(2, 22, 2)
        else:
            if initial_length % 2 != 0:
                raise ValueError("The initial length must be divisible by 2!")
            actual_initial_length = initial_length
            
        self.expand(amount=actual_initial_length)

    def expand(self, amount=None):
        if amount is None:
            amount = self.length_growth_rate
            
        start_index = self.current_length
        self.current_length += amount
        
        for i in range(start_index, self.current_length):
            # Check if we are at index 0 through 9
            if i < 10:
                self.values.append(2**(i + 1))
            else:
                # Any index after 9 just becomes 0
                self.values.append(0)

# --- Example Usage ---

# Force a list of 14 items to see the cutoff in action
my_list = DynamicExponentialList(length_growth_rate=5, initial_length=14)

# Let's print the list with its index so it's easy to read
for index, value in enumerate(my_list.values):
    print(f"Index {index}: {value}")
