showroom = set()

showroom.add("model s")
showroom.add("legacy")
showroom.add("GTR")
showroom.add("tocoma")

print("length of showroom =", len(showroom))

showroom.add("tocoma")

print(showroom)

showroom2 = set(["xterra", "camry"])

showroom.update(showroom2)

showroom.discard("GTR")

junkyard = set(["land cruiser", "cutlass", "explorer", "tocoma", "xterra"])

together = junkyard.intersection(showroom)

print("shared =", together)

print("union =", showroom.union(junkyard))

showroom.discard("xterra")

print("final showrrom =", showroom)