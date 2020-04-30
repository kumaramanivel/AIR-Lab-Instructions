#!/usr/bin/env python
import rospy
import random
from turtlesim.msg import *
from turtlesim.srv import *
from geometry_msgs.msg import Twist
from std_srvs.srv import *
import time
from math import *

turtle_x = 0
turtle_y = 0
turtle_theta = 0

def kill_turtle():
    ### This declares a new service named kill. All requests are passed to killTurtle function
    killTurtle = rospy.ServiceProxy('/kill', Kill)
    try:
        ## turtle1 is the name of turtle
        killTurtle("turtle1")
    except:
        pass

def spawn_turtle():
    global turtle_x, turtle_y, turtle_theta


    try:
        # create a service to spawn a new turtle
        spawnTurtle = rospy.ServiceProxy('/spawn', Spawn)

        turtle_x = random.randint(1, 10)
        turtle_y = random.randint(1, 10)
        turtle_theta = random.uniform(-1,1)

        ## Spawn a turtle at random x, y, theta with name turtle1
        spawnTurtle(turtle_x, turtle_y, turtle_theta, "turtle1")
    except:
        pass

def move_turtle():
    ## declares that node is publishing to the '/turtle1/cmd_vel' topic using the message type "Twist".
    turtle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    time.sleep(0.5)

    turtle_twist = Twist()
    turtle_twist.linear.x = 1
    turtle_twist.linear.y = 0
    turtle_twist.linear.z = 0
    turtle_twist.angular.z = random.randint(-1,1)

    ### publishes a Twist message to '/turtle1/cmd_vel' topic.
    turtle_pub.publish(turtle_twist)

def clear_background():
    #to make background empty
    clearStage = rospy.ServiceProxy('/clear', Empty)
    clearStage()

def turtlePose(data):
    # turtlePose function is invoked with the message as the first argument.
    global turtle_x, turtle_y, turtle_theta
    turtle_x = data.x
    turtle_y = data.y
    turtle_theta = data.theta

def distance_between_runner_hunter():

    ### You need to fill in this function
    ### This function calculates the distance between hunter and runner
    ### You also need to find the angle hunter needs to take in order to approach the runner.

    ### If the distance >= 1, you need to update the linear and angular velocities of hunter
    ### If the distance < 1, it means the hunter caught the runner
    ### and you need to kill the runner, clear the background and spawn the runner at a random positon

    pass

#to make publisher and subscriber and call other methods
if __name__ == '__main__':
    try:
        # gives the name of node to rospy
        rospy.init_node('hunterrunner', anonymous=True)

        # This declares that your node subscribes to the "/turtle1/pose" topic which is of type Pose.
        #When new messages are received, turtlePose function is invoked with the message as the first argument.
        rospy.Subscriber("/turtle1/pose", Pose, turtlePose)
        time.sleep(0.5) ## Don't remove sleep

        ### The code below is just to demonstrate what each funtion does.
        ### You need a different flow.
        

        while True:

            print "Enter 1 to kill the turtle \nEnter 2 to spawn the turtle \nEnter 3 to move the turtle \nEnter 4 to clear the background: \n"
            user_input = input()

            if user_input == 1:
                kill_turtle()

            elif user_input == 2:
                spawn_turtle()

            elif user_input == 3:
                move_turtle()

            elif user_input == 4:
                clear_background()


    except rospy.ROSInterruptException:
        print "Exit"
