from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsWkbTypes
import datetime
from PyQt5.QtWidgets import QMessageBox


def merge_layers(target_layer_name="Istorija_ruta"):
    try:
        project = QgsProject.instance()
        layers = project.mapLayersByName(target_layer_name)

        if not layers:
            raise Exception(f"Sloj '{target_layer_name}' nije pronađen.")

        target_layer = layers[0]
        layers_to_merge = [
            layer
            for layer in project.mapLayers().values()
            if layer.type() == QgsVectorLayer.VectorLayer
            and layer.geometryType() == QgsWkbTypes.LineGeometry
            and layer.name() != target_layer_name
        ]

        if not layers_to_merge:
            print("Nema novih slojeva za dodavanje.")
        else:
            target_layer.startEditing()

            for layer in layers_to_merge:
                print(f"Spajam sloj: {layer.name()}")

                for feature in layer.getFeatures():
                    new_feature = QgsFeature(target_layer.fields())
                    new_feature.setGeometry(feature.geometry())

                    if (
                        "DIST_KM" in feature.fields().names()
                        and "Udaljenost" in target_layer.fields().names()
                    ):
                        new_feature["Udaljenost"] = feature["DIST_KM"]

                    if (
                        "DURATION_H" in feature.fields().names()
                        and "Trajanje" in target_layer.fields().names()
                    ):
                        duration_in_hours = feature["DURATION_H"]
                        duration_in_minutes = duration_in_hours * 60
                        new_feature["Trajanje"] = duration_in_minutes

                    if "Taksi_ID" in target_layer.fields().names():
                        new_feature["Taksi_ID"] = (
                            f"Taksi_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                        )

                    target_layer.addFeature(new_feature)

                QgsProject.instance().removeMapLayer(layer)

            target_layer.commitChanges()
            print("Svi novi slojevi su spojeni u sloj 'Istorija_Ruta'.")
    except Exception as e:
        QMessageBox.warning(
            None, "Greška", f"Došlo je do greške: {str(e)}", QMessageBox.Ok
        )
