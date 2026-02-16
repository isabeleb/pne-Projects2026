temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

average_temperature = sum(temperatures) / len(temperatures)

day_count = 0
for t in temperatures:
    if t > 17:
        day_count += 1

print("-Temperature on Wednesday:", temperatures[2])

print("-Maximum temperature:", max(temperatures))

print("-Minimum temperature:", min(temperatures))

print("-Average temperature:" , round(average_temperature, 1))

print("-Days above 17:" , day_count)

print("-Temperatures from lowest to highest:", sorted(temperatures) )
