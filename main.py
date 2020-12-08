def on_button_pressed_a():
    global Mode
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    Mode += 1
    if 6 < Mode:
        Mode = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Mode, ship
    music.play_melody("C F C5 A - - - - ", 120)
    Mode = 9
    ship = images.create_big_image("""
        . . . . . . . . . .
        # # # # . . # # # .
        . . # . . . # # . .
        . . . # # # # # . .
        . . . . . . . . . .
        """)
    while Mode == 9:
        ship.scroll_image(1, 200)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    global graph
    music.play_tone(175, music.beat(BeatFraction.WHOLE))
    graph += 1
    while graph == 2:
        graph = 0
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def UTA():
    global lang, kvoc
    lang = randint(1, 3)
    kvoc = randint(0, len(klist) - 1)
    basic.show_string("" + (elist[kvoc]))
    if lang == 1:
        basic.show_string("(K)")
        basic.show_string("" + (klist[kvoc]))
    if lang == 2:
        basic.show_string("(M)")
        basic.show_string("" + (mlist[kvoc]))
    if lang == 3:
        basic.show_string("(N)")
        basic.show_string("" + (nlist[kvoc]))
gees = 0
temp = 0
light2 = 0
direction = 0
graph = 0
ship: Image = None
elist: List[str] = []
klist: List[str] = []
mlist: List[str] = []
nlist: List[str] = []
kvoc = 0
lang = 0
Mode = 0
mvoc = 0
basic.show_icon(IconNames.HEART)
basic.show_icon(IconNames.SMALL_HEART)
basic.show_icon(IconNames.HEART)
basic.show_string("Tricorder!")
Mode = 1
lang = 2
kvoc = 0
nlist = ["yawne",
    "kaltxi",
    "tawsip",
    "'eylan",
    "kelku",
    "safla",
    "tiyora'",
    "'itan",
    "'ite",
    "'ipu",
    "uvan",
    "syure",
    "yom"]
mlist = ["cyare",
    "Sucuy'gar",
    "me'sen",
    "burc'ya",
    "yaim",
    "bralov",
    "parjai",
    "ad",
    "ad",
    "nuh'la",
    "geroya",
    "kai'tome",
    "epar"]
klist = ["bang",
    "nuqneH",
    "'ejDo'",
    "jup ",
    "juH",
    "Qapla'",
    "yay",
    "puqloD",
    "puqbe'",
    "tlhaq",
    "Quj",
    "Soj",
    "Sop"]
elist = ["beloved",
    "hello",
    "starship",
    "friend",
    "home",
    "success",
    "victory",
    "son",
    "daughter",
    "funny",
    "game",
    "food",
    "eat"]

def on_forever():
    global direction, light2, temp, gees
    while 1 == Mode:
        basic.show_string("compass")
        while 1 == Mode:
            direction = Math.round(input.compass_heading() / 90)
            if graph == 1:
                led.plot_bar_graph(input.compass_heading(), 375)
            else:
                basic.show_string("" + str(direction))
    while 2 == Mode:
        basic.show_string("light")
        while 2 == Mode:
            light2 = input.light_level()
            if graph == 1:
                led.plot_bar_graph(light2, 255)
            else:
                basic.show_string("" + str(light2))
    while 3 == Mode:
        basic.show_string("temp")
        while 3 == Mode:
            temp = input.temperature() * 9 / 5 + 32
            if graph == 1:
                led.plot_bar_graph(temp, 120)
            else:
                basic.show_string("" + str(temp))
    while 4 == Mode:
        basic.show_string("gees")
        while 4 == Mode:
            gees = 0 / 1000
            if graph == 1:
                led.plot_bar_graph(input.acceleration(Dimension.STRENGTH), 1500)
            else:
                basic.show_string("" + str(gees))
    while 5 == Mode:
        basic.show_string("Audio")
        while 5 == Mode:
            if graph == 1:
                led.plot_bar_graph(input.sound_level(), 255)
            else:
                basic.show_number(input.sound_level())
    while 6 == Mode:
        basic.show_string("UTA")
        while 6 == Mode:
            UTA()
basic.forever(on_forever)
