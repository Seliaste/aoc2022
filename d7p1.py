disk = {"/":{}}

tree = []

lines =  open("input","r").readlines()

res2 = []

def calc_size(dictio,name="root"): 
    res = 0
    for val in dictio:
        if isinstance(dictio[val],int):
            res += dictio[val]
        else:
            res += calc_size(dictio[val],val)
    global res2 
    res2.append(res)
    return res

for line in lines:
    line = line.strip("\n").split(" ")
    match line:
        case ['$','cd',arg]:
            if arg == "..":tree.pop()
            else:tree.append(arg)
        case ['$','ls']:
            pass
        case ['dir',dirname]:
            tmp = disk
            for val in tree:
                tmp = tmp[val]
            tmp.update({dirname:{}})
        case [size,name]:
            tmp = disk
            for val in tree:
                tmp = tmp[val]
            tmp.update({name:int(size)})

used = (calc_size(disk))

size_to_free = 30000000 - (70000000 - used)

print(size_to_free)

best = 1000000000000000000000000

for val in res2:
    print(val)
    if val >= size_to_free and val < best:
        best = val

print(best)