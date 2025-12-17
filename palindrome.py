def palindrome(s):
    n=len(s)
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    odd_count=0
    odd_char=""
    for ch in freq:
        if freq[ch]%2!=0:
            odd_count+=1
            odd_char=ch
    if odd_count>1:
         return "NO SOLUTION"
    result=[""]*n
    left=0
    right=n-1
    if odd_count==1:
        result[n//2]=odd_char
        freq[odd_char]-=1
    for ch in freq:
        while freq[ch] > 0:
            result[left]=ch
            result[right]=ch
            left+=1
            right-=1
            freq[ch]-=2
    return "".join(result)
s=input()
print(palindrome(s))