from game.code.resources.ores import Chalcocite, Chalcopyrite

if __name__ == '__main__':
    resource = Chalcopyrite(100, is_active = False)
    print(resource._hardness)
    print(resource._content)
    resource = Chalcocite(100, is_active = False)
    print(resource._hardness)
    print(resource._content)