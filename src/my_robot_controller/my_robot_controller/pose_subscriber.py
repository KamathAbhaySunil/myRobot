#!usr/bin/env python3
import rclpy
from rclpy import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber_=self.create_subscription(Pose, "/turtle1/pose",10)
    
    def psoe_callback(self.msg: Pose)

def main(args=None):

    rclpy.init(args=args)




    rclpy.shurdown()