screen bedroomdoor:
    imagebutton:
        idle "dooridle22.png"
        hover "doorhover2.png"
        focus_mask True
        action Jump("hallway")
    imagebutton:
        idle "dooridle.png"
        hover "doorhover.png"
        focus_mask True
        activate_sound "audio/door_opening.mp3"
        action Jump("leave_house")


screen bedroomdoorFR:
    imagebutton:
        idle "dooridle22.png"
        hover "doorhover2.png"
        focus_mask True
        action Jump("hallwayFR")
    imagebutton:
        idle "dooridle.png"
        hover "doorhover.png"
        focus_mask True
        activate_sound "audio/door_opening.mp3"
        action Jump("leave_houseFR")

screen bedroomdoorNL:
    imagebutton:
        idle "dooridle22.png"
        hover "doorhover2.png"
        focus_mask True
        action Jump("hallwayNL")
    imagebutton:
        idle "dooridle.png"
        hover "doorhover.png"
        focus_mask True
        activate_sound "audio/door_opening.mp3"
        action Jump("leave_houseNL")

image scribble_anim:
    "scribble 1.png"
    pause 0.5
    "scribble 2.png"
    pause 0.5
    repeat

image desk_anim:
    "desk 2.png"
    pause 1
    "desk 3.png"
    pause 1
    repeat

image waiting_anim:
    "waiting.png"
    pause 1
    "waiting 2.png"
    pause 1
    repeat

image end_anim:
    "bathroom1.png"
    pause 1.5
    "bathroom2.png"
    pause 1.5
    "bathroom3.png"
    pause 1.5
    "bathroom4.png"
    pause 1.5
    "bathroom5.png"
    pause 1.5
    "bathroom6.png"
    pause 1.5
    "bathroom7.png"
    pause 1.5
    "bathroom8.png"
    pause 1.5
    "bathroom9.png"
    pause 1.5
    "bathroom10.png"
    pause 1.5
    repeat

screen ending(txt):
    text txt:
        style "ending_text"
        align (0.5, 0.5)

screen endingFR(txt):
    text txt:
        style "ending_text"
        align (0.5, 0.5)

screen endingNL(txt):
    text txt:
        style "ending_text"
        align (0.5, 0.5)