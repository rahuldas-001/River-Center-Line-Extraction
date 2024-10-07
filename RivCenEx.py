# -*- coding: utf-8 -*-
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Polygon
from skimage.morphology import medial_axis
from skimage import measure
import numpy as np
import rasterio
from rasterio.features import rasterize
from rasterio.transform import from_origin
import os 

os.chdir("D:/AIRBMP/Paper related work/Subansiri/River Centerline Example")


# Function to rasterize polygon
def polygon_to_raster(polygon, pixel_size=1):
    minx, miny, maxx, maxy = polygon.bounds
    width = int((maxx - minx) / pixel_size)
    height = int((maxy - miny) / pixel_size)
    
    transform = from_origin(minx, maxy, pixel_size, pixel_size)
    
    # Create an empty raster
    raster = np.zeros((height, width), dtype=np.uint8)
    
    # Rasterize the polygon
    shapes = [(polygon, 1)]
    raster = rasterize(shapes, out_shape=raster.shape, transform=transform, fill=0)
    
    return raster, transform

# Function to compute centerline using medial axis transformation
def polygon_centerline(polygon):
    # Rasterize the polygon
    raster, transform = polygon_to_raster(polygon)
    
    # Compute the medial axis (centerline)
    skeleton = medial_axis(raster)
    
    # Get coordinates of the skeleton
    contours = measure.find_contours(skeleton, 0.5)
    
    # Convert the skeletonized raster back to lines in real-world coordinates
    lines = []
    for contour in contours:
        coords = [(transform * (coord[1], coord[0])) for coord in contour]
        line = LineString(coords)
        lines.append(line)
    
    return lines

# Read polygon shapefile and visualize
def visualize_centerline(shapefile_path, output_path):
    # Load the shapefile
    gdf = gpd.read_file(shapefile_path)
    
    # Compute centerlines
    centerlines = []
    for polygon in gdf.geometry:
        if isinstance(polygon, Polygon):
            lines = polygon_centerline(polygon)
            centerlines.extend(lines)
    
    # Create a GeoDataFrame with the centerlines
    centerline_gdf = gpd.GeoDataFrame(geometry=centerlines, crs=gdf.crs)
    
    # Save centerlines to a new shapefile
    centerline_gdf.to_file(output_path, driver='ESRI Shapefile')
    print(f"Centerline shapefile saved to {output_path}")
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, color='blue', edgecolor='k', alpha=0.5, label='Original Polygons')
    centerline_gdf.plot(ax=ax, color='red', linestyle='--', linewidth=2, label='Centerlines')
    plt.title('Polygon Centerlines Visualization')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()

# Example usage
shapefile_path = "Buridihing.shp"  # Replace with your shapefile path
output_path = "Buridihing_centerline_shapefile.shp"  # Replace with desired output path
visualize_centerline(shapefile_path, output_path)

