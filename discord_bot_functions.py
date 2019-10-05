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
              "Qiyana",
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
    elif champ_id == 412:
        return "Thresh"
    elif champ_id == 23:
        return "Tryndamere"
    elif champ_id == 79:
        return "Gragas"
    elif champ_id == 69:
        return "Cassiopeia"
    elif champ_id == 136:
        return "Aurelion Sol"
    elif champ_id == 13:
        return "Ryze"
    elif champ_id == 78:
        return "Poppy"
    elif champ_id == 14:
        return "Sion"
    elif champ_id == 1:
        return "Annie"
    elif champ_id == 202:
        return "Jhin"
    elif champ_id == 43:
        return "Karma"
    elif champ_id == 111:
        return "Nautilus"
    elif champ_id == 240:
        return "Kled"
    elif champ_id == 99:
        return "Lux"
    elif champ_id == 103:
        return "Ahri"
    elif champ_id == 2:
        return "Olaf"
    elif champ_id == 112:
        return "Viktor"
    elif champ_id == 34:
        return "Anivia"
    elif champ_id == 27:
        return "Singed"
    elif champ_id == 86:
        return "Garen"
    elif champ_id == 127:
        return "Lissandra"
    elif champ_id == 57:
        return "Maokai"
    elif champ_id == 25:
        return "Morgana"
    elif champ_id == 28:
        return "Evelynn"
    elif champ_id == 105:
        return "Fizz"
    elif champ_id == 74:
        return "Heimerdinger"
    elif champ_id == 238:
        return "Zed"
    elif champ_id == 68:
        return "Rumble"
    elif champ_id == 82:
        return "Mordekaiser"
    elif champ_id == 37:
        return "Sona"
    elif champ_id == 96:
        return "Kog'Maw"
    elif champ_id == 55:
        return "Katarina"
    elif champ_id == 117:
        return "Lulu"
    elif champ_id == 22:
        return "Ashe"
    elif champ_id == 30:
        return "Karthus"
    elif champ_id == 12:
        return "Alistar"
    elif champ_id == 122:
        return "Darius"
    elif champ_id == 67:
        return "Vayne"
    elif champ_id == 110:
        return "Varus"
    elif champ_id == 77:
        return "Udyr"
    elif champ_id == 89:
        return "Leona"
    elif champ_id == 126:
        return "Jayce"
    elif champ_id == 134:
        return "Syndra"
    elif champ_id == 80:
        return "Pantheon"
    elif champ_id == 92:
        return "Riven"
    elif champ_id == 121:
        return "Kha'Zix"
    elif champ_id == 42:
        return "Corki"
    elif champ_id == 268:
        return "Azir"
    elif champ_id == 51:
        return "Caitlyn"
    elif champ_id == 76:
        return "Nidalee"
    elif champ_id == 85:
        return "Kennen"
    elif champ_id == 3:
        return "Galio"
    elif champ_id == 45:
        return "Veigar"
    elif champ_id == 432:
        return "Bard"
    elif champ_id == 150:
        return "Gnar"
    elif champ_id == 90:
        return "Malzahar"
    elif champ_id == 104:
        return "Graves"
    elif champ_id == 254:
        return "Vi"
    elif champ_id == 10:
        return "Kayle"
    elif champ_id == 39:
        return "Irelia"
    elif champ_id == 64:
        return "Lee Sin"
    elif champ_id == 420:
        return "Illaoi"
    elif champ_id == 60:
        return "Elise"
    elif champ_id == 106:
        return "Volibear"
    elif champ_id == 20:
        return "Nunu"
    elif champ_id == 4:
        return "Twisted Fate"
    elif champ_id == 24:
        return "Jax"
    elif champ_id == 102:
        return "Shyvana"
    elif champ_id == 429:
        return "Kalista"
    elif champ_id == 36:
        return "Dr. Mundo"
    elif champ_id == 427:
        return "Ivern"
    elif champ_id == 131:
        return "Diana"
    elif champ_id == 223:
        return "Tahm Kench"
    elif champ_id == 63:
        return "Brand"
    elif champ_id == 113:
        return "Sejuani"
    elif champ_id == 8:
        return "Vladimir"
    elif champ_id == 154:
        return "Zac"
    elif champ_id == 421:
        return "Rek'Sai"
    elif champ_id == 133:
        return "Quinn"
    elif champ_id == 84:
        return "Akali"
    elif champ_id == 163:
        return "Taliyah"
    elif champ_id == 18:
        return "Tristana"
    elif champ_id == 120:
        return "Hecarim"
    elif champ_id == 15:
        return "Sivir"
    elif champ_id == 236:
        return "Lucian"
    elif champ_id == 107:
        return "Rengar"
    elif champ_id == 19:
        return "Warwick"
    elif champ_id == 72:
        return "Skarner"
    elif champ_id == 54:
        return "Malphite"
    elif champ_id == 157:
        return "Yasuo"
    elif champ_id == 101:
        return "Xerath"
    elif champ_id == 17:
        return "Teemo"
    elif champ_id == 75:
        return "Nasus"
    elif champ_id == 58:
        return "Renekton"
    elif champ_id == 119:
        return "Draven"
    elif champ_id == 35:
        return "Shaco"
    elif champ_id == 50:
        return "Swain"
    elif champ_id == 91:
        return "Talon"
    elif champ_id == 40:
        return "Janna"
    elif champ_id == 115:
        return "Ziggs"
    elif champ_id == 245:
        return "Ekko"
    elif champ_id == 61:
        return "Orianna"
    elif champ_id == 114:
        return "Fiora"
    elif champ_id == 9:
        return "Fiddlesticks"
    elif champ_id == 31:
        return "Cho'Gath"
    elif champ_id == 33:
        return "Rammus"
    elif champ_id == 7:
        return "LeBlanc"
    elif champ_id == 16:
        return "Soraka"
    elif champ_id == 26:
        return "Zilean"
    elif champ_id == 56:
        return "Nocturne"
    elif champ_id == 222:
        return "Jinx"
    elif champ_id == 83:
        return "Yorick"
    elif champ_id == 6:
        return "Urgot"
    elif champ_id == 203:
        return "Kindred"
    elif champ_id == 21:
        return "Miss Fortune"
    elif champ_id == 62:
        return "Wukong"
    elif champ_id == 53:
        return "Blitzcrank"
    elif champ_id == 98:
        return "Shen"
    elif champ_id == 201:
        return "Braum"
    elif champ_id == 5:
        return "Xin Zhao"
    elif champ_id == 29:
        return "Twitch"
    elif champ_id == 11:
        return "Master Yi"
    elif champ_id == 44:
        return "Taric"
    elif champ_id == 32:
        return "Amumu"
    elif champ_id == 41:
        return "Gangplank"
    elif champ_id == 48:
        return "Trundle"
    elif champ_id == 38:
        return "Kassadin"
    elif champ_id == 161:
        return "Vel'Koz"
    elif champ_id == 143:
        return "Zyra"
    elif champ_id == 267:
        return "Nami"
    elif champ_id == 59:
        return "Jarvan IV"
    elif champ_id == 81:
        return "Ezreal"
    elif champ_id == 518:
        return "Neeko"
    elif champ_id == 350:
        return "Yuumi"
    elif champ_id == 517:
        return "Sylas"
    elif champ_id == 555:
        return "Pyke"
    elif champ_id == 145:
        return "Kai'sa"
    elif champ_id == 142:
        return "Zoe"
    elif champ_id == 516:
        return "Ornn"
    elif champ_id == 141:
        return "Kayn"
    elif champ_id == 497:
        return "Rakan"
    elif champ_id == 498:
        return "Xayah"
    elif champ_id == 164:
        return "Camille"
    elif champ_id == 427:
        return "Ivern"
    elif champ_id == 240:
        return "Kled"
    elif champ_id == 136:
        return "Aurelion Sol"
    elif champ_id == 202:
        return "Jhin"
    elif champ_id == 420:
        return "Illoai"
