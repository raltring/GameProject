from Code.Resources.Ores.Chalcopyrite import Chalcopyrite

if __name__ == '__main__':
    resource = Chalcopyrite(100, is_active = False)
    print(resource._hardness)
    print(resource._content)
