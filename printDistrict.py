import json

# Load the GeoJSON files
with open('combined_geojson.json') as f:
    formatted_mh2_data = json.load(f)

matching_features = set()
if 'features' in formatted_mh2_data:
    for formatted_mh2_feature in formatted_mh2_data['features']:
        formatted_mh2_properties = formatted_mh2_feature.get('properties', {})
        formatted_mh2_district_name = formatted_mh2_properties.get('DISTRICT')
        matching_features.add(formatted_mh2_district_name)

for i in matching_features:
    print(i)