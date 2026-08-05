from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description() -> LaunchDescription:
    joint_topic = LaunchConfiguration("joint_topic")
    render_hz = ParameterValue(LaunchConfiguration("render_hz"), value_type=int)

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "joint_topic",
                default_value="xela_joint_publisher",
                description="JointState topic published by hand_controller and consumed by the simulator.",
            ),
            DeclareLaunchArgument(
                "render_hz",
                default_value="60",
                description="MuJoCo viewer render rate (Hz).",
            ),
            Node(
                package="xela_sparshskin_sim",
                executable="hand_controller.py",
                name="hand_controller",
                output="screen",
            ),
            Node(
                package="xela_sparshskin_sim",
                executable="taxel_pertubation.py",
                name="taxel_pertubation",
                output="screen",
            ),
            Node(
                package="xela_sparshskin_sim",
                executable="process_hand_sensors_into_pointcloud",
                name="process_hand_sensors_into_pointcloud",
                output="screen",
                parameters=[
                    {
                        "joint_topic": joint_topic,
                        "render_hz": render_hz,
                    }
                ],
            ),
        ]
    )
