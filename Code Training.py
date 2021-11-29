#!/usr/bin/env python
# coding: utf-8

# ### Code Training

# In[ ]:


v = []
w = []
e = []
r = []
q = []
l = []
def add(v, w):
    for t in range(0, 10):
        if len(v) < 10:
            t = int(input("Enter Number for First vector: "))
            v.append(t)
            print("Write \"next\" if you want to jump to the next vector or \"no\" to Continue")
            u = input()
            if u == 'next':
                print(v)
                for i in range(0, 10):
                    i = int(input("Enter Number for Second vector: "))
                    w.append(i)  
                    print("To End Say \"stop\" or \"no\" to Continue")
                    p = input()
                    if p == 'stop':
                        print(w)
                        if len(v) == len(w):
                            for f in range(len(v)):
                                z = v[f] + w[f]
                                e.append(z)
                            print(e)
                            m = int(input("Write Another Number: "))
                            for c in range(len(v)):
                                b = m * v[c]
                                n = m * w[c]
                                r.append(b)
                                q.append(n)
                                
                            for o in range(len(v)):
                                O = v[o] * w[o]
                                l.append(O)
                            print("Scalar Product of First Vector" + str(r))
                            print("Scalar Product of Second Vector" + str(q))
                            print("Dot Product " + str(sum(l)))
                            break   
                        elif len(v) != len(w):
                                print("Please Be Sure That The Two vectors Have The Same Length")
       
add(v ,w)

