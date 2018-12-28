# @class_declaration interna_gd_secuencias #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_secuencias(modelos.mtd_gd_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_secuencias #
class flcolagedo_gd_secuencias(interna_gd_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_secuencias #
class gd_secuencias(flcolagedo_gd_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_secuencias_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
