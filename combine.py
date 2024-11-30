import xml.etree.ElementTree as ET
from datetime import datetime
import os

def combine_tcx_files(input_folder, output_folder):
    """
    Combines all TCX files in the input folder into a single TCX file and saves it in the output folder.

    Args:
        input_folder (str): Path to the folder containing input TCX files.
        output_folder (str): Path to the folder where the combined TCX file will be saved.
    """
    # Get list of TCX files in the input folder
    input_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".tcx")]
    
    if not input_files:
        raise ValueError("No TCX files found in the input folder.")

    # Parse the first file to use as the base
    base_tree = ET.parse(input_files[0])
    base_root = base_tree.getroot()

    # Define namespaces
    namespaces = {
        "tcx": "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"
    }

    # Find the Activities element in the base file
    activities = base_root.find("tcx:Activities", namespaces)

    if activities is None:
        raise ValueError("The base TCX file does not contain an <Activities> element.")

    # Append activities from other files
    for file in input_files[1:]:
        tree = ET.parse(file)
        root = tree.getroot()
        file_activities = root.find("tcx:Activities", namespaces)

        if file_activities is not None:
            for activity in file_activities:
                activities.append(activity)

    # Update the creation time for the combined file (optional)
    metadata = base_root.find("tcx:Metadata", namespaces)
    if metadata is not None:
        creation_time = metadata.find("tcx:Time", namespaces)
        if creation_time is not None:
            creation_time.text = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Write the combined file to disk
    output_file = os.path.join(output_folder, "combined_workout.tcx")
    base_tree.write(output_file, encoding="utf-8", xml_declaration=True)
    return output_file

# Example usage
if __name__ == "__main__":
    input_folder = "inputs"  # Replace with your input folder path
    output_folder = "output"  # Replace with your output folder path

    try:
        output_file = combine_tcx_files(input_folder, output_folder)
        print(f"Combined TCX file saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
