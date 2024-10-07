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
**Skeletonization**: Skeletonization is applied to extract the centerline from the rasterized polygons.
**Post-Processing**: The skeletonized lines are converted back to geographic coordinates.
**Visualization**: The original river geometry and the computed centerline are visualized using matplotlib, and the centerline is saved as a new shapefile.

**Important Notes**
**Multichannel Rivers:** The code handles multichannel rivers by converting MultiPolygon geometries into individual Polygon geometries.
**Aspect Ratio:** The aspect ratio of the plot is set to be equal for better visualization.
**Pixel Size: ** The pixel size used in rasterization may need adjustment to balance processing time and accuracy.

Example Output
The following is an example of the centerline visualization:  The original river geometry is shown in blue, while the extracted centerline is in yellow.
