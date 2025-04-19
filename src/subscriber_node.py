#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloSubscriber(Node):
    def __init__(self):
        super().__init__("hello_subscriber")
        self.subscription = self.create_subscription(
            String, "hello_topic", self.listener_callback, 10
        )
        self.get_logger().info("Subscriber node has been started")

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')


def main():
    rclpy.init()
    subscriber = HelloSubscriber()

    try:
        rclpy.spin(subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        subscriber.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
