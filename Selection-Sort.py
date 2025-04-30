class Solution: 
    def selectionSort(self, l):
        n=len(l)
        for i in range(n-1):
            index=i
            for j in range(i+1,n):
                if l[j]<l[index]:
                    index=j
            l[index],l[i]=l[i],l[index]
        return l


