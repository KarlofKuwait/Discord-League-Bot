"""
Name: Discord Bot - Riot API return values
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 05/06/2019
"""

topchamps = ["Aatrox", "Akali", "Camille", "Cho'Gath", "Darius",
             "Dr. Mundo", "Fiora", "Gangplank", "Garen", "Gnar",
             "Illoai", "Irelia", "Jax", "Jayce", "Kayle",
             "Kennen", "Kled", "Malphite", "Maokai", "Mordekaiser",
             "Nasus", "Neeko", "Olaf", "Ornn", "Pantheon",
             "Poppy", "Pyke", "Quinn", "Renekton", "Rengar",
             "Riven", "Rumble", "Ryze", "Shen", "Singed",
             "Sion", "Sylas", "Tahm Kench", "Teemo", "Tryndamere",
             "Urgot", "Vayne", "Vladimir", "Volibear", "Wukong",
             "Yasuo", "Yorick"]
jngchamps = ["Aatrox", "Ammumu", "Elise", "Evelynn", "Fiddlesticks",
             "Gragas", "Graves", "Hecarim", "Ivern", "Jarvan IV",
             "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred",
             "Lee Sin", "Master Yi", "Nidalee", "Nocturne", "Nunu & Willump"
             "Pantheon", "Rammus", "Rek'Sai", "Rengar", "Sejuani",
             "Shaco", "Shyvana", "Skarner", "Trundle", "Twitch",
             "Udyr", "Vi", "Volibear", "Warwick", "Wukong",
             "Xin Zhao", "Zac"]
midchamps = ["Aatrox", "Ahri", "Akali", "Anivia", "Annie",
             "Azir", "Cassiopeia", "Corki", "Diana", "Ekko",
             "Fizz", "Irelia", "Kassadin", "Katerina", "Leblanc",
             "Lissandra", "Lux", "Malzahar", "Morgana", "Neeko",
             "Orianna", "Pyke", "Ryze", "Swain", "Sylas",
             "Syndra", "Taliyah", "Talon", "Twisted Fate", "Veigar",
             "Vel'Koz", "Viktor", "Vladimir", "Xerath", "Yasuo",
             "Zed", "Ziggs", "Zilean", "Zoe"]
adcchamps = ["Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin",
             "Jinx", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian",
             "Miss Fortune", "Sivir", "Tristana", "Twitch", "Varus",
             "Vayne", "Xayah"]
supchamps = ["Alistar", "Bard", "Blitzcrank", "Brand", "Bruam",
             "Fiddlesticks", "Galio", "Janna", "Karma", "Leona",
             "Lulu", "Lux", "Morgana", "Nami", "Nautilus",
             "Pyke", "Rakan", "Sona", "Soraka", "Taric",
             "Thresh", "Vel'koz", "Xerath", "Yummi", "Zilean",
             "Zyra"
             ]

def findchamp(id):
    if id == 266:
        return "Aatrox"
    if id == 412:
        return "Thresh"
    if id == 23:
        return "Tryndamere"
    if id == 79:
        return "Gragas"
    if id == 69:
        return "Cassiopeia"
    if id == 136:
        return "Aurelion Sol"
    if id == 13:
        return "Ryze"
    if id == 78:
        return "Poppy"
    if id == 14:
        return "Sion"
    if id == 1:
        return "Annie"
    if id == 202:
        return "Jhin"
    if id == 43:
        return "Karma"
    if id == 111:
        return "Nautilus"
    if id == 240:
        return "Kled"
    if id == 99:
        return "Lux"
    if id == 103:
        return "Ahri"
    if id == 2:
        return "Olaf"
    if id == 112:
        return "Viktor"
    if id == 34:
        return "Anivia"
    if id == 27:
        return "Singed"
    if id == 86:
        return "Garen"
    if id == 127:
        return "Lissandra"
    if id == 57:
        return "Maokai"
    if id == 25:
        return "Morgana"
    if id == 28:
        return "Evelynn"
    if id == 105:
        return "Fizz"
    if id == 74:
        return "Heimerdinger"
    if id == 238:
        return "Zed"
    if id == 68:
        return "Rumble"
    if id == 82:
        return "Mordekaiser"
    if id == 37:
        return "Sona"
    if id == 96:
        return "Kog'Maw"
    if id == 55:
        return "Katarina"
    if id == 117:
        return "Lulu"
    if id == 22:
        return "Ashe"
    if id == 30:
        return "Karthus"
    if id == 12:
        return "Alistar"
    if id == 122:
        return "Darius"
    if id == 67:
        return "Vayne"
    if id == 110:
        return "Varus"
    if id == 77:
        return "Udyr"
    if id == 89:
        return "Leona"
    if id == 126:
        return "Jayce"
    if id == 134:
        return "Syndra"
    if id == 80:
        return "Pantheon"
    if id == 92:
        return "Riven"
    if id == 121:
        return "Kha'Zix"
    if id == 42:
        return "Corki"
    if id == 268:
        return "Azir"
    if id == 51:
        return "Caitlyn"
    if id == 76:
        return "Nidalee"
    if id == 85:
        return "Kennen"
    if id == 3:
        return "Galio"
    if id == 45:
        return "Veigar"
    if id == 432:
        return "Bard"
    if id == 150:
        return "Gnar"
    if id == 90:
        return "Malzahar"
    if id == 104:
        return "Graves"
    if id == 254:
        return "Vi"
    if id == 10:
        return "Kayle"
    if id == 39:
        return "Irelia"
    if id == 64:
        return "Lee Sin"
    if id == 420:
        return "Illaoi"
    if id == 60:
        return "Elise"
    if id == 106:
        return "Volibear"
    if id == 20:
        return "Nunu"
    if id == 4:
        return "Twisted Fate"
    if id == 24:
        return "Jax"
    if id == 102:
        return "Shyvana"
    if id == 429:
        return "Kalista"
    if id == 36:
        return "Dr. Mundo"
    if id == 427:
        return "Ivern"
    if id == 131:
        return "Diana"
    if id == 223:
        return "Tahm Kench"
    if id == 63:
        return "Brand"
    if id == 113:
        return "Sejuani"
    if id == 8:
        return "Vladimir"
    if id == 154:
        return "Zac"
    if id == 421:
        return "Rek'Sai"
    if id == 133:
        return "Quinn"
    if id == 84:
        return "Akali"
    if id == 163:
        return "Taliyah"
    if id == 18:
        return "Tristana"
    if id == 120:
        return "Hecarim"
    if id == 15:
        return "Sivir"
    if id == 236:
        return "Lucian"
    if id == 107:
        return "Rengar"
    if id == 19:
        return "Warwick"
    if id == 72:
        return "Skarner"
    if id == 54:
        return "Malphite"
    if id == 157:
        return "Yasuo"
    if id == 101:
        return "Xerath"
    if id == 17:
        return "Teemo"
    if id == 75:
        return "Nasus"
    if id == 58:
        return "Renekton"
    if id == 119:
        return "Draven"
    if id == 35:
        return "Shaco"
    if id == 50:
        return "Swain"
    if id == 91:
        return "Talon"
    if id == 40:
        return "Janna"
    if id == 115:
        return "Ziggs"
    if id == 245:
        return "Ekko"
    if id == 61:
        return "Orianna"
    if id == 114:
        return "Fiora"
    if id == 9:
        return "Fiddlesticks"
    if id == 31:
        return "Cho'Gath"
    if id == 33:
        return "Rammus"
    if id == 7:
        return "LeBlanc"
    if id == 16:
        return "Soraka"
    if id == 26:
        return "Zilean"
    if id == 56:
        return "Nocturne"
    if id == 222:
        return "Jinx"
    if id == 83:
        return "Yorick"
    if id == 6:
        return "Urgot"
    if id == 203:
        return "Kindred"
    if id == 21:
        return "Miss Fortune"
    if id == 62:
        return "Wukong"
    if id == 53:
        return "Blitzcrank"
    if id == 98:
        return "Shen"
    if id == 201:
        return "Braum"
    if id == 5:
        return "Xin Zhao"
    if id == 29:
        return "Twitch"
    if id == 11:
        return "Master Yi"
    if id == 44:
        return "Taric"
    if id == 32:
        return "Amumu"
    if id == 41:
        return "Gangplank"
    if id == 48:
        return "Trundle"
    if id == 38:
        return "Kassadin"
    if id == 161:
        return "Vel'Koz"
    if id == 143:
        return "Zyra"
    if id == 267:
        return "Nami"
    if id == 59:
        return "Jarvan IV"
    if id == 81:
        return "Ezreal"
    if id == 518:
        return "Neeko"
    if id == 350:
        return "Yuumi"
    if id == 517:
        return "Sylas"
    if id == 555:
        return "Pyke"
    if id == 145:
        return "Kai'sa"
    if id == 142:
        return "Zoe"
    if id == 516:
        return "Ornn"
    if id == 141:
        return "Kayn"
    if id == 497:
        return "Rakan"
    if id == 498:
        return "Xayah"
    if id == 164:
        return "Camille"
    if id == 427:
        return "Ivern"
    if id == 240:
        return "Kled"
    if id == 136:
        return "Aurelion Sol"
    if id == 202:
        return "Jhin"
    if id == 420:
        return "Illoai"