# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    
    has_peeked = False
    peeked_element = None
    
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """       
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.has_peeked:
            return self.peeked_element
        
        self.peeked_element = self.next()
        self.has_peeked = True
        
        return self.peeked_element

    def next(self):
        """
        :rtype: int
        """
        
        if self.has_peeked or not self.iterator.hasNext():
            self.has_peeked = False
            return self.peeked_element
        
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext() or self.has_peeked;
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].