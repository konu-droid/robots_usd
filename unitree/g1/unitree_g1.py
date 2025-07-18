# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for Unitree robots.

The following configurations are available:

* :obj:`G1_HANDS_CFG`: G1 humanoid robot with inspire hands

Reference: https://github.com/unitreerobotics/unitree_ros
"""

import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetMLPCfg, DCMotorCfg, ImplicitActuatorCfg, IdealPDActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR

G1_HANDS_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        # usd_path=f"/home/konu/Documents/upwork/humanoid_imitation_metasoul/HOVER/neural_wbc/isaac_lab_wrapper/neural_wbc/isaac_lab_wrapper/isaaclab_asset/g1_hands/g1_hands.usd",
        usd_path=f"/home/konu/Documents/upwork/humanoid_imitation_metasoul/HOVER/neural_wbc/isaac_lab_wrapper/neural_wbc/isaac_lab_wrapper/isaaclab_asset/g1_29dof_rev_1_0_with_inspire_hand_DFQ.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.0005,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.74),
        joint_pos={".*": 0.0},
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_hip_yaw_joint",
                ".*_hip_roll_joint",
                ".*_hip_pitch_joint",
                ".*_knee_joint",
                "waist.*joint"
            ],
            effort_limit=300,
            velocity_limit=100.0,
            stiffness={
                ".*_hip_yaw_joint": 150.0,
                ".*_hip_roll_joint": 150.0,
                ".*_hip_pitch_joint": 200.0,
                ".*_knee_joint": 200.0,
                "waist.*joint": 200.0,
            },
            damping={
                ".*_hip_yaw_joint": 5.0,
                ".*_hip_roll_joint": 5.0,
                ".*_hip_pitch_joint": 5.0,
                ".*_knee_joint": 5.0,
                "waist.*joint": 5.0,
            },
        ),
        "feet": ImplicitActuatorCfg(
            effort_limit=20.0,
            joint_names_expr=[".*_ankle_pitch_joint", ".*_ankle_roll_joint"],
            stiffness=20.0,
            damping=2.0,
        ),
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_shoulder_pitch_joint",
                ".*_shoulder_roll_joint",
                ".*_shoulder_yaw_joint",
                ".*_elbow_joint",
                ".*_elbow_roll_joint",
                ".*_wrist_pitch_joint",
                ".*_wrist_roll_joint",
                ".*_wrist_yaw_joint",
            ],
            effort_limit=10.0,
            velocity_limit=10.0,
            stiffness=40.0,
            damping=10.0,
        ),
        "hands": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_index_proximal_joint",
                ".*_index_intermediate_joint",
                ".*_middle_proximal_joint",
                ".*_middle_intermediate_joint",
                ".*_ring_proximal_joint",
                ".*_ring_intermediate_joint",
                ".*_pinky_proximal_joint",
                ".*_pinky_intermediate_joint",
                ".*_thumb_proximal_yaw_joint",
                ".*_thumb_proximal_pitch_joint",
                ".*_thumb_intermediate_joint",
                ".*_thumb_distal_joint",
            ],
            effort_limit=0.5,
            velocity_limit=10.0,
            stiffness=3.0,
            damping=0.1,
            friction=0.01,
            
        ),
    },
)
"""Configuration for the Unitree G1 Humanoid robot."""
