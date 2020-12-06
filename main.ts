input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    graph += 1
    while (graph == 2) {
        graph = 0
    }
})
input.onButtonPressed(Button.A, function () {
    Mode += 1
    if (6 < Mode) {
        Mode = 1
    }
})
input.onButtonPressed(Button.B, function () {
    Mode = 9
    ship = images.createBigImage(`
        . . . . . . . . . .
        # # # # . # # # # .
        . . # . . . # . . .
        . . . # # # # # . .
        . . . . . . . . . .
        `)
    while (Mode == 9) {
        ship.scrollImage(1, 200)
    }
})
function UTA () {
    lang = randint(1, 3)
    kvoc = randint(0, klist.length - 1)
    basic.showString("" + (elist[kvoc]))
    if (lang == 1) {
        basic.showString("(K)")
        basic.showString("" + (klist[kvoc]))
    }
    if (lang == 2) {
        basic.showString("(M)")
        basic.showString("" + (mlist[kvoc]))
    }
    if (lang == 3) {
        basic.showString("(N)")
        basic.showString("" + (nlist[kvoc]))
    }
}
let gees = 0
let temp = 0
let light2 = 0
let direction = 0
let ship: Image = null
let graph = 0
let elist: string[] = []
let klist: string[] = []
let mlist: string[] = []
let nlist: string[] = []
let kvoc = 0
let lang = 0
let Mode = 0
let mvoc = 0
basic.showIcon(IconNames.Heart)
basic.showIcon(IconNames.SmallHeart)
basic.showIcon(IconNames.Heart)
basic.showString("Tricorder!")
Mode = 1
lang = 2
kvoc = 0
nlist = ["yawne", "kaltxi", "tawsip", "'eylan", "kelku", "safla", "tiyora'", "'itan", "'ite", "'ipu", "uvan", "syure", "yom"]
mlist = ["cyare", "Sucuy'gar", "me'sen", "burc'ya", "yaim", "bralov", "parjai", "ad", "ad", "nuh'la", "geroya", "kai'tome", "epar"]
klist = ["bang", "nuqneH", "'ejDo'", "jup ", "juH", "Qapla'", "yay", "puqloD", "puqbe'", "tlhaq", "Quj", "Soj", "Sop"]
elist = ["beloved", "hello", "starship", "friend", "home", "success", "victory", "son", "daughter", "funny", "game", "food", "eat"]
basic.forever(function () {
    while (1 == Mode) {
        basic.showString("compass")
        while (1 == Mode) {
            direction = Math.round(input.compassHeading() / 90)
            basic.showString("" + (direction))
        }
    }
    while (2 == Mode) {
        basic.showString("light")
        while (2 == Mode) {
            light2 = input.lightLevel()
            if (graph == 1) {
                led.plotBarGraph(
                light2,
                255
                )
            } else {
                basic.showString("" + (light2))
            }
        }
    }
    while (3 == Mode) {
        basic.showString("temp")
        while (3 == Mode) {
            temp = input.temperature() * 9 / 5 + 32
            if (graph == 1) {
                led.plotBarGraph(
                temp,
                120
                )
            } else {
                basic.showString("" + (temp))
            }
        }
    }
    while (4 == Mode) {
        basic.showString("gees")
        while (4 == Mode) {
            gees = 0 / 1000
            if (graph == 1) {
                led.plotBarGraph(
                input.acceleration(Dimension.Strength),
                1500
                )
            } else {
                basic.showString("" + (gees))
            }
        }
    }
    while (5 == Mode) {
        basic.showString("Audio")
        while (5 == Mode) {
            if (graph == 1) {
                led.plotBarGraph(
                input.soundLevel(),
                255
                )
            } else {
                basic.showNumber(input.soundLevel())
            }
        }
    }
    while (6 == Mode) {
        basic.showString("UTA")
        while (6 == Mode) {
            UTA()
        }
    }
})
