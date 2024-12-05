from exceptions import LayerNotFoundException
from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_total_duration():
    try:
        target_layer_name = LAYER_NAME

        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise LayerNotFoundException()

        target_layer = layers[0]
        durations = []

        for feature in target_layer.getFeatures():
            if feature["Trajanje"] is not None:
                durations.append(feature["Trajanje"])

        if durations:
            total_duration_minutes = sum(durations)
            total_duration_hours = total_duration_minutes / 60
            QMessageBox.information(
                None,
                "Total drive duration",
                f"Total drive duration is: {total_duration_hours:.2f} hours",
                QMessageBox.Ok,
            )
        else:
            QMessageBox.warning(
                None, "Error", "Don't have enough data.", QMessageBox.Ok
            )
    except Exception as e:
        QMessageBox.warning(None, "Error", f"Error occured.: {str(e)}", QMessageBox.Ok)
