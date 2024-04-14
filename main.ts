function checkCombination () {
    if (userCombinationNotes.length == combinationNotes.length) {
        match = true
        for (let i = 0; i <= combinationNotes.length - 1; i++) {
            if (userCombinationNotes[i] != combinationNotes[i]) {
                match = false
                break;
            }
        }
        if (match) {
            basic.showIcon(IconNames.Yes)
            radio.sendString("D")
        } else {
            basic.showIcon(IconNames.No)
        }
        userCombinationNotes = []
    }
}
radio.onReceivedString(function (receivedString) {
    if (receivedString == "C") {
        test = true
        music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
    }
})
let xVal = 0
let match = false
let userCombinationNotes: number[] = []
let combinationNotes: number[] = []
let test = false
test = false
radio.setGroup(199)
// Note C4
// Note D4
// Note F4
combinationNotes = [
262,
294,
330,
330,
349
]
basic.forever(function () {
    if (test == true) {
        xVal = pins.analogReadPin(AnalogPin.P0)
        if (xVal > 750 && xVal < 1150) {
            music.playTone(262, music.beat(BeatFraction.Whole))
            userCombinationNotes.push(262)
        } else if (xVal > 500 && xVal < 750) {
            music.playTone(294, music.beat(BeatFraction.Whole))
            userCombinationNotes.push(294)
        } else if (xVal > 250 && xVal < 500) {
            music.playTone(330, music.beat(BeatFraction.Whole))
            userCombinationNotes.push(330)
        } else if (xVal > 250 && xVal < 500) {
            music.playTone(330, music.beat(BeatFraction.Whole))
            userCombinationNotes.push(330)
        } else if (xVal > 150 && xVal < 250) {
            music.playTone(349, music.beat(BeatFraction.Whole))
            userCombinationNotes.push(349)
        } else {
            checkCombination()
        }
    }
})
