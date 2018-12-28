# @class_declaration interna_gd_documentos #
import importlib

from YBUTILS.viewREST import helpers

from models.flcolagedo import models as modelos


class interna_gd_documentos(modelos.mtd_gd_documentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flcolagedo_gd_documentos #
class flcolagedo_gd_documentos(interna_gd_documentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gd_documentos #
class gd_documentos(flcolagedo_gd_documentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcolagedo.gd_documentos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
