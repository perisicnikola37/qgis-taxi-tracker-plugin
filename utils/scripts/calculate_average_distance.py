from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_average_distance():
    try:
        target_layer_name = LAYER_NAME

        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise Exception(f"Sloj '{target_layer_name}' nije pronađen.")

        target_layer = layers[0]
        distances = []

        for feature in target_layer.getFeatures():
            if feature["Udaljenost"] is not None:
                distances.append(feature["Udaljenost"])

        if distances:
            average_distance = sum(distances) / len(distances)
            QMessageBox.information(
                None,
                "Prosječna kilometraža",
                f"Prosječna kilometraža je: {average_distance:.2f} km",
                QMessageBox.Ok,
            )
        else:
            QMessageBox.warning(
                None,
                "Greška",
                "Nema vrijednosti za udaljenost u sloju.",
                QMessageBox.Ok,
            )
    except Exception as e:
        QMessageBox.warning(
            None, "Greška", f"Došlo je do greške: {str(e)}", QMessageBox.Ok
        )
