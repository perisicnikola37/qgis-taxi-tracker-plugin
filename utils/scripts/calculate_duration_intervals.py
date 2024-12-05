from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from config_loader import LAYER_NAME


def calculate_duration_intervals():
    try:
        target_layer_name = LAYER_NAME

        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise Exception(f"Sloj '{target_layer_name}' nije pronađen.")

        target_layer = layers[0]
        duration_intervals = {0: 0, 30: 0, 60: 0, 120: 0}

        for feature in target_layer.getFeatures():
            duration = feature["Trajanje"]
            if duration is not None:
                if duration <= 30:
                    duration_intervals[0] += 1
                elif duration <= 60:
                    duration_intervals[30] += 1
                elif duration <= 120:
                    duration_intervals[60] += 1
                else:
                    duration_intervals[120] += 1

        result = "\n".join(
            [
                f"Interval {key}-{key+30 if key != 120 else '∞'} minuta: {count} ruta"
                for key, count in duration_intervals.items()
            ]
        )
        QMessageBox.information(None, "Distribucija trajanja", result, QMessageBox.Ok)
    except Exception as e:
        QMessageBox.warning(
            None, "Greška", f"Došlo je do greške: {str(e)}", QMessageBox.Ok
        )
