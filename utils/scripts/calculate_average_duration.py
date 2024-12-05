from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_average_duration():
    try:
        target_layer_name = LAYER_NAME

        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise Exception(f"Sloj '{target_layer_name}' nije pronađen.")

        target_layer = layers[0]
        durations = []

        for feature in target_layer.getFeatures():
            if feature["Trajanje"] is not None:
                durations.append(feature["Trajanje"])

        if durations:
            average_duration = sum(durations) / len(durations)
            QMessageBox.information(
                None,
                "Prosječno trajanje vožnji",
                f"Prosječno trajanje vožnji je: {average_duration:.2f} minuta",
                QMessageBox.Ok,
            )
        else:
            QMessageBox.warning(
                None, "Greška", "Nema vrednosti za trajanje u sloju.", QMessageBox.Ok
            )
    except Exception as e:
        QMessageBox.warning(
            None, "Greška", f"Došlo je do greške: {str(e)}", QMessageBox.Ok
        )
