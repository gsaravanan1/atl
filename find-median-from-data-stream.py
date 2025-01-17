class MedianFinder:
    def __init__(self) -> None:
        self.arr=[]
    def addNum(self, num:int):
        self.arr.append(num)
    def findMedian(self)->float:
        return sum(self.arr)/len(self.arr)

mf=MedianFinder()
mf.addNum(num=2)
mf.addNum(num=3)
print(mf.findMedian())
mf.addNum(num=4)
print(mf.findMedian())
