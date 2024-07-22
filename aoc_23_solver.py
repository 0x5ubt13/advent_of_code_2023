#!/usr/bin/python

def solve_day_5():
    maps = {
        "seeds": [],
        "seed_to_soil": [],
        "soil_to_fertilizer": [],
        "fertilizer_to_water": [],
        "water_to_light": [],
        "light_to_temperature": [],
        "temperature_to_humidity": [],
        "humidity_to_location": []
    }
    key = ""
    # seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = False, False, False, False, False, False, False
    with open("Day_05/day_05_test_input.txt", "r") as f:
        for line in f:
            line = line.strip().split(" ")
            print(f"line: {line}")
            if "seeds:" in line:
                maps["seeds"].append(line[1:])
                print(f"maps['seeds']: {maps['seeds']}")
                continue

            if "seed-to-soil" in line:
                key = "seed_to_soil"
                continue
            if "soil-to-fertilizer" in line:
                key = "soil_to_fertilizer"
                continue
            if "fertilizer-to-water" in line:
                key = "fertilizer_to_water"
                continue
            if "water-to-light" in line:
                key = "water_to_light"
                continue
            if "light-to-temperature" in line:
                key = "light_to_temperature"
                continue
            if "temperature-to-humidity" in line:
                key = "temperature_to_humidity"
                continue
            if "humidity-to-location" in line:
                key = "humidity_to_location"
                continue
            if line == [''] or line == '' or key == "":
                continue
            
            print(f"key: {key}")
            maps[key].append(line)


    for k, v in maps.items():
        print("k:", k, "v:", v)

        # match key:
        #     case "seed_to_soil":
        #         maps["key"].append(line)
        #     case "soil_to_fertilizer":
        #         maps["soil_to_fertilizer"].append(line)
        #     case "fertilizer_to_water":
        #         maps["fertilizer_to_water"].append(line)
        #     case "water_to_light":
        #         maps["water_to_light"].append(line)
        #     case "light_to_temperature":
        #         maps["light_to_temperature"].append(line)
        #     case "temperature_to_humidity":
        #         maps["temperature_to_humidity"].append(line)
        #     case "humidity-to-location":
        #         maps["humidity-to-location"].append(line)
        
def main():
    solve_day_5()


if __name__ == '__main__':
    main()