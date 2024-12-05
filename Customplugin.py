# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Taxi tracker
                                 A QGIS plugin
 Taxi tracker
        begin                : 2024-12-04
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Nikola
        email                : perisicnikola37@gmail.com
 ***************************************************************************/


"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

# utils
from utils import merge_layers
from utils.scripts.calculate_total_duration import calculate_total_duration
from utils.scripts.calculate_average_distance import calculate_average_distance
from utils.scripts.calculate_average_duration import calculate_average_duration
from utils.scripts.calculate_average_speed import calculate_average_speed
from utils.scripts.calculate_duration_intervals import calculate_duration_intervals
from utils.scripts.calculate_total_distance import calculate_total_distance

from .resources import *

from .Customplugin_dialog import CustompluginDialog
import os.path


class Customplugin:
    def __init__(self, iface):
        """Constructor."""
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = os.path.join(
            self.plugin_dir, "i18n", "Customplugin_{}.qm".format(locale)
        )

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        self.actions = []
        self.menu = self.tr("&Customplugin")

        self.first_start = None

    def tr(self, message):
        return QCoreApplication.translate("Customplugin", message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None,
    ):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):
        icon_path_duration = ":/plugins/Customplugin/taxi_icon.png"
        self.add_action(
            icon_path_duration,
            text=self.tr("MERGE"),
            callback=self.merge_layers,
            parent=self.iface.mainWindow(),
        )

        icon_path_duration = ":/plugins/Customplugin/icon.png"
        self.add_action(
            icon_path_duration,
            text=self.tr("Calculate Total Duration"),
            callback=self.calculate_total_duration,
            parent=self.iface.mainWindow(),
        )

        icon_path_duration = ":/plugins/Customplugin/icon.png"
        self.add_action(
            icon_path_duration,
            text=self.tr("Calculate Average Distance"),
            callback=self.calculate_average_distance,
            parent=self.iface.mainWindow(),
        )

        icon_path_duration = ":/plugins/Customplugin/icon.png"
        self.add_action(
            icon_path_duration,
            text=self.tr("Calculate Average Duration"),
            callback=self.calculate_average_duration,
            parent=self.iface.mainWindow(),
        )

        icon_path_duration = ":/plugins/Customplugin/icon.png"
        self.add_action(
            icon_path_duration,
            text=self.tr("Calculate Average Speed"),
            callback=self.calculate_average_speed,
            parent=self.iface.mainWindow(),
        )

        icon_path_duration = ":/plugins/Customplugin/icon.png"
        self.add_action(
            icon_path_duration,
            text=self.tr("Calculate Duration Intervals"),
            callback=self.calculate_duration_intervals,
            parent=self.iface.mainWindow(),
        )

        icon_path_duration = ":/plugins/Customplugin/icon.png"
        self.add_action(
            icon_path_duration,
            text=self.tr("Calculate Total Distance"),
            callback=self.calculate_total_distance,
            parent=self.iface.mainWindow(),
        )

        self.first_start = True

    def merge_layers(self):
        merge_layers()

    def calculate_total_duration(self):
        calculate_total_duration()

    def calculate_average_distance(self):
        calculate_average_distance()

    def calculate_average_duration(self):
        calculate_average_duration()

    def calculate_average_speed(self):
        calculate_average_speed()

    def calculate_duration_intervals(self):
        calculate_duration_intervals()

    def calculate_total_distance(self):
        calculate_total_distance()

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(self.tr("&Customplugin"), action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        if self.first_start == True:
            self.first_start = False
            self.dlg = CustompluginDialog()

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            pass
