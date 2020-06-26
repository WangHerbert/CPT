def path(response):
    if response == 'y':
        return 'y'
    elif response == 'n':
        return 'n'
    else:
        return ('Please enter y or n')

def story():
    global path
    global route
    route = '1'        
    while route == '1':
        response = input('Would you like to wake up? (y/n): ')
        if path(response) == 'y':
            print ()
            print ("You've just woken up and your head is pounding.")
            print ("After taking some time to recuperate, you sit up in the bed you've waken up on.")
            print ("Taking a look around you realize you're in a prison cell; directly in front of you there are inch thick bars that stare you in the face and no windows. The only source of light is a single light blub that dangles from the ceiling.")
            print ("With nothing to do you start examining the walls. You notice that one of the bricks are loose.")
            print ()
            route = 'a'

        elif path(response) == 'n':
            print ("You remain asleep, never to wake up again.")
            print ()
            print ("Game Over")
            break

        else:
            print (path(response))

    while route == 'a':
        response = input("Do you try to pry the brick off the wall? (y/n): ")
        if path(response) == 'y':
            print ()
            print ('After some prying you eventually manage to remove the brick from the wall, but you lose grip and drop it creating a loud bang')
            print ('A guard rushes over to see what caused the commotion, but before he reaches your cell you notice a piece of paper in the hole left by the brick')
            print ("You quickly stuff the paper away and explain the noise by showing the fallen brick. He's a tall broad man with a plain blue uniform, nothing special expect for a large patch." )
            print ('Before you can examine the patch further, he leaves satisfied with your answer.')
            print ('All you were able to make out was a very distinct image of a pelican')
            print ("Once he's gone you open up the folded piece of paper and see that it's a map of the prison ")
            print ("On the back of the paper you see a plan detailing the in and out of the prison and a plan of how to escape")
            print ()
            route = 'b'

        elif path(response) == 'n':
            print ('With nothing to do you sit on your bed eating the 3 meals provided each day')
            print ('Days turn into weeks, turn into months, turn into years')
            print ('You get to an age where it hurts to sit up every morning and you develop cancer')
            print ('In a state close to death you are finally brought out of your cell to a medical bay')
            print ('Not worth their time and money with an agressive brain cancer they let you die')
            print ()
            print ('Game Over')
            break

        else:
            print (path(response))

    while route == 'b':
        response = input("Do you follow the advice of this unknown stranger? (y/n): ")
        if path(response) == 'y':
            print ()
            print ("You follow the instructions. First by saying a code word to a guard.")
            print ("Though you were told this would get them on your side, it turns out this was a hoax.")
            print ("The brick and the paper were just an eleborate set up and you have just fallen for it.")
            print ('He opens the door and knocks you out with a wack on the head.')
            print ('As you lose conciousness the last thing you hear is a female voice that says "Just wipe his memory."')
            print ()
            print ('Game Over')
            break

        elif path(response) == 'n':
            print ()
            print ('You put the paper in your shoe and forget about it.')
            print ('Days go past while you sit in the prison cell trying to remember your past.')
            print ('One day the guards enter your cell without warning and lead you to a courtyard.')
            print ('There are other prisoners that are scattered around, but are unwilling to talk despite your advances')
            print ('After a couple minutes of small talk you finally meet someone that seems friendly enough')
            print ("His name is Matt and like you he doesn't remember anything of his past before finding himself in prison")
            print ("After some small talk, you tell him about the paper you found in your cell.")
            print ()
            route = 'c'

        else:
            print (path(response))

    while route == 'c':
        response = input('Curious he asks for the paper, do you give it to him? (y/n): ')
        if path(response) == 'y':
            print ('You give him the paper and think nothing of it, after an hour outside you are lead back to your cell')
            print ('You sleep peacefully through the night, until you are abruptly waken up by a guard who is performing a suprise cell check')
            print ('With nothing on you of note you pass the cell check')
            print ('The next day you are lead outside to the courtyard again, you look around to see Matt as you enjoyed his company but he in nowhere to be found')
            print ('With no one else to talk to you grow restless, desperate you begin to approach a guard')
            print ()
            route = 'd'

        elif path(response) == 'n':
            print ('You give him the paper and think nothing of it, after an hour outside you are lead back to your cell')
            print ('You sleep peacefully through the night, until you are abruptly waken up by a guard who is performing a suprise cell check')
            print ('He requires you to take off you shoes and sees the paper hidden inside')
            print ('Considered contraband he drags you off to a medical ward where you are knocked unconcious and your memory is wiped')
            print ()
            print ('Game Over')

        else:
            print(path(response))
    
    while route == 'd':
        response = input('Unsure of how friendly this compound is, do you talk to the guard? (y/n): ')
        if path(response) == 'y':
            print ('Suprisingly he is willing to talk, it turns out he was tricked into living at the prison and also wants to escape')
            print ('Unwilling to give his personal details you ask it is unclear how trustworthy he is')
            print ('However, he says he has a plan to escape he just needs another person to help him')
            print ()
            route = 'e'

        elif path(response) == 'n':
            print ('You walk away from the guard, but another prisoner sees your interest in talking to him')
            print ('He approaches you and says "You don'"'"'t understand how things work around here. Don'"'"'t ever talk to the guards"')
            print ('Angered at your actions, he shanks you')
            print ()
            print ('Game Over')
            break
        
        else:
            print(path(response))

    while route == 'e':
        response = input('Do you follow the plan of this guard you just met? (y/n): ')
        if path(response) == 'y':
            print ("He tells you that he'll find you in your cell tonight")
            print ('You are once again lead out of the courtyard and sleep soundly')
            print ('You wake up and hear the sound of you cell door opening and you look up to see the guard from earlier')
            print ('He motions for you to follow him and you do. He leads you down a hallway and to an exit.')
            print ('When you get outside you are faced with a 60 feet wall, it is now clear why he needed your help')
            print ('Fuelled by adrenaline, you slowly boost each other up the wall')
            print ('At the top there is a helicopter with accomplices waiting, you and the guard get in a fly away')
            print ('In the air you notice that although they are wearing different clothes thet all have the same image of a pelician tattooed from earlier')
            print ('Noticing the pelician you suddenly get a sick feeling in your stomach')
            print ()
            route = 'f'

        elif path(response) == 'n':
            print ('For refusing his offer his demeanor suddenly changes')
            print ('He yells for other guards and says that you attacked him')
            print ('They pummel you and you are knocked unconcious')
            print ()
            print ('Game Over')
        
        else:
            print (path(response))
    
    while route == 'f':
        response = input('The doors of the helicopter are open, do you jump out of the helicopter? (y/n): ')
        if path(response) == 'y':
            print ('You get up and before they realize what you are about to do, you take a leap of faith')
            print ('While you are falling you see a patch of trees next to a farm and you aim for that')
            print ('You land feet first and although the trees broke your fall, you have shattered your legs')
            print ('However, despite the pain your in the most important thing is that you are alive')
            print ('In shock it is hard for you to stay awake, but as you are about to fall asleep a local farmer runs to help')
            print ('He was awoken by the sound of your landing and he says the ambulence is coming')
            print ('You are brought to the local hospital where you make a full recovery')
            print ()
            print ('Congrats! ' "You've escaped")
            break
        
        elif path(response) == 'n':
            print ('In the helicopter, the pilot injects you with something')
            print ('Feeling woozy, you question what he put in you')
            print ('He says "Don'"'"'t worry, it will help you sleep. You need it"')
            print ('So you do fall asleep, but you never wake up')
            print ()
            print ("Game Over")
            break

        else:
            print(path(response))

if __name__ == "__main__":
    story()