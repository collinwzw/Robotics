# Instead of moving a distribution, move (and modify) it using a convolution.
# 06_b_convolve_distribution
# Claus Brenner, 26 NOV 2012
from pylab import plot, show, ylim
from distribution import *

def move(distribution, delta):
    """Returns a Distribution that has been moved (x-axis) by the amount of
       delta."""
    return Distribution(distribution.offset + delta, distribution.values)

def convolve(a, b):
    """Convolve distribution a and b and return the resulting new distribution."""
    
    i=0
    b_value=[]
    while b.value(b.offset+i) != 0:
        b_value.append(b.value(b.offset+i))
        i=i+1
    #print(b_value)
    # --->>> Put your code here.
    #print(a.start)
    #print(a.__repr__)
    #print(a.stop)
    #print(a.value(0))
    j=0
    a_value=[]
    while a.value(a.offset+j) != 0:
        #print(a.value(a.offset+i))
        a_value.append(a.value(a.offset+j))
        j+=1
    c_size=len(a_value)+(len(b_value))-1
    c_value=[0] * int(c_size)
    
    k=0
    for o in range(0,j):
        for p in range(0,i):
            
            c_value[k]=a_value[o]*b_value[p]+c_value[k]
            k+=1
            
        k=o+1
        
    c=Distribution(a.offset,c_value)
    c=move(c,b.offset+1)
    return c # Replace this by your own result.


if __name__ == '__main__':
    arena = (0,1000)

    # Move 3 times by 20.
    moves = [20] * 50

    # Start with a known position: probability 1.0 at position 10.
    position = Distribution.unit_pulse(10)
    plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         linestyle='steps')

    # Now move and plot.
    for m in moves:
        move_distribution = Distribution.triangle(m, 2)
        position = convolve(position, move_distribution)
        plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             linestyle='steps')

    ylim(0.0, 1.1)
    show()
