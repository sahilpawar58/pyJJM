import json

def combine_geojson(file1, file2, output_file):
    # Load GeoJSON data from the first file
    with open(file1) as f:
        geojson1 = json.load(f)

    # Load GeoJSON data from the second file
    with open(file2) as f:
        geojson2 = json.load(f)

    # Combine features from both files
    combined_features = geojson1['features'] + geojson2['features']
    
    # Create a new GeoJSON object with the combined features
    combined_geojson = {
        "type": "FeatureCollection",
        "features": combined_features
    }

    # Save the combined GeoJSON data to a new file
    with open(output_file, 'w') as f:
        json.dump(combined_geojson, f, indent=2)

# Example usage:
combine_geojson('mh1.geojson', 'mh2.geojson', 'combined_geojson.json')
