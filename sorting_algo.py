#Selection Sort
def selection_sort(list_test):
    for i in range (len(list_test)):
        min_idx=i
        for j in range (i+1,len(list_test)):
            if j<len(list_test):
                if list_test[j]<list_test[min_idx]:
                    min_idx=j
        list_test[i],list_test[min_idx]=list_test[min_idx],list_test[i]
    print(list_test)

#Bubble sort
def bubble_sort(list_test):
    for i in range (len(list_test)):
        for j in range (0,len(list_test)-1):
            if list_test[j]>list_test[j+1]:
                list_test[j],list_test[j+1]=list_test[j+1],list_test[j]
    print(list_test)
    

#Insertion Sort  
def insertion_sort(list_test):
    i,j=0,1
    while list_test[-1]!=max(list_test) and j<=len(list_test):
        if (list_test[i]>list_test[j]):
            list_test[i],list_test[j]=list_test[j],list_test[i]
            j+=1
    print(list_test)
list_test = [64, 34, 25, 12, 22, 11, 9] 
insertion_sort(list_test)
