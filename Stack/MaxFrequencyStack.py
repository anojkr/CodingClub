"""
    push(int x): map the element (x) with frequency HashMap and update the maxfreq variable
    ( i.e. holds the maximum frequency till now ). setMap maintains a stack which contains all
    the elements with same frequency.

    pop(): First get the maxfreq element from setMap and then decrement the frequency of the popped element.
    After popping, if the stack becomes empty then decrement the maxfreq.

"""
import collections
class FreqStack:

    def __init__(self):
        self.HashMap = collections.defaultdict(list)
        self.freqMap = collections.defaultdict(int)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        currFreq = self.freqMap.get(val)
        newFreq = 0
        if currFreq != None:
            newFreq = self.freqMap.get(val) + 1
        else:
            newFreq = 1
        self.freqMap[val] = newFreq
        if self.maxFreq < newFreq:
            self.maxFreq = newFreq
        self.HashMap[newFreq].append(val)

    def pop(self) -> int:
        setMapMaxFreq = self.HashMap.get(self.maxFreq)
        if len(setMapMaxFreq) == 1:
            self.maxFreq -= 1
        ele = setMapMaxFreq.pop()
        self.freqMap[ele] -= 1
        return ele

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
