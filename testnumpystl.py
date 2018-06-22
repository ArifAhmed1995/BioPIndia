import os

import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

## Lags a lot for even slightly complex structures.

# Using an existing stl file:
your_mesh = mesh.Mesh.from_file('/home/arif7/Desktop/BIOP/Software/BioPIndia/exampleSTLfiles/Ray.stl')

# Or creating a new mesh (make sure not to overwrite the `mesh` import by
# naming it `mesh`):
VERTICE_COUNT = 100
data = numpy.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
your_mesh = mesh.Mesh(data, remove_empty_areas=False)

# The mesh normals (calculated automatically)
your_mesh.normals
# The mesh vectors
your_mesh.v0, your_mesh.v1, your_mesh.v2
# Accessing individual points (concatenation of v0, v1 and v2 in triplets)
assert (your_mesh.points[0][0:3] == your_mesh.v0[0]).all()
assert (your_mesh.points[0][3:6] == your_mesh.v1[0]).all()
assert (your_mesh.points[0][6:9] == your_mesh.v2[0]).all()
assert (your_mesh.points[1][0:3] == your_mesh.v0[1]).all()

your_mesh.save('new_stl_file.stl')

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

stlfile = os.path.dirname(os.path.abspath(__file__)) + "/exampleSTLfiles/Ray.stl"
your_mesh = mesh.Mesh.from_file(stlfile)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
