from exceptions import LayerNotFoundException
from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_total_distance():
    try:
        target_layer_name = LAYER_NAME

        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise LayerNotFoundException()

        target_layer = layers[0]

        total_distance = sum(
            [
                feature["Udaljenost"]
                for feature in target_layer.getFeatures()
                if feature["Udaljenost"] is not None
            ]
        )

        QMessageBox.information(
            None,
            "Total drive distance",
            f"Total drive distance is: {total_distance:.2f} km",
            QMessageBox.Ok,
        )

    except Exception as e:
        QMessageBox.warning(None, "Error", f"Error occured: {str(e)}", QMessageBox.Ok)
