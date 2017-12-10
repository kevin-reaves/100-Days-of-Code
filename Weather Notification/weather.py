from weather import Weather

weather = Weather()

lookup = weather.lookup(36081)
condition = lookup.condition()

print(condition.text())