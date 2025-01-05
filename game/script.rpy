# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Gillion", window_style="windowGill")
define c = Character("Chip", window_style="windowChip")
define j = Character("Jay", window_style="windowJay")
define o = Character("Old Man Earl")

define juiceScore = 0
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
            j "Juice... why juice? Earl, I'm on watch, I can't - do you {i}want{/i} the ship to get attacked?"

            "Before you can even realize the mistake of objecting, Earl smacks you upside the head."

            o "And do you wanna die in that fuckin' stronghold 'cause you don't got any juice? Didn't think so! Get your stupid fuckin' ass into the kitchen, you fuckin' bitch!"
            
            "Earl hurries off, leaving a trail of curses behind him. You sigh heavily, giving the Black Sea one last calculating glare before following him. It's almost time to switch with Chip, anyways. Not that Chip's good at keeping watch and staying focused."
    
        "Obey Earl":
            j "Huh, juice. Alright, yeah, just give me a second."

            "Earl huffs and storms off, muttering something about how lazy young people are nowadays. You shake your head at the Black Sea, a small smile growing on your face. You hope you'll return to that annoying old man's complaints by the end of the night."

            "Turning around, you leave the water and your spiraling thoughts behind for the time being."

    # This ends the game.
    jump juice

    

label juice:
    show image "Kitchen_scaled_3x_pngcrushed.png"
    play music "5 - Grand Strategy.mp3"

    ```
    Earl leads the way to the Albatross' kitchen. Trailing close behind, you find the kitchen in a turbulent condition. The Black Sea has tossed pots and pans onto counters and shattered glass on the floor; apparently, nobody has bothered to clear everything up since the last big wave.

    Taking out a bowl, Earl places it onto an empty spot of counter. There's a pile of random "food" beside it.

    ```

    o ```I've got a stupid fuckin' kitchen to clean, so you'll have to pick out the ingredients yourself! 
    
    I grabbed a buncha shit from the fridge and put it there, grab whatcha want. Four ingredients max! Muddied juice tastes like ass.

    Whatever you choose, just take it and squeeze it over the fuckin' bowl! I know you'd refuse to do it the old-fashioned way, fuckin' bitch.```

    j "I mean, yeah, I don't want fucking diseases."

    "You wash your hands quickly in the sink before glancing over at the ingredients pile. You make your first decision."

return
