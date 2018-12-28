# @class_declaration interna_gd_versionesdoc #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_versionesdoc(modelos.mtd_gd_versionesdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_versionesdoc #
class flcolagedo_gd_versionesdoc(interna_gd_versionesdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_versionesdoc #
class gd_versionesdoc(flcolagedo_gd_versionesdoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_versionesdoc_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
