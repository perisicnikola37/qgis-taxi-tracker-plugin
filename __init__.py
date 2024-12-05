# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Taxi tracker plugin
        begin                : 2024-12-04
        copyright            : (C) 2024 by Nikola
        email                : perisicnikola37@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface):  # pylint: disable=invalid-name
    """Load Customplugin class from file Customplugin."""
    from .Customplugin import Customplugin

    return Customplugin(iface)
