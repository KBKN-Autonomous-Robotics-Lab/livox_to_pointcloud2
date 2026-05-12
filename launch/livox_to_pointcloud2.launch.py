from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    # 共通
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Lidar1（既存）
    livox_custom_topic_1 = LaunchConfiguration('livox_custom_topic_1')
    livox_pcloud_topic_1 = LaunchConfiguration('livox_pcloud_topic_1')

    # Lidar2（新規）
    livox_custom_topic_2 = LaunchConfiguration('livox_custom_topic_2')
    livox_pcloud_topic_2 = LaunchConfiguration('livox_pcloud_topic_2')

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use simulation time'
    )

    livox_custom_topic_arg_1 = DeclareLaunchArgument(
        'livox_custom_topic_1', default_value='/livox/lidar',
        description='Custom LiDAR topic (lidar1)'
    )
    livox_pcloud_topic_arg_1 = DeclareLaunchArgument(
        'livox_pcloud_topic_1', default_value='/converted_pointcloud2',
        description='Pointcloud2 topic (lidar1)'
    )

    livox_custom_topic_arg_2 = DeclareLaunchArgument(
        'livox_custom_topic_2', default_value='/livox/lidar2',
        description='Custom LiDAR topic (lidar2)'
    )
    livox_pcloud_topic_arg_2 = DeclareLaunchArgument(
        'livox_pcloud_topic_2', default_value='/converted_pointcloud2_lidar2',
        description='Pointcloud2 topic (lidar2)'
    )

    livox_to_pointcloud2_node_1 = Node(
        package='livox_to_pointcloud2',
        executable='livox_to_pointcloud2_node',
        name='livox_to_pointcloud2_lidar1',
        parameters=[{
            'use_sim_time': use_sim_time,
            'sub_topic': livox_custom_topic_1,
            'pub_topic': livox_pcloud_topic_1
        }],
        output='screen'
    )

    livox_to_pointcloud2_node_2 = Node(
        package='livox_to_pointcloud2',
        executable='livox_to_pointcloud2_node',
        name='livox_to_pointcloud2_lidar2',
        parameters=[{
            'use_sim_time': use_sim_time,
            'sub_topic': livox_custom_topic_2,
            'pub_topic': livox_pcloud_topic_2
        }],
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(use_sim_time_arg)
    ld.add_action(livox_custom_topic_arg_1)
    ld.add_action(livox_pcloud_topic_arg_1)
    ld.add_action(livox_custom_topic_arg_2)
    ld.add_action(livox_pcloud_topic_arg_2)
    ld.add_action(livox_to_pointcloud2_node_1)
    ld.add_action(livox_to_pointcloud2_node_2)

    return ld
