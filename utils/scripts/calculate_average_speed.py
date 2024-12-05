from exceptions import LayerNotFoundException
from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_average_speed():
    try:
        target_layer_name = LAYER_NAME

        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise LayerNotFoundException()

        target_layer = layers[0]
        speeds = []

        for feature in target_layer.getFeatures():
            distance = feature["Udaljenost"]
            duration = feature["Trajanje"]
            if distance is not None and duration is not None and duration > 0:
                speed = distance / (duration / 60)  # Convert duration to hours
                speeds.append(speed)

        if speeds:
            average_speed = sum(speeds) / len(speeds)
            QMessageBox.information(
                None,
                "Average speed",
                f"Average speed is: {average_speed:.2f} km/h",
                QMessageBox.Ok,
            )
        else:
            QMessageBox.warning(None, "Error", "No data for speed.", QMessageBox.Ok)
    except Exception as e:
        QMessageBox.warning(None, "Error", f"Error occured: {str(e)}", QMessageBox.Ok)
