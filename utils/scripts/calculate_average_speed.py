from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_average_speed():
    try:
        target_layer_name = LAYER_NAME

        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise Exception(f"Sloj '{target_layer_name}' nije pronađen.")

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
                "Prosječna brzina",
                f"Prosječna brzina je: {average_speed:.2f} km/h",
                QMessageBox.Ok,
            )
        else:
            QMessageBox.warning(
                None, "Greška", "Nema podataka za brzinu.", QMessageBox.Ok
            )
    except Exception as e:
        QMessageBox.warning(
            None, "Greška", f"Došlo je do greške: {str(e)}", QMessageBox.Ok
        )
