#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time


class HelloPublisher(Node):
    def __init__(self):
        super().__init__("hello_publisher")
        self.publisher = self.create_publisher(String, "hello_topic", 10)
        self.timer = self.create_timer(5.0, self.publish_message)
        self.get_logger().info("Publisher node has been started")

    def publish_message(self):
        msg = String()
        msg.data = "Hello World"
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')


def main():
    rclpy.init()
    publisher = HelloPublisher()

    try:
        rclpy.spin(publisher)
    except KeyboardInterrupt:
        pass
    finally:
        publisher.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
