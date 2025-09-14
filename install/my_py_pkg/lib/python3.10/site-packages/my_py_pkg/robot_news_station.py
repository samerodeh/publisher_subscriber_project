import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("Robot_News_Station")
        self.robot_name = "C3PO"
        self.publisher_ = self.create_publisher(String, "news", 10)
        self.timer_ = self.create_timer(1.0, self.publish_news)
        self.get_logger().info("Robot News Station is up and running!")


    def publish_news(self):
        msg = String()
        msg.data = "Hi, this is " + self.robot_name + " bringing you the latest news!"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published news: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
