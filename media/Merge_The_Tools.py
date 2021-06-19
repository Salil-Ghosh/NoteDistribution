def merge_the_tools(string, k):
    # your code goes here
    t=[]
    i=0
    
    while i <(len(string)):
        t.append(string[i:i+k])
        i=i+k
    
    def deldup(string):
        c=Counter(string)
        s=string
        for i in c:
            if c[i]>1:
                while c[i]>1:
                    li=s.rsplit(i,1)
                    s="".join(li)
                    c[i]-=1
        return s
    
    ts=list(map(deldup,t))
    for i in ts:
        print(i)
from collections import Counter     

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)