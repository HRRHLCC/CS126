class Spacecraft:
    def __init__(self, name, fuel_level):
        self._name = name
        self._fuel_level = fuel_level  
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name
        else:
            print("invalid str")
    
    name = property(get_name, set_name)

    def get_fuel_level(self):
        return self._fuel_level
    
    def set_fuel_level(self, fuel):
        if isinstance(fuel, (int, float)) and fuel >= 0:
            self._fuel_level = fuel
        else:
            print("invalid int")
    
    fuel_level = property(get_fuel_level, set_fuel_level)

    def display_status(self):
        print(f"Spacecraft '{self._name}' has {self._fuel_level}% fuel left.")