# @class_declaration interna_gd_conexiones #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_conexiones(modelos.mtd_gd_conexiones, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_conexiones #
class flcolagedo_gd_conexiones(interna_gd_conexiones, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_conexiones #
class gd_conexiones(flcolagedo_gd_conexiones, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_conexiones_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
