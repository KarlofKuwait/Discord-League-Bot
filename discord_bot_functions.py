"""
Name: Discord Bot Functions - Riot API return values
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 07/06/2019
"""
TOP_CHAMPS = ["Aatrox", "Akali", "Camille", "Cho'Gath", "Darius",
              "Dr. Mundo", "Fiora", "Gangplank", "Garen", "Gnar",
              "Illoai", "Irelia", "Jax", "Jayce", "Kayle",
              "Kennen", "Kled", "Malphite", "Maokai", "Mordekaiser",
              "Nasus", "Neeko", "Olaf", "Ornn", "Pantheon",
              "Poppy", "Pyke", "Quinn", "Renekton", "Rengar",
              "Riven", "Rumble", "Ryze", "Shen", "Singed",
              "Sion", "Sylas", "Tahm Kench", "Teemo", "Tryndamere",
              "Urgot", "Vayne", "Vladimir", "Volibear", "Wukong",
              "Yasuo", "Yorick"]
JNG_CHAMPS = ["Aatrox", "Ammumu", "Elise", "Evelynn", "Fiddlesticks",
              "Gragas", "Graves", "Hecarim", "Ivern", "Jarvan IV",
              "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred",
              "Lee Sin", "Master Yi", "Nidalee", "Nocturne", "Nunu & Willump"
              "Pantheon", "Rammus", "Rek'Sai", "Rengar", "Sejuani",
              "Shaco", "Shyvana", "Skarner", "Trundle", "Twitch",
              "Udyr", "Vi", "Volibear", "Warwick", "Wukong",
              "Xin Zhao", "Zac"]
MID_CHAMPS = ["Aatrox", "Ahri", "Akali", "Anivia", "Annie",
              "Azir", "Cassiopeia", "Corki", "Diana", "Ekko",
              "Fizz", "Irelia", "Kassadin", "Katerina", "Leblanc",
              "Lissandra", "Lux", "Malzahar", "Morgana", "Neeko",
              "Orianna", "Pyke", "Ryze", "Swain", "Sylas",
              "Syndra", "Taliyah", "Talon", "Twisted Fate", "Veigar",
              "Vel'Koz", "Viktor", "Vladimir", "Xerath", "Yasuo",
              "Zed", "Ziggs", "Zilean", "Zoe"]
ADC_CHAMPS = ["Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin",
              "Jinx", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian",
              "Miss Fortune", "Sivir", "Tristana", "Twitch", "Varus",
              "Vayne", "Xayah"]
SUP_CHAMPS = ["Alistar", "Bard", "Blitzcrank", "Brand", "Bruam",
              "Fiddlesticks", "Galio", "Janna", "Karma", "Leona",
              "Lulu", "Lux", "Morgana", "Nami", "Nautilus",
              "Pyke", "Rakan", "Sona", "Soraka", "Taric",
              "Thresh", "Vel'koz", "Xerath", "Yummi", "Zilean",
              "Zyra"
             ]


def find_champ(champ_id):
    if champ_id == 266:
        return "Aatrox"
    if champ_id == 412:
        return "Thresh"
    if champ_id == 23:
        return "Tryndamere"
    if champ_id == 79:
        return "Gragas"
    if champ_id == 69:
        return "Cassiopeia"
    if champ_id == 136:
        return "Aurelion Sol"
    if champ_id == 13:
        return "Ryze"
    if champ_id == 78:
        return "Poppy"
    if champ_id == 14:
        return "Sion"
    if champ_id == 1:
        return "Annie"
    if champ_id == 202:
        return "Jhin"
    if champ_id == 43:
        return "Karma"
    if champ_id == 111:
        return "Nautilus"
    if champ_id == 240:
        return "Kled"
    if champ_id == 99:
        return "Lux"
    if champ_id == 103:
        return "Ahri"
    if champ_id == 2:
        return "Olaf"
    if champ_id == 112:
        return "Viktor"
    if champ_id == 34:
        return "Anivia"
    if champ_id == 27:
        return "Singed"
    if champ_id == 86:
        return "Garen"
    if champ_id == 127:
        return "Lissandra"
    if champ_id == 57:
        return "Maokai"
    if champ_id == 25:
        return "Morgana"
    if champ_id == 28:
        return "Evelynn"
    if champ_id == 105:
        return "Fizz"
    if champ_id == 74:
        return "Heimerdinger"
    if champ_id == 238:
        return "Zed"
    if champ_id == 68:
        return "Rumble"
    if champ_id == 82:
        return "Mordekaiser"
    if champ_id == 37:
        return "Sona"
    if champ_id == 96:
        return "Kog'Maw"
    if champ_id == 55:
        return "Katarina"
    if champ_id == 117:
        return "Lulu"
    if champ_id == 22:
        return "Ashe"
    if champ_id == 30:
        return "Karthus"
    if champ_id == 12:
        return "Alistar"
    if champ_id == 122:
        return "Darius"
    if champ_id == 67:
        return "Vayne"
    if champ_id == 110:
        return "Varus"
    if champ_id == 77:
        return "Udyr"
    if champ_id == 89:
        return "Leona"
    if champ_id == 126:
        return "Jayce"
    if champ_id == 134:
        return "Syndra"
    if champ_id == 80:
        return "Pantheon"
    if champ_id == 92:
        return "Riven"
    if champ_id == 121:
        return "Kha'Zix"
    if champ_id == 42:
        return "Corki"
    if champ_id == 268:
        return "Azir"
    if champ_id == 51:
        return "Caitlyn"
    if champ_id == 76:
        return "Nidalee"
    if champ_id == 85:
        return "Kennen"
    if champ_id == 3:
        return "Galio"
    if champ_id == 45:
        return "Veigar"
    if champ_id == 432:
        return "Bard"
    if champ_id == 150:
        return "Gnar"
    if champ_id == 90:
        return "Malzahar"
    if champ_id == 104:
        return "Graves"
    if champ_id == 254:
        return "Vi"
    if champ_id == 10:
        return "Kayle"
    if champ_id == 39:
        return "Irelia"
    if champ_id == 64:
        return "Lee Sin"
    if champ_id == 420:
        return "Illaoi"
    if champ_id == 60:
        return "Elise"
    if champ_id == 106:
        return "Volibear"
    if champ_id == 20:
        return "Nunu"
    if champ_id == 4:
        return "Twisted Fate"
    if champ_id == 24:
        return "Jax"
    if champ_id == 102:
        return "Shyvana"
    if champ_id == 429:
        return "Kalista"
    if champ_id == 36:
        return "Dr. Mundo"
    if champ_id == 427:
        return "Ivern"
    if champ_id == 131:
        return "Diana"
    if champ_id == 223:
        return "Tahm Kench"
    if champ_id == 63:
        return "Brand"
    if champ_id == 113:
        return "Sejuani"
    if champ_id == 8:
        return "Vladimir"
    if champ_id == 154:
        return "Zac"
    if champ_id == 421:
        return "Rek'Sai"
    if champ_id == 133:
        return "Quinn"
    if champ_id == 84:
        return "Akali"
    if champ_id == 163:
        return "Taliyah"
    if champ_id == 18:
        return "Tristana"
    if champ_id == 120:
        return "Hecarim"
    if champ_id == 15:
        return "Sivir"
    if champ_id == 236:
        return "Lucian"
    if champ_id == 107:
        return "Rengar"
    if champ_id == 19:
        return "Warwick"
    if champ_id == 72:
        return "Skarner"
    if champ_id == 54:
        return "Malphite"
    if champ_id == 157:
        return "Yasuo"
    if champ_id == 101:
        return "Xerath"
    if champ_id == 17:
        return "Teemo"
    if champ_id == 75:
        return "Nasus"
    if champ_id == 58:
        return "Renekton"
    if champ_id == 119:
        return "Draven"
    if champ_id == 35:
        return "Shaco"
    if champ_id == 50:
        return "Swain"
    if champ_id == 91:
        return "Talon"
    if champ_id == 40:
        return "Janna"
    if champ_id == 115:
        return "Ziggs"
    if champ_id == 245:
        return "Ekko"
    if champ_id == 61:
        return "Orianna"
    if champ_id == 114:
        return "Fiora"
    if champ_id == 9:
        return "Fiddlesticks"
    if champ_id == 31:
        return "Cho'Gath"
    if champ_id == 33:
        return "Rammus"
    if champ_id == 7:
        return "LeBlanc"
    if champ_id == 16:
        return "Soraka"
    if champ_id == 26:
        return "Zilean"
    if champ_id == 56:
        return "Nocturne"
    if champ_id == 222:
        return "Jinx"
    if champ_id == 83:
        return "Yorick"
    if champ_id == 6:
        return "Urgot"
    if champ_id == 203:
        return "Kindred"
    if champ_id == 21:
        return "Miss Fortune"
    if champ_id == 62:
        return "Wukong"
    if champ_id == 53:
        return "Blitzcrank"
    if champ_id == 98:
        return "Shen"
    if champ_id == 201:
        return "Braum"
    if champ_id == 5:
        return "Xin Zhao"
    if champ_id == 29:
        return "Twitch"
    if champ_id == 11:
        return "Master Yi"
    if champ_id == 44:
        return "Taric"
    if champ_id == 32:
        return "Amumu"
    if champ_id == 41:
        return "Gangplank"
    if champ_id == 48:
        return "Trundle"
    if champ_id == 38:
        return "Kassadin"
    if champ_id == 161:
        return "Vel'Koz"
    if champ_id == 143:
        return "Zyra"
    if champ_id == 267:
        return "Nami"
    if champ_id == 59:
        return "Jarvan IV"
    if champ_id == 81:
        return "Ezreal"
    if champ_id == 518:
        return "Neeko"
    if champ_id == 350:
        return "Yuumi"
    if champ_id == 517:
        return "Sylas"
    if champ_id == 555:
        return "Pyke"
    if champ_id == 145:
        return "Kai'sa"
    if champ_id == 142:
        return "Zoe"
    if champ_id == 516:
        return "Ornn"
    if champ_id == 141:
        return "Kayn"
    if champ_id == 497:
        return "Rakan"
    if champ_id == 498:
        return "Xayah"
    if champ_id == 164:
        return "Camille"
    if champ_id == 427:
        return "Ivern"
    if champ_id == 240:
        return "Kled"
    if champ_id == 136:
        return "Aurelion Sol"
    if champ_id == 202:
        return "Jhin"
    if champ_id == 420:
        return "Illoai"
