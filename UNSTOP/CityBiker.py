def highestAltitude(n, arr):
    pSum=[0]*n
    pSum[0]=arr[0]
    max_altitude=max(0,pSum[0])
    for i in range(1,n):
        pSum[i]=pSum[i-1]+arr[i]
        max_altitude=max(max_altitude,pSum[i])
    return max_altitude

    # Write your logic here

  # Placeholder return

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = highestAltitude(n, arr)
    print(result)