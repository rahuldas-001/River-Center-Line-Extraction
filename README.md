# River-Center-Line-Extraction

This project provides a Python-based solution to extract the centerline of meandering or single channel river geometry, from shapefile data. The code uses libraries such as `GeoPandas`, `Shapely`, `rasterio`, and `skimage` to compute and visualize the centerline using skeletonization techniques.

## Requirements

To run this project, you need the following Python packages:

- `geopandas`
- `shapely`
- `rasterio`
- `numpy`
- `matplotlib`
- `skimage`

**How It Works**
**Load Shapefile**: The script reads a polygon shapefile (.shp) containing river geometries.
**Convert Polygons to Raster**: The polygons are rasterized with a specified pixel size.
**Skeletonization**: Skeletonization extracts the centerline from the rasterized polygons.
**Post-Processing**: The skeletonized lines are converted back to geographic coordinates.
**Visualization**: The original river geometry and the computed centerline are visualized using Matplotlib, and the centerline is saved as a new shapefile.

**Important Notes**:  The code works best for single-channel or meandering river channel geometries. The code's capability to process complex channel meandering rivers is in progress. 



**Example Output** : 

The following is an example of the extraction and visualization of the Buridihing River in Assam, India centerline visualization:  The original river geometry is shown in blue, while the extracted centerline is in yellow.


![image](https://github.com/user-attachments/assets/a9cfe107-4af3-498d-a2ca-21116ab97959)
![image](https://github.com/user-attachments/assets/e56b25cd-242f-44dd-93cf-52e29232d13c)





