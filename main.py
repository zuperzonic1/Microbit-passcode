def checkCombination():
    global match, userCombinationNotes
    if len(userCombinationNotes) == len(combinationNotes):
        match = True
        i = 0
        while i <= len(combinationNotes) - 1:
            if userCombinationNotes[i] != combinationNotes[i]:
                match = False
                break
            i += 1
        if match:
            basic.show_icon(IconNames.YES)
            radio.send_string("D")
        else:
            basic.show_icon(IconNames.NO)
        userCombinationNotes = []

def on_received_string(receivedString):
    global test
    if receivedString == "C":
        test = True
        music.play(music.string_playable("C5 B A G F E D C ", 120),
            music.PlaybackMode.UNTIL_DONE)
radio.on_received_string(on_received_string)

xVal = 0
match = False
userCombinationNotes: List[number] = []
combinationNotes: List[number] = []
test = False
test = False
radio.set_group(199)
# Note C4
# Note D4
# Note F4
combinationNotes = [262, 294, 330, 330, 349]

def on_forever():
    global xVal
    if test == True:
        xVal = pins.analog_read_pin(AnalogPin.P0)
        if xVal > 750 and xVal < 1150:
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            userCombinationNotes.append(262)
        elif xVal > 500 and xVal < 750:
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            userCombinationNotes.append(294)
        elif xVal > 250 and xVal < 500:
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            userCombinationNotes.append(330)
        elif xVal > 250 and xVal < 500:
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            userCombinationNotes.append(330)
        elif xVal > 150 and xVal < 250:
            music.play_tone(349, music.beat(BeatFraction.WHOLE))
            userCombinationNotes.append(349)
        else:
            checkCombination()
basic.forever(on_forever)
