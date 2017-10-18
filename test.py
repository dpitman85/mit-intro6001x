def general_poly(L):
    def pow(x):
        sum = 0
        L.reverse()
        for i in range(len(L)):
            sum += L[i]*(x**i) 
        return sum
    return pow
    
    
print(general_poly([1, 2, 3, 4])(10))