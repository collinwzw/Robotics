# Histogram implementation of a bayes filter - combines
# convolution and multiplication of distributions, for the
# movement and measurement steps.
# 06_d_histogram_filter
# Claus Brenner, 28 NOV 2012
from pylab import plot, show, ylim
from distribution import *

def move(distribution, delta):
    """Returns a Distribution that has been moved (x-axis) by the amount of
       delta."""
    return Distribution(distribution.offset + delta, distribution.values)



# --->>> Copy your convolve(a, b) and multiply(a, b) functions here.
def multiply(a, b):
    """Multiply two distributions and return the resulting distribution."""

    # --->>> Put your code here.
    difference=a.offset-b.offset
    if difference > 0:
        i=difference
        j=0
    else:
        i=0
        j=-difference
    #print(j)
    #print(b.offset+len(b.values)-i)
    #print(a.offset+len(a.values)-j-1)
    b_value=[]
    for int_b in range(b.offset+i,b.offset+len(b.values)):
        if a.value(int_b) == 0:
            break;
        #print(int_b)
        b_value.append(b.value(int_b))
    #print(b.value(b.offset+i))
    a_value=[]
    for int_a in range(a.offset+j,a.offset+len(a.values)):
        if b.value(int_a) == 0:
            break;
        #print(a.value(a.offset+len(a.values)-j-1))
        #print(int_a)
        a_value.append(a.value(int_a))
    #print(len(b_value))
    #print(len(a_value))

    c_value=[]
    for int_c in range(0,len(a_value)):
        c_value.append(a_value[int_c]*b_value[int_c])
    
    
    c=Distribution(b.offset+i,c_value)
    c.normalize()
    #print(c)
    return c  # Modify this to return your result.

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
    #print(len(b_value))
    k=0
    for o in range(0,j):
        for p in range(0,i):
            #print()
            c_value[k]=a_value[o]*b_value[p]+c_value[k]
            k+=1
            
        k=o+1
        
    c=Distribution(a.offset,c_value)
    c=move(c,b.offset+1)
    return c # Replace this by your own result.

if __name__ == '__main__':
    arena = (0,220)

    # Start position. Exactly known - a unit pulse.
    start_position = 10
    position = Distribution.unit_pulse(start_position)
    plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         linestyle='steps')

    # Movement data.
    controls  =    [ 20 ] * 10

    # Measurement data. Assume (for now) that the measurement data
    # is correct. - This code just builds a cumulative list of the controls,
    # plus the start position.
    p = start_position
    measurements = []
    for c in controls:
        p += c
        measurements.append(p)

    # This is the filter loop.
    for i in range(len(controls)):
        # Move, by convolution. Also termed "prediction".
        control = Distribution.triangle(controls[i], 10)
        position = convolve(position, control)
        plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             color='b', linestyle='steps')

        # Measure, by multiplication. Also termed "correction".
        measurement = Distribution.triangle(measurements[i], 50)
        position = multiply(position, measurement)
        plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             color='r', linestyle='steps')

    show()
