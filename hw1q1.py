#Write a code (Python, Java, C++, or MATLAB) that does the following: (50 points)
#Asks the user to enter unit lattice for an element with a cubic crystal structure. (5 pts)
#Asks the user if the structure is body centered or face centered. (5 pts)
#Displays a 3-D crystal structure of the unit cell, including locations of the atoms in the crystal and labels the lattice constant. (20 pts)
#Then asks the user to choose a family of planes; e.g. (100), (110), or (111) and identifies the planes in
#the 3-D crystal structure. (20 pts)
#You should submit the code and a printout of the output for a given input from the user.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def get_unit_cell():
    #user inputs for lattice constsnt & structure
    lattice_constant = float(input("Enter the lattice constant : "))
    structure_type = input("Is the structure body centered (BCC) or face centered (FCC)? ").strip().upper()
    return lattice_constant, structure_type

def plot_unit_cell(ax, lattice_constant, structure_type):
    # Define the unit cell vertices
    vertices = lattice_constant * np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1],
                                            [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]])
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='b')
    
    # Plot the edges
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6), (4, 7), (5, 7), (6, 7)]
    for edge in edges:
        ax.plot(*zip(vertices[edge[0]], vertices[edge[1]]), color='k')
    
    # Plot additional atoms for BCC or FCC
    if structure_type == 'BCC':
        ax.scatter([lattice_constant / 2], [lattice_constant / 2], [lattice_constant / 2], color='r')
    elif structure_type == 'FCC':
        fcc_atoms = lattice_constant * np.array([[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0], [1, 0.5, 0.5],
                                                 [0.5, 1, 0.5], [0.5, 0.5, 1]])
        ax.scatter(fcc_atoms[:, 0], fcc_atoms[:, 1], fcc_atoms[:, 2], color='r')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'{structure_type} Unit Cell with Lattice Constant {lattice_constant} Å')

def identify_planes(ax, lattice_constant, family_of_planes):
    if family_of_planes == '100':
        for i in range(2):
            ax.plot_surface(np.array([[i, i], [i, i]]) * lattice_constant,
                            np.array([[0, 1], [0, 1]]) * lattice_constant,
                            np.array([[0, 0], [1, 1]]) * lattice_constant, color='g', alpha=0.3)
    elif family_of_planes == '110':
        for i in range(2):
            ax.plot_surface(np.array([[0, 1], [0, 1]]) * lattice_constant,
                            np.array([[i, i], [i, i]]) * lattice_constant,
                            np.array([[0, 0], [1, 1]]) * lattice_constant, color='g', alpha=0.3)
    elif family_of_planes == '111':
        x = np.array([[0, 1], [0, 1]]) * lattice_constant
        y = np.array([[0, 0], [1, 1]]) * lattice_constant
        z = np.array([[0, 1], [1, 0]]) * lattice_constant
        ax.plot_surface(x, y, z, color='g', alpha=0.3)                  

def main():
    lattice_constant, structure_type = get_unit_cell()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_unit_cell(ax, lattice_constant, structure_type)
    plt.show()
    
    family_of_planes = input("Choose a family of planes (e.g., 100, 110, 111): ").strip()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_unit_cell(ax, lattice_constant, structure_type)
    identify_planes(ax, lattice_constant, family_of_planes)
    plt.show()

if __name__ == "__main__":
    main()
