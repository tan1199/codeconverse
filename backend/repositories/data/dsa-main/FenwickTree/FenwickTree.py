class FenwickTree:

    def __init__(self, arr) -> None:
        self.arr = arr
        self.fenwickTree = [0] + [i for i in arr]
        self.buildTree()
    

    def buildTree(self):
        for i in range(1, len(self.fenwickTree)):
            parentIndex = i + FenwickTree.lsb(i)
            if(parentIndex<len(self.fenwickTree)): 
                self.fenwickTree[parentIndex] += self.fenwickTree[i]


    def query(self, index):
        index+=1
        ans = 0 
        while(index>0):
            ans += self.fenwickTree[index]
            index -= FenwickTree.lsb(index)
        return ans


    def rangeQuery(self, start, end=None):
        return self.query(end) - self.query(start)

    def update(self, index, new_val):
        prev = self.arr[index]
        index += 1
        while(index<len(self.fenwickTree)):
            self.fenwickTree[index] -= prev
            self.fenwickTree[index] += new_val
            index = index + FenwickTree.lsb(index)

    @staticmethod
    def lsb(num):
        return num ^ (num & (num-1))
    
FenwickTree = FenwickTree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print(FenwickTree.fenwickTree)

print(FenwickTree.query(8))
print(FenwickTree.query(13))
print(FenwickTree.query(15))

FenwickTree.update(8, 19)
print(FenwickTree.fenwickTree)


# print(FenwickTree.lsb(108))
# print(FenwickTree.lsb(104))
# print(FenwickTree.lsb(96))
# print(FenwickTree.lsb(64))
# print(FenwickTree.lsb(0))
