
class BinarySearchTree:
    def __init__(self, data=None):
        self._data=data
        self._left=None
        self._right=None

    def getData(self):
        return self._data

    def setData(self, d):
        self._data = d


    def isEmpty(self):
        return self._left == self._right == self._data == None


    def size(self):
        sz = 0
        if self._left:
            sz += self._left.size()
        if self.getData():
            sz += 1
        if self._right:
            sz += self._right.size()
        return sz


    def insert(self, x):
        if self.isEmpty():
            self.setData( x )
        elif x < self.getData():
            if self._left:
                self._left.insert( x )
            else:
                self._left = BinarySearchTree( x )
        else:  # x >= data
            if self._right:
                self._right.insert( x )
            else:
                self._right = BinarySearchTree( x )






