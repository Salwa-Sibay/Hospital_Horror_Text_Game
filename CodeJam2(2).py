#A small roleplay text game where the user has choices to pick and based on their
#choices, they'll get different results.

#For improvements: Add descriptions of the rooms, make the time they can stay in
#that room random, also make it so that they meet different nurses in the halls
#the rooms will be in a dictionary and without a passcard you cannot enter them
#the nurses may open the door for you but after you leave, the door will
#automatically close and deleted from the dictionary so you can't enter it again.

#^Didn't do all that, I'll focus on adding "graphics" or turtle drawings so the
#player can visualize their surroundings better, should also add something that
#lets you store the people you meet and what you know about them, should probably
#create a while loop for hp and throw the welcome part also in a function just
#so it can rewind.

#Add graphic for hallway, also add more text based options that can lower your
#hp, might also add a 'time' clock so you know how long you are/were playing,
#the ability to logout would be nice too. Might add a place where you can type
#in your own clues to remember.

#Adjust clues to function, make it so you can also remove clues. Show how many
#clues the person has, maybe add hints for clues? Expand on moving to rooms. Btw,
#search up the flower language, I will add some minor hints in seemingly
#unimportant details.

import time
import random
import turtle

hp=100

r=random.randint(1, 3)
b=random.randint(4, 6)
s=random.randint(7, 9)

Clues=[]

def draw_1():
    leo=turtle.Turtle()
    beo=turtle.Turtle()
    seo=turtle.Turtle()
    geo=turtle.Turtle()

    leo.hideturtle()
    beo.hideturtle()
    seo.hideturtle()
    geo.hideturtle()

    geo.color("grey")
   
    beo.penup()
    beo.goto(150, 50)
    beo.pendown()
    beo.backward(600)

    leo.penup()
    leo.goto(-100, 0)
    leo.pendown()
    for num in range(4):
        leo.forward(200)
        leo.right(90)

    seo.penup()
    seo.goto(150, -200)
    seo.pendown()
    seo.left(90)
    seo.forward(400)
    
    seo.penup()
    seo.goto(150, -125)
    seo.pendown()
    seo.right(90)
    seo.forward(400)

    seo.penup()
    seo.goto(150, -150)
    seo.pendown()
    seo.forward(400)

    seo.penup()
    seo.goto(150, -75)
    seo.pendown()
    seo.forward(50)
    seo.right(90)
    seo.forward(15)
    seo.left(90)
    seo.forward(350)

    leo.penup()
    leo.goto(150, 200)
    leo.pendown()
    leo.forward(50)
    leo.right(90)
    leo.forward(15)
    leo.left(90)
    leo.forward(350)

    leo.penup()
    leo.goto(150, 125)
    leo.pendown()
    leo.forward(400)

    geo.penup()
    geo.begin_fill()
    geo.goto(215, 175)
    geo.pendown()
    geo.goto(350, 160)
    geo.right(90)
    geo.forward(75)
    geo.goto(215, 100)
    geo.goto(215, 175)
    geo.end_fill()

    leo.penup()
    leo.goto(150, 70)
    leo.pendown()
    leo.forward(400)

    beo.penup()
    beo.goto(-200, 50)
    beo.pendown()
    beo.left(90)
    beo.forward(400)

    geo.penup()
    geo.begin_fill()
    geo.goto(-225, 175)
    geo.pendown()
    for num in range(4):
        geo.forward(15)
        geo.right(90)
    geo.end_fill()

def draw_2():  
    leo=turtle.Turtle()
    seo=turtle.Turtle()
    geo=turtle.Turtle()
    beo=turtle.Turtle()

    leo.hideturtle()
    seo.hideturtle()
    geo.hideturtle()
    beo.hideturtle()

    geo.color('grey')
    beo.color('white')
    
    seo.pensize(5)

    beo.penup()
    beo.begin_fill()
    beo.goto(-550, 550)
    beo.pendown()
    for num in range(4):
        beo.forward(1000)
        beo.right(90)
    beo.end_fill()

    leo.penup()
    leo.goto(-375, -25)
    leo.pendown()
    leo.forward(700)

    leo.penup()
    leo.goto(-250, -25)
    leo.pendown()
    leo.left(90)
    leo.forward(400)

    geo.penup()
    geo.begin_fill()
    geo.goto(-285, 125)
    geo.pendown()
    for num in range(2):
        geo.forward(25)
        geo.right(90)
        geo.forward(50)
        geo.right(90)
    geo.end_fill()

    seo.penup()
    seo.goto(-275, 275)
    seo.pendown()
    seo.goto(-400, 275)

    leo.penup()
    leo.goto(-175, -25)
    leo.pendown()
    leo.forward(400)
    leo.penup()
    leo.goto(-25, -25)
    leo.pendown()
    leo.forward(400)

    seo.penup()
    seo.goto(-50, 275)
    seo.pendown()
    seo.goto(-150, 275)

    seo.penup()
    seo.goto(-35, 100)
    seo.pendown()
    seo.left(180)
    seo.forward(25)

    leo.penup()
    leo.goto(325, -25)
    leo.pendown()
    leo.forward(400)
    leo.penup()
    leo.goto(175, -25)
    leo.pendown()
    leo.forward(400)

    seo.penup()
    seo.goto(200, 275)
    seo.pendown()
    seo.goto(300, 275)

    seo.penup()
    seo.goto(310, 100)
    seo.pendown()
    seo.forward(25)

def who_blue_pup():
    insrt=int(input("How many clues do you want to add? "))
    for i in range(insrt):
        add=input("Clue: ")
        Clues.append(add)

    print("These are your clues so far "+str(Clues))
    dnsrt=input("Do you want to delete any clues?\n(Yes)(No) ")
    if dnsrt=="Yes":
        print("You have", len(Clues), "clues.")
        print(str(Clues))
        sd=str(len(Clues))
        ds=int(input("Which number do you want to delete? (0-"+sd+")"))
        Clues.remove(Clues[ds])
        print("These are your current clues "+str(Clues))

#||==##==--~  just here to split up text and graphics  ~--==##==||#

def start_game():
    
    draw_1()

    pa=input("Oh? A visitor? When did you get here? I'm Louise, I seem to have\
 forgotten your name again?\n(Insert your name) ").title()
    time.sleep(b)

    print("'Oh yeahh, now I remember, you're that funky little student! How's ____\
 been doing lately?'\n'Haven't seen them in a while...'")
    time.sleep(r)

    print("*Louise looks out the small window and her face stretches into a sad\
 smile*")
    time.sleep(s)

    print("'Being in this hospital all day long is tiring, the memories and days just\
 blend you know?'")
    time.sleep(r)
    ba=input("(Stay silent)(Smile and nod) ")


    if ba=="Stay silent":
        print("*Louise sharply turns around, her eyes have a strange glint in them*")
        time.sleep(r)
        print("'Say, what's wrong with you? You don't seem as you usually do'\n*Sh\
e abruptly smiles and a shiver moves down your back*")
        time.sleep(b)
        print("'Say, who are you?'")
        sa=input("(Stay silent)(What do you mean?) ")
        time.sleep(r)
        
        if sa=="Stay silent":
            print("*The room grows quiet, she keeps staring at you, the smile is gone\
 from her face, then a noise interrupts*")
            time.sleep(b)
            print("'Wahh, I'm so sorry I came late! Huh?",\
 pa, "is here? Wowww, we haven't seen you in a while! How's ____? All of us\
 nurses are worried for him you know?~'\n*You look up and see a young nurse, with\
 a hairstyle that's just as energetic as her voice. She winks and smiles at you*")
            time.sleep(s)
            print("'"+pa+", do you mind leaving the room real quick? Nurse Jane has\
 to help miss Louise with her clothes~'")
            time.sleep(b)
            print("'Can you please speak like an actual nurse, Jane?'\n'Aww, you\
're so boringggg'")
            time.sleep(b)
            print("*You leave the room, there's a large hallway before you and you\
 shiver*\n*Your back is drenched with cold sweat, somehow miss Louise doesn't\
 strike you as an innocent lady...*")
            draw_2()
            ha=1

        if sa=="What do you mean?":
            print("'...'\n'Aiyah, I was just joking, no need to take me seriously. You\
 're probably really stressed with school and you still come and see us old people'\
 \n*Louise smiles again, but this time it seems more real*")
            time.sleep(b)
            print("*Now you are much more relaxed after understanding part of the\
 situation. You chat with the old lady peacefully, soon, someone comes in*")
            time.sleep(r)
            print("*A young nurse with a slight smile walks in, her hair seems to\
 bounce with each step she takes and her aura screams cheerful*")
            print("'Oh?", pa+"? EEEH?! Wow, you're here! Hey, where's ____? Aww, \
 I guess he probably got sick of us old nurses...'\n'Hey! Jane, do your job\
 properly!'\n'Aw shucks Miss Louise, I didn't mean to be late! Um,", pa, "do\
 you mind leaving the room real quick? I need to change Louise's clothes.'")
            time.sleep(s)
            print("*You get up to leave and find out that your back is drenched with\
 cold sweat, but smile and leave through the door that Jane came in through*")
            time.sleep(r)
            print("...\n*Now you are left alone in a spacious, but completely empty\
 hallway*")
            draw_2()
            ha=1

#||==##==--~  second branch off  ~--==##==||#

    if ba=="Smile and nod":
        print("*She sighs, it almost feels as though something's burdening her*\n\
 'Poor child, you always come see us...Are the kids in your school bullying you\
 again? Maybe you should stop coming to see us, being around us old people isn't\
 good for you in the long run...'")
        time.sleep(b)
        da=input("(Don't say that, I like coming here)(I'm fine how I am) ")
        if da=="I'm fine how I am":
            print("*Louise frowns, she seems to want another answer from you...*")
            time.sleep(r)
            print("'I don't mean don't come. But, maybe spend some more time with the\
 kids in your class. We all wish that you can also have friends who aren't in the\
 elderly hospital.'")
            time.sleep(r)
            print("*The sound of a knock interrupts her speech*")
            time.sleep(b)
            print("'Come in!'\n'I heard you talking and thought you had a guest over.\
 Hmm? Oh, it's", pa+". Wow, seems like you haven't been here in forever, sorry\
 for being a little late today, hehe~'\n'Stop hehe-ing and get your job done, Jane'\
 \n'Right, right. ? ____'s not here today? Weird...'")
            time.sleep(s)
            print("'Ah! Can you leave while I change Miss Louise's clothes? Thanks'")
            time.sleep(b)
            print("*You leave out the door, and find a long, empty hallway*")
            ha=1
            
        if da=="Don't say that, I like coming here":
            print("*Louise seems to truly smile, it seems your presence is important\
 to her*")
            time.sleep(r)
            print("*A comfortable silence grows and you hear the sound of the door\
 opening*")
            time.sleep(r)
            print("'Hello~ Hm?", pa+"?! Huh?! You're here?! And by yourself too...\
 Where's ____? You guys didn't drift apart right?'\n'Jane, when can I expect you\
 to do your job?'\n'Ehh?? No need to be so fussy, I brought your clothes!", pa\
, "can you leave real quick? I need to help Miss Louise with changing her\
 clothes.")
            time.sleep(s)
            print("*You nod and leave the room through the door that Jane entered,\
 you find youself alone in a large, empty hallway*")
            draw_2()
            ha=1

#||==##==--~  lists for rooms  ~--==##==||#

    Rooms={
        'coded': {'1a':" The room you came out of",
        '3a':" The room next to 2a",
        '3b':" The room across from 3a"},
        'uncoded': {'2a':" The room next to 1a",
        '2b':" The room across from 2a"},
        'keyed': {'1b':" The room across 1a, it has a key lock"}
    }

    First_Interior={
        '3a':" A storage room, at first glance it seems to house boxes of canned\
 and dried food...There's used cans everywhere. It doesn't seem very sanitary",
        '3b':" A laundry room, it's quite small, there's surprisingly no dirty\
 laundry. A lot of baskets neatly stacked",
        '2a':" An empty hospital room, there's a room divider that seperates two\
 beds",
        '2b':" ? It's not a room? It leads down to a set of stairs",
        '1b':" The door creaks, it's absolutely quiet. It takes a few moments for\
 your eyes to adjust to the lack of light. There's a weird, metal table on wheels\
 in the back of the room"
    }

    Second_Interior={
        '3a':" The metal shelves only have boxes and cans at the front, the back\
 seems to be an extremely realistic...3D printed cover? Cover for what?",
        '3b':" Nothing special, there's a clothes line behind the baskets and some\
 clothes have a faint pink stain in certain areas. Many of them seem to have been\
 mended multiple times, but there are also a lot of new and unblemished clothes",
        '2a':" A pot of anemone, begonia, and some lemon balm spread a comforting\
 scent, they're still fresh, so they must've been put in recently. What season do\
 they grow in again..?",
        '2b':" The stairs are surprisngly ungloomy, too bright in fact, and only go\
 down. They are also really steep, seems easy to fall down and get hurt.",
        '1b':" ? No light switches anywhere, the metal table seems to have a lot\
 of scratches all over it. Quite a few bumps too, under the table are a two\
 blankets with small bears and hearts over it. They seem to have a pattern with '\
 property of-' then it cuts off."
        }
 
        
    if ha==1:
        time.sleep(b)
        print("...\n*What do do now?*\n*You don't have any of your old memories...*")
        time.sleep(b)
        print("*What...happened to you before...?*\n*Did someone...do this to you\
?*")
        time.sleep(b)
        print("*The more you try to remember, the more you draw up a blank...*\n\
*You take deep breaths*")
        time.sleep(s)
        for i in range(4):
            time.sleep(1)
            print("Huu")
            time.sleep(2)
            print("Haaah")
        time.sleep(r)
        print("*Now you are calm, time to reorganize your thoughts. Who is ____?*\n\
*Why does your head hurt when you try to think of them...?*")
        time.sleep(b)
        print("*Anyway, you can't stay here in the middle of the hallway, there seems\
 to be code locks on the doors, no signs though...*")
        fu=input("(Go to the doors)(Wait until you are called back inside) ")
        time.sleep(r)

#||==##==--~  third branch off  ~--==##==||#

        if fu=="Go to the doors":
            print("*You go near the doors, there's three across from you and three\
 behind you, including the one you walked out from*")
            time.sleep(s)
            print(Rooms)
            time.sleep(s)
##not working for some reason v i think there's something wrong with random...
            
##            ma=random.choice(str(Rooms['uncoded']))
##            print("*There's only two unlocked doors, the rest all have codelocks\
## except for room 1b,", str(Rooms['uncoded'])+"*")
##            time.sleep(b)
##            print("*You enter room "+ma+"*")
##            if ma=='2a':
##                print(First_Interior['2a'])
##                fa=1
##            else:
##                print(First_Interior['2b'])
##                fa=1
##            if fa==1:
##                time.sleep(b)
##                who_blue_pup()
##            va=input("*Take another look?*\n(Yes)(No) ")
##            if va=="Yes":
##                print(Second_Interior[ma])
##                who_blue_pup()
##            else:
##                time.sleep(r)
##                print("*You leave the room and take care to close the door slowly*")

                
        else:
            print("*You wait outside for some time*")
            for i in range(3):
                time.sleep(1.5)
                print("...")
            print("*BAM!*\n *What was that?? Sounded like something collided with\
 a wall...*")
            time.sleep(r)
            print("*Did...something happen..?*")
            time.sleep(r)
            print("*Weren't they just changing clothes? Where'd the noise come\
 from?*")
            time.sleep(b)
            print("*The noise repeats, but somehow with more urgency and louder\
 than before..*\n*You try to focus and differentiate where it's coming from*")
            for i in range(3):
                time.sleep(1.5)
                print("...")
            res=Rooms.get('keyed', {}).get('1b')
            print("It's"+str(res)+". 1b...\n*What to do now?*")
            time.sleep(b)
            za=input("(Observe the door)(Wait) ")
            
            if za=="Observe the door":
                print("*The door's locked...you don't have a key*")
                time.sleep(b)
                print("*You stand there awkwardly in front of 1b*\n*Then a sound\
 surprises you*")
                print("'Hey! What are you doing there?!'")
                time.sleep(r)
                print("*You whip your head around to find a short, skinny-to-the\
-bone nurse that seems to be profusely frowning*")
                time.sleep(r)
                print("'Huh? Heard a noise??'")
                print("*You hear her mumble something, but all you can catch is\
'unexpected', 'surprising', and 'not what they told me'*")
                time.sleep(b)
                print("*It seems that this nurse is new, someone you don't know\
...*\n*Maybe you can...try and find out some things from her as a third person?*")
                time.sleep(s)
                print("'Hey! HEY!'\n'I'm trying to talk to you!'\n'What do you mean\
 you didn't hear me?! Sheesh! I asked you what it sounded like and why you're\
 here!'")
                time.sleep(r)

#||==##==--~  fourth branch off  ~--==##==||
                
                bu=input("(Tell the truth)(A small white lie) ")
                if bu=="Tell the truth":
                    print("'What? Banging against the door?!'\n'No nono nonono\
, that's not suppos-- t- h-p---...'")
                    time.sleep(r)
                    print("*Her voice gets increasingly lower as she talks and soon\
 it's just nonsensical mumbling*")
                    print("'AGHHHHH, I'm gonna go insane! I should've never accepted\
 this job from clumsy Jane!!'\n'Speaking of which, she's in with Miss Louise?\
 No wonder you're out here, she takes too long to do anything.'")
                else:
                    print("'S-screeching?! Don't be preposterous! This is an elderly\
 hospital, where would they have the energy or vocal chords to screech!'")
                    print("*You shrug your shoulders and turn around*")
                    time.sleep(b)
                    print("'W-wait! Where are you going?'\n'You're not dressed as\
 a nurse, are you new? Let me show you where the clothes are.'")
            else:
                print("*You wait*\n*The sound abruptly stops, just as you are\
 waiting...*")
                print("'Hm? Who are you? Why are you standing outside the door\
 like that..?'")
                time.sleep(b)
                print("*You snap back from your daze and find a short, incredibly\
 skinny nurse*")
                print("'Ahh, I see. Jane kicked you out, huh? She probably left\
 you out here for long, she's quite scatter-brained and slow in her work.'")
                time.sleep(r)
                print("'By any chance...are you the", pa, "that I've been hearing\
 about?'")
                pu=input("(Yes)(No) ")
                if pu=="Yes":
                    print("'Hm, that's what I thought. It's nice to meet you, I'm\
 Maria.'")
                else:
                    print("'Ah, I'm sorry. I just heard about", pa, "from Jane and\
 mistook you from them, I apologize. My name is Maria.'\n*An awkward silence ensues\
*")
                    for i in range(3):
                        time.sleep(1.5)
                        print("...")

while hp>0:
    #using time.sleep to make sure that the user has time to read the text as
    #it runs
    print("Note from the programmer: \n Welcome to this game, it's essentially\
 about a weird hospital where you somehow lose your memories and don't remember\
 anything.")
    time.sleep(r)
    print("Will you survive..?")
    time.sleep(3)
    print("Ps, when you want to quit the game, 'X' out the shell, not turtle.")
    time.sleep(b)
    print("_______________________________________________________________________")
    
    start_game()

if hp==0:
    print("How did you actually manage to get your hp to 0?? Whatever, I don't \
feel like adding multiple difficulties so just re-play it from the beginning, \
maybe change your choices?")
    time.sleep(r)
    qaq=input("(Yes)(No) ")
    if qaq=="Yes":
        print("Have a fresh start, buddy.\nTry not to fail.")
        start_game()
    else:
        print("Then what are you waiting for? Don't waste my time and cut off the\
program, I don't need spoiled brats who quit easily to test my game.")
        time.sleep(r)
        print("*Rolls eyes*")
        exit()
