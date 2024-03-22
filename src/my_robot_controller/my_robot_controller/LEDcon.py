#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class StatusSubscriber(Node):

    def __init__(self):
        super().__init__("LED_Subscriber")
        self.subscriber_=self.create_subscription(Bool, "/led_status", self.status_callback_, 10)


    def status_callback_(self, msg: Bool):
        if msg.data:
            self.get_logger().info("The LED is ON")           
        else:
            self.get_logger().info("The LED is OFF")

def main(args=None):

    rclpy.init(args=args)
    node = StatusSubscriber()
    rclpy.spin(node)
    rclpy.shutdown

if __name__ == '__main__':
    main()
