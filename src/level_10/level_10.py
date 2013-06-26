'''
Created on 2013-4-12

@author: nan
'''

def run():
    marris = look_and_say(3)
    for i in range(31):
        member = marris.next()
        print member
        if i == 30:
            print len(member)
    pass

def look_and_say(member):
    print 'entering look_and_say'
    memberList = list(str(member))
    nextMemberList = [member]
    
    while(1):
        yield member
        memberList = list(str(member))
        nextMemberList = []
        count = 1
        a = 0
        for i in range(len(str(member))):
            if (len(str(member)) > 1)and (i != len(str(member)) - 1):
                if (memberList[i] == memberList[i + 1]):
                    count += 1
                    continue
            a = memberList[i]
            nextMemberList.append(str(count))
            nextMemberList.append(a)
            count = 1
        
        member = "".join(nextMemberList)

def better1():
    import itertools
    
    def compress(g):
        for key, subgenerator in itertools.groupby(g):
            yield len(list(subgenerator))
            yield key
    
    def mk_recurse_n(f, n):
        def inner(g):
            for i in range(n):
                g = f(g)
            return g
        return inner
    
    g = mk_recurse_n(compress, 30)([1])
    a = list(g)
    print len(a)

def better2():
    import re
    def describe(s):
        return "".join([str(len(m.group(0))) + m.group(1)
                        for m in re.finditer(r"(\d)\1*", s)])
    s = "1"
    for dummy in range(30):
        s = describe(s)
    print len(s)  # prints 5808

def better3():
    import re
    def describe(s):
        sets = re.findall("(1+|2+|3+)", s)  # like "111", "2", ...
        return "".join([str(len(x)) + x[0] for x in sets])
