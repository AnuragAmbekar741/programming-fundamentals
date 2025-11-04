class Tuple_in_python:
    """
    A simple tuple-like data structure implementation from scratch.
    Key features: Immutable, ordered, hashable.
    """
    
    def __init__(self, *args):
        """
        Initialize tuple with elements.
        Args are stored in a private list (which we won't modify after init).
        """
        # Store in a private list (we'll make it immutable)
        self._data = list(args)
        # Pre-calculate hash for efficiency
        self._hash = None
    
    def __getitem__(self, index):
        """Allow indexing: my_tuple[0], my_tuple[-1], etc."""
        return self._data[index]
    
    def __len__(self):
        """Return length: len(my_tuple)"""
        return len(self._data)
    
    def __repr__(self):
        """String representation: (1, 2, 3)"""
        return '(' + ', '.join(str(item) for item in self._data) + ')'
    
    def __eq__(self, other):
        """Check equality: my_tuple1 == my_tuple2"""
        if not isinstance(other, Tuple_in_python):
            return False
        if len(self) != len(other):
            return False
        return all(self[i] == other[i] for i in range(len(self)))
    
    def __hash__(self):
        """Make it hashable for dictionary keys"""
        if self._hash is None:
            # Convert to tuple for hashing (since lists aren't hashable)
            self._hash = hash(tuple(self._data))
        return self._hash
    
    def __iter__(self):
        """Allow iteration: for item in my_tuple"""
        return iter(self._data)
    
    def __contains__(self, item):
        """Check membership: item in my_tuple"""
        return item in self._data
    
    def count(self, value):
        """Count occurrences of value"""
        count = 0
        for item in self._data:
            if item == value:
                count += 1
        return count
    
    def index(self, value):
        """Find index of first occurrence of value"""
        for i, item in enumerate(self._data):
            if item == value:
                return i
        raise ValueError(f"{value} is not in tuple")
    
    def __add__(self, other):
        """Concatenation: my_tuple1 + my_tuple2"""
        if isinstance(other, Tuple_in_python):
            return Tuple_in_python(*(self._data + other._data))
        return NotImplemented
    
    def __mul__(self, n):
        """Repetition: my_tuple * 3"""
        if isinstance(n, int):
            return Tuple_in_python(*(self._data * n))
        return NotImplemented
    
    def __lt__(self, other):
        """Less than comparison"""
        if not isinstance(other, Tuple_in_python):
            return NotImplemented
        return self._data < other._data
    
    def __le__(self, other):
        """Less than or equal"""
        return self == other or self < other
    
    def __gt__(self, other):
        """Greater than"""
        if not isinstance(other, Tuple_in_python):
            return NotImplemented
        return self._data > other._data
    
    def __ge__(self, other):
        """Greater than or equal"""
        return self == other or self > other


# Test the implementation
if __name__ == "__main__":
    # Create tuples
    t1 = Tuple_in_python(1, 2, 3)
    t2 = Tuple_in_python(4, 5)
    t3 = Tuple_in_python(1, 2, 3)
    
    print(f"t1 = {t1}")              # (1, 2, 3)
    print(f"t2 = {t2}")              # (4, 5)
    print(f"Length: {len(t1)}")      # 3
    
    # Indexing
    print(f"t1[0] = {t1[0]}")        # 1
    print(f"t1[-1] = {t1[-1]}")      # 3
    
    # Equality
    print(f"t1 == t3: {t1 == t3}")   # True
    
    # Concatenation
    t4 = t1 + t2
    print(f"t1 + t2 = {t4}")         # (1, 2, 3, 4, 5)
    
    # Repetition
    t5 = t1 * 2
    print(f"t1 * 2 = {t5}")          # (1, 2, 3, 1, 2, 3)
    
    # Iteration
    print("Items in t1:")
    for item in t1:
        print(f"  {item}")
    
    # Membership
    print(f"2 in t1: {2 in t1}")     # True
    print(f"5 in t1: {5 in t1}")     # False
    
    # Count
    t6 = Tuple_in_python(1, 2, 2, 3, 2)
    print(f"Count of 2 in {t6}: {t6.count(2)}")  # 3
    
    # Index
    print(f"Index of 2 in {t6}: {t6.index(2)}")  # 1
    
    # Hashable (for dictionary keys)
    my_dict = {
        Tuple_in_python(1, 2): "first",
        Tuple_in_python(3, 4): "second"
    }
    print(f"Dictionary: {my_dict}")  # {(1, 2): 'first', (3, 4): 'second'}
    
    # Comparison
    t7 = Tuple_in_python(1, 2, 3)
    t8 = Tuple_in_python(1, 2, 4)
    print(f"{t7} < {t8}: {t7 < t8}")  # True