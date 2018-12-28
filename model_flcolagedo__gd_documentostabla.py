# @class_declaration interna_gd_documentostabla #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_documentostabla(modelos.mtd_gd_documentostabla, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_documentostabla #
class flcolagedo_gd_documentostabla(interna_gd_documentostabla, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_documentostabla #
class gd_documentostabla(flcolagedo_gd_documentostabla, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_documentostabla_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
