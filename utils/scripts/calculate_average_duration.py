from exceptions import LayerNotFoundException
from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_average_duration():
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
            average_duration = sum(durations) / len(durations)
            QMessageBox.information(
                None,
                "Average drive duration",
                f"Average drive duration is: {average_duration:.2f} minutes",
                QMessageBox.Ok,
            )
        else:
            QMessageBox.warning(
                None, "Error", "There are no values in the layer.", QMessageBox.Ok
            )
    except Exception as e:
        QMessageBox.warning(None, "Error", f"Error occured: {str(e)}", QMessageBox.Ok)
