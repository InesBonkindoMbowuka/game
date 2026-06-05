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

screen resources_qr():

    tag menu

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "Extra Resources & Information"
        text "Scan the QR code to learn more."

        add "images/resources-QR.png"

        textbutton "Menu" action MainMenu()

screen resources_qrFR():

    tag menu

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "Extra Resources & Information"
        text "Scan le code QR pour en apprendre plus."

        add "images/resources-QR.png"

        textbutton "Menu" action MainMenu()

screen resources_qrNL():

    tag menu

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "Extra Bronnen & Informatie"
        text "Scan de QR code om meer te leren."

        add "images/resources-QR.png"

        textbutton "Menu" action MainMenu()