#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        # Lista de waypoints (x, y)
        self.waypoints = [
            (0.5, 0.0),
            (0.5, 0.5),
            (0.0, 0.5),
            (0.0, 0.0)
        ]
        
        self.current_wp = 0  # índice do waypoint atual
        self.robot_x, self.robot_y = 0.0, 0.0  # posição simulada
        self.speed = 0.1  # velocidade linear (m/s)

        self.timer = self.create_timer(0.1, self.navigate)

    def navigate(self):
        if self.current_wp >= len(self.waypoints):
            self.stop_robot()
            self.get_logger().info('✅ Todos os waypoints foram percorridos!')
            return

        target_x, target_y = self.waypoints[self.current_wp]
        dx = target_x - self.robot_x
        dy = target_y - self.robot_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < 0.05:
            self.get_logger().info(f'📍 Chegou ao waypoint {self.current_wp + 1}: ({target_x:.2f}, {target_y:.2f})')
            self.current_wp += 1
            time.sleep(1)
            return

        angle = math.atan2(dy, dx)
        self.robot_x += self.speed * math.cos(angle) * 0.1
        self.robot_y += self.speed * math.sin(angle) * 0.1

        msg = Twist()
        msg.linear.x = self.speed
        msg.angular.z = 0.0
        self.publisher.publish(msg)

    def stop_robot(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = WaypointNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
