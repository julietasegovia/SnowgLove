# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image background = im.Scale("images/background.jpg", 1920, 1080)
image town = im.Scale("images/town.jpg", 1920, 1080)
image shop = im.Scale("images/shop.jpg", 1920, 1080)
image igloo = im.Scale("images/igloo.jpg", 1920, 1080)
image workshop = im.Scale("images/workshop.jpg", 1920, 1080)
image end = im.Scale("images/end.jpg", 1920, 1080)
image end_screen = im.Scale("images/end_screen.jpg", 1920, 1080)

image snowballs_mad:
    "snowballs_mad.png"
    zoom 1.5 

image snowballs_neutral:
    "snowballs_neutral.png"
    zoom 1.5 

image snowballs_smile:
    "snowballs_smile.png"
    zoom 1.5 

image poly_mad:
    "poly_upset.png"
    zoom 1.5 

image poly_neutral:
    "poly_neutral.png"
    zoom 1.5 

image poly_smile:
    "poly_smile.png"
    zoom 1.5 

image pingui_mad:
    "pingui_mad.png"
    zoom 2

image pingui_neutral:
    "pingui_neutral.png"
    zoom 2 

image pingui_smile:
    "pingui_smile.png"
    zoom 2 

image mus_mad:
    "mus_mad.png"
    zoom 1.5

image mus_neutral:
    "mus_neutral.png"
    zoom 1.5

image mus_smile:
    "mus_smile.png"
    zoom 1.5

define pi = Character("Pingüí", color="#103f79")
define m = Character("Mus", color="#725440")
define po = Character("Poly", color="#ffee8c")
define s = Character("Snowballs", color="#79e1af")
define y = Character("You", color="#e2e3e6")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "..."

    "You wake up."
    
    "You feel your legs getting numb from the cold as you brush off a pile of snow out of your face."

    scene background with fade

    "As you manage to regain your stance you notice the snowy landscape."

    "You look to your right and notice the bag filled with your equipment. You take it with you."

    "Suddenly you remembered why your here, in the North Pole, on a cold December evening."

    "You're here to observe the aurora borealis at night."

    "But you don't remember how you got here, or how you ended up burried in snow."

    "You see a couple of buildings on the horizon and start walking towards them."

    "As you try to cover yourself from the freezing breeze, you suddenly crush into something cold."

    show snowballs_mad

    s "Hey! Watch your step lady!"

    "You stare at the figure before you. Three snowballs piled on top of each other, with a carrot for nose and rocks for eyes."

    "You know what this is, this is a snowman. And did it just... talk?"

    y "I must be hallucinating... There's no way I'm getting in an argument with a snowman..."

    s "SNOWMAN?? I'm a snoWOMAN, thank you very much."

    s "My name is Snowballs. {i}The first S is silent.{/i}"

    s "And I'm sick and tired of living in the shadow of snowmen!"

    y "No, hey, I get it. I'm an astronomer, a woman in STEM..."

    s "A woman in STEM? Try being a woman in SLED."

    s "That's right, that thing is wobbly. Makes me naseous!"

    hide snowballs_mad
    show snowballs_neutral

    s "Anyways..."

    s "I've never seen you before."

    s "Where you heading?"
    
    y "I, uh... I don't know."

    y "I mean, I have nothing to do until midnight."

    "Snowballs goes quiet for a bit"

    hide snowballs_neutral
    show snowballs_smile

    s "Fine. Follow me."

    hide snowballs_smile

    "Snowballs turns around."

    "Then, you see only the snowball on the bottom of Snowballs structure start to roll forward, leaving a trail of the same diameter."

    "You question if wether or not following a talking snowma... snowoman is the smartest choice."

    "But you realize you don't have any other choice."

    "So you follow."

    scene town

    show snowballs_smile

    s "This is the town."

    s "You have a while before midnight, just hang out here 'til then."

    s "Anyways, I have to leave. I'm heading to the sauna."

    hide snowballs_smile

    s "See ya, astronomer!"

    "You can't even argue before the snowoman leaves."

    "You're still a little numb from the snow as you register this new place."

    "You look around."

    "Where should you go?"

    menu:
        "Gift Shop":
            jump shop

        "Misterious Factory":
            jump workshop

        "Outside of Town":
            jump igloo

    label shop:
        scene shop with fade

        "You enter a warm and lively gift shop."

        "Your typical store background music is playing. Each shelve decorated with cringy but unique christmas ornaments."

        "Everything in this store seems calm and slow."

        pi "FORTY DOLLARS?"

        "You turn around to see the person screaming."

        show pingui_mad

        "A penguin is screaming to himself as he holds a miniature reindeer statue."

        pi "Can you believe it? Forty dollars!"

        y "That's... quite pricy, yeah"

        pi "They should be ashamed of themselves"

        hide pingui_mad
        show pingui_neutral

        y "From all the things I've seen today this shouldn't be the one catching my eye but..."

        y "Aren't penguins from the South Pole?"

        pi "God forbid a hardworking non-flying bird takes a little vacation"

        hide pingui_neutral
        show pingui_smile

        pi "Yeah, I'm from the south. Where Christmas is in Summer!"

        pi "I bet that old man on the red suit melts each time he crosses the Equator..."

        hide pingui_smile
        show pingui_neutral

        pi "Now, I might be a tourist but you don't look like a local either."

        y "You're right, I'm an astronomer. I'm just here to see the aurora."

        hide pingui_neutral
        show pingui_smile

        pi "Oh! I got recommended this aurora attraction a bunch!"

        pi "Tell ya what, if you help me {i}steal this statue{/i} I'll take you to the best spot to watch the aurora!"

        pi "Whatcha say?"

        menu:
            "Hell no, I'm out":
                jump back_to_town
            "Uh... Sure...":
                jump pingui_yes

    label pingui_yes:

        pi "That's what I'm talking about!"

        hide pingui_smile
        show pingui_mad

        pi "Now, quick. Hide it with your equipment. And walk out with a straight face."

        "You walk out of the store avoiding eye contact as much as possible."

        scene town with fade

        show pingui_smile

        pi "Ha! You're a hell of a criminal, north girl!"

        hide pingui_smile
        show pingui_neutral

        pi "Thanks a bunch! My feathers are to clumsy for me to do this alone."

        y "Yeah... Sure, can you take me to see the aurora now?"

        pi "Ah, of course! You ain't no dumb criminal!"

        pi "Follow me, north girl!"

        jump end

    label workshop:
        scene workshop with fade

        "The building is huge."

        "Every single light of every single room seems to be lit."

        "You can hear the muffled noises of many people chatting there."

        "You're still too far to figure out what any of it is."

        "As you get closer you see someone lurking outside."

        menu:
            "Go ask the person where to see the aurora.":
                jump mus_yes

            "Go back to town to try better luck":
                jump back_to_town


        label mus_yes:
        "You slowly approach that person, looking for directions"

        y "Excuse me..."

        m "EEK!"

        "The person jumps and you take a few steps back"

        show mus_mad 

        m "SHH!"

        y "What do you mean shh? You just screamed!"

        m "I'm undercover! No one can find me!"

        y "Huh?"

        m "{i}Sigh...{/i}"
        
        m "I shouldn't be telling you this but I need to take this weight off my shoulders"
        
        hide mus_mad
        show mus_neutral

        m "I know I look like a reindeer..."

        y "{i}You look like a moose with a plastic clown nose on...{/i}"

        m "But I'm actually a moose, sent by the Canadian Uinted Moose to spy on the reindeer."

        hide mus_neutral
        show mus_mad

        m "We are sick and tired of everyone loving reindeers. Moose are cool too!"

        m "I'm here to watch and learn why do people love them so much. Soon, we moose will be as popular and loved as reindeer!"

        hide mus_mad
        show mus_neutral

        m "..."

        m "Uh... And who are you?"

        y "I'm an astronomer looking for the perfect spot to watch the aurora."

        m "You're not a local. Y-you're not Canadian are you? You can't tell anyone what I just told you!"

        y "..."

        y "Ugh... Fine."

        show mus_smile

        m "THANK YOU!"

        hide mus_smile
        show mus_neutral

        m "After I'm done with my secret mission, let me take you to see the aurora!"

        y "Sounds great"

        jump end




    label igloo:
 
        scene igloo with fade
        "You start heading away from the lights and buildings."

        "The breeze violently moves your lashes as you step further into the dark."

        "You see a big pile of snow at the distance."

        "Like, you could fit inside that snow pile."

        play sound "roar.mp3"

        "..."

        "You freeze. And not because of the cold."

        "You're fingers tremble in fear as you slowly accept the fact that you're now bear food."

        po "Oh, sorry."

        show poly_neutral

        po "My yawns are pretty loud sometimes."

        "You're still quivering as you look up to the big white bear in front of you."

        "The bear looks at you confused. As you don't answer, they take the lead again."

        hide poly_neutral
        show poly_smile

        po "My name is Poly, that igloo right there is my home."

        hide poly_smile
        show poly_neutral

        po "Now, I don't know many of the town folk, but you seem forgein"

        y "Uh, yeah, I'm not from here. I'm just here for an anstronomic investigation... I want to see the aurora borealis."

        y "I don't blame you for not going to town often... That place is a little crazy"

        hide poly_neutral
        show poly_mad

        po "Right..."

        po "I'm just not too comfortable around most people."

        y "You seem pretty comfortable around me"

        hide poly_mad
        show poly_smile

        po "Really? I've been really practicing on not beign akward"

        po "..."

        hide poly_smile
        show poly_neutral

        y "..."

        po "Uh, so... What's your favorite milk?"

        y "..."

        y "Uh... skimmed"

        po "Cool, cool"

        po "..."

        y "..."

        menu:
            "You don't need to try so hard to make people like you, for the little time I've known you, I think your really cool":
                jump poly_yes
            "k bye":
                jump back_to_town 

    label poly_yes:
        show poly_smile

        po "Seriously? You mean that?"

        po "That's so sweet astronomer! Thank you"

        po "..."

        po "You know, there's a very nice spot by my igloo to see the aurora..."

        hide poly_smile
        show poly_neutral

        po "Uh would you wan't to come, maybe? If you're not busy, that is..."

        menu:
            "I'd love that":
                jump poly_yes_yes
            
            "I'm alright":
                jump poly_no

    label poly_yes_yes:

        show poly_smile

        po "A-Awesome"

        po "Follow me!"

        jump end

    label poly_no:
        
        show poly_neutral

        po "Oh, right, I get it."

        po "But if you change your mind, you know where to find me."

        jump back_to_town

    label back_to_town:
        scene town with fade

        "Well..."

        "That was a weird interaction."

        "Let's Ignore that and go somewhere else."

        menu:
            "Spa":
                jump sauna

            "Gift Shop":
                jump shop

            "Misterious Factory":
                jump santa

            "Outside of Town":
                jump igloo

    label end:

        scene aurora with fade
        "You made it."

        "You got to see the aurora."

        "And your new friend is right there with you."

        "It's beautiful."

        "Wait..."

        play sound "sleigh.mp3"

        "What's that sound?"

        scene end with fade

        play music "sleigh_ride.mp3"

        "..."

        "Oh my god."

        scene end_screen with fade

        ""

    scene 
    # This ends the game.

    return
