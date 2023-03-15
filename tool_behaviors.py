#!/usr/bin/env python

# /**
#  * @file tool_behaviors.py
#  * @author Samay
#  * @brief 
#  * @version 1.0
#  * @date 2023-06-03
#  * 
#  * @copyright Copyright (c) 2022
#  * 
#  */

import os
import time
import rospy
from niryo_robot_python_ros_wrapper import *


if __name__ == '__main__':
	rospy.init_node('ned2_behavior')
	niryo_robot = NiryoRosWrapper()
	niryo_robot.calibrate_auto()


	sensor_data_path = "/media/niryo/<device>/dataset/2Tool_2Objects_dataset/"

	robot_name = 'ned2'

	tools = ['metalspoon', 'plasticspoon']
	contents = ['wheat', 'chickpea']

	tool = tools[int(input(f'[INTERACTIVE]. Select one of the following tools:\n1. {tools[0]}\n2. {tools[1]}\n* Choice : '))-1]
	content = contents[int(input(f'[INTERACTIVE]. Select one of the following contents:\n1. {contents[0]}\n2. {contents[1]}\n* Choice : '))-1]

	sensor_data_path += robot_name + '_' + tool + '/' + content + '/'

	trial_num = len(os.listdir(sensor_data_path))

	sensor_data_path += f'trial-{trial_num}' + '_' + str(time.time()) + '/'

	tools_x = {'metal-spoon': 0.044, 'plastic-spoon': 0.064}
	tools_y = {'metal-spoon': -0.048, 'plastic-spoon': -0.048}
	tools_z = {'metal-spoon': 0.66, 'plastic-spoon': 0.66}

	tool_x = tools_x[tool]
	tool_y = tools_y[tool]
	tool_z = tools_z[tool]

	data_issue_flag = False

	behavior_name = '1-look'

	look_behavior(sensor_data_path + behavior_name + '/', tool_x, tool_y, tool_z, 1.0)
	rospy.sleep(2.0)
	data_issue_flag = check_data(sensor_data_path + behavior_name + '/')

	behavior_name = '2-stirring-slow'
	stirring_behavior_1(sensor_data_path + behavior_name + '/', tool_x, tool_y, tool_z, 1.0)
	rospy.sleep(2.0)
	data_issue_flag = check_data(sensor_data_path + behavior_name + '/')

	behavior_name = '3-stirring-fast'
	stirring_behavior_2(sensor_data_path + behavior_name + '/', tool_x, tool_y, tool_z, 1.0)
	rospy.sleep(2.0)
	data_issue_flag = check_data(sensor_data_path + behavior_name + '/')

	behavior_name = '4-stirring-twist'
	stirring_behavior_3(sensor_data_path + behavior_name + '/', tool_x, tool_y, tool_z, 1.0)
	rospy.sleep(2.0)
	data_issue_flag = check_data(sensor_data_path + behavior_name + '/')

	behavior_name = '5-whisk'
	stirring_behavior_4(sensor_data_path + behavior_name + '/', tool_x, tool_y, tool_z, 1.0)
	rospy.sleep(2.0)
	data_issue_flag = check_data(sensor_data_path + behavior_name + '/')

	behavior_name = '6-poke'
	stirring_behavior_5(sensor_data_path + behavior_name + '/', tool_x, tool_y, tool_z, 1.0)
	rospy.sleep(2.0)
	data_issue_flag = check_data(sensor_data_path + behavior_name + '/')

	####################
	# Open the gripper
	####################

	delete_trial(sensor_data_path + behavior_name + '/')
