#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class custo(Node):
    def __init__(self):
        super().__init__("apple")
        self.listen = self.create_subscription(String,"pineapple",self.call_prt,10)
        self.get_logger().info("Listener has started")
    def call_prt(self,msg):
        self.get_logger().info("I have heard "+str(msg.data))

        
def main(args=None):
    rclpy.init(args=args)
    node = custo()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
