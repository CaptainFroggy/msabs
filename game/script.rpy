# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Gillion")
define c = Character("Chip")
define j = Character("Jay")
define o = Character("Old Man Earl")
# image deck = "/Deck_scaled_3x_pngcrushed"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show image "Deck_scaled_3x_pngcrushed.png"
    play music "3 - Rebel's Elegy.mp3" 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    """
    Today is the day! 
    
    You are going to find out the secrets of your family, the family that you have abandoned and are now fighting against! Isn't that a wonderful thought?

    After it was decided that the Albatross would take the left path to the Navy stronghold, you've been on watch duty. You never know when the Black Sea might send a half-dozen horrifying creatures up to the surface of the unnervingly calm waters. 
    
    The gentle lapping of dark, thick water against your ship is slowly driving you insane.
    
    After an hour of sitting and watching, though, your mind can't help but wander. The day before you is a dark one. 
    
    Who knows what will happen in the stronghold? Are you leading your crew into inescapable danger? What if you discover something in the Navy stronghold that's even worse than you could have ever imagined? 
    
    Your grandmother has been hiding something, and you know that whatever it is, it isn't good. What if it's something that will loom in your shadow for the rest of your life?

    Footsteps on wooden boards hustle over to your side. You glance over and see the last member of your crew that you expected.

    """
    o "C'mon, I got work for you to do! There's juice to make!"

    "He looks at you expectantly. Did you miss something earlier? Did you accidentally agree to help him with juice-making? Juicing? You blink at him. He's being entirely serious."

    menu:
        "Keep Watch":
            j "Juice… why juice? Earl, I'm on watch, I can't - do you {i}want{/i} the ship to get attacked?"

            "Before you can even realize the mistake of objecting, Earl smacks you upside the head."

            o "And do you wanna die in that fuckin' stronghold 'cause you don't got any juice? Didn't think so! Get your stupid fuckin' ass into the kitchen, you fuckin' bitch!"
            
            "Earl hurries off, leaving a trail of curses behind him. You sigh heavily, giving the Black Sea one last calculating glare before following him. It's almost time to switch with Chip, anyways. Not that Chip's good at keeping watch and staying focused."
    
        "Obey Earl":
            j "Huh, juice. Alright, yeah, just give me a second."

            "Earl huffs and storms off, muttering something about how lazy young people are nowadays. You shake your head at the Black Sea, a small smile growing on your face. You hope you'll return to that annoying old man's complaints by the end of the night."

            "Turning around, you leave the water and your spiraling thoughts behind for the time being."

    # This ends the game.

    return
