def majority_element_indexes(lst):
    '''
    return the index of majority element if exist
    A element 
    <<<
    '''
    # find the count of each element
    # sort the count of each element
    # get the top count
    # return the position if top count > floor(len(lst)) 
    count={}
    for i in lst:
        if i not in count.keys():
            count[i]=0
        count[i]+=1
    # sort and get the top count, sort by 
    top_count = sorted(count.items(),key=lambda x: x[1],reverse=True)[0]
    print(top_count)
    # print index of 
    top_index = [i for i in range(len(lst)) if (lst[i]==top_count[0]) ]
    for i in range(len(lst)):
        print(i)
        if (lst[i]==top_count[1]):
            print(lst[i])
    print(top_index)

    


if __name__ == "__main__":
    test_lst = [1,1,2,3,0,1]
    majority_element_indexes(test_lst)