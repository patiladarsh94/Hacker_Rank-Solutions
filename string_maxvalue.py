
'''Jane loves strings more than anything. She has a string with her, and value of string over function
can be calculated as given below:
Jane wants to know the maximum value ofamong all the substrings of string Can you help her?

Input Format
A single line containing string

Output Format Print the maximum value of among all the substrings of string

The string consists of lowercase English alphabets.

Sample Input : aaaaaa

Explanation 0

f('a') = 6
f('aa') = 10
f('aaa') = 12
f('aaaa') = 12
f('aaaaa') = 10
f('aaaaaa') = 6


Sample Output: 12'''




from itertools import combinations 
def max_value(string):
    list1=[]
    count=0
    res = [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2)]
    for string1 in res:
        for i in range(0,len(string)):
            if i<=len(string)-len(string1):
                if string1==string[i:i+len(string1)]:
                    count+=1
        list1.append(count*len(string1))
        #print(string1,len(string1),count)
        count=0
        #list1.append((len(string1))*string.count(string1))
        
    return max(list1)

string=input("Enter the string")
print(max_value(string))
