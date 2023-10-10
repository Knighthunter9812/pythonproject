"""d1={}
#d2={"harry":"burger","skullf":"fish"}
#print(d2["harry"])
d3={"harry":"f","me":"12","shub":{"b":"n","nbv":"vfg"}}#dictionary inside dictionary
print(d3["shub"])
d3["ank"]="junk"#add the item
print(d3)
#d4=d3#now d4  will only point to d3 means any changes in d3 will reflect in d4 also
del d3["me"]#delete the item
print(d3)
d4=d3.copy()
d3.update({"rat":"mouse"})
print(d3.keys())
print(d3.items())
"""
d={}
key=input("enter item:")
value=input("enter value:")
d[key]=value
print(d)