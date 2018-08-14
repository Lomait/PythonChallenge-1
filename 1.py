
# coding: utf-8

# In[1]:

l1=['Iraq', 'Japan', 'Australia', 'Egypt', 'Turkey']
l2=['Sydney', 'Istanbul', 'Tokyo', 'Baghdad', 'Cairo']
l3=[]
for i in l1:
    for k in l2:       
        if i=='Iraq' and k=='Baghdad':
            l3.append([i, k])
        elif i=='Japan' and k=='Tokyo':
            l3.append([i, k])
        elif i=='Australia' and k=='Sydney':
            l3.append([i, k])
        elif i=='Egypt' and k=='Cairo':
            l3.append([i, k])
        elif i=='Turkey' and k=='Istanbul':
            l3.append([i, k])
            print l3


# In[ ]:



