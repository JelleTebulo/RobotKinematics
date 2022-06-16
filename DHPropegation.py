from MyLibraries import *

# Project: Coding Denavit-Hartenberg Tables Using Python - Cartesian Robot
# Author: Addison Sears-Collins
# Date created: August 21, 2020

# theta is the angle from x(n-1) to x(n) around z(n-1)
# alpha is the angle from z(n-1) to z(n) around x(n)
# r or a is the distance between the origin of the n-1 frame and the origin of the n frame along the x(n) direction
# d is the distance from x(n-1) to x(n) along the z(n-1) direction.

# Link lengths in centimeters
a1 = 1  # Length of link 1
a2 = 1  # Length of link 2
a3 = 1  # Length of link 3
a4 = 1  # Length of link 4
a5 = 1  # Length of link 5
a6 = 1  # Length of link 6

# Initialize values for the displacements
d1 = 1  # Displacement of link 1

# Initialize values for the joint angles (degrees)
theta_1 = 0  # Joint 1
theta_2 = 0  # Joint 2
theta_3 = 0  # Joint 3
theta_4 = 0  # Joint 4
theta_5 = 0  # Joint 5
theta_6 = 0  # Joint 5

# Declare the Denavit-Hartenberg table.
# It will have four columns, to represent:
# theta, alpha, r, and d
# We have the convert angles to radians.
d_h_table = np.array([[np.deg2rad(theta_1)    , np.deg2rad(-90), a2 , a1],
                      [np.deg2rad(theta_2-90) , np.deg2rad(180), a3 , 0],
                      [np.deg2rad(theta_3+180), np.deg2rad(90) , -a4, 0],
                      [np.deg2rad(theta_4)    , np.deg2rad(-90), 0  , -a5],
                      [np.deg2rad(theta_5)    , np.deg2rad(90) , 0  , 0],
                      [np.deg2rad(theta_6+180), np.deg2rad(180), 0  , -a6]])

# Homogeneous transformation matrix from frame 0 to frame 1
i = 0
homgen_0_1 = np.array([[np.cos(d_h_table[i, 0]), -np.sin(d_h_table[i, 0]) * np.cos(d_h_table[i, 1]),
                        np.sin(d_h_table[i, 0]) * np.sin(d_h_table[i, 1]), d_h_table[i, 2] * np.cos(d_h_table[i, 0])],
                       [np.sin(d_h_table[i, 0]), np.cos(d_h_table[i, 0]) * np.cos(d_h_table[i, 1]),
                        -np.cos(d_h_table[i, 0]) * np.sin(d_h_table[i, 1]), d_h_table[i, 2] * np.sin(d_h_table[i, 0])],
                       [0, np.sin(d_h_table[i, 1]), np.cos(d_h_table[i, 1]), d_h_table[i, 3]],
                       [0, 0, 0, 1]])

# Homogeneous transformation matrix from frame 1 to frame 2
i = 1
homgen_1_2 = np.array([[np.cos(d_h_table[i, 0]), -np.sin(d_h_table[i, 0]) * np.cos(d_h_table[i, 1]),
                        np.sin(d_h_table[i, 0]) * np.sin(d_h_table[i, 1]), d_h_table[i, 2] * np.cos(d_h_table[i, 0])],
                       [np.sin(d_h_table[i, 0]), np.cos(d_h_table[i, 0]) * np.cos(d_h_table[i, 1]),
                        -np.cos(d_h_table[i, 0]) * np.sin(d_h_table[i, 1]), d_h_table[i, 2] * np.sin(d_h_table[i, 0])],
                       [0, np.sin(d_h_table[i, 1]), np.cos(d_h_table[i, 1]), d_h_table[i, 3]],
                       [0, 0, 0, 1]])

# Homogeneous transformation matrix from frame 2 to frame 3
i = 2
homgen_2_3 = np.array([[np.cos(d_h_table[i, 0]), -np.sin(d_h_table[i, 0]) * np.cos(d_h_table[i, 1]),
                        np.sin(d_h_table[i, 0]) * np.sin(d_h_table[i, 1]), d_h_table[i, 2] * np.cos(d_h_table[i, 0])],
                       [np.sin(d_h_table[i, 0]), np.cos(d_h_table[i, 0]) * np.cos(d_h_table[i, 1]),
                        -np.cos(d_h_table[i, 0]) * np.sin(d_h_table[i, 1]), d_h_table[i, 2] * np.sin(d_h_table[i, 0])],
                       [0, np.sin(d_h_table[i, 1]), np.cos(d_h_table[i, 1]), d_h_table[i, 3]],
                       [0, 0, 0, 1]])

homgen_0_3 = homgen_0_1 @ homgen_1_2 @ homgen_2_3

# Print the homogeneous transformation matrices
print("Homogeneous Matrix Frame 0 to Frame 1:")
print(homgen_0_1)
print()
print("Homogeneous Matrix Frame 1 to Frame 2:")
print(homgen_1_2)
print()
print("Homogeneous Matrix Frame 2 to Frame 3:")
print(homgen_2_3)
print()
print("Homogeneous Matrix Frame 0 to Frame 3:")
print(homgen_0_3)
print()