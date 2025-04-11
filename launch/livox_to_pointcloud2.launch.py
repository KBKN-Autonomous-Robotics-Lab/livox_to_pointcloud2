from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')
    livox_custom_topic = LaunchConfiguration('livox_custom_topic')
    livox_pcloud_topic = LaunchConfiguration('livox_pcloud_topic')

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use simulation time'
    )
    livox_custom_topic_arg = DeclareLaunchArgument(
        'livox_custom_topic', default_value='/livox/lidar',
        description='Custom LiDAR topic'
    )
    livox_pcloud_topic_arg = DeclareLaunchArgument(
        'livox_pcloud_topic', default_value='/converted_pointcloud2',
        description='Pointcloud2 topic'
    )

    # livox to pointcloud2
    livox_to_pointcloud2_node = Node(
        package='livox_to_pointcloud2',
        executable='livox_to_pointcloud2_node',
        parameters=[{
            'use_sim_time': use_sim_time,
            'sub_topic': livox_custom_topic,
            'pub_topic': livox_pcloud_topic
        }],
        output='screen'
    )
    
    ld = LaunchDescription()
    ld.add_action(use_sim_time_arg)
    ld.add_action(livox_custom_topic_arg)
    ld.add_action(livox_pcloud_topic_arg)
    ld.add_action(livox_to_pointcloud2_node)

    return ld

