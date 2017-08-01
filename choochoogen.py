#!/usr/bin/env python3

import random

ENGINES = ["🚂"]
CARS = ["🚃","🚋"]
SCENES = ["desert","forest","field","beach"]

ORBS = ["🌕","🌙","☀","☁"]
DESERT_TILES = ["🌵","🌵","🌴","🌴","🐪","🐢","🐎"]
FOREST_TILES = ["🌲","🌲","🌲","🌲","🐇","🌳","🌳"]
BEACH_TILES = ["🌴","🌴","🍍","🐢","🗿","🐚"]
FIELD_TILES = ["🌾","🌾","🌾","🌻","🐍","🐈"]
WILDFLOWERS_TILES = ["🌼","🌺","🏵️","🌷","🌷","🐝","🦋"]
SEA_TILES =["🐬","🐳","🐙"]

HELL_TILES = ["🔥","👻","😈","💀"]
HEAVEN_TILES = ["📯👼","✨","🐕","👼"]
SPACE_TILES = ["👾","👽","💫","🚀","🛰"]
UNDERSEA_TILES = ["🐟","🐙","🐬","🐋"]

class Scene():
    def __init__(self, mode, height = 4, item_rarity = 10, top_border = None, bottom_border = None):
        self.mode = mode
        self.height = height
        self.item_rarity = item_rarity

        self.top_border = top_border
        self.bottom_border = bottom_border

        self.sky = ""
        self.landscape = []

        self.train = self.pick_engine() + self.pick_body()
    
    def pick_engine(self):
        leading_spaces = random.randint(0,9)
        self.engine = ""
        for _ in range(leading_spaces):
            self.engine += " "
        self.engine += random.choice(ENGINES)
        return self.engine

    def pick_body(self):
        self.body = ""
        cars = random.randint(3,8)
        for _ in range(cars):
            self.body += random.choice(CARS)
        return self.body
    
    def make_sky(self):
        self.sky = ""

        orb = random.choice(ORBS)
        orb_placement = random.randint(0,12)

        for _ in range(orb_placement):
            self.sky += u"\u2800"
        self.sky += orb + u"\uFE0F"
        
        return self.sky

    def make_sea(self):
        return self.fill_row(tileset = SEA_TILES, space_char = "🌊", length = 12)
     
    def fill_row(self, tileset = None, space_char = " ", length = 20):
        row = ""

        if not tileset:
            tileset = self.tileset
            
        for spot in range(length):
            tile = random.randint(1, self.item_rarity)
            if tile == 1:
                row += random.choice(tileset)
            else:
                row += space_char
        return row

    def generate(self):
        self.landscape = []

        if self.top_border:
            self.landscape.append(self.top_border)
        else:
            self.make_sky()
            self.landscape.append(self.fill_row())

        self.landscape.extend([self.fill_row(), self.fill_row()])

        if self.bottom_border:
            self.landscape.append(self.bottom_border)
        else:
            self.landscape.append(self.fill_row())

        tweet = ""
        if self.sky:
            tweet += self.sky + "\n"
            
        tweet += self.landscape[0] + "\n" + \
                 self.landscape[1] + "\n" + \
                 self.train + "\n" + \
                 self.landscape[2] + "\n" + \
                 self.landscape[3]

        return tweet

class Desert(Scene):
    def __init__(self):
        super(Desert, self).__init__("desert")
        self.tileset = DESERT_TILES

class Forest(Scene):
    def __init__(self):
        super(Forest, self).__init__("forest")
        self.tileset = FOREST_TILES

class Field(Scene):
    def __init__(self):
        super(Field, self).__init__("field")
        self.tileset = FIELD_TILES

class Wildflowers(Scene):
    def __init__(self):
        super(Wildflowers, self).__init__("wildflowers")
        self.tileset = WILDFLOWERS_TILES

class Beach(Scene):
    def __init__(self):
        super(Beach, self).__init__("beach")
        self.tileset = BEACH_TILES
        self.bottom_border = self.make_sea()

class Space(Scene):
    def __init__(self):
        super(Space, self).__init__("space")
        self.top_border = "⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟"
        self.bottom_border = "⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟"
        self.tileset = SPACE_TILES

class Hell(Scene):
    def __init__(self):
        super(Hell, self).__init__("hell")
        self.top_border = "🔥👹🔥👹🔥👹🔥👹🔥👹🔥👹"
        self.bottom_border = "🔥👹🔥👹🔥👹🔥👹🔥👹🔥👹"
        self.tileset = HELL_TILES

class Heaven(Scene):
    def __init__(self):
        super(Heaven, self).__init__("heaven")
        self.top_border = "☁👼☁👼☁👼☁👼☁👼☁👼"
        self.bottom_border = "☁👼☁👼☁👼☁👼☁👼☁👼"
        self.tileset = HEAVEN_TILES

class Undersea(Scene):
    def __init__(self):
        super(Undersea, self).__init__("undersea")
        self.top_border = "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊"
        self.bottom_border = "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊"
        self.tileset = UNDERSEA_TILES
        
def maketrain():
    standard_scenes = [Desert, Beach, Forest, Field]
    special_scenes = [Space, Undersea, Heaven, Hell]

    if random.randint(1,12) == 12:
        scene = random.choice(special_scenes)()
    else:
        scene = random.choice(standard_scenes)()

    return scene.generate()

if __name__ == "__main__":
    maketrain()
