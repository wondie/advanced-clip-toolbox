import arcpy
import os
# Set the raster files
raster = arcpy.GetParameterAsText(0)

# Set the shapefiles folder as the current workspace
arcpy.env.workspace  = arcpy.GetParameterAsText(1)

# Output Directory
out_directory = arcpy.GetParameterAsText(2)

if not os.path.isdir(out_directory):
    os.mkdir(out_directory)


shapefiles = arcpy.ListFeatureClasses()

for shapefile in shapefiles:
    arcpy.AddMessage("Clipping " + raster + " with " + shapefile + ".shp")

    desc = arcpy.Describe(shapefile)
    extent = desc.extent
    output_path = os.path.join(
        out_directory, '{}_{}'.format(
            shapefile.replace('.shp', ''),
            os.path.basename(raster)
        )
    )

    arcpy.Clip_management(
        raster, str(extent), output_path,
        shapefile, "#",
        "ClippingGeometry", "NO_MAINTAIN_EXTENT")
