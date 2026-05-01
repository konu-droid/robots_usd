# 🤖 robots_usd 🚀

Welcome to the **robots_usd** repository! This collection contains a variety of custom **Universal Scene Description (USD)** files designed specifically for use in **NVIDIA Isaac Sim** and **Isaac Lab**. 

Whether you are building complex robotic simulations or training RL agents, these models provide high-fidelity representations of mobile and manipulator robots, many of which come with ROS2 integration for seamless control.

---

## 🛠️ How to Use

Getting your robots into the simulation is simple:

1. **Clone the Repository**: Download the assets to your local machine.
2. **Open Isaac Sim/Lab**: Launch NVIDIA Isaac Sim or Isaac Lab.
3. **Load the Model**: 
   - Navigate to the `robots_usd` folder.
   - Drag and drop the desired `.usd` file directly into your scene, or use `File` $\rightarrow$ `Open`.
4. **Initialize**: Configure your physics, joints, and controllers within the Isaac Sim environment.

---

## 🤖 Available Robot Models

Here are the robot models available in this repository. Each model is provided as a `.usd` file for universal compatibility.

### 🐻 Hyperspawn
- **Model**: [`dropbear.usd`](hyperspawn/dropbear.usd)
- ![Dropbear](images/dropbear.png)

### 🦾 Kuka
- **Model**: [`kuka_w_hand.usd`](kuka/kuka_w_hand.usd)
- ![Kuka](images/kuka.png)

### 🐢 Leatherback
- **Model**: [`leatherback.usd`](leatherback/leatherback.usd)
- ![Leatherback](images/leatherback.png)

### 🤖 LeRobot
- **Models**: 
  - [`SO_ARM100.usd`](lerobot/so100/SO_ARM100.usd) (Standard)
  - [`SO_ARM100_ROS2.usd`](lerobot/so100/SO_ARM100_ROS2.usd) (Integrated with ROS2 nodes)
  - [`SO_ARM100_CAMERA_ROS2.usd`](lerobot/so100/SO_ARM100_CAMERA_ROS2.usd) (Camera + ROS2 integration)
  - [`so101.usd`](lerobot/so101/so101.usd) (Updated variant)
- ![LeRobot](images/lerobot.png)

### 📱 Pal Robotics (Tiago)
- **Models**:
  - [`tiago_omni.usd`](pal/tiago/tiago_omni.usd) (Omnidirectional base)
  - [`tiago_omni_ros2.usd`](pal/tiago/tiago_omni_ros2.usd) (Omni base with ROS2)
  - [`tiago_moveit2.usd`](pal/tiago/tiago_moveit2.usd) (Configured for MoveIt2)
  - [`tiago_pmb2.usd`](pal/tiago/tiago_pmb2.usd) (PMB2 variant)
  - [`tiago_pro.usd`](pal/tiago_pro/tiago_pro.usd) (Professional version)
- ![Tiago](images/tiago.png)

### 🖐️ Unitree
- **Model**: [`g1_hands.usd`](unitree/g1/g1_hands/g1_hands.usd)
- ![Unitree G1](images/unitree_g1.png)

---

## 📦 Additional Assets

Beyond the robots, we provide several utility assets to help you build your simulation environments.

### 🏠 Environment Objects
- `Mug.usd` ☕
- `cube.usd` 🧊
- `thor_table.usd` 🪑
- `brick.usd` 🧱
- ![Assets](images/assets.png)

### ⚙️ Component Assets
- **LeRobot Components**: `Female_Buckle.usd`, `Male_Buckle.usd`, `Male_Buckle_Simple.usd`, `Male_Buckle_deformable.usd` (Used for fine-tuning LeRobot assembly).

---

*Happy Simulating!* 🚀
