import json

# Load the GeoJSON files
with open('maharashtra.geojson') as f:
    maharashtra_data = json.load(f)

with open('combined_geojson.json') as f:
    formatted_mh2_data = json.load(f)

# Iterate through features in maharashtra.geojson
if 'features' in maharashtra_data:
    for maharashtra_feature in maharashtra_data['features']:
        maharashtra_properties = maharashtra_feature.get('properties', {})
        maharashtra_district_name = maharashtra_properties.get('District')
        maharashtra_district_id = maharashtra_properties.get('District_ID')

        # Find matching features in formatted_mh2.geojson
        matching_features = []
        if 'features' in formatted_mh2_data:
            for formatted_mh2_feature in formatted_mh2_data['features']:
                formatted_mh2_properties = formatted_mh2_feature.get('properties', {})
                formatted_mh2_district_name = formatted_mh2_properties.get('DISTRICT')

                # Compare district names
                if maharashtra_district_name.lower() == formatted_mh2_district_name.lower():
                    matching_features.append(formatted_mh2_feature)

        # Print properties for each match
        if matching_features:
            print(f"District: {maharashtra_district_name}, ID: {maharashtra_district_id}")
            for matching_feature in matching_features:
                matching_properties = matching_feature.get('properties', {})
                print(f"{matching_properties['NAME']},", end="")
            print()
        else:
            print(f"No match found for district: {maharashtra_district_name} and {maharashtra_district_id}")
else:
    print("No features found in the GeoJSON file.")
