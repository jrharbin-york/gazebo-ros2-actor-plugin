import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from datetime import datetime
import math

class PathPublisher(Node):
    def __init__(self):
        super().__init__('human_path_pub')
        self.pub = self.create_publisher(Path, '/cmd_path', 10)
        self.timer = self.create_timer(1.0, self.publish_path)

    def publish_path(self):
        path_msg = Path()
        path_msg.header.stamp = self.get_clock().now().to_msg()
        path_msg.header.frame_id = 'world'

        num_points = 5
        for i in range(num_points):
            p = PoseStamped()
            p.header = path_msg.header
            p.pose.position.x = 2.0 * i
            p.pose.position.y = 0.0
            p.pose.position.z = 0.0
            p.pose.orientation.x = 0.0
            p.pose.orientation.y = 0.0
            p.pose.orientation.z = 0.0
            p.pose.orientation.w = 1.0
            path_msg.poses.append(p)

        self.pub.publish(path_msg)
        self.get_logger().info(f'Published path with {num_points} points.')

def main(args=None):
    rclpy.init(args=args)
    node = PathPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
