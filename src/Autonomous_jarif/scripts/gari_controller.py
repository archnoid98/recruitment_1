#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from coordinates import coordinates

rospy.init_node('move_turtlebot')


coords = coordinates


pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def move_turtlebot():
    rate = rospy.Rate(10)  
    twist = Twist()

    for coord in coords:
        while not rospy.is_shutdown():
            x_goal, y_goal = coord
            x_current, y_current = rospy.get_param('/odom').pose.pose.position.x, rospy.get_param('/odom').pose.pose.position.y


            linear_vel = 0.2 
            angular_vel = 0.5 

            twist.linear.x = linear_vel
            twist.angular.z = angular_vel


            while abs(x_current - x_goal) > 0.3 or abs(y_current - y_goal) > 0.3:
                pub.publish(twist)
                rate.sleep()

            
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)

            rospy.sleep(1)  

if __name__ == '__main__':
    try:        
        move_turtlebot()

    except rospy.ROSInterruptException:
        
         pass