def sumn_rec(n):
    if n>0:
        res=n+sumn_rec(n-1)
        return res
    else:
        res=0
        return res
print(sumn_rec(5))

'''def tri_recursion(5):
    result = 5 + def tri_recursion(4):
                      result = 4 + def tri_recursion(3):
                                      result = 3 +def tri_recursion(2):
                                                      result = 2 + def tri_recursion(1):
                                                                         result = 1+def tri_recursion(0):
                                                                                       result = 0
                                                                                       return result
                                                                         return result
                                                      return result
                                      return result
                      return result
    return result
'''