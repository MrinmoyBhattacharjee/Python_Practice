def recur(p):
    if p==0:
        print("##")
    else:
        recur(p)
        p=p-1
recur(5)