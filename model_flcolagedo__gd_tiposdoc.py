# @class_declaration interna_gd_tiposdoc #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_tiposdoc(modelos.mtd_gd_tiposdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_tiposdoc #
class flcolagedo_gd_tiposdoc(interna_gd_tiposdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_tiposdoc #
class gd_tiposdoc(flcolagedo_gd_tiposdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_tiposdoc_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
