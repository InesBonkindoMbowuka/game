define e = Character("", window_background="gui/textbox_thoughts.png")
define u = Character("You", window_background="gui/textbox_you.png", color="#ffffff")
define uf = Character("Toi", window_background="gui/textbox_you.png", color="#ffffff")
define un = Character("Jij", window_background="gui/textbox_you.png", color="#ffffff")
define d = Character("Receptionist", callback=make_voice("speech_d", "audio/femalegibberish.mp3"), window_background="gui/textbox_desk.png", color="#0e60db", what_color="#0e60db")
define i = Character("Interviewer", callback=make_voice("speech_i", "audio/male_alien.mp3"), window_background="gui/textbox_inter.png", color="#db8d0e", what_color="#db8d0e")
define o = Character("Old lady",callback=make_voice("speech_o", "audio/old_voice.mp3"), window_background="gui/textbox_you.png", color="#db180e", what_color="#db180e")



label start:

    call screen language_menu


##English version
label startENG:
    stop music fadeout 1.0
    
    play music "audio/game_music.mp3" fadein 1.0
    scene bg bedroom

    e "Good news!"
    e "Out of the 145 job applications you've sent, one company finally got back to you."
    e "Today is your interview at XXX."

    scene bg room

    e "Time to leave for the interview."

    call screen bedroomdoor 
    
    return

label hallway:
    u "I don't need to go to my room right now."
    call screen bedroomdoor
    return  

label leave_house:

    u "Alright, time to head out."
    scene bg street
    play sound "audio/trafic.mp3" loop channel "ambience"
    
    e "The weather is gloomy, as always"
    o "Watch where you're going kid!"
    e "A woman bumps into you from the side."
    show old lady at left with moveinleft
    o "We welcome people like you into this country, and this is how you repay us?"
    u "I'm sorry, I didn't mean to bump into you."
    o "You liar! You lot always lie about everything!"
    e "the lady walks away with a sigh."
    
    jump lobby

label lobby:
    stop music fadeout 1.0

    scene black with fade
    play sound "audio/steps.mp3" channel "steps"
    $ renpy.movie_cutscene("images/doors.webm")
    stop sound channel "steps"
    stop sound channel "ambience"
    play music "audio/corp.mp3" fadein 1.0
    play sound "audio/office.mp3" loop
    scene desk 1 with fade

    e "You arrive at the job office"
    e "The atmosphere is completely different here."
    e "It's like the gloomy darkness has fully disappeared"
    e "The front desk lady glances at you, then looks back at her screen."
    d "Can i help you?" 
    show desk_anim at center
    u "I am here for a job interview with XXX"
    d "Oh, sure go sit there."
    e "The lady goes back to her tasks."
    hide desk_anim
    jump waiting_room
    return

label waiting_room:

    scene waiting with fade
    
    show waiting_anim at center
    e "You sit down in the waiting room"
    e "A man stares at you from across the room"
    e "And next to him sits..."
    e "A bunny? Who knew bunnies could apply for this position as well."
    e "As the man continues to stare. You hear your name called from the hallway."
    hide waiting_anim
    jump interview
    return

label interview:
    scene black with fade
    stop sound fadeout 1.0
    scene happy with fade  
    e "A man is sitting at his desk"
    i "Oh. You're here to clean the office? I'm actually in the middle of something."

    menu:
        "Be offended and walk out":
            u "Goodbye sir."
            stop music fadeout 1.0
            scene bg street
            e "You decide the disrespect is not worth the job and walk back home."
            jump end_scene
            return

        "Tell him you are here for the job interview.":
            u "No, I am here for the job interview. My name is XXX."
            jump awkward_answer
    return

label awkward_answer:
    scene neutral
    i "Oh? *puzzled* Well… Sit down *looks down at his laptop* Huh. Your name doesn't sound foreign."

    menu:
        "Ask to clarify what he means.":
            u "confused you ask* I don’t really understand what you mean by that."
            scene angry
            i "Oh, nevermind i didnt mean anything by that"
            u "*You shrug off his comment* So…"
            jump continuation1

        "Awkwardly laugh and move on":
            u "HAHAHA, yes I hear that often."
            jump continuation2
        

        "Walk away":
            u "Goodbye sir."
            stop music fadeout 1.0
            scene bg street
            e "You decide the disrespect is not worth the job and walk back home."
            jump end_scene
            return


    return

label continuation1:
    scene neutral
    i "Yes so, I see here that you graduated from XXX university with a Masters degree in XXX?"
    u "Yes I graduated in XXX."
    i "Right… I studied there as well… which professor do you know…"

    menu:
        "Give him the name of a few professors you remember.":
            u "Oh yes I had XXX for the XXX class do you know him?"
            i "Yes, yes *surprised*His class was pretty difficult."
            u "Not really, I enjoyed his classes the most!"
            scene angry
            i "moving on to the job interview…"
            jump part2

        "Ask why that matters for you to get the job.":
            u "I don't really know what that has to do with the job requirments..."
            i "Oh, nothing really it was just to be sure... I think we will wrap up the interview here i just remember i have an urgent meeting. *leads you out*"
            e "he walks you out of the building in a hurry."
            stop music fadeout 1.0
            scene bg street with fade
            e "You wonder why the interviewer acted so oddly and walk back home."
            jump end_scene
            return 

        "Walk away":
            u "Goodbye sir."
            stop music fadeout 1.0
            scene bg street with fade
            e "You decide the disrespect is not worth the job and walk back home."
            jump end_scene
            return  
    return

label continuation2:
    scene neutral
     
    i "Right… is that your real name? XXX?"
    
    menu:
        "Confused but say yes.":
            u "Euhm... yes, that is my actual legal name."
            scene angry
            i "Alright... *suspicion coated voice* Let's move on to interview"
            jump part2

        "Walk away":
            u "Goodbye sir."
            stop music fadeout 1.0
            scene bg street with fade
            e "You decide the disrespect is not worth the job and walk back home."
            jump end_scene
            return 

label part2:
    scene neutral

    i "So for this job you need to have a professional look. Such as your clothes. Which looks fine right now."
    i "However your hair… Could you maybe put it in a bun or straighten it?"
    scene angry
    i "I love the WILD look like this but it may be distracting in the office."

    menu:
        "Ask why your current haircut isn't professional.":
            e "You cannot believe what the man just said to you, your hair looks fine, you took an hour this morning to make it look presentable"
            u "What about my haircut isn't professional if i may ask?"
            scene happy
            i "I mean i'm all for the big, bold, confident look. But it is a lot."
            u "I understand. I'll look into changing it."
            i "Great! Well, this is about it for me. You will be contacted in the next few days to know if you got the job. Goodbye. *big smile*"
            jump part3

        "Tell him off, politely.":
            e "You cannot believe what the man just said to you, your hair looks fine, you took an hour this morning to make it look presentable"
            u "I'm sorry if this comes off as rude but i don't see how my hair is not professional. It is my natural hair."
            scene angry
            i "Is it? Oh well, Still. It would be nice if you could... straighten it perhaps."
            u "I don't think so, if that's okay with you i think we should end this meeting here."
            i "No need to get so agressive with me!"
            u "Goodbye sir."
            stop music fadeout 1.0
            scene bg street with fade 
            e "You decide the disrespect is not worth the job and walk back home."
            jump end_scene
            return 
        
        "Tell him off, rudely.":
            e "You cannot believe what the man just said to you, your hair looks fine, you took an hour this morning to make it look presentable"
            u "Excuse me but i do not understand what this comment has to do with anything? How is my hair not presentable?"
            scene angry
            i "*defensive and a bit scared* Oh my god, there is no need to yell at me and be agressive."
            i "These are the office rules. If you want to work here you must abide by them!"
            i "I think this wraps up our meeting for today. Thank you and goodbye."
            stop music fadeout 1.0
            scene bg street with fade
            e "You decide the disrespect is not worth the job and walk back home."
            jump end_scene
            return 

    return

label part3:
    scene neutral

    u "What about the needed skills for this job?"
    i "Oh everything is here and i'm sure it'll be fine. *looks at clock* Time to wrap this up. You'll be contacted if there's anything else. Goodbye."
    
    menu:
        "Leave":
            e "You exit the job interview with a heavy heart. You hope you get the job as you do need one urgently."
            jump end_scene 
    return

label end_scene:
    stop music fadeout 1.0
    play music "audio/game_music.mp3" fadein 1.0
    scene bg bedroom with fade

    e "A few days later a mail comes in."
    e "Thank you for considering working here, unfortunatlly..."
    e "Your eyes water up but you try to swallow them back down. Next time will be the time you'll find the job."
    jump message

    return

label message:
    play music "audio/game_music.mp3" fadein 1.0
    scene black with fade 
    show end_anim at center
    e "Like many others, you're being punished for something out of your control."
    e "The crime?"
    jump ending
    return

label ending:
    scene black with fade
    show screen ending("Being born as a black woman")
    pause
    show screen ending("Misogynoir:\nAnti-Black racism + misogyny directed towards Black women")
    pause
    hide screen ending
    call screen resources_qr
    return


##French version

label startFR:
    stop music fadeout 1.0
    
    play music "audio/game_music.mp3" fadein 1.0
    scene bg bedroom

    e "Bonne nouvelle !"
    e "Parmi les 145 candidatures que vous avez envoyées, une entreprise vous a enfin répondu."
    e "Aujourd'hui, vous avez un entretien chez XXX."

    scene bg room

    uf "Il est temps de me préparer pour l'entretien."

    call screen bedroomdoorFR
    
    return


label hallwayFR:
    uf "Je n'ai pas besoin d'aller dans ma chambre pour le moment."
    call screen bedroomdoorFR
    return  


label leave_houseFR:

    uf "Bon, il est temps d'y aller."
    scene bg street
    
    play sound "audio/trafic.mp3" loop channel "ambience"
    e "Le temps est morose, comme toujours"
    o "Regarde où tu vas, gamine !"
    e "Une femme vous percute sur le côté."
    show old lady at left with moveinleft
    o "On accueille des gens comme vous dans ce pays, et c'est comme ça que vous nous remerciez ?"
    uf "Je suis désolée, je ne voulais pas vous bousculer."
    o "Menteuse ! Vous mentez toujours sur tout !"
    e "La femme s'éloigne en soupirant."
    
    jump lobbyFR


label lobbyFR:
   
    scene black with fade
    play sound "audio/steps.mp3" channel "steps"
    $ renpy.movie_cutscene("images/doors.webm")
    stop sound channel "steps"
    stop sound channel "ambience"
    play music "audio/corp.mp3" fadein 1.0
    play sound "audio/office.mp3" loop
    scene desk 1 with fade

    e "Vous arrivez dans les bureaux de l'entreprise"
    e "L'atmosphère est complètement différente ici."
    e "C'est comme si toute la grisaille extérieure avait disparu"
    e "La réceptionniste vous jette un coup d'œil avant de retourner à son écran."
    d "Puis-je vous aider ?"
    show desk_anim at center
    u "Je suis ici pour un entretien d'embauche chez XXX"
    d "Ah, bien sûr. Allez vous asseoir là-bas."
    e "La réceptionniste reprend son travail."
    hide desk_anim
    jump waiting_roomFR
    return


label waiting_roomFR:

    scene waiting with fade

    show waiting_anim at center
    e "Vous vous asseyez dans la salle d'attente"
    e "Un homme vous fixe depuis l'autre côté de la pièce"
    e "Et à côté de lui se trouve..."
    e "Un lapin ? Qui aurait cru que les lapins pouvaient aussi postuler pour ce poste ?"
    e "Alors que l'homme continue de vous fixer, vous entendez votre nom appelé depuis le couloir."
    hide waiting_anim
    jump interviewFR
    return


label interviewFR:
    scene black with fade
    stop sound fadeout 1.0
    scene happy with fade  
    e "Un homme est assis à son bureau"
    i "Oh. Vous êtes là pour faire le ménage ? Je suis en plein milieu de quelque chose."

    menu:
        "Se sentir offensée et partir":
            uf "Au revoir monsieur."
            scene bg street
            e "Vous décidez que ce manque de respect ne vaut pas cet emploi et vous rentrez chez vous."
            jump end_sceneFR
            return

        "Dire que vous êtes ici pour l'entretien d'embauche":
            uf "Non, je suis ici pour l'entretien d'embauche. Je m'appelle XXX."
            jump awkward_answerFR
    return


label awkward_answerFR:
    scene neutral
    i "Oh ? *perplexe* Bien… Asseyez-vous. *regarde son ordinateur portable* Hm. Votre nom ne semble pas étranger."

    menu:
        "Demander ce qu'il veut dire":
            uf "*confuse* Je ne comprends pas vraiment ce que vous voulez dire par là."
            scene angry
            i "Oh, ce n'était rien."
            uf "*Vous ignorez son commentaire* Alors…"
            jump continuation1FR

        "Rire nerveusement et continuer":
            uf "HAHAHA, oui j'entends souvent ça."
            jump continuation2FR

        "Partir":
            uf "Au revoir monsieur."
            scene bg street
            e "Vous décidez que ce manque de respect ne vaut pas cet emploi et vous rentrez chez vous."
            jump end_sceneFR
            return


label continuation1FR:
    scene neutral
    i "Donc, je vois ici que vous avez obtenu un Master à l'université XXX ?"
    uf "Oui, j'ai obtenu mon diplôme à XXX."
    i "Ah… J'y ai étudié aussi… quels professeurs connaissez-vous ?"

    menu:
        "Donner quelques noms de professeurs":
            uf "Oui, j'avais XXX en cours de XXX, vous le connaissez ?"
            i "Oui, oui *surpris* Son cours était assez difficile."
            uf "Pas vraiment, j'ai adoré ses cours."
            scene angry
            i "Bon, revenons à l'entretien…"
            jump part2FR

        "Demander pourquoi cela est important":
            uf "Je ne comprends pas vraiment le rapport avec le poste..."
            i "Oh, ce n'est rien… juste pour être sûr… je dois y aller, désolé."
            e "Il vous raccompagne rapidement vers la sortie."
            scene bg street with fade
            e "Vous vous demandez pourquoi l'intervieweur était si étrange."
            jump end_sceneFR
            return 

        "Partir":
            uf "Au revoir monsieur."
            scene bg street with fade
            e "Vous décidez que ce manque de respect ne vaut pas cet emploi et vous rentrez chez vous."
            jump end_sceneFR
            return  


label continuation2FR:
    scene neutral
     
    i "D'accord… c'est bien votre vrai nom ? XXX ?"
    
    menu:
        "Répondre oui":
            uf "Euh… oui, c'est bien mon nom légal."
            scene angry
            i "Très bien… passons à l'entretien."
            jump part2FR

        "Partir":
            uf "Au revoir monsieur."
            scene bg street with fade
            e "Vous décidez que ce manque de respect ne vaut pas cet emploi et vous rentrez chez vous."
            jump end_sceneFR
            return 


label part2FR:
    scene neutral

    i "Pour ce poste, il faut une apparence professionnelle. Vos vêtements sont corrects."
    i "Cependant vos cheveux… pourriez-vous les attacher ou les lisser ?"
    scene angry
    i "J'aime beaucoup ce style SAUVAGE, mais cela peut distraire au bureau."

    menu:
        "Demander pourquoi":
            e "Vous n'en revenez pas."
            uf "En quoi ma coiffure n'est-elle pas professionnelle ?"
            scene happy
            i "Je suis pour les styles forts et confiants, mais c'est assez voyant."
            uf "Je comprends."
            i "Parfait. Nous vous recontacterons."
            jump part3FR

        "Répondre poliment":
            e "Vous n'en revenez pas."
            uf "Je ne comprends pas en quoi ma coiffure n'est pas professionnelle."
            scene angry
            i "Je pense que ce serait mieux de la lisser."
            uf "Je préfère ne pas le faire."
            i "Pas besoin d'être agressive."
            uf "Au revoir."
            scene bg street with fade 
            e "Vous rentrez chez vous."
            jump end_sceneFR
            return 
        
        "Répondre sèchement":
            e "Vous n'en revenez pas."
            uf "Comment ma coiffure n'est-elle pas présentable ?"
            scene angry
            i "Il n'y a pas besoin de crier."
            i "Ce sont les règles du bureau."
            i "L'entretien est terminé."
            scene bg street with fade
            e "Vous rentrez chez vous."
            jump end_sceneFR
            return 


label part3FR:
    scene neutral

    uf "Quelles compétences sont nécessaires ?"
    i "Tout est ici, ça devrait aller. L'entretien est terminé."

    menu:
        "Partir":
            e "Vous quittez l'entretien avec un poids sur le cœur."
            jump end_sceneFR
    return


label end_sceneFR:

    play music "audio/game_music.mp3" fadein 1.0
    scene bg bedroom with fade

    e "Quelques jours plus tard, un mail arrive."
    e "Merci d'avoir postulé, malheureusement..."
    e "Vous retenez vos larmes."
    jump messageFR


label messageFR:
    play music "audio/game_music.mp3" fadein 1.0
    scene black with fade 
    show end_anim at center
    e "Comme beaucoup d'autres, vous êtes pénalisée pour quelque chose hors de votre contrôle."
    e "Le crime ?"
    jump endingFR
    return

label endingFR:
    scene black with fade
    show screen endingFR("Être une femme noire.")
    pause
    show screen endingFR("La misogynoir : un terme désignant la combinaison du racisme anti-noir et du sexisme envers les femmes noires.")
    pause
    hide screen endingFR
    call screen resources_qrFR
    return

##Nederlandse versie

label startNL:
    stop music fadeout 1.0
    
    play music "audio/game_music.mp3" fadein 1.0
    scene bg bedroom

    e "Goed nieuws!"
    e "Van de 145 sollicitaties die je hebt verstuurd, heeft eindelijk één bedrijf gereageerd."
    e "Vandaag heb je een sollicitatiegesprek bij XXX."

    scene bg room

    un "Het is tijd om me klaar te maken voor het gesprek."

    call screen bedroomdoorNL 
    
    return


label hallwayNL:
    un "Ik hoef nu niet naar mijn kamer te gaan."
    call screen bedroomdoorNL
    return  


label leave_houseNL:

    un "Oké, tijd om te gaan."
    scene bg street
    play sound "audio/trafic.mp3" loop channel "ambience"
    e "Het weer is somber, zoals altijd."
    o "Kijk uit waar je loopt, kind!"
    e "Een vrouw botst tegen je vanaf de zijkant."
    show old lady at left with moveinleft
    o "We laten mensen zoals jij toe in dit land en zo bedank je ons?"
    un "Sorry, ik bedoelde het niet zo."
    o "Lieg niet! Jullie liegen altijd over alles!"
    e "De vrouw loopt zuchtend weg."
    
    jump lobbyNL


label lobbyNL:
   
    scene black with fade
    play sound "audio/steps.mp3" channel "steps"
    $ renpy.movie_cutscene("images/doors.webm")
    stop sound channel "steps"
    stop sound channel "ambience"
    play music "audio/corp.mp3" fadein 1.0
    play sound "audio/office.mp3" loop
    scene desk 1 with fade

    e "Je komt aan bij het kantoor."
    e "De sfeer is hier totaal anders."
    e "Alsof de sombere buitenwereld hier niet bestaat."
    e "De receptioniste kijkt je even aan en gaat dan weer verder met haar werk."
    d "Kan ik je helpen?"
    show desk_anim at center
    un "Ik ben hier voor een sollicitatiegesprek bij XXX."
    d "Ah, zeker. Ga daar maar zitten."
    e "De receptioniste gaat weer verder met haar werk."
    hide desk_anim
    jump waiting_roomNL
    return


label waiting_roomNL:

    scene waiting with fade

    show waiting_anim at center
    e "Je gaat in de wachtzaal zitten."
    e "Een man staart je aan vanaf de andere kant van de zaal."
    e "En naast hem zit..."
    e "Een konijn?"
    e "Wie had gedacht dat konijnen ook konden solliciteren."
    e "Terwijl de man blijft staren, hoor je je naam uit de gang geroept."
    hide waiting_anim
    jump interviewNL
    return


label interviewNL:
    scene black with fade
    stop sound fadeout 1.0
    scene happy with fade  
    e "Een man zit achter zijn bureau."
    i "Oh. Ben je hier om het kantoor schoon te maken? Ik ben eigenlijk bezig met iets."

    menu:
        "Beledigd zijn en weggaan":
            un "Tot ziens meneer."
            scene bg street
            e "Je besluit dat dit gebrek aan respect het niet waard is en gaat naar huis."
            jump end_sceneNL
            return

        "Zeggen dat je voor het sollicitatiegesprek komt":
            un "Nee, ik ben hier voor het sollicitatiegesprek. Mijn naam is XXX."
            jump awkward_answerNL
    return


label awkward_answerNL:
    scene neutral
    i "Oh? *verward* Goed… ga zitten. *kijkt naar zijn laptop* Hm. Je naam klinkt niet buitenlands."

    menu:
        "Vragen wat hij bedoelt":
            un "*verward* Ik begrijp niet echt wat u bedoelt."
            scene angry
            i "Oh, dat was niks."
            un "*Je negeert zijn opmerking* Dus…"
            jump continuation1NL

        "Gênant lachen en doorgaan":
            un "HAHAHA ja dat hoor ik vaker."
            jump continuation2NL

        "Weglopen":
            un "Tot ziens meneer."
            scene bg street
            e "Je besluit dat dit gebrek aan respect het niet waard is en gaat naar huis."
            jump end_sceneNL
            return


label continuation1NL:
    scene neutral
    i "Dus ik zie hier dat je bent afgestudeerd aan XXX universiteit met een master?"
    un "Ja, ik ben afgestudeerd aan XXX."
    i "Ah… ik heb daar ook gestudeerd… welke professoren ken je?"

    menu:
        "Enkele professoren noemen":
            un "Ja, ik had XXX voor XXX, kent u hem?"
            i "Ja, ja *verrast* zijn lessen waren behoorlijk moeilijk."
            un "Niet echt, ik vond ze juist leuk."
            scene angry
            i "Goed, terug naar het gesprek…"
            jump part2NL

        "Vragen waarom dat belangrijk is":
            un "Ik begrijp niet echt wat dit met de job te maken heeft..."
            i "Oh, niets eigenlijk… gewoon om zeker te zijn… ik moet helaas gaan."
            e "Hij begeleidt je snel naar buiten."
            scene bg street with fade
            e "Je vraagt je af waarom hij zo vreemd deed."
            jump end_sceneNL
            return 

        "Weglopen":
            un "Tot ziens meneer."
            scene bg street with fade
            e "Je besluit dat dit gebrek aan respect het niet waard is en gaat naar huis."
            jump end_sceneNL
            return  


label continuation2NL:
    scene neutral
     
    i "Oké… is dat echt je naam? XXX?"
    
    menu:
        "Ja zeggen":
            un "Eh… ja, dat is mijn echte naam."
            scene angry
            i "Goed… laten we doorgaan."
            jump part2NL

        "Weglopen":
            un "Tot ziens meneer."
            scene bg street with fade
            e "Je besluit dat dit gebrek aan respect het niet waard is en gaat naar huis."
            jump end_sceneNL
            return 


label part2NL:
    scene neutral

    i "Voor deze job moet je er professioneel uitzien. Je kleding is prima."
    i "Maar je haar… zou je het kunnen opsteken of stijlen?"
    scene angry
    i "Ik vind de WILDE stijl leuk, maar het kan afleidend zijn op kantoor."

    menu:
        "Vragen waarom":
            e "Je kan het niet geloven."
            un "Wat is er precies niet professioneel aan mijn haar?"
            scene happy
            i "Ik hou van een sterke uitstraling, maar het is wel veel."
            un "Ik begrijp het."
            i "Goed. We nemen contact met je op."
            jump part3NL

        "Bedrijfs politiek beleefd weigeren":
            e "Je kunt het niet geloven."
            un "Ik begrijp niet waarom mijn haar niet professioneel zou zijn."
            scene angry
            i "Misschien zou het beter zijn als je het stijlt."
            un "Dat ga ik niet doen."
            i "Je hoeft niet agressief te doen."
            un "Tot ziens."
            scene bg street with fade 
            e "Je gaat naar huis."
            jump end_sceneNL
            return 
        
        "Gemeen reageren":
            e "Je kan het niet geloven."
            un "Hoe is mijn haar niet netjes? Ik geef toch geen commentaar over uw kapsel."
            scene angry
            i "Je hoeft niet te schreeuwen."
            i "Dit zijn de regels."
            i "Het gesprek is voorbij."
            scene bg street with fade
            e "Je gaat naar huis."
            jump end_sceneNL
            return 


label part3NL:
    scene neutral

    un "Welke vaardigheden zijn nodig?"
    i "Alles staat hier, het komt wel goed. Het gesprek is klaar."

    menu:
        "Vertrekken":
            e "Je verlaat het gesprek met een zwaar gevoel."
            jump end_sceneNL
    return


label end_sceneNL:
    play music "audio/game_music.mp3" fadein 1.0
    scene bg bedroom with fade

    e "Een paar dagen later komt er een mail."
    e "Bedankt voor je sollicitatie, helaas..."
    e "Je probeert je tranen in te houden."
    jump messageNL


label messageNL:
    
    scene black with fade 
    show end_anim at center
    e "Zoals velen word je beoordeeld op iets waar je geen controle over hebt."
    e "Het misdrijf?"
    jump endingNL
    return

label endingNL:
    scene black with fade
    show screen endingNL("Geboren zijn als een zwarte vrouw.")
    pause
    show screen endingNL("Misogynoir: een term voor de combinatie van anti-zwart racisme en misogynie tegen zwarte vrouwen.")
    pause
    hide screen endingNL
    call screen resources_qrNL
    return