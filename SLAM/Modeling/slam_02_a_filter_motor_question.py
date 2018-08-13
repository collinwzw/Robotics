# Implement the first move model for the Lego robot.
from math import sin, cos, pi
from pylab import *
from lego_robot import *

# This function takes the old (x, y, heading) pose and the motor ticks
# (ticks_left, ticks_right) and returns the new (x, y, heading).
def filter_step(old_pose, motor_ticks, ticks_to_mm, robot_width):

    # Find out if there is a turn at all.
    if motor_ticks[0] == motor_ticks[1]:
        # No turn. Just drive straight.
        #print(old_pose[0])
        #print(motor_ticks[0])
        
        
        x=old_pose[0]+motor_ticks[0]*ticks_to_mm*math.cos(old_pose[2])
        y=old_pose[1]+motor_ticks[0]*ticks_to_mm*math.sin(old_pose[2])
        theta= old_pose[2]
        
        #print(ticks)
        # --->>> Implement your code to compute x, y, theta here.
        return (x, y, theta)

    else:
        # Turn. Compute alpha, R, etc.
        alpha=(motor_ticks[1]-motor_ticks[0])*ticks_to_mm/robot_width
        radius=motor_ticks[0]*ticks_to_mm/alpha
        x_center=old_pose[0]-(radius+robot_width/2)*math.sin(old_pose[2])
        y_center=old_pose[1]+(radius+robot_width/2)*math.cos(old_pose[2])
        theta=(old_pose[2]+alpha)%(6.2832)
        x=x_center+(radius+robot_width/2)*math.sin(theta)
        y=y_center-(radius+robot_width/2)*math.cos(theta)
        
        #print(else)
        # --->>> Implement your code to compute x, y, theta here.
        return (x, y, theta)

if __name__ == '__main__':
    # Empirically derived conversion from ticks to mm.
    ticks_to_mm = 0.349

    # Measured width of the robot (wheel gauge), in mm.
    robot_width = 150.0

    # Read data.
    logfile = LegoLogfile()
    logfile.read("robot4_motors.txt")

    # Start at origin (0,0), looking along x axis (alpha = 0).
    pose = (0.0, 0.0, 0.0)
    #print(pose[0])
    # Loop over all motor tick records generate filtered position list.
    filtered = []
    for ticks in logfile.motor_ticks:
        pose = filter_step(pose, ticks, ticks_to_mm, robot_width)
        filtered.append(pose)

     #Draw result.
    for pose in filtered:
        print(pose)
        plot([p[0] for p in filtered], [p[1] for p in filtered], 'bo')
    show()
