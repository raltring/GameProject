from game.code.resources.resource import Resource
import game.code.io.resource_configurations as conf

class Ore(Resource):
    """
    Parent class for any ore object in the game.
    """
    def __init__(self, hardness:float, quantity:float, content:dict[str,float], is_active:bool = True):
        super(Ore, self).__init__(hardness, quantity, content, is_active)

class Chalcopyrite(Ore):

    def __init__(self, quantity:float, is_active:bool = True):
        """
        Class for the creation and maintenance of a resource. Inherits from the Ore class.

        quantity is the total amount of the chalcopyrite ore available.
        is_active is whether or not the resource is currently alive and iteractable (active)
        """
        configuration = conf.get_ore_configuration("Chalcopyrite")
        super(Chalcopyrite, self).__init__(configuration["hardness"], quantity, 
                                           configuration["content"], is_active)
        
class Chalcocite(Ore):

    def __init__(self, quantity:float, is_active:bool = True):
        """
        Class for the creation and maintenance of a resource. Inherits from the Ore class.

        quantity is the total amount of the chalcocite ore available.
        is_active is whether or not the resource is currently alive and iteractable (active)
        """
        configuration = conf.get_ore_configuration("Chalcocite")
        super(Chalcocite, self).__init__(configuration["hardness"], quantity, 
                                           configuration["content"], is_active)