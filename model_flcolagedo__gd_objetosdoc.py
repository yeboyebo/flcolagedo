# @class_declaration interna_gd_objetosdoc #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_objetosdoc(modelos.mtd_gd_objetosdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_objetosdoc #
class flcolagedo_gd_objetosdoc(interna_gd_objetosdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_objetosdoc #
class gd_objetosdoc(flcolagedo_gd_objetosdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_objetosdoc_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
