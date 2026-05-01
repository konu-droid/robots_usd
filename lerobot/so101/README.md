# using the ros2 packages
place all the folders from the so_101_ros2_package into your src.
then colcon build the workspace.

now launching demo.launch.py should launch everything needed for moveit2

to make a new moveit2 setup use the urdf present in so_arm_100_hardware/simulation/SO101/so101_new_calib.urdf

Please make sure you have all these packages installed for your moveit2 to work.

apt install ros-jazzy-topic-based-ros2-control -y \
    ros-dev-tools \
    ros-jazzy-moveit* \
    ros-jazzy-ros2-control \
    ros-jazzy-ros2-controllers \
    ros-jazzy-gripper-controllers
