def array_diff(a, b):
    #your code here
    count = 0
    if len(b)==0:
        return a
    for i in b:
        if i in a:
            for n in range(a.count(i)):
                a.remove(i)
    return a            
