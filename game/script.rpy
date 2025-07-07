init python:

##############################################################################
# This function is optional. Only include it if you want automatic pauses between punctuation
 #   def typography(what):
 #        replacements = [
 #               ('. ','. {w=.2}'), # Moderate pause after periods
 #               ('? ','? {w=.25}'), # Long pause after question marks
 #               ('! ','! {w=.25}'), # Long pause after exclamation marks
 #               (', ',', {w=.15}'), # Short pause after commas
 #       ]
 #       for item in replacements:
 #           what = what.replace(item[0],item[1])
 #       return what
 #   config.say_menu_text_filter = typography # This ensures the text block has the same ID value, even after all the replacements are made
##############################################################################

##############################################################################
    # This function makes the continuous text sounds
    def text_sounds_jay(event, interact=False, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # This grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): # This creates a sound queue based on how many characters are in the dialog block
                renpy.sound.queue(f"audio/blip-jay-3.wav", channel="sound", loop=False) # Change "popcat" to the name of your sound file
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")

    def text_sounds_chip(event, interact=False, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # This grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): # This creates a sound queue based on how many characters are in the dialog block
                renpy.sound.queue(f"audio/blip-chibo-3.wav", channel="sound", loop=False) # Change "popcat" to the name of your sound file
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")

    def text_sounds_gill(event, interact=False, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # This grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): # This creates a sound queue based on how many characters are in the dialog block
                renpy.sound.queue(f"audio/blip-gilly.mp3", channel="sound", loop=False) # Change "popcat" to the name of your sound file
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")
##############################################################################

define g = Character("Gillion Tidestrider", window_style="windowGill", callback=text_sounds_gill)
define c = Character("Chip", window_style="windowChip", callback=text_sounds_chip)
define j = Character("Jay Ferin", window_style="windowJay", callback=text_sounds_jay)
define o = Character("Old Man Earl")

define juiceScore = 0 #keeps track of the juice

label start:
   
    scene deck
    play music "3_rebels_elegy.mp3"

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

            "Earl huffs and storms off, muttering something about how lazy young people are nowadays. You shake your head at the Black Sea, a small smile growing on your face. You hope you'll survive your venture into the Navy stronghold and return to that annoying old man's complaints."

            "Turning around, you leave the water and your spiraling thoughts behind for the time being."

    jump kitchen

label kitchen:
    scene kitchen
    play music "5_grand_strategy.mp3"
    
    ```
    Earl leads the way to the Albatross' kitchen. Trailing close behind, you find the kitchen in a turbulent condition. The Black Sea has tossed pots and pans onto counters and shattered glass on the floor; nobody has bothered to clear everything up since the last big wave.

    Taking out a bowl, Earl places it onto an empty spot of counter. There's a pile of random "food" beside it.

    ```

    o ```I've got a stupid fuckin' kitchen to clean, so you'll have to pick out the ingredients yourself! 
    
    I grabbed a buncha shit from the fridge and put it there, grab whatcha want. Four ingredients max! Muddied juice tastes like ass.

    Whatever you choose, just take it and squeeze it over the fuckin' bowl! I know you'd refuse to do it the old-fashioned way, fuckin' bitch.```

    j "I mean, yeah, I don't want fucking diseases."

    "You wash your hands quickly in the sink before glancing over at the ingredients pile. You make your first decision."


    menu:
        "Gilly Egg":
            "Eggs go in juice, right? That sounds like a cooking thing. Does making juice count as cooking? You're cracking the egg open before you think it all the way through. However, it is the sadness that cracks your soul upon realizing your error that will remain with you forever."

            "The egg white, the yolk, and a few eggshell pieces look back at you from the bowl. You sincerely hope none of the crew contract salmonella."

            $ juiceScore += 1
            
        "Strawberries":
            "Strawberries! Those are edible, and more importantly, a recognizable juice flavor. You grab a plate of strawberries and squeeze the juice out of all of them, one by one, into the bowl."
            
            "...Okay, maybe you don't squeeze all of them. Strawberries are just too damn delicious. Maybe you munch on one while Earl isn't looking. Or a few. Or several."

            $ juiceScore += 2
       
        "Secret meat":
            "How long has this been in the fridge? You vaguely remember Duke Duke D. Dukem, Duke of Duke giving it to you, the captains of the Riptide Pirates. That was before the Block. Before you held your bow up to Gillion's heart. Before you left your family behind."

            "You squeeze the secret juice out of the secret meat as quickly as possible. Those days are long gone. Best to move past them now."

        
    "There are so many more choices to make. You hunt for your next victim in the ingredient stack."
        
    menu:
        
        "Strange Slime":
            "Sitting directly on the counter, without a plate, is about a cup's worth of purple slime. The color is actually somewhat familiar, but you can't exactly place why..."
            
            j "Earl, where'd you get this?"
            
            o "I told you it was in the fridge, you idiot! Dontcha ever listen to me?"
            
        "Coconut":
            "There is something vile and horrible residing in your soul today. Picking up a lone coconut, you cut it open with a knife and begin shaving coconut flakes into the juice. Every flake is accompanied by a piece of your heart."

            "Your crew will mutiny after this, you are sure. But the looks on their faces when they take their first sip of the juice... it will be worth it."

            $ juiceScore += 1

        "Bananas":
            "It's time to answer one of the big questions: can you juice a banana? With a strength stat of eight, the answer is no. You stare at the mashed bananas pasted onto your hands and soaking in the bowl. How could it have disappointed you so?"

            "You hope the mashed bananas will disintegrate into the rest of the juice. It'll still taste good, right?"

            $ juiceScore += 2

        
            
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
    
            "Finally, a simple {i}pop!{/i} sounds, and you are free to empty the revealed treasure into the bowl. You wipe the sweat from your brow. This is a trifling victory... but a victory nonetheless."

            $ juiceScore += 2

        "Pocket Sand":
            "None of the remaining ingredients look good enough. You frown at your creation. Surely there's something else around here that will do. Sticking your hands into your pockets, you rummage around and pull out a handful of sand."
          
            "You shrug and sprinkle it into the bowl. Nobody will even notice. A soft crunch is good for you. Besides, you're certain that half the crew has already eaten sand before."
          
        "Hot Sauce":
            "You hold three packets of hot sauce in your hands. Do you dare use them? Do you risk the wrath of your crew, your family? Could you yourself even tolerate the amalgamation it will create?"
    
            "It's for the best, you tell yourself. You need the pep in your step today - but you can't even bear to look as you tear the packets open and let the crimson fly."

            $ juiceScore += 1
            

        
    "As you mix your mysterious brew together, Earl shuffles over. He's managed to clean the entire kitchen while you made the juice. It's probably cleaner than it was before the Albatross sailed into the Black Sea."


    o "Aren't you finished yet? How long could it possibly take to make some fuckin' juice! Give that to me!"

    "Earl yanks the bowl from your hands and sweeps away."

    o "I'll finish this myself! Go tell the others this'll be out in a few! Fuckin' bitch."

    "With the old man gone, there's nothing to do but leave your possibly treacherous mistakes behind. You exit the kitchen back onto the main deck."
    
    jump deck

label deck:
    scene deck
    play music "4_pirates_legacy.mp3" 

    ```
    As you walk out, you notice that someone is lying on the deck, eyes to the sky. Their brown hair swathes their neck, and their long, red coat is unbuttoned. The bare chest that is revealed by this has a giant, black hole in it.

    You wonder if it's painful being undead. No beating heart, no light in your eyes, and no breath from your lips. What is it like to be something that should not naturally exist?

    You walk over to Chip and tower over him.

    ```

    j "What are you doing?"

    "Chip sighs dramatically and hides his eyes in an elbow. He sniffs a couple times, even though he doesn't need the air. You almost believe he's upset."

    c "Earl said there'd be juice an hour ago. If I were Gillion, I'd be having a duel with him right now. How come Earl gets off easy?"

    "Rolling your eyes, you kick his side lightly. He whimpers pathetically and doesn't budge. Geez, when did he get so attached to juice? He probably can't even taste anything, now that he's dead and all."

    j "Well, Earl's finishing it up now. Please don't kill Earl. He's old, and like, about to die anyways, if we don't get him out of here."

    c "He's so, so old... I can't believe I died before he did."

    "The playful atmosphere has evaporated. The tearfulness has faded from Chip's voice, replaced by the real tone he gets when he's sad: apathetic. He still hasn't removed the arm from his eyes, so you can't read his expression well. You know it's just another method of avoiding eye contact."

    j "Yeah, well, Earl didn't go fight a giant spider lady, did he? Something was bound to happen to one of us at some point. We're not exactly the most careful."

    c "...Yeah. And I'm the stupidest of us all."

    "Of course, he's not wrong. But Chip calling himself stupid isn't a regular occurrence, and you don't like how the comment needles into your heart. It wasn't Chip's fault that Captain Widow stole his heart. It was just the Black Sea being difficult, as it loves to be."

    j "You were unconscious, Chip. There was nothing you could've done. Gillion and I were the ones that let it happen. You can't blame yourself for something like that."

    "There's silence from him. Finally, he removes the arm from his face and sits up, still refusing to look at you."

    ```
    It's not worth it to press Chip on the issue - not right now, at least. Not when there's already so much to worry about. The last thing you need is to start a fight right when you're about to delve into one of the most dangerous places you'll ever go.

    Chip walks away towards the bow of the ship with his head down. You turn and head in the opposite direction. Your conversation with him doesn't sit right in your stomach, but you can't do anything about it now.

    You march about the ship and gather the rest of the crew. Earl likes to make a big party out of juice. Although this time, it's your juice, not his. You hope the others can't tell from how it tastes. What does Earl even put into his own juice regularly?

    Once everyone is assembled on the main deck, Earl kicks open the kitchen door and rushes over to the crew. A large silver platter is balanced on his left hand, a glass for each person teetering dangerously about.

    ```
    o "Go on, drink up! You gonna let your juice go to waste? If you don't finish it, I'll throw the rest in your face!"

    "Without needing to be told twice, the crew sip their juices politely. You watch everyone closely for their reactions."
    
    
    #play music "5_grand_strategy.mp3"

    if juiceScore == 8: 
        jump goodJuice
    elif juiceScore >= 1:
        jump okJuice
    else:
        jump badJuice
    
label badJuice:

    play music "5_grand_strategy.mp3"
   
    ```
    Queen and Gryffon are leaning against the ship's railing, cups of purplish-black ichor in hand. Now that your crew is actually about to drink your juice, you feel a deep sense of unease settle in you. Maybe juice is not supposed to look like goo.

    The pair drink from their glasses. Queen nods their head as they take a few sips, eyes burning a hole through the wooden planks in front of them. They hum in - well, not exactly pleasure. Maybe they're just humming because of their curse.

    Gryffon chugs his entire cup down. It's only after the cup is empty that a horrified expression glistens in his eyes. His eyes flicker over to Earl and then to the sea over his shoulder. He opts for the middle-ground; squeezing his eyes shut and taking a shuddering breath.

    Igneous gives his juice a puzzled look, but then shrugs and takes a normal swig. His face morphs through fifteen different phases of disgust before calming into acceptance. He sets his glass back down onto the crate behind him.

    Meanwhile, Chip is giving his bubbling tankard a visibly upset look. When he catches you watching him, he gives you a weak smile and tearfully takes a tiny sip. He nearly chokes on it but manages to keep it down.

    ```
    c "Wow! That was... delicious, Earl. And not difficult at all to drink. Gill, what do you think?"

    "Gillion doesn't respond. Standing next to Chip, his blue skin has paled into an off-white. His cup falls from his hand and clatters on the deck. The remaining liquid spills onto the deck, melting the boards like acid."

    g "“Earl, what did we do to deserve this?"

    "Everyone turns their attention to Earl, who is holding up the last glass to Drey. Drey laughs and starts walking away."

    "Drey Ferin" "Ain't no way you're gettin' me to drink that, old man."

    "Earl ignores everyone - except for you. You, he gives a challenging stare."

    o "You gonna drink that or not? Fuckin' bitch."

    ```
    Oh no. He's got you exactly where he wants you. Was this his plan all along? Did he know you would fuck up the juice this badly? Was this whole endeavor meant to teach you some sort of lesson? Are you meant to appreciate his juice more now?

    You stare at the cup in your hand. There will be consequences if you do not drink the juice, you know it. Besides, it can't be that bad - none of the others spat it out, at least. Hopefully, your stomach acid is stronger than the juice.

    Praying to Aster that you won't regret it, you take a large swig. The taste is utterly indescribable, but decidedly the worst thing you've ever drank. It leaves a burning aftertaste in the back of your throat, and heartburn has already set it. 
    
    Your stomach roils in fear; it knows what's coming. A gag reflex makes you cough, but the juice refuses to leave your body.

    ```
    j "This is... {i}great{/i}, Earl. Thanks."

    "A loud {i}thunk!{/i} draws the attention of the crew to Gryffon, who has face-planted onto the deck. He doesn't move, and a black substance is leaking out of his mouth."

    "Queen drops to their knees and shakes Gryffon's body."

    "Queen" "Gryffon, la! Are you alright, my dear friend, la?"

    ```
    Before they can make any progress in awakening him, though, Queen's expression goes blank. They collapse beside Gryffon in a similar condition.
    
    Gillion quickly rushes over to the crew members, hands lighting up with healing magic. He places his hands on the shoulders of Queen and Gryffon, but neither are revived. As the magic fades, Gillion looks over his shoulder at his fellow captains.
    ```
    g "...They're dead. Earl killed them with his sick juice."

    ```
    Dizziness overwhelms your head. A thousand questions flood before your eyes, too quick to latch onto long enough to say aloud. 
    
    How could you have possibly made a juice powerful enough to insta-kill them? Why did Earl let you make it? How is juice going to be the thing that kills you while you sail the Black Sea?
    
    You fall to your knees, and your skull hits the deck. Numbness prickles across your skin. Next time, you won't put pocket sand in your juice.
    ```
    #play music 13 - Power of Friendship.mp3
    #uncomment once we have this track

    scene black
    #change once we have special end screen
    ```
    Well done. You discovered the earliest way to die. Unfortunately, you murdered not only all three captains, but also three members of your crew. 
    
    What were you hoping to achieve with that abominable juice? Are you an assassin sent by the Navy?
    
    The only survivors of the tragic juice accident were Earl, Drey, and Finn. They attempted to dump your bodies overboard, but between a halfling, a human with unusable arms, and an old triton unable to stand for long, they gave up after twenty minutes.
    
    They abandoned the Albatross via teleporter and, once on Zero, told Ollie and Ensa the unfortunate news of your demise. 
    
    There was no time to grieve, however; they were going to need money fast, now that their bosses were dead. The trio of old men hitched a ride on a trading ship bound for Loffinlot and future prosperity.
    
    Earl set up a new juice tavern, regaining his fame and earning enough wealth to last him many lifetimes. 
    
    While Allport had drained him of his joy for juicing, returning to his hometown instead rejuvenated his passion. He was finally ready to settle down, this time with two lovers rather than just one.
    
    Finn was able to rest in Loffinlot uninterrupted. Without constantly being in mortal danger, his health improved immensely. There was always a smile on his face and a cup of juice in his hand. Twenty years later, he published the sequel to \"Dark Puckered Hole.\"
    
    Drey enjoyed life in Loffinlot with his new partners, but both those fateful nights in the Black Sea would haunt his step forever. 
    
    The raging storm and losing Arlin to the tide, and later the tragic accident of his niece and her crew's deaths. He would never know whether Arlin was alive or not, and it kept him up many a night.
    
    The Albatross drifted across inky waves eternally. The survivors of the Black Sea spoke of the ghost ship inhabited by three dead captains taken by the ichor. The Albatross sailed only at night, and the captains smote any who crossed their path.
    
    So, good job. Is this the ending you wanted? Surely not. There are still secrets to discover and lives to save. Try again - and next time, stick to the recipe.

    ```
    return

label okJuice:
    play music "5_grand_strategy.mp3"  
    
    ```
    Most of the crew are silent as they drink. Your eyes scan them as paranoia begins brewing in your gut. What if they don't like it? What if they all blame you? What if they all die because you accidentally made poisonous juice?
    
    Instead of some extreme reaction, though, everyone seems to simply... drink. 
    
    Nobody makes a fuss - although, as the seconds tick by, you're slightly annoyed that not one of them has even said anything about the juice. Aren't they polite enough for a \"thanks for making juice for everybody!\"

    You raise your glass to Earl. You will be the change you wish to see in the world.
    ```
    j "Thanks, Earl!"

    "When you knock it back, however, you understand why everyone was so hesitant. The taste is slightly off, like someone made an unwise substitution. The aftertaste is tangy and sticks to your tongue. It's not horrible, but it sure leaves a lot to be desired."

    jump chipPOV

label goodJuice:
    play music "5_grand_strategy.mp3" 
    
    ```
    Everyone hums in enjoyment as they drink their juice. You feel relief wash over you. For some unknown reason, you have a sense that you just dodged a hefty bullet.
    
    Chip takes a few massive gulps before slamming his tankard down on the barrel behind him. The specks of juice that remain fly from the force. He wipes the pink from his top lip.

    ```
    c "Amazing as usual, Earl. Got any more?"

    o "Not for you! I'm savin' myself a few glasses. You keep your dirty hands off it, or I'll kill you, fuckin' bitch!"

    c "Geez, okay, okay, I get it. I'll leave your juice alone."

    "Gillion falls to his knees, and for a moment, you worry that he has a secret allergy. But instead of choking to death, he prostrates to Earl."

    g "This juice... it is holy, Earl. Thank you for your services. I never need to consume liquid again, except through my absorbent pores."

    o "...Whateva."

    "You've gotta get in on this. Taking a sip, you're shocked by how absolutely delicious your creation is. The strawberries and bananas have blended together perfectly, and the milk and honey sweeten the mixture."
    
    "You have a hard time stopping yourself from unhinging your jaw and inhaling the rest, but you manage to cling onto your dignity."

    jump afterJuice

label afterJuice:

    ```
    Everyone begins to disperse, leaving you and your two fellow captains on the main deck. 
    
    You sidle up to the ship's wooden railing. The rosewood splinters poking your fingertips serve as a reminder that you remain safe for now as you look out towards your destination.

    No, there's nothing there, not at the moment. But you should be arriving soon, and nerves are vibrating under your skin.
    
    Gillion throws his legs over the railing and sits down on it, also looking ahead.

    ```
    g "Do you have any idea what we'll find in there, Jay?"

    j "No, not really. But it's a secret Navy stronghold, so I assume nothing too good. Who knows what they've left guarding the place."

    "Chip looks out into the ocean, bushy hair hiding his face."

    c "Whatever it is, we'll deal with it. We always do. We'll get in there, find that information Jay wants, and get out lickety-split. Besides, it can't be much worse than what we've already run into."

    "You slap Chip upside the head. He really is the biggest idiot in Mana."

    j "Great, now we're all going to die. Thanks, Chip."

    c "Hey, I'm just tryin' to liven your spirits! You've been moping all day."

    j "I've been moping? You were the one who was lying on the deck feeling sorry for yourself!"

    c "Yeah, well, you've also been a jerk!"

    g "Guys, stop, please."

    "You and Chip glare at each other. You, a jerk? Is he delusional? You've been nothing but nice to him all day. 
    
    Being totally confident in anything is just asking to be proven wrong, and you're just making sure Chip doesn't curse you all with a painful demise."

    g "I think our chances of survival are a lot higher if we don't start fighting before we even get to the stronghold. I'm sure it's not that hard to be nice to each other."

    "He's right, unfortunately. You sigh and roll your eyes, gazing back out into the ocean. Chip, too, turns away. You'll figure out whatever is wrong with Chip later."

    j "We should be there soon. Be ready for trouble."

    jump chipPOV

label chipPOV:
    scene black #change to loading screen later
    scene deck
    play music "4_pirates_legacy.mp3"

    ```
    The minutes tick by, then hours. Night falls upon the Black Sea and air sits heavily in your lungs. 
    
    You breathe not for need of oxygen, but out of habit. It's a laborious effort, but it helps you clutch onto the last strands of your humanity.
    
    Nighttime doesn't feel right here. While monsters have always haunted sleeping people from their closets and under their beds, the bristling on the back of your neck isn't natural. 
    
    Someone - or something - is watching your every move. Are they benevolent, cruel, or a neutral party? Are you falling into their trap?
    
    From across the main deck, Jay is putting her magical spyglass to her eye and peering out into the void. 
    
    It's impossible to see beyond the glowing lanterns of the ship. Everything is black, like the ichor that you spit out when nobody is watching.

    ```
    j  "Let's... pull up the rows for the night and stay here. Something's weird."

    "You don't like the confused, wary look that's growing on your fellow captain's face."

    c "Well, which direction is it?"

    g "Yeah - are we there yet?"

    "Jay sticks the spyglass back into the pouch attached to her waist and crosses her arms. In a picture where her hair should be blowing in the breeze, it appears weighed down by the world."

    j "We're basically on top of it right now."

    "Gillion casually leans slightly sideways, eyes wandering to the lapping waters below."

    g "Well, it didn't {i}sink,{/i} did it?"

    "That would make sense. You've been to a lot of crazy places during your travels, including underwater." 
    
    "It wouldn't surprise you if the Navy forced their soldiers to learn how to breathe underwater just for a guard posting."

    c "Oh, that might be how it works."

    j "I don't know. I mean, how would a stronghold sink?"

    g "I mean, it's called R.A.F.T., it would be pretty embarrassing."
    
    g "...Do you want me to check, or is that fucking crazy?"

    j "No, not in the ocean, no."

    "You think back to when Gillion pulled Jay and Earl from the ocean." 
    
    "Earl had coughed up mountains of filthy water afterwards and Jay was utterly unconscious, but Gillion had only seemed strangely shaken. You distinctly remember the water congealing into puddles of wobbly slime, left in trails around the ship from Gillion's bare feet."

    j "It definitely didn't sink."

    g "Uhhhh, ROCK TEST!"

    "Gillion snatches a stray pebble from the deck and in a blue blur, his arm winds back and shoots the pebble off into the distance in front of the ship."

    "You have a different idea, however. You can't see your stalker anywhere around you, as the darkness is cloaking them - but what if they're observing from above? Craning your head back, you narrow your eyes to cut through the black."

    "Before you can get a good look, however, a piercing caw! echoes across the water. Your eyes snap to a massive abomination that swoops over the ship." 
    
    "It has wings of thin bones that drip black ichor onto the deck as it passes over, and a human face with eyes sewn shut and no jaw."

    "Your hands jump to the swords at your sides, but your instinct isn't needed. Bright purple magic zaps the beast from the sky." 
    
    "The creature disintegrates into dust that floats down into your eyes. However, the particles don't stop you from seeing the sky and space around the ship ripple as the purple magic evaporates."

    "Adrenaline begins to seep into your system. Empty air isn't supposed to do that."

    c "We're in a test tube!"

    jump outside

label outside:
    show black #change to turrets later
    play music "1_prophetic_hero.mp3"

    ```The mirage of darkness melts like butter, revealing claustrophobic iron walls that surround the entire ship.
    
    Stretching off into the distance before you is your destination, a haunting tower that reaches into the sky. The docks are waiting for you at the foot of the tower, but they're terribly far away.

    You look back at the way you came, and horror jabs into your missing heart. The only apparent exit is through a pair of closing steel doors. The exit is narrowing, but the Albatross could still slip through if you managed to get turned around soon enough.

    Magical whirring catches your splintering attention. You snap your head skywards once more and notice something you didn't before. 
    
    Atop the walls of this bay are countless massive silver turrets. Their nozzles are elongating and aiming directly at the Albatross as the same purple energy that killed the flying creature begins to glow inside each one of them.

    This isn't exactly the best situation you've ever been in. Surely, though, you can work your way out of being blasted into oblivion - right?

    Jay clutches her head in her hands, looking around in a panic.
```
    j "So, maybe this place isn't as abandoned as I thought."

    g "Jay, you outrank these turrets, right?"

    j "{i}No?!{/i}"

    "Of course Jay would get you into this situation. She told you that the stronghold would be completely abandoned and safe to enter. 
    
    Well, it is the Black Sea, so you should have expected some sort of resistance - nothing is ever easy for the Riptide Pirates - but still! She could have set a more realistic expectation!"

    c "Jay, remember when you said that nobody was going to be here!? If we die, my last words are, 'I told you so!'"

    "Jay gives you a scathing glare but doesn't respond. You heave a sigh, knowing that now is not the time to get into an argument."

    c "In or out?"

    "She stares at you with wild eyes for a long second, then glances back and forth between the exit and stronghold. Finally, she gives you a strong nod."

    j "I think we gotta keep going."

    "You hesitate for a moment. Coming to the stronghold like Jay had wanted has already proved more dangerous than expected. What if her judgement is wrong again? Should you protect your crew and give up on the Navy secrets?"

    "If you manage to take them all out - and keep the exit doors open -, you might be able to send some of your crew to safety outside the stronghold walls while you and your fellow captains venture forth."

    "The rest of your crew have flooded onto the main deck, waiting for their captains to give them a command. Captain, what should you do?"

    menu:
        "Turn back":
            "The secrets aren't worth the trouble. Whatever secrets the Navy has in there are way too important to be accessible. There could be another Captain Widow waiting inside, ready to take the hearts of your friends."

            "The last thing you want is for your family to turn into undead monsters like you."

            c "TURN THE SHIP AROUND!"

            "Your crew hurry back downstairs to start rowing, but when you move to follow, Jay places herself between you and the door."

            j "What the fuck are you doing!? We need to keep going!"

            c "I can't do that, Jay. Not this time. I'm not risking the crew's lives for whatever you're looking for."

            j "There might be useful information for all of us! This isn't just about me. We might be able to find something that'll help us win the war."

            "As the ship turns around under your feet, Gillion lifts his arms and summons the power of storm. A massive funnel of wind propels the ship towards the bay's exit. Both you and Jay are knocked off your feet by the force of it."

            "Magic blasts fizzle out in the empty seawater you were moments before. The turrets are re-targeting at the Albatross, but you know you'll make it back out to open waters. The wind buffets hair into your eyes as you try your best to ignore Jay's betrayed expression."
        
            c "I'm not losing my crew to the Black Sea again."

            play music "4_pirates_legacy.mp3"

            "The exit doors scrape the tail end of the ship as you skim through passageway. As the Albatross slows to a stop, swaying heavily from front to back, Jay hops onto her feet and marches down into the ship, slamming the door behind her."

            "You remain sitting on the deck. The danger and the fear fade to a distant humming in your ears. Your eyes slip close, and you take a deep breath. Not because you need it. You'll never need it again. You breathe because you didn't know how dear life was until you no longer had it."

            "Until Jay's heart is ripped from her body, she will not understand your decision to run away."

            show black 

            #play music "13_power_of_friendship.mp3" 

            ``` You have achieved absolutely nothing. In fact, the only thing that has changed since you began this journey is the relationship between Jay and Chip. You really had it out for them, didn't you?

            The Riptide Pirates have all survived, but at what cost? Jay's and Chip's trust in each other has shattered. When the time comes for the next big decision, what if their stubbornness leads to a fate worse than secrets left undiscovered? What if Gillion is caught in the crossfire, or the crew?

            You are a coward. You would run from danger because you're too afraid to endanger the Riptide Pirates. But what is life without a challenge? What is life when you give up at the first skipped heartbeat?

            You do not deserve an ending. So, I leave you with this: Mana's fate is precarious. The world is at the brink of war, and you will never know if Jay and Chip are able to reconcile their differences. The tale will remain unfinished.

            Are you brave enough to start again?```

            return
        
        "Fight the Turrets":
            "You set your jaw and ignore Jay. No, there's a way you can win this without fleeing one way or the other. Your crew's lives are on the line; you will get them out."

            c "We go, the crew goes back! Jay, get the turrets off our back! Gill, keep the exit open! Crew, get a rowboat ready!"


            ```
            Jay stares at you incredulously as the crew starts preparing a rowboat. You decidedly ignore her and focus on the fiery magic bubbling under your skin. If she won't do anything about the turrets, you'll have to.

            Gillion runs past you to the other end of the Albatross and creates a large ice block between the exit doors. It halts the doors, but cracks begin running through the block. He glances over his shoulder back at you, nervously eyeing his temporary solution.
            ```

            g "That won't last for long! Who's going in the rowboat, the crew or us?"

            c "Us! So, get in!!"

            ```
            You release a powerful blast of fire magic at the nearest three turrets. Orange flames lick at the iron, and for a moment, hope burns in your chest. You've got this! Your plans always work out in the end.

            The hope fades with the fire. The turrets remain pristine in the aftermath, and the purple magic in their nozzles glow brighter than before.

            It's in this moment that you realize you were not a being built to last.
            
            You remember the feeling that surges over your body quite well. Your hands grasp at a pearl that has long since shattered as lightning cracks your skull open. 

            The nightmares are fleeing your head through the new crevice and your mouth as you scream in anguish. After your heart was stolen, you thought you'd never feel this much ever again.

            Purple swamps your vision, and your nerves are buzzing too brightly to sense anything. The hole in your chest grows. It consumes your bones, flesh, and clothes, until you are nothing but a soul and dust, lying on the deck of your ship in a breezeless hellscape.

            In the last moments before you fade from existence, you vaguely catch a glimpse of fluffy brown hair, wide green eyes, and a shining smile in the corner of your eye, like a shadow moving on its own.
            ```
            show black 

            #play music "13_power_of_friendship.mp3" 

            ```
            There is nobody left. The Riptide Pirates - and the Black Rose Pirates along with them - are all dead. It's incredible how you were able to kill so many people so quickly.

            The Albatross was obliterated along with its passengers. There was no remnant of the great heroes of Mana left. The world descended into darkness as war raged the islands and seas of the world. The Navy's iron fist tightened, and rebels died by the thousands.

            While the world burned, a small boy waited for his family to return. He stared off at the Southern Sea's horizon, waiting for the familiar frogtopus figurehead to emerge from the dark waters. Hope burned in his heart for the Riptide Pirates to return to him, to fix the world and save the dying innocents.

            Time passed, and the boy grew. He found himself in a familiar body, but he felt just as sad as the last time he wore it. That would not quell his desperate belief, though. They would return - yes, it had been six years, but that didn't mean anything.
            
            Eventually, though, when his mother laid a hand on his shoulder and drew him back inside, he did not look back.

            Will you draw his gaze to look again at the horizon?

            Will you return the shining smile to his face once more?
            ```
            return
        
        "Keep Going":
            "There's fear in Jay's expression, but determination still glints like a spark in her golden eye. At the end of the day, you trust her. If she believes you can get through this, you know you will. The crew just has to be quick about it."

            c "Fuck it. Keep going!"

            "Jay looks at you with a relieved smile on her face, and you wish it would quell the uneasiness in your bones. The crew rush to their positions at the oars, Gillion moving behind the mast and raising his hands to the sails."

            g "Everyone row like - just as an example - you're gonna get disintegrated in FOUR SECONDS!"

            "The power of storm bursts from him and the wind blasts into your sails. The bow rears toward the sky, inky water spraying across your face, and the Albatross barrels forward." 
            
            "You swear you can feel the purple, glowing magic crawling on your dead skin like a spider, moving with you as the Albatross picks up speed. From behind, you can hear the exit doors click shut. There's no turning back now."

            Gryffon "What are we gonna do when we get there if it's still aiming at us? Do we all get off the ship? Do we stay on the ship?"

            "You look at Jay and see her at the railing, knuckles white as she clutches at it, and she glances between the turrets and the dark water spanning before the ship. You follow her gaze, straining to see the path ahead, but between the distance and the rocking of the ship, you can't get a clear view."

            g "Why would they design it like this, Jay?! What kind of sick fucking Navy shit is this?"

            j "I don't know! I don't know why this is even happening. These are usually manned!"

            g "Maybe we could appeal to their emotions if they're manned. WE'RE SORRY!"

            j "They don't have emotions! No, Gill, they're unmanned."

            "Gillion's face twists in horror as he whips around to look at the turrets. You grip the mast as the Albatross rushes across the sea, toward the docks that slowly manifest from the darkness. The sharp purple glow fades as you sail further and further from the stronghold's entrance, but you remain rigid. Who knows what the range on those turrets are?"

            "The Albatross gradually slows as it approaches the docks, and in less than a minute, it's bumping into them with a crack! The tower looms above you, but your attention is elsewhere; you're waiting for the explosive power of the turrets to hit the ship and kill you alongside your entire crew."

            "Fortunately, though, it never comes."
            
            g "Do you think they're gone, Jay?"

            j "I think we're in the clear, yeah."

            "You release your breath in a whistle through your teeth. You made it - all of you did. The turrets stay quiet, and your crew and your co-captains stay alive. You are safe... for now."

            jump inside

label inside:
    play music "5_grand_strategy.mp3"

    ```
    The Albatross rocks as it's secured to the dock by your crew. Onshore, the road ahead winds toward a small town that surrounds the main tower in a ring of ruins and ash. 

    The dark shapes of Hollowed lumber through otherwise empty streets; skeletons litter the ground around the creatures, their rib cages pierced by spears pointed skyward. Old armor and swords lie fallen beneath the human remains and the feet of those who have become monstrosities.

    Dread can no longer make your stomach churn, but you feel the wariness deep in your bones nonetheless. The remnants of the town don't look like a battle; they look like a failed escape.

    Following the road further with your eyes, you see it leads to a rusting, open portcullis. Behind it looms a massively steep staircase, and although you cannot see much past the portcullis, you assume the main entrance to the actual stronghold must be at the top.

    With unease, you and your fellow captains order the crew to remain onboard and stay safe inside Finn's library, with Gryffon and Queen searching for alternative ways past the portcullis from the safety of the ship, in case you're unable to raise it from the other side. 

    With the Mirror of Life Trapping broken and Gillion's refusal to take off his bass slippers to instead wear Jay's stealthy magic boots, Gillion decides to hide in the portable hole while you and Jay sneak through the Hollowed-infested town.

    Gryffon approaches to see you off, putting a hand on Jay's shoulder once she finishes casting invisibility on the Albatross.
    ```
    Gryffon "Alright, cap. Remember, it's nighttime, so we gotta hurry. But good luck - and none of you die."
    
    j "We'll be quick."

    "You think of the heart pulled from your throat, of torn arteries and veins between your lips, of the blood you still find in your teeth. You think of the empty hole in your chest and the black ichor that rests on your tongue."

    c "Not again."

    "With a nod, Gryffon lets Jay go, allowing you to be on your way. You and Jay head down the path, darting around toppled houses to avoid the attention of the Hollowed. The buildings are decayed, some blackened and covered in soot, and others nothing more than ruins."

    

return
