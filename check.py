#!/usr/bin/env python3

###where l is a list of names
for i in range(0,len(l)):
    try: 
        l[i][1]
        print(l[i][1] + "-" + "okay")
    except IndexError:
        print(l[i][1] + "-" + "fuck")


