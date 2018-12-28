# @class_declaration interna_gd_documentostablamod #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_documentostablamod(modelos.mtd_gd_documentostablamod, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_documentostablamod #
class flcolagedo_gd_documentostablamod(interna_gd_documentostablamod, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_documentostablamod #
class gd_documentostablamod(flcolagedo_gd_documentostablamod, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_documentostablamod_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
