class Resource(object):
    
    def __init__(self, hardness, quantity, content, is_active = True):
        """
        Parent calss for resource objects. Describes the difficulty of extraction, total content at max and remaining of resource, what 
        resource is provided from extraction, and if the item is currently active.

        hardness - describes the difficulty of extraction of resource from the tile
	    quantity - describes the total content of the resource in the tile
        content - dictionary of components of the ore that lists all components and the stoichiometric ratio of the components
	    is_active - boolean value that describes whether any resoure remains and if tile is still active	    
        """
        self._hardness = hardness                    
        self._quantity = quantity                    
        self._remaining = quantity                   
        self._is_active = is_active                  
        self._content = content                      