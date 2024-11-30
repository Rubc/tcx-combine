# TCX Combine Script

This Python script combines multiple TCX (Training Center XML) files from a specified input folder into a single TCX file. The resulting combined file is saved in a designated output folder.

## Features
- Combines all TCX files in the `inputs` folder.
- Preserves the structure and integrity of the TCX data.
- Updates the metadata creation time in the combined TCX file.
- Outputs the combined file to the `output` folder.

## Requirements
- Python 3.6 or later

## Setup
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install Python if it is not already installed.
3. Ensure you have the required input TCX files in the `inputs` folder.

## Usage
1. Place the TCX files you want to combine in the `inputs` folder.
2. Run the script:
   ```bash
   python combine_tcx_files.py
   ```
3. The combined TCX file will be saved in the `output` folder as `combined_workout.tcx`.

## Folder Structure
- `inputs/`: Folder for the TCX files to be combined.
- `output/`: Folder where the combined TCX file will be saved.

## Example
To combine multiple workout files:
1. Place `workout1.tcx`, `workout2.tcx`, and other TCX files in the `inputs/` folder.
2. Run the script:
   ```bash
   python combine_tcx_files.py
   ```
3. The combined file will appear in the `output/` folder:
   ```
   output/combined_workout.tcx
   ```