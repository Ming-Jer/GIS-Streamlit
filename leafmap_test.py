import leafmap

m = leafmap.Map(center=[40, -100], zoom=4)
#cities = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
#regions = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson"
cities = "data/worldcities.csv"
regions ="data/world-administrative-boundaries.geojson"

m.add_geojson(regions, layer_name="World Regions")
m.add_points_from_xy(
    cities,
    x="lng",
    y="lat",
    color_column="region",
    icon_names=["gear", "map", "leaf", "globe"],
    spin=True,
    add_legend=True,
)