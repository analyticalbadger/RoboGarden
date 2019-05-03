def CountList(list):
    return len(list)

def SumList(list):
    return sum(list)

def AverageList(list):
    return sum(list)/len(list)

def MaxList(list):
    a = max(list)
    b = list.index(max(list))
    return (a, b)

def MinList(list):
    a = min(list)
    b = list.index(min(list))
    return (a, b)
