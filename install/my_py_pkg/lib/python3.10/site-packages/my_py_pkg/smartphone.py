import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("smartphone")
        self.subscriber = self.create_subscription(
            String, "news", self.callback_robot_news, 10
        )

    def callback_robot_news(self, msg: String):
        self.get_logger().info(f"Robot news received: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
