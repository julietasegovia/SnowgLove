# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image background = im.Scale("images/background.jpg", 1920, 1080)

image snowballs_mad:
    "snowballs_mad.png"
    zoom 1.5 

image snowballs_neutral:
    "snowballs_neutral.png"
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

    scene background

    "As you manage to regain your stance you notice the snowy landscape."

    "You look to your right and notice the bag filled with your equipment. You take it with you."

    "Suddenly you remembered why your here, in the North Pole, on a cold December evening."

    "You're here to observe the aurora borealis at night."

    "But you don't remember how you got here, or how you ended up burried in snow."

    "You see a couple of buildings on the horizon and start walking towards them."

    "As you try to cover yourself from the freezing breeze, you suddenly crush into something cold."

    show snowballs_mad

    s "Hey! Watch your step lady!"

    show snowballs_neutral

    "You stare at the figure before you. Three snowballs piled on top of each other, with a carrot for nose and rocks for eyes."

    "You know what this is, this is a snowman. And did it just... talk?"

    y "I must be hallucinating... There's no way I'm getting in an argument with a snowman..."

    hide snowballs_neutral
    show snowballs_mad

    s "SNOWMAN?? I'm a snoWOMAN, thank you very much."

    s "My name is Snowballs. (the first S is silent)"

    s "And I'm sick and tired of living in the shadow of snowmen!"

    y "No, hey, I get it. I'm an astronomer, a woman in STEM..."

    s "A woman in STEM? Try being a woman in SLED. Santa's sled."

    s "That's right, that thing is wobbly. Makes me naseous!"

    # This ends the game.

    return
