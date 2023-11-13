class BagOfWords:

    def __repr__(self) -> str:
        return ", ".join(f"{word}: {count}" for word, count in sorted(self._data.items(), key=lambda x: -x[1]))
    
    def __contains__(self, item) -> bool:
        return item in self._data
    
    def __iter__(self):
        for i, _ in sorted(self._data.items(), key=lambda x: -x[1]):
            yield i

    def __add__(self, arg):
        if not isinstance(arg, BagOfWords):
            raise TypeError("Unsupported operand type for +")
        
        res = {k: v for k, v in self._data.items()}
        for k, v in arg._data.items():
            res[k] = res.get(k, 0) + v

        return BagOfWords(res)
    
    def __getitem__(self, arg):
        if arg in self._data:
            return self._data[arg]
        else:
            raise IndexError("Index out of range")
        
    def __setitem__(self, arg, val):
        if arg in self._data:
            self._data[arg] = val
        else:
            raise IndexError("Index out of range")
