# @class_declaration interna_gd_camposplantilla #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_camposplantilla(modelos.mtd_gd_camposplantilla, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_camposplantilla #
class flcolagedo_gd_camposplantilla(interna_gd_camposplantilla, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_camposplantilla #
class gd_camposplantilla(flcolagedo_gd_camposplantilla, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_camposplantilla_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
