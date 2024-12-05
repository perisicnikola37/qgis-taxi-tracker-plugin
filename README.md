## QGIS Plugin: Taxi route Analysis

<div style="display: flex; align-items: center;">
    <img src="https://github.com/user-attachments/assets/1228884f-1d2b-4797-b322-9804bc617508" alt="image1" style="height: 200px; margin-right: 10px;">
    <img src="https://github.com/user-attachments/assets/023b5b3e-d21d-420b-b9d9-e623d842a053" alt="image2" style="height: 200px;">
</div>

### Overview

This QGIS plugin enables route data analysis from a layer in QGIS using various metrics such as total distance, duration, average speed, and duration intervals. The plugin loads its configuration from a JSON file (`config.json`), allowing dynamic adjustment of the layer name without the need to modify the code.

### Requirements
- <a href="https://plugins.qgis.org/plugins/ORStools/" target="_blank">ORS tools</a> - The ORS tools plugin for QGIS is essential for integrating with the OpenRouteService API. It enables advanced routing, distance analysis, and other geospatial operations.

API Key Configuration

Once installed, the ORS tools plugin requires an API key to function:

1. Obtain an API key from OpenRouteService.
2. In QGIS, navigate to `Plugins` > `ORS Tools` > `Settings`.
3. Enter your API key in the provided field and save.

### Installation

Download the plugin from the repository. Zip this folder. Attach it as .zip file in QGIS plugin manager.

### Configuration
The plugin uses the config.json file to load its configuration. This file should define the name of the layer containing the route data. For example:

```json
{
 "LAYER_NAME": "Route_history"
}
```

**LAYER_NAME**: The name of the layer in QGIS that contains the route data. Modify this name according to your layer before running the plugin.

### Usage

1. Load Your Route Data Layer:
In QGIS, load the layer containing your route data, such as Distance (in kilometers) and Duration (in minutes).

2. Run the Desired Analysis:
From the plugin's menu, select the analysis you want to perform. For example:
- Calculate Total Duration of all routes.
- Calculate Average Distance of all routes.
- Calculate Average Speed of all routes.
- Calculate Duration Intervals.
- Calculate Total Distance of all routes.

3. View Results:
After running the analysis, the results will be displayed in the form of informational dialogs in QGIS.

### Development
If you would like to contribute to the development of this plugin or have any suggestions, feel free to open an **issue** or **pull request** on GitHub.

### License
This plugin is open-source and uses the MIT license.
