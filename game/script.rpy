define g = Character("Gillion", window_style="windowGill")
define c = Character("Chip", window_style="windowChip")
define j = Character("Jay", window_style="windowJay")
define o = Character("Old Man Earl")

define juiceScore = 0 #keeps track of the juice

label start:
   
    show image "Deck_scaled_3x_pngcrushed.png"
    play music "3 - Rebel's Elegy.mp3" 

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

            $ juiceScore += 1
       
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

    jump deck

label deck:
    show image "Deck_scaled_3x_pngcrushed.png"
    play music "4 - Pirate's Legacy.mp3" 

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

    "The playful atmosphere has evaporated. The tearfulness has faded from Chip's voice, replaced by the real tone he gets when he's sad; apathetic. He still hasn't removed his arm from his eyes, so you can't read his expression well - although, you know it's just another form of avoiding eye contact."

    j "Yeah, well, Earl didn't go fight a giant spider lady, did he? Something was bound to happen to one of us at some point. We're not exactly the most careful."

    c "...Yeah. And I'm the stupidest of us all."

    "Of course, he's not wrong. But Chip calling himself stupid isn't a regular occurrence, and you don't like how the comment needles into your heart. It wasn't Chip's fault that Captain Widow stole his heart. It was just the Black Sea being difficult, as it loves to be."

    j "You were unconscious, Chip. There was nothing you could've done. Gillion and I were the ones that let it happen. You can't blame yourself for something like that."

    "There's silence from him. Finally, he removes the arm from his face and sits up, still refusing to look at you."

    ```
    It's not worth it to press Chip on the issue - not right now, at least. Not when there's already so much to worry about. The last thing you need is to start a fight right when you're about to delve into one of the most dangerous places you'll ever go.

    Chip walks away towards the bow of the ship with his head down. You turn and head in the opposite direction. Your conversation with him doesn't sit right in your stomach, but you can't do anything about it now.

    
    ```
    play music "5 - Grand Strategy.mp3"

    if juiceScore == 8: 
        jump goodJuice
    elif juiceScore >= 1:
        jump okJuice
    else:
        jump badJuice
    
label badJuice:
    #play music "5 - Grand Strategy.mp3"
    ```
    You march about the ship and gather the rest of the crew. Earl likes to make a big party out of juice. Although this time, it's your juice, not his. You hope the others can't tell from how it tastes. What does Earl even put into his own juice regularly?

    Once everyone is assembled on the main deck, Earl kicks open the kitchen door and rushes over to the crew. A large silver platter is balanced on his left hand, a glass for each person teetering dangerously about.

    ```
    o "Go on, drink up! You gonna let your juice go to waste? If you don't finish it, I'll throw the rest in your face!"

    "Without needing to be told twice, the crew sip their juices politely. You watch everyone closely for their reactions."
    
    ```
    Queen and Gryffon are leaning against the ship's railing, cups of purplish-black ichor in hand. Now that your crew is actually about to drink your juice, you feel a deep sense of unease settle in you. Maybe juice is not supposed to look like goo.

    The pair drink from their glasses. Queen nods their head as they take a few sips, eyes burning a hole through the wooden planks in front of them. They hum in - well, not exactly pleasure. Maybe they're just humming because of their curse.

    Gryffon chugs his entire cup down. It's only after the cup is empty that a horrified expression glistens in his eyes. His eyes flicker over to Earl and then to the sea over his shoulder. He opts for the middle-ground; squeezing his eyes shut and taking a shuddering breath.

    Igneous gives his juice a puzzled look, but then shrugs and takes a normal swig. His face morphs through fifteen different phases of disgust before calming into acceptance. He sets his glass back down onto the crate behind him.

    Meanwhile, Chip is giving his bubbling tankard a visibly upset look. When he catches you watching him, he gives you a weak smile and tearfully takes a tiny sip. He nearly chokes on it but manages to keep it down.

    ```
    c "Wow! That was… delicious, Earl. And not difficult at all to drink. Gill, what do you think?"

    "Gillion doesn't respond. Standing next to Chip, his blue skin has paled into an off-white. His cup falls from his hand and clatters on the deck. The remaining liquid spills onto the deck, melting the boards like acid."

    g "“Earl, what did we do to deserve this?"

    "Everyone turns their attention to Earl, who is holding up the last glass to Drey. Drey laughs and starts walking away."

    "Drey Ferin" "Ain't no way you're gettin' me to drink that, old man."

    "Earl ignores everyone - except for you. You, he gives a challenging stare."

    o "You gonna drink that or not? Fuckin' bitch"

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
    #play music 13 – Power of Friendship.mp3
    #uncomment once we have this track

    show black
    #change once we have special end screen
    ```
    Well done. You discovered the earliest way to die. Unfortunately, you murdered not only all three captains, but also three members of your crew. 
    
    What were you hoping to achieve with that abominable juice? Are you an assassin sent by the Navy?
    
    The only survivors of the tragic juice accident were Earl, Drey, and Finn. They attempted to dump your bodies overboard, but between a halfling, a human with unusable arms, and an old triton unable to stand for long, they gave up after twenty minutes.
    
    They abandoned the Albatross via teleporter and, once on Zero, told Ollie and Ensa the unfortunate news of your demise. 
    
    There was no time to grieve, however; they were going to need money fast, now that their bosses were dead. The trio of old men hitched a ride on a trading ship bound for Loffinlot and future prosperity.
    
    Earl set up a new juice tavern, regaining his fame and earning enough wealth to last him many lifetimes. 
    
    While Allport had drained him of his joy for juicing, returning to his hometown instead rejuvenated his passion. He was finally ready to settle down, this time with two lovers rather than just one.
    
    Finn was able to rest in Loffinlot uninterrupted. Without constantly being in mortal danger, his health improved immensely. There was always a smile on his face and a cup of juice in his hand. Twenty years later, he published the sequel to “Dark Puckered Hole.”
    
    Drey enjoyed life in Loffinlot with his new partners, but both those fateful nights in the Black Sea would haunt his step forever. 
    
    The raging storm and losing Arlin to the tide, and later the tragic accident of his niece and her crew's deaths. He would never know whether Arlin was alive or not, and it kept him up many a night.
    
    Across the world, the Albatross drifted across inky waves. The survivors of the Black Sea spoke of the ghost ship inhabited by three dead captains taken by the ichor. The Albatross sailed only at night, and the captains smote any who crossed their path.
    
    So, good job. Is this the ending you wanted? Surely not. There are still secrets to discover and lives to save. Try again - and next time, stick to the recipe.

    ```
    return

label okJuice:
    ```
    Most of the crew are silent as they drink. Your eyes scan them as paranoia begins brewing in your gut. What if they don't like it? What if they all blame you? What if they all die because you accidentally made poisonous juice?
    
    Instead of some extreme reaction, though, everyone seems to simply… drink. 
    
    Nobody makes a fuss - although, as the seconds tick by, you're slightly annoyed that not one of them has even said anything about the juice. Aren't they polite enough for a \"thanks for making juice for everybody!\"

    You raise your glass to Earl. You will be the change you wish to see in the world.
    ```
    j "Thanks, Earl!"

    "When you knock it back, however, you understand why everyone was so hesitant. The taste is slightly off, like someone made an unwise substitution. The aftertaste is tangy and sticks to your tongue. It's not horrible, but it sure leaves a lot to be desired."

    jump chipPOV

label goodJuice:
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

    jump chipPOV

label chipPOV:
return
