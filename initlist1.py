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
            self.values.append(2**(i + 1))

# --- Example Usage ---

# Let's force a really long list so we can see the slice in action
my_list = DynamicExponentialList(length_growth_rate=5, initial_length=20)

print(f"Total items in list: {len(my_list.values)}")

# Add [:10] to only print index 0 through 9
print("First 9 items only:", my_list.values[:9])