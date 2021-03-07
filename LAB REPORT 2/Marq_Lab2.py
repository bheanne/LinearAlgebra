import numpy as np
import matplotlib.pyplot as plt

Vector1 = np.array([12,30])
Vector2 = np.array([11,21])
Vector3 = np.array([1,4])
Vector4 = np.array([-1,-25])
Vector5 = np.array([-12,-24])

##A Addition & Subtraction
Addition = np.add(Vector1, Vector2)
Subtraction = np.subtract(Vector1, Vector3)
Combi1 = np.subtract(np.add(Vector1, Vector2), Vector3)
print("\n⊹˙⋆°••°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹✭⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°••°⋆˙⊹")
print("\nAdding Vector1 & Vector2 is equal to", Addition)
print("\nSubtracting Vector1 & Vector3 is equal to", Subtraction)
print("\nSubtracting", Addition, "to Vector3 is equal to", Combi1)

##B Multiplication & Division
Multiplication = np.multiply(Vector3, Vector5)
Division = np.divide(Vector3, Vector4)
Combi2 = np.multiply(np.divide(Vector3, Vector4), Vector5)
print("\n⊹˙⋆°••°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹✭⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°••°⋆˙⊹")
print("\nMultiplying Vector3 & Vector5 is equal to", Multiplication)
print("\nDividing Vector3 & Vector4 is equal to", Division)
print("\nDividing", Multiplication, "to Vector5 is equal to", Combi2)

##C Squarring & Square Root
Square = np.square(Vector2)
Square_Root = np.sqrt(Vector2)
Combi3 = np.square(np.sqrt(Vector2))
print("\n⊹˙⋆°••°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹✭⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°••°⋆˙⊹")
print("\nThe Square of Vector2 is", Square)
print("\nThe Square Root of Vector2 is", Square_Root)
print("\nThe Square of the Square Root of Vector2 is", Combi3)

##D Summation
Summation = np.sum(Vector2)
print("\n⊹˙⋆°••°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹✭⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°••°⋆˙⊹")
print("\nThe Summation of Vector2 is", Summation)

##Visualizing the Data
print("\n⊹˙⋆°••°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹✭⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°••°⋆˙⊹")
plt.title("Visualization of the Data")
plt.xlim(-50, 100)
plt.ylim(-50, 100)

##Vectors
plt.scatter(Vector1[0], Vector1[1], label='Vector1', c='red')
plt.scatter(Vector2[0], Vector2[1], label='Vector2', c='orange')
plt.scatter(Vector3[0], Vector3[1], label='Vector3', c='yellow')
plt.scatter(Vector4[0], Vector4[1], label='Vector4', c='greenyellow')
plt.scatter(Vector5[0], Vector5[1], label='Vector5', c='lime')

##Results
plt.scatter(Addition[0], Addition[1], label='Addition', c='aquamarine')
plt.scatter(Subtraction[0], Subtraction[1], label='Subtraction', c='aqua')
plt.scatter(Combi1[0], Combi1[1], label ='Add and Subtract', c='deepskyblue')
plt.scatter(Division[0], Division[1], label='Division', c='blue')
plt.scatter(Multiplication[0], Multiplication[1], label='Multiplication', c='blue')
plt.scatter(Combi2[0], Combi2[1], label='Multiply and Divide', c='darkviolet')
plt.scatter(Square[0], Square[1], label='Square', c='fuchsia')
plt.scatter(Square_Root[0], Square_Root[1], label='Square Root', c='magenta')
plt.scatter(Combi3[0], Combi3[1], label='Square and Square Root', c='deeppink')

##Resultant Vector
plt.quiver(Vector1[0], Vector1[1], Vector2[0], Vector2[1], angles='xy', scale_units='xy', scale=1, color='mistyrose')
plt.quiver(5, 21, Vector4[0], Vector4[1], angles='xy', scale_units='xy', scale=1, color='violet')
Vector6 = Vector2 + Vector4
plt.quiver(Vector3[0], Vector3[1], Vector6[0], Vector6[1], angles='xy', scale_units='xy', scale=1, color='skyblue')

R_mag = np.sqrt(np.sum(Vector1 ** 2 + Vector4 ** 2))  ##Euclidean Distance / Euclidean Norm
rise = Vector6[1]
run = Vector6[0]
slope = rise / run
print('The slope is: ', slope)

plt.grid()
plt.legend()
plt.show()
