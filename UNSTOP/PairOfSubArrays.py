def calculate_pairs(n, arr):
    dic={}
    for i in range(n):
        sump=0
        for j in range(i,n):
            sump+=arr[j]
            if sump not in dic:
                dic[sump]=[]
            dic[sump].append((i,j))
    ans=0
    for sump in dic:
        lst=dic[sump]
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                l1,r1=lst[i]
                l2,r2=lst[j]
                if r1<l2 or r2<l1:
                    ans+=1
    return ans
        



    



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])  # The first line of input, integer N
    arr = list(map(int, data[1:n+1]))  # The second line of input, N space-separated integers
    result = calculate_pairs(n, arr)
    print(result)

if __name__ == "__main__":
    main()