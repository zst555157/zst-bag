'''from numpy import*
def integrate(f,a,b,n=100):
    x=linspace(a,b,n+1)
    h=x[1]-x[0]
    i=h*(sum(f(x))-0.5*(f(a)+f(b)))
    return i'''



c=[5,10,40,45]
i=c.index(10)
c.append(50)
c.insert(2,20)
def f(c):
    return (9.0/5)*c+32
