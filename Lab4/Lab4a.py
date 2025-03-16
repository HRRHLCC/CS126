from spacecraft import Spacecraft

ship1 = Spacecraft("Explorer I", 75)
ship2 = Spacecraft("Galaxy Cruiser", 50)
ship3 = Spacecraft("Star Chaser", 90)

ship1.display_status()
ship2.display_status()
ship3.display_status()

ship1.fuel_level = 65
ship2.name = "Nebula Voyager"
ship3.fuel_level = 20

print("\nUpdated Spacecraft Statuses:")
ship1.display_status()
ship2.display_status()
ship3.display_status()