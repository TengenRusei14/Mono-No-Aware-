# 5 Characters
define n = Character("Narrator")
define mc = Character("Serious Samurai")
define wc = Character("Hanna")
define h = Character("Hanaki")
define c = Character("Shouganai")
define u = Character("Ukiyo")

default wheel_result = ""
default wheel_options = []
default wheel_display = []

init python:
    import random

    def spin():
        global wheel_result
        wheel_result = random.choice(wheel_options)

label wheel:

    n "The Wheel of Fate begins to spin..."

    python:
        import random

        for i in range(18):
            idx = random.randint(0, len(wheel_display) - 1)
            renpy.show(
                "text",
                what=Text(wheel_display[idx], size=60, color="#ffffff"),
                at_list=[truecenter]
            )
            renpy.pause(0.08)
            renpy.hide("text")

    $ spin()

    $ final_index = wheel_options.index(wheel_result)

    show text "[wheel_display[final_index]]" with dissolve
    pause 1.5
    hide text with dissolve

    return

label splashscreen:
    show text "Valerian Crow" with dissolve
    pause(2)
    hide text with dissolve
    pause(1.5)

    show text "Disclaimer \n This is a special type of Visual Novel that aligns with the Juniper Dev very serious game jam and that is spin to win so instead of allowing you to choose your options yourselves the wheel of fate shall decide and there are multiple endings to explore so let's see if you are lucky enough to play both in less than 3 attempts" with dissolve
    pause(10)
    hide text with dissolve
    pause(1.5)
    return

label start:
    n "Awaken dear Samurai"
    n "You have travelled far beyond the living world"
    n "In search of your wife 'hanaki'"
    n "A love so serious and pure, but be warned samurai you do not have free will...."
    n "Everything is decided by the wheel of fate"

    "You slowly begin to wake up and check who is it that was speaking to you"
    "But you find no one, just your body laying on the endless snow in an unknown world"
    "But you know as to why you came here"
    
    show ss at right
    mc "hanaki"
    mc "Where have you gone?"
    mc "Your soul is not bound to this world"
    mc "I shall take you back with me"
    mc "To our home......and our son...."
    mc "Shiba"
    hide ss

    "You open your eye's and focus on the world ahead"
    "An endless terrain covered in snow"
    "It's different from the land you imagined"
    "It was quite peaceful, and really quiet"
    "You then thought to yourself....."

    show ss at right
    mc "If Hell is this peaceful, then how would heaven be"
    mc "But that is straying from my objective"
    mc "I will find her"
    hide ss 

    show text " Love " with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    "You begin to walk for hours on end"
    "And you find yourself at a intersection, there are 2 paths and only one is the right one"

    $ wheel_display = ["Left", "Right"]
    $ wheel_options = ["good", "bad"]

    call wheel from _call_wheel

    jump expression wheel_result

label good:
    "You decide to go left"
    "And continue walking until you discover a small village down ahead"
    "Although desolate you decide to go either way"
    "You arrive and at the entrance and find a girl"
    "A fairly young maiden bearing a sword"
    "And behind her......"
    "You see an endless amount of graves stretching beyond the horizon"
    "More than your brother's at Sengaku-Ji"

    show ss at right
    mc "Is death what you wish to protect"

    show hanna at left
    wc "Ironic"
    wc "The dead dying in the land of the death"
    wc "The dead suffer twice as if once was not enough"
    wc "But I shall honor their death's once more"

    show text "Honor" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    mc "I respect you"
    mc "But I must go through"

    wc "And step on the souls of the poor?"

    mc "I am in search of a soul....."
    
    wc "The soul that belongs to your wife"
    wc "A faithful husband with a hopeless dream"

    mc "How did you know?"

    wc "You are not the first and sadly not the last"
    wc "You do not belong here, return home"
    wc "I shall not let you pass"
    hide ss
    hide hanna

    $ wheel_display = ["Respect Her Wishes", "Kill hanna"]
    $ wheel_options = ["good1", "bad1"]

    call wheel from _call_wheel_1

    jump expression wheel_result

label good1:
    "You understand the value of a soul"
    "For you have lost one yourself"
    "You have my....."

    show text "Respect" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show ss
    mc "I understand"
    mc "I shall be on my way"
    
    "You were never a fan of many words"
    "So you simply wander back into the distance"
    "And begin contemplating on your objective"
    "Is what you want truly worth it"
    "Is your wife really in need of saving serious samurai?"

    mc "Before I go I have a question young lady"
    mc "You seem to know a lot about this place"

    show hanna
    wc "This is Hellheim"
    wc "The land where the dead live a new life"
    wc "Some even form families and begin new lives"
    wc "But if you truly wish to find her then I suggest travellng to the Land of Norse"
    wc "Just head north until you find another village"

    mc "You have my thanks"

    wc "No worries, Serious Samurai"

    "You are shocked and question how she knows your name"
    "But you do not question"
    "You feel it in your guts...."
    "She is way stronger than you would ever be"
    "So you begin to depart"
    hide ss
    hide hanna

    $ wheel_display = ["North", "South"]
    $ wheel_options = ["north", "south"]

    call wheel from _call_wheel_2

    jump expression wheel_result

label north:

    "You decide to follow the young maidens instructions"
    "You begin to go North"
    "Travelling for what seemed like 5 days"
    "But there was no way to tell, all you see is snow"

    show ss
    mc "A village"
    mc "One where the dead are living"
    hide ss

    "And in the distance you see her....."
    "hanaki"
    "But she is not alone"
    "There is a man and a kid alongside her"
    "And she seems to be....."

    show text "Happy" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    "The young maiden was right"
    "She has started a new life here, And has seemed to forget about you and Shiba"
    "You feel enraged"
    "You came all this way just to find her with a new family"

    $ wheel_display = ["Approach hanaki", "Return Home"]
    $ wheel_options = ["b_ending", "m_ending"]

    call wheel from _call_wheel_3

    jump expression wheel_result

label m_ending:

    show ss
    mc "We all move on"
    hide ss

    show text "Mono no aware" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show ss
    mc "We are all souls, we are bound to ourselves"
    mc "And not anyone else"
    mc "I came her to save her, but all that I came here for is to lie to myself"
    mc "I knew she was gone but kept refusing"
    hide ss
    
    show text "Everything ends - and because it does, it matters more." with dissolve
    pause(2.5)
    hide text with dissolve
    pause(1.5)

    show text "So letting things go isn't denial, it is accepting that it's existence is simply a portion of the love and the memory is worth much more." with dissolve
    pause(2.5)
    hide text with dissolve
    pause(1.5)

    "You have learnt a lot"

    show text "Serious Samurai" with dissolve 
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show text "Good Ending" with dissolve
    pause(1.5)

    return


label bad:

    "You decided to take the right path"
    "Right sounds like right doesn't it"
    "You travel down the road for week searching for any form of civilisation"
    "And there it was"
    "And as you look closer you begin to see a familiar face"
    "And that face is that of......"

    show text "hanaki" with dissolve
    pause(1.5)
    hide text with dissolve    

    "But she is not alone"
    "She has a kid about the age of Shiba"
    "And a man holding her hand"
    "You are enraged and decide to walk all the way to the town"
    "But you do not do anything just yet"
    "You decide to watch before reacting"

    show ss at right
    mc "This is a lie"

    show hannaki at left
    h "Honey where are we going"
    hide hannaki

    show shouganai at left
    c "Don't worry dear I have a suprise for the both of yall"
    hide shouganai

    show ukiyo at left
    u "Yayy!!"
    hide ukiyo

    "Your blood continues to boil"
    "You decide to take action"

    $ wheel_display = ["Kidnap Her", "Let her go"]
    $ wheel_options = ["b_ending", "m_ending"]
    
    call wheel from _call_wheel_4

    jump expression wheel_result

label bad1:
    "You draw your blade."

    show hanna at left
    wc "So this is your answer."

    show ss at right
    mc "Forgive me."

    "The village falls silent."

    "One swift strike is all it takes."

    "hanna falls into the snow."

    "The graves remain unguarded."

    "You continue your journey."

    "Rows upon rows of graves stretch beyond the horizon."

    "Days pass."

    "You continue walking."

    "The cold grows harsher."

    "The snow grows deeper."

    "There is no village."

    "There is no hanaki."

    "Only endless graves."

    mc "I have come too far..."

    "Your legs finally give way."

    "You collapse into the freezing snow."

    "Your eyes slowly close."

    "Another grave is added to HellHeim."
    hide ss
    hide hanna

    show text "Disgusting" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show text "Serious Samurai" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show text "Bad Ending" with dissolve
    pause(1.5)

    return


label south:

    "You ignore hanna's advice."

    show ss at right
    mc "North or south makes no difference."

    "You begin walking south."

    "One day passes."

    "Then another."

    "Nothing changes."

    "Only endless snow."

    "There is no village."

    "No souls."

    "No sign of hanaki."

    "Your food is long gone."

    "Your strength begins to fade."

    mc "Was I..."

    mc "Wrong?"

    "Your body can no longer endure the freezing cold."

    "You collapse into the snow."

    "The wind slowly buries your body."
    hide ss

    show text "Lost" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show text "Serious Samurai" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show text "Bad Ending" with dissolve
    pause(1.5)

    return


label b_ending:

    "You step out from your hiding place."

    show ss at right
    mc "hanaki."

    "She turns toward you."

    show hannaki at left
    h "Can I help you?"

    mc "It's me."

    mc "Your husband."

    h "..."

    h "I'm sorry."

    h "I don't know who you are."

    mc "No."

    mc "You're lying."
    hide hannaki

    show shouganai at left
    c "Sir."

    c "Please leave my family alone."
    hide shouganai

    mc "She is MY family!"

    show ukiyo at left
    u "Mom..."
    hide ukiyo

    "Your anger overwhelms your reason."

    "You draw your sword."
    show hannaki at left

    h "Stop!"

    "Steel cuts through the quiet air."

    "The snow is stained red."
    hide hannaki

    show ukiyo at left
    u "Dad!"

    "hanaki falls to her knees beside the lifeless body."
    hide ukiyo

    show hannaki at left
    h "Why..."

    h "Why would you do this?"

    mc "Come with me."

    h "Never."

    "You seize her arm."

    "She struggles."

    "You drag her away from the only home she remembers."

    "Days later, you return to the world of the living."

    "The ritual succeeds."

    "hanaki opens her eyes."

    "But they are empty."

    "She speaks no words."

    "She shows no emotion."

    "She simply exists."

    mc "..."

    mc "hanaki?"

    "There is no reply."

    "You got exactly what you wished for."

    "And lost everything that mattered."
    hide ss
    hide hannaki
    hide shouganai
    hide ukiyo
    
    show text "Obsession" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show text "Serious Samurai" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    show text "True Bad Ending" with dissolve
    pause(1.5)

    return


