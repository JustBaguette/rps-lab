#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class custo(Node):
    def __init__(self):
        super().__init__("papaya")
        self.pusher = self.create_publisher(String,"pineapple",10)
        self.timer=self.create_timer(1,self.call_push)
        self.get_logger().info("Radio has started")
        self.i = "Fruits are great"
    def call_push(self):
        push = String()
        push.data = self.i
        self.pusher.publish(push)
        self.get_logger().info("The radio has sent "+str(push.data))




        

def main(args=None):
    rclpy.init(args=args)
    node = custo()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
