def uniqueSets(a):
    return list(set(a))

def uniqueNoSets(a):
    ans = []
    for elem in a:
        if elem not in ans:
            ans.append(elem)

    return ans