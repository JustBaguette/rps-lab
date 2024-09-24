#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import time



class MyNode(Node):
    def __init__(self):
        super().__init__("Py_test")
        self.counter = 0
        self.get_logger().info("Hello Ros2")
        self.create_timer(0.5,self.callback)
    def callback(self):
        self.counter+=1
        self.get_logger().info("Hello" + str(self.counter))
            

def main(args = None):
    rclpy.init(args=args)
    node = MyNode()
    # node = Node("py_test")
    # node.get_logger().info("Wassup")
    # for i in range(6):
    #     time.sleep(0.5)
    #     node.get_logger().info("Hello ros "+str(i))
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()