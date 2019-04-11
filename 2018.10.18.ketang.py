
def ln(x,N=50):
    y=(x-1)/(x+1)
    t=1
    r=0
    p=0
    for n in range(1,N+1):
        r=r+t/(2*n-1)
        t=y**2*t
        p=2*y*r+p
        return p
    x=2.00
    print("%.8f"%p)
        
