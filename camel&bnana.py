a=3000                     #total bananas
l=1000
s=0
while(a>l):
    n=(a/l)*2-1            #no. of trips
    x=l//n                 #distance of check post trips
    s=s+x                  #storing no of bananas consumed
    a=a-l                  #next load of banana
kmleft=a-s
bananasneeded=kmleft
bananasleft=a-bananasneeded
print(bananasleft)