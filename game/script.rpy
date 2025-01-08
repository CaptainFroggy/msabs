# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Gillion", window_style="windowGill")
define c = Character("Chip", window_style="windowChip")
define j = Character("Jay", window_style="windowJay")
define o = Character("Old Man Earl")

define juiceScore = 0 #keeps track of the juice
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
    jump kitchen

    

label kitchen:
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


    menu:
        "Strawberries":
            "Strawberries! Those are edible, and more importantly, a recognizable juice flavor. You grab a plate of strawberries and squeeze the juice out of all of them, one by one, into the bowl."
            
            "…Okay, maybe you don't squeeze all of them. Strawberries are just too damn delicious. Maybe you munch on one while Earl isn't looking. Or a few. Or several."

            $ juiceScore += 2
    
        "Gilly Egg":
            "Eggs go in juice, right? That sounds like a cooking thing. Does making juice count as cooking? You're cracking the egg open before you think it all the way through. However, it is the sadness that cracks your soul upon realizing your error that will remain with you forever."

            "The egg white, the yolk, and a few eggshell pieces look back at you from the bowl. You sincerely hope none of the crew contract salmonella."
       
        "Secret meat":
            "How long has this been in the fridge? You vaguely remember Duke Duke D. Dukem, Duke of Duke giving it to you, the captains of the Riptide Pirates. That was before the Block. Before you held your bow up to Gillion's heart. Before you left your family behind."

            "You squeeze the secret juice out of the secret meat as quickly as possible. Those days are long gone. Best to move past them now."

        
    "There are so many more choices to make. You hunt for your next victim in the ingredient stack."
        
    menu:
        "Bananas":
            "It's time to answer one of the big questions: can you juice a banana? With a strength stat of eight, the answer is no. You stare at the mashed bananas pasted onto your hands and soaking in the bowl. How could it have disappointed you so?"

            "You hope the mashed bananas will disintegrate into the rest of the juice. It'll still taste good, right?"

            $ juiceScore += 2

            
        "Coconut":
            "There is something vile and horrible residing in your soul today. Picking up a lone coconut, you cut it open with a knife and begin shaving coconut flakes into the juice. Every flake is accompanied by a piece of your heart."

            "Your crew will mutiny after this, you are sure. But the looks on their faces when they take their first sip of the juice… it will be worth it."

            $ juiceScore += 1

        "Strange Slime":
            "Sitting directly on the counter, without a plate, is about a cup's worth of purple slime. The color is actually somewhat familiar, but you can't exactly place why…"
            
            j "Earl, where'd you get this?"
            
            o "I told you it was in the fridge, you idiot! Dontcha ever listen to me?"
            
            "Well, it's at least semi-liquid, which is more than you can say about some of your other options. You drop it into the bowl without a second thought and instantaneously repress the memory of the little scream that the slime makes as it hits the juice."

   
    "What next, master chef?"
    
    menu:
        "Milk":
            "Milk in juice makes sense. A little dairy never hurt anybody! Well, except for dairy-intolerant people. To be fair, nobody has told you that they're dairy intolerant, so if they die, it's their fault."
          
            "You start pouring milk from a jug and wait for Earl to say when. Except after half the jug has been dumped, you glance over at him and notice he's not even paying attention to you. You sheepishly put the cap back on."

            $ juiceScore += 2

        "Salted Pork":
            "Every good juice has a non-liquid. The pulp in orange juice, the boba in milk tea, the - well, actually, that's about it. But you've got the next genius non-liquid in drink idea: chunks of salted pork."

            "You grab a thick slice of salted pork and chop it into chunks, then toss it all into the bowl. When you look over at Earl for approval, there's a hint of defeat behind his usual grumpy expression. He's just a hater."

            $ juiceScore += 1

        "Black Seawater":
            j "Earl, did you - did you fill up a bottle with black seawater? This could like, fucking kill us in our sleep!"
            
            o "Can't a guy experiment? Toss it at one of your enemies if you don't like it!"
            
            "You hold the bottle at an arm's length, unsure of what to do with it. The last thing you want to do is accidentally drop it on the ship. An idea then blossoms in your mind. Earl is right; this is a good moment to experiment."
            
            "What if you can find a way to neutralize the effects of the seawater, or even inverse them? You could create the antidote for corruption from the Black Sea! This is a game changer."

            "Hope sparking in your heart, you empty the entire bottle into the bowl. This feels like the very right, very safe option to pick."

    "The stack of ingredients is nearly gone now, and the bowl is almost full. Which ingredient should you pick for the finishing touch?"
    
    menu:
        "Honey":
            "Honey is delicious in tea - it must be delicious in juice, too. You snatch a jar of honey and attempt to yank the lid off, but only wrench your hand in the process. Horrified, you realize that whoever last used it didn't remember to wipe the rim. The lid is glued shut onto the jar."
        
            "You can't let this defeat you. Not a simple honey jar, not this time. You grip the lid tightly and grit your teeth. Limbs twisting and turning this and that way, tears well in your eyes as you summon every ounce of might your body contains."
    
            "Finally, a simple pop! sounds, and you are free to empty the revealed treasure into the bowl. You wipe the sweat from your brow. This is a trifling victory… but a victory nonetheless."

            $ juiceScore += 2
  
        "Hot Sauce":
            "You hold three packets of hot sauce in your hands. Do you dare use them? Do you risk the wrath of your crew, your family? Could you yourself even tolerate the amalgamation it will create?"
    
            "It's for the best, you tell yourself. You need the pep in your step today - but you can't even bear to look as you tear the packets open and let the crimson fly."

            $ juiceScore += 1

        "Pocket Sand":
            "None of the remaining ingredients look good enough. You frown at your creation. Surely there's something else around here that will do. Sticking your hands into your pockets, you rummage around and pull out a handful of sand."
          
            "You shrug and sprinkle it into the bowl. Nobody will even notice. A soft crunch is good for you. Besides, you're certain that half the crew has already eaten sand before."
          
    "As you mix your mysterious brew together, Earl shuffles over. He's managed to clean the entire kitchen while you made the juice. It's probably cleaner than it was before the Albatross sailed into the Black Sea."


    o "Aren't you finished yet? How long could it possibly take to make some fuckin' juice! Give that to me!"

    "Earl yanks the bowl from your hands and sweeps away."

    o "I'll finish this myself! Go tell the others this'll be out in a few! Fuckin' bitch."

    "With the old man gone, there's nothing to do but leave your possibly treacherous mistakes behind. You exit the kitchen back onto the main deck."

    if juiceScore == 8:
        "amazing juice good job"
    elif: juiceScore >= 0:
        "ok juice, it's fine"
    else:
        "terrible jiuce awful job"

return
