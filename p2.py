from numpy import *
'''
def pathlength(x,y,n):
    sum_length=0
    for i in range(0,n+1):
        sum_length+=sqrt(pow(x[i]-x[i-1],2)+pow(y[i]-y[i-1],2))

    return sum_length

n=int(input('请输入：'))
tetha=linspace(0,2*pi,n+1)
x,y=1/2*cos(tetha),1/2*sin(tetha)
print(pathlength(x,y,n))
'''
from matplotlib.pyplot import *
from matplotlib.animation import FuncAnimation
'''
#import matplotlib.animation FunAnimation as FA
g=981  #cm/s^2
s=7.9e-4 #N/cm
p=1 #g/cm^3
h=5000  #cm
#tanh
fig=figure(figsize=[12,8])
axis([0,510,0,400])
def c(x):
    return sqrt((g*x)*(1+4*s*pi**2/(p*g*x**2))*tanh(2*pi*h/x)/(2*pi))

x=linspace(1,500,500)
y=c(x)

def update(frames):
    xl,yl=x[:frames%500],y[:frames%500]
    plot(xl,yl,'.')

animation=FuncAnimation(fig,update,interval=1)
show()
'''
str_line="""Other notes A simple mathematical formula characterizes
the other notes on the chromatic scale They are divided equally on a
logarithmic base 2 scale there are twelve notes on the chromatic scale
and we get the i th note above a given note by multiplying its frequency
by the i12th power of 2 In other words the frequency of each note in the
chromatic scale is precisely the frequency of the previous note in the scale
multiplied by the twelfth root of two This information suffices to create
music For example to play the tune Frere Jacques we just need to play each
of the notes A B C A by producing sine waves of theappropriate frequency
for about half a second each and then repeat the pattern"""
#print(sum([len(i) for i in str_line.split()])+len(str_line.split()))
#x=linspace(0,5,100)

#from ODESolver import *

def MC(f,a,b,n=10000):
    x=linspace(a,b,n+1)
    return (b-a)/(n+1)*sum(f(x))

f=lambda x:e**(-x**2)
a,b=eval(input('数:'))


print(MC(f,a,b))


#2/sqrt(pi)



























