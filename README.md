# Hacker_rank solutions
# Sock Merchant 

def sock_pairs(n,sock_list):
    if n>=1 and n<=100:
        pair=0
        sock_set=set(sock_list)
        tmp_sock=list(sock_set)
        for sock in tmp_sock:
            count=sock_list.count(sock)
            #print(sock,count)
            pair+=int(count/2)
        return pair

num=int(raw_input())
list1=map(int,raw_input().split(' '))
print(sock_pairs(num,list1))
