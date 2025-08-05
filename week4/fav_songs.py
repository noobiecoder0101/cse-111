# fav_songs = ["daylight", "billie jean", "the rain"]
# fav_songs.append("from the start")
# del fav_songs[0]
# for songs in fav_songs:
#     print(f"now playing: {songs}")

#dictionaries study

elements = {
    "hydrogen": {
        "molarmass": 1.008,
        "symbol": "H"
    },
    "helium": {
        "molarmass": 4.0026,
        "symbol": "He"
    },
    "carbon": {
        "molarmass": 12.011,
        "symbol": "C"
    },
    "oxygen": {
        "molarmass": 15.999,
        "symbol": "O"
    },
    "nitrogen": {
        "molarmass": 14.007,
        "symbol": "N"
    }
}

print(elements ["hydrogen"])

elements["oxygen"] = {
    "molarmass" : 16.00,
    "symbol" : "O",
    "catchphrase": "breathe"
}

elements["oxygen"]["molarmass"] = 16.09
del elements["oxygen"]["catchphrase"]

for name, data in elements.items:
    # print(f"Element: {name}")
    # for key, value in data.items():
    #     print (f"{key}: {value}")