from Code.Resources.Resource import Resource
import Code.IO.ResourceConfigurations as ResConf

class Chalcopyrite(Resource):

    def __init__(self, quantity, is_active = True):
        """
        Class for the creation and maintenance of a resource. Inherits from the Resource class.

        quantity is the total amount of the chalcopyrite ore available.
        is_active is whether or not the resource is currently alive and iteractable (active)
        """
        configuration = ResConf.get_ore_configuration("Chalcopyrite")
        super().__init__(configuration["hardness"], quantity, configuration["content"], is_active)