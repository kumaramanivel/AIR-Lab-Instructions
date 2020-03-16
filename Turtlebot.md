# Turtlebot2 instructions
> The page shows the instructions to operate Turtlebot2 platform.

## How to start the robot?
* Turn on the robot using the button on the base of the robot.
* Turn on the laptop.
* Make sure the USB from the robot is connected to the laptop.
* Please ensure that the wireless keyboard belongs to the same laptop that you are using.
* Sign in to your account on the laptop. If you do not have your account, contact the lab administrator.

## Running the robot for the first time.
Before running the robot, you need to run the following commands.
```
$ echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc`
$ echo "export TURTLEBOT_3D_SENSOR=astra" >> ~/.bashrc`
```

Once you run the above commands in the terminal, close the terminal.

## Starting the robot
Open a terminal and write the following command to start the robot.

`roslaunch turtlebot_bringup minimal.launch --screen`

To control the robot using the keyboard (i.e. teleop) write the following command in a new terminal.

`roslaunch turtlebot_teleop keyboard_teleop.launch --screen`

Keep the teleop terminal focused, and use the keys to move the robot.

## Generating a map with the robot
Follow the above two steps to start the robot and also the teleop node. Then run the following commands to generate a map.

The below command starts the gmapping node.

`roslaunch turtlebot_navigation gmapping_demo.launch --screen`

Now, run the following command to start 'rviz' visualization tool.

`roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`

Now teleop the robot while focusing the teleop node terminal.

While you are moving the robot around, the map will be incrementally built. Once you have the map of the required area, run the following command to save the map.

`rosrun map_server map_saver -f ~/mapName`

The map will be saved in your home directory with the name of the map you specified in the above command. Close all the ROS terminals.


## Navigating the robot using the generated map
Again, run the below command to start the robot.

`roslaunch turtlebot_bringup minimal.launch --screen`

To navigate the robot, run the following commands.

`roslaunch turtlebot_navigation amcl_demo.launch map_file:=~/mapName.yaml`

Then run the following command to start the 'rviz' visualization tool.

`roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`

Then use the 2D Pose estimate button to give an initial pose of the robot. Now, using the 2D Navigation goal button you can give a goal to the robot and the robot will autonomously navigate to the 2D coordinate.

Once you are done working with the turtlebot, turn it off and also turn off the laptop.
