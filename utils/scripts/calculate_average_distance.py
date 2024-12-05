from exceptions import LayerNotFoundException
from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_average_distance():
    try:
        target_layer_name = LAYER_NAME

        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise LayerNotFoundException()

        target_layer = layers[0]
        distances = []

        for feature in target_layer.getFeatures():
            if feature["Udaljenost"] is not None:
                distances.append(feature["Udaljenost"])

        if distances:
            average_distance = sum(distances) / len(distances)
            QMessageBox.information(
                None,
                "Average distance",
                f"Average distance is: {average_distance:.2f} km",
                QMessageBox.Ok,
            )
        else:
            QMessageBox.warning(
                None,
                "Error",
                "Missing data for distance in layer.",
                QMessageBox.Ok,
            )
    except Exception as e:
        QMessageBox.warning(None, "Error", f"Error occured: {str(e)}", QMessageBox.Ok)
