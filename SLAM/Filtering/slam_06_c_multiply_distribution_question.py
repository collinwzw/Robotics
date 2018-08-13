# Multiply a distribution by another distribution.
# 06_c_multiply_distribution
# Claus Brenner, 26 NOV 2012
from pylab import plot, show
from distribution import *

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


if __name__ == '__main__':
    arena = (0,1000)

    # Here is our assumed position. Plotted in blue.
    position_value = 400
    position_error = 100
    position = Distribution.triangle(position_value, position_error)
    plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         color='b', linestyle='steps')

    # Here is our measurement. Plotted in green.
    # That is what we read from the instrument.
    measured_value = 550
    measurement_error = 200
    measurement = Distribution.triangle(measured_value, measurement_error)
    plot(measurement.plotlists(*arena)[0], measurement.plotlists(*arena)[1],
         color='g', linestyle='steps')

    # Now, we integrate our sensor measurement. Result is plotted in red.
    position_after_measurement = multiply(position, measurement)
    plot(position_after_measurement.plotlists(*arena)[0],
         position_after_measurement.plotlists(*arena)[1],
         color='r', linestyle='steps')

    show()
