#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStation : public rclcpp::Node
{
public:
    RobotNewsStation() : Node("robot_news_station")
    {
        publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&RobotNewsStation::publish_news, this)
        );
        RCLCPP_INFO(this->get_logger(), "Robot News Station Node has been started.");
    }
private:
    void publish_news()
    {
        auto message = example_interfaces::msg::String();
        message.data = "Breaking News: Robot News Station is operational!";
        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
        publisher_->publish(message);
    }
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStation>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}