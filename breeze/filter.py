class FilterOptions:
    def __init__(self, size=10, page=0):
        self._page = page
        self._size = size

    @property
    def size(self):
        return self._size

    @property
    def page(self):
        return self._page
