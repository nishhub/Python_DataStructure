def solutions(ranks):
    count = 0
    for rank in range(0, len(ranks)):
        for i in range(0, len(ranks)):
            #print(ranks[rank])
            if ranks[rank]+1 == ranks[i]:
                count += 1
                break
                
    return count
    
ranks = [4,2,0,1]
print(solutions(ranks))


given an integer n returns an array containing n distinct integers that sum up to 0
