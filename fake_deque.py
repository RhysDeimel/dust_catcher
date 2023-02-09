class FakeDeque:
    """
    collections.deque isn't fully implemented in MicroPython v1.19.1, so
    I was unable to use it to calc the moving average fan RPM.
    
    This is a naïve implementation to fulfill that purpose
    """

    def __init__(self, maxlen=60):
        self.maxlen = maxlen
        self._data = {i: 0 for i in range(self.maxlen)}
        self.counter = 0

    def append(self, val):
        self._data[self.counter] = val
        self.counter += 1

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, val):
        self._counter = val % self.maxlen

    def __repr__(self):
        return f"FakeDeque({list(self._data.values())})"

    def __iter__(self):
        yield from list(self._data.values())
