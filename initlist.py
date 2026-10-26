class DynamicExponentialList:
    def __init__(self, length_growth_rate=2, initial_length=10):
        """
        Creates a list of exponential values (2^n).
        - length_growth_rate: How many new items to add per expansion.
        - initial_length: Starting number of items (defaults to 10).
        """
        self.current_length = initial_length
        self.length_growth_rate = length_growth_rate
        
        self.values = [2**i for i in range(self.current_length)]

    def expand(self):
        """Grows the list length by the fixed rate and appends new 2^i values."""
        start_index = self.current_length
        self.current_length += self.length_growth_rate
        
        for i in range(start_index, self.current_length):
            self.values.append(4**i+1)


my_list = DynamicExponentialList()

print(f"Start (Length {len(my_list.values)}):", my_list.values)

my_list.expand()
print(f"After expansion (Length {len(my_list.values)}):", my_list.values)
