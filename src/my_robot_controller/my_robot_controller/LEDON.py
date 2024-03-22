#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class LEDPubNode(Node):
    def __init__(self):
        super().__init__("LED_Publisher")
        self.publisher_ = self.create_publisher(Bool, 'led_status', 10)
        self.timer = self.create_timer(0.5, self.run_input_loop)
        self.get_logger().info('LED controller node Initialized')
        

    def publish_led_state(self, state):
        msg = Bool()
        msg.data = state
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing LED Status: {state}')

    def run_input_loop(self):
        self.get_logger().info('Type N and enter to switch the LED on \n Type F and enter to switch the LED off')
        while (1):
            user_input = input('Enter command:')
            if user_input == 'n':
                self.publish_led_state(True)
            elif user_input == 'f':
                self.publish_led_state(False)
            elif user_input == 'c':
                self.get_logger().info('Node is closing')
                self.destroy_node()
                rclpy.shutdown()
            else :
                break





def main(args=None):
    rclpy.init(args=args)
    node = LEDPubNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()