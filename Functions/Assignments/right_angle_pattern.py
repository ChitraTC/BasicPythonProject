def pattern(r):       #pattern(3)
    if r==0:          #r!=0
        return
    else:
        pattern(r-1)  #pattern(3-1)     pattern(2)
        print("* "*r)                   #2!=0
                                        #pattern(2-1)         pattern(1)
                                                              #1!=0
r=int(input("Enter the num of rows: "))                       #pattern(1-1)      pattern(0)
pattern(r)                                                                       #0==0
                                                                                 #return to caller fun
#                                                              print("* "*1)
#                                        *                      *
#                                        * *
#                       *
#                       * *
#                       * * *
#