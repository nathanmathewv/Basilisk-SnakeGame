import pygame                                                                                                           # module for game development in python
import random                                                                                                           # module for creating random values
import mysql.connector as sqltor                                                                                        # module for connection with sql
import pyglet                                                                                                           # module for the video
import time                                                                                                             # module for time
import sys                                                                                                              # module for controlling events in system

window = pyglet.window.Window(960, 540, "BASILISK")                                                                     # sets the size of video to 960x650
player = pyglet.media.Player()                                                                                          # creating a media player object

source = pyglet.media.StreamingSource()                                                                                 # creating a source object
media_load = pyglet.media.load("intro_video.mp4")                                                                       # loads the intro video
player.queue(media_load)                                                                                                # loads media into the queue
player.play()                                                                                                           # plays the video

@window.event                                                                                                           # part of the format for doing video plying with pyglet
def on_draw():                                                                                                          # sets up the screen for drawing onto screen, this function doesnt need to be called
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0, 0)

@window.event
def on_key_press(symbol, modifier):                                                                                     # closes everything if a key is pressed and moves to next screen
    player.pause()                                                                                                      # pauses video
    window.close()                                                                                                      # closes the video player

pyglet.app.run()                                                                                                        # runs the video

mycon = sqltor.connect(host="localhost", user="root", passwd="password", database="snake_game",                         # sets up the mysql database
                       charset="utf8")  # connects with mysql
if mycon.is_connected() == False:  # checks connection with mysql                                                       # checks if mysql is connected to python
    print("error connecting to MySQL database")                                                                         # prints error if it doesnt connect to mysql
else:
    print("connection successful")                                                                                      # prints successful if successful in connecting to mysql

pygame.init()                                                                                                           # initialise the entire pygame

display = pygame.display.set_mode((960, 540))                                                                           # set the initial size of the gui display

goto = [0]                                                                                                              # this is for checking if player has selected quickplay option

def display_sql():                                                                                                      # function for displaying the items in the mysql table
    cursor = mycon.cursor()                                                                                             # sets up cursor object
    cursor.execute("select * from scores")                                                                              # gets all the data from the scores table in mysql
    data = cursor.fetchall()                                                                                            # all data in one variable
    return data                                                                                                         # returns data to where function was called


def message(msg, color, width_location, height_location, size):                                                         # function to print any data
    mesg_offset_length = len(msg)                                                                                       # statement to centre the message in a block
    mesg = pygame.font.SysFont("Corbel", size).render(msg, True, color)                                                 # setting size, font and color of text
    display.blit(mesg, (width_location - mesg_offset_length, height_location))                                          # inserts message onto the display
    pygame.display.update()                                                                                             # updates the screen after entering new message


def message_2(msg, color, width_location, height_location, size):                                                       # function to print any data
    mesg = pygame.font.SysFont("Corbel", size).render(msg, True, color)                                                 # setting size, font and color of text
    display.blit(mesg, (width_location, height_location))                                                               # inserts message onto the display
    pygame.display.update()                                                                                             # updates the screen after entering new message


def leaderboard_stat():                                                                                                 # function to get top 5 players
    lead = display_sql()                                                                                                # collects all data from mysql
    players = len(lead)
    for i in range(players):                                                                                            # bubble sort to get the players with the highest scores
        for j in range(0, players - i - 1):
            if lead[j][1] < lead[j + 1][1]:
                lead[j], lead[j + 1] = lead[j + 1], lead[j]
    top1, top2, top3, top4, top5 = lead[0], lead[1], lead[2], lead[3], lead[4]
    return [top1, top2, top3, top4, top5]                                                                               # returns top 5 players


def leaderboard_func():                                                                                                 # function for the leaderboard
    sub_button_intro = ("songs/sub_button.mp3")                                                                         # audio file for clicking the back button
    font = pygame.font.SysFont('Corbel', 30)                                                                            # sets the font and the text size for the leaderboard stuff
    data = leaderboard_stat()                                                                                           # gets the top 5 names from mysql table with leaderboard_stat function

    name_0, name_1, name_2, name_3, name_4 = data[0][0], data[1][0], data[2][0], data[3][0], data[4][0]                 # names of top 5 players
    score_0, score_1, score_2, score_3, score_4 = data[0][1], data[1][1], data[2][1], data[3][1], data[4][1]            # scores of top 5 players

    i_2 = 0                                                                                                             # variable for fade
    flag_9 = [0]                                                                                                        # this flag is for being able to do fade each time you click on leaderboard
    clean = pygame.image.load("wallpaper/wallpaper_clean.png")                                                          # backdrop for fade
    clean = pygame.transform.scale(clean, (960, 540))                                                                   # setting backdrop to required size
    clean = clean.convert()                                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster

    leaderboard_fadein = pygame.image.load("wallpaper/wallpaper_leaderboard_fadein.png")                                # leaderboard image that fades in
    leaderboard_fadein = pygame.transform.scale(leaderboard_fadein, (960, 540))                                         # scales image to correct size
    leaderboard_fadein = leaderboard_fadein.convert()                                                                   # converts the pygame.surface to same pixel format as the one created by us, makes code faster

    txt_surface_3 = font.render(str(name_0), True, (255, 255, 255))                                                     # converts first name to image
    txt_surface_4 = font.render(str(name_1), True, (255, 255, 255))                                                     # converts second name to iage
    txt_surface_5 = font.render(str(name_2), True, (255, 255, 255))                                                     # converts third name to image
    txt_surface_6 = font.render(str(name_3), True, (255, 255, 255))                                                     # converts fourth name to image
    txt_surface_7 = font.render(str(name_4), True, (255, 255, 255))                                                     # converts fifth image to image

    txt_surface_8 = font.render(str(score_0), True, (255, 255, 255))                                                    # converts first score to image
    txt_surface_9 = font.render(str(score_1), True, (255, 255, 255))                                                    # converts second score to image
    txt_surface_10 = font.render(str(score_2), True, (255, 255, 255))                                                   # converts third score to image
    txt_surface_11 = font.render(str(score_3), True, (255, 255, 255))                                                   # converts fourth score to image
    txt_surface_12 = font.render(str(score_4), True, (255, 255, 255))                                                   # converts fifth score to image

    if flag_9[0] == 0:                                                                                                  # th4is condition prevents multiple fades from happening together
        while i_2 != 255:                                                                                               # fade in from black
            leaderboard_fadein.set_alpha(i_2)                                                                           # set brightness for leaderboard image
            txt_surface_3.set_alpha(i_2)                                                                                # set brightness for name 1
            txt_surface_4.set_alpha(i_2)                                                                                # set brightness for name 2
            txt_surface_5.set_alpha(i_2)                                                                                # set brightness for name 3
            txt_surface_6.set_alpha(i_2)                                                                                # set brightness for name 4
            txt_surface_7.set_alpha(i_2)                                                                                # set brightness for name 5
            
            txt_surface_8.set_alpha(i_2)                                                                                # set brightness for score 1
            txt_surface_9.set_alpha(i_2)                                                                                # set brightness for score 2
            txt_surface_10.set_alpha(i_2)                                                                               # set brightness for score 3
            txt_surface_11.set_alpha(i_2)                                                                               # set brighntess for score 4
            txt_surface_12.set_alpha(i_2)                                                                               # set brightness for score 5

            display.blit(clean, (0, 0))                                                                                 # backdrop for fade
            display.blit(leaderboard_fadein, (0, 0))                                                                    # fade in image

            display.blit(txt_surface_3, (415, 140))                                                                     # blits name 1
            display.blit(txt_surface_4, (415, 195))                                                                     # blits name 2
            display.blit(txt_surface_5, (415, 248))                                                                     # blits name 3
            display.blit(txt_surface_6, (415, 301))                                                                     # blits name 4
            display.blit(txt_surface_7, (415, 353))                                                                     # blits name 5
    
            display.blit(txt_surface_8, (600, 140))                                                                     # blits score 1
            display.blit(txt_surface_9, (600, 195))                                                                     # blits score 2
            display.blit(txt_surface_10, (600, 248))                                                                    # blits score 3
            display.blit(txt_surface_11, (600, 301))                                                                    # blits score 4
            display.blit(txt_surface_12, (600, 353))                                                                    # blits score 5

            pygame.time.delay(1)                                                                                        # delay to adjust speed of fade(this is min time)
            i_2 = i_2 + 5                                                                                               # brightness value step
            pygame.display.update()                                                                                     # updates screen after every step
            flag_9[0] = 1                                                                                               # prevents fade from happening again and again

    flag_9[0] = 0                                                                                                       # allows fade to happen properly next time

    image = pygame.image.load('wallpaper/wallpaper_clean.png')                                                          # clean image with nothing on it
    image = pygame.transform.scale(image, (960, 540))                                                                   # sets the size of the image
    image = image.convert()                                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster
    display.blit(image, (0, 0))                                                                                         # blits clean image onto screen
    pygame.display.update()                                                                                             # updates screen

    back = pygame.image.load("icons/back.png")                                                                          # back icon
    back_dark = pygame.image.load("icons/back_dark.png")                                                                # dark back icon
    back = pygame.transform.scale(back, (50, 50))                                                                       # scales size of icon
    back_dark = pygame.transform.scale(back_dark, (50, 50))                                                             # scales dark back icon

    leaderboard = pygame.image.load("icons/leaderboard_actual.png")                                                     # leaderboard image
    leaderboard = pygame.transform.scale(leaderboard, (400, 400))                                                       # sets the size of the leaderboard image
    display.blit(leaderboard, (960 / 2 - 200, 30))                                                                      # blits the image of leaderboard

    message_2(str(name_0), (255, 255, 255), 415, 140, 30)                                                               # blits name 1
    message_2(str(name_1), (255, 255, 255), 415, 195, 30)                                                               # blits name 2
    message_2(str(name_2), (255, 255, 255), 415, 248, 30)                                                               # blits name 3
    message_2(str(name_3), (255, 255, 255), 415, 301, 30)                                                               # blits name 4
    message_2(str(name_4), (255, 255, 255), 415, 353, 30)                                                               # blits name 5

    message_2(str(score_0), (255, 255, 255), 600, 140, 30)                                                              # blits score 1
    message_2(str(score_1), (255, 255, 255), 600, 195, 30)                                                              # blits score 2
    message_2(str(score_2), (255, 255, 255), 600, 248, 30)                                                              # blits score 3
    message_2(str(score_3), (255, 255, 255), 600, 301, 30)                                                              # bltis score 4
    message_2(str(score_4), (255, 255, 255), 600, 353, 30)                                                              # blits score 5

    pygame.display.update()                                                                                             # updates the screen
    done = False                                                                                                        # checks if back is clicked

    while not done:                                                                                                     # while leaderboard is still going on
        for event in pygame.event.get():                                                                                # check for the prescense of any event
            mousepos = pygame.mouse.get_pos()                                                                           # find the position of the mouse
            if event.type == pygame.QUIT:                                                                               # checks if you close the window
                done = True                                                                                             # makes the program end
                pygame.quit()                                                                                           # quits pygame

            if 305 <= mousepos[0] <= 355 and 450 <= mousepos[1] <= 500:                                                 # checks if the mouse is over the back button
                display.blit(back, (305, 450))                                                                          # makes the back button light color
                if event.type == pygame.MOUSEBUTTONDOWN:                                                                # checks if the button is pressed
                    sub_button_intro_sound = pygame.mixer.Sound(sub_button_intro)                                       # loads the sound for back button sound
                    pygame.mixer.Channel(3).set_volume(0.5)                                                             # sets the volume to half
                    pygame.mixer.Channel(3).play(sub_button_intro_sound)                                                # plays the back button sound
                    done = True                                                                                         # ends back button, goes back
                    i_2 = 255                                                                                           # fade variable
                    if flag_9[0] == 0:                                                                                  # prevents fade from happening again and again
                        while i_2 != 0:                                                                                 # fades to black
                            leaderboard_fadein.set_alpha(i_2)                                                           # setting the leaderboard fade brightness
                            txt_surface_3.set_alpha(i_2)                                                                # setting the brightness of name 1
                            txt_surface_4.set_alpha(i_2)                                                                # setting the brightness of name 2
                            txt_surface_5.set_alpha(i_2)                                                                # setting the brightness of name 3
                            txt_surface_6.set_alpha(i_2)                                                                # setting the brightness of name 4
                            txt_surface_7.set_alpha(i_2)                                                                # setting the brightness of name 5

                            txt_surface_8.set_alpha(i_2)                                                                # setting the brightness of score 1
                            txt_surface_9.set_alpha(i_2)                                                                # setting the brightness of score 2
                            txt_surface_10.set_alpha(i_2)                                                               # setting the brightness of score 3
                            txt_surface_11.set_alpha(i_2)                                                               # setting the brightness of score 4
                            txt_surface_12.set_alpha(i_2)                                                               # setting the brighntess of score 5

                            display.blit(clean, (0, 0))                                                                 # backdrop for fade
                            display.blit(leaderboard_fadein, (0, 0))                                                    # fade in image

                            display.blit(txt_surface_3, (415, 140))                                                     # blitting name 1
                            display.blit(txt_surface_4, (415, 195))                                                     # blitting name 2
                            display.blit(txt_surface_5, (415, 248))                                                     # blitting name 3
                            display.blit(txt_surface_6, (415, 301))                                                     # blitting name 4
                            display.blit(txt_surface_7, (415, 353))                                                     # blitting name 5

                            display.blit(txt_surface_8, (600, 140))                                                     # blitting score 1
                            display.blit(txt_surface_9, (600, 195))                                                     # blitting score 2
                            display.blit(txt_surface_10, (600, 248))                                                    # blitting score 3
                            display.blit(txt_surface_11, (600, 301))                                                    # blitting score 4
                            display.blit(txt_surface_12, (600, 353))                                                    # blitting score 5

                            pygame.time.delay(1)                                                                        # delay for fade
                            i_2 = i_2 - 5                                                                               # step value for fade
                            pygame.display.update()                                                                     # update the screen
                            flag_9[0] = 1                                                                               # prevents fade from happening multiple times

                    flag_9[0] = 0
            else:
                display.blit(back_dark, (305, 450))                                                                     # if you dont click on button it becomes dark

        pygame.display.update()                                                                                         # update the screen

    display.blit(image, (0, 0))                                                                                         # blitting clean image


def about_func():                                                                                                       # function for when you click on about button
    sub_button_intro = ("songs/sub_button.mp3")                                                                         # sound for when you click on about button

    i_2 = 0                                                                                                             # variable for step value
    flag_10 = [0]                                                                                                       # flag to prevent fade from happening again and again
    clean = pygame.image.load("wallpaper/wallpaper_clean.png")                                                          # backdrop for fade
    clean = pygame.transform.scale(clean, (960, 540))                                                                   # scales the backdrop to right size
    clean = clean.convert()                                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster

    about_fadein = pygame.image.load("wallpaper/wallpaper_about_fadein.png")                                            # fade image
    about_fadein = pygame.transform.scale(about_fadein, (960, 540))                                                     # scales the fadein image
    about_fadein = about_fadein.convert()                                                                               # converts the pygame.surface to same pixel format as the one created by us, makes code faster

    if flag_10[0] == 0:                                                                                                 # condition to prevent fade from happening again and again
        while i_2 != 255:                                                                                               # fade in till max brightness
            about_fadein.set_alpha(i_2)                                                                                 # set the brightness value
            display.blit(clean, (0, 0))                                                                                 # blitting the backdrop image
            display.blit(about_fadein, (0, 0))                                                                          # blitting the fade in image

            pygame.time.delay(1)                                                                                        # time delay for the fade
            i_2 = i_2 + 5                                                                                               # step value for the fade
            pygame.display.update()                                                                                     # update the screen after each fade
            flag_10[0] = 1                                                                                              # flag to prevent fade from happening again and again
    flag_10[0] = 0                                                                                                      # flag to prevent fade from happening again and again

    image = pygame.image.load('wallpaper/wallpaper_clean.png')                                                          # backdrop clean image
    image = pygame.transform.scale(image, (960, 540))                                                                   # scales the iamge to right size
    image = image.convert()                                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster
    display.blit(image, (0, 0))                                                                                         # blits background image
    pygame.display.update()                                                                                             # updates the whole screen

    back = pygame.image.load("icons/back.png")                                                                          # loads in the back icon into pygame from file
    back_dark = pygame.image.load("icons/back_dark.png")                                                                # loads in the dark back icon into pygame from file

    copyright = pygame.image.load("icons/copyright.png")                                                                # loads in the copyright icon into pygame from file

    back = pygame.transform.scale(back, (50, 50))                                                                       # scales the back icon to right size
    back_dark = pygame.transform.scale(back_dark, (50, 50))                                                             # scales the dark back icon to right size

    copyright = pygame.transform.scale(copyright, (15, 15))                                                             # scales the copyright icon to right size

    message("Created by Kevin, Nathan, Keshav, Karthik", (255, 255, 255), 310, 150, 25)                                 # blits the message
    message("Credits to bensound.com for providing the music.", (255, 255, 255), 290, 180, 25)                          # blits the message
    message("Credits to Kurzgesagt for providing such vibrant backdrops.", (255, 255, 255), 250, 210, 25)               # blits the message
    message("Additional thank you to abhijit for music suggestions and our friends for beta testing.", (255, 255, 255), # blits the message
            150, 240, 25)
    message("Moreover we have gratitude for our teacher for providing us this golden opporutunity", (255, 255, 255),    # blits the message
            140, 270, 25)
    message("Basilisk .All Rights Reserved", (255, 255, 255), 430, 300, 17)                                             # blits the message
    display.blit(copyright, (380, 300))                                                                                 # blits the copyright icon

    pygame.display.update()                                                                                             # updates teh whole screen

    done = False                                                                                                        # variable to check when the back icon is clicked on

    while not done:                                                                                                     # condition for when back is clicked
        for event in pygame.event.get():                                                                                # check for any events in pygame
            mousepos = pygame.mouse.get_pos()                                                                           # get the position of the mouse
            if event.type == pygame.QUIT:                                                                               # check if the close button is clicked on
                done = True                                                                                             # leaves the about function
                pygame.quit()                                                                                           # quits pygame

            if 305 <= mousepos[0] <= 355 and 450 <= mousepos[1] <= 500:                                                 # condition for when mouse is over the back button
                display.blit(back, (305, 450))                                                                          # turns the back button light when mouse is over it
                if event.type == pygame.MOUSEBUTTONDOWN:                                                                # checks the presence of any key pressed
                    done = True                                                                                         # makes done true if back is clicked
                    sub_button_intro_sound = pygame.mixer.Sound(sub_button_intro)                                       # loads in the soudn for whe the back button is clicked on
                    pygame.mixer.Channel(3).set_volume(1)                                                               # sets the volume of the button click sound
                    pygame.mixer.Channel(3).play(sub_button_intro_sound)                                                # plays the sound of the button click

                    i_2 = 255                                                                                           # variable to store the brightness value
                    if flag_10[0] == 0:                                                                                 # flag to prevent the fade from running again and again
                        while i_2 != 0:                                                                                 # fade to black
                            about_fadein.set_alpha(i_2)                                                                 # setting teh brightness for about fade in image
                            display.blit(clean, (0, 0))                                                                 # blits the backdrop for the fade
                            display.blit(about_fadein, (0, 0))                                                          # blits the fade in screen

                            pygame.time.delay(1)                                                                        # adds a time delay for the fade
                            i_2 = i_2 - 5                                                                               # step value for the fade
                            pygame.display.update()                                                                     # udpates the screen
                            flag_10[0] = 1                                                                              # flag prevents the fade from running again and again
                    flag_10[0] = 0                                                                                      # flag prevents the fade from running again and again
            else:                                                                                                       # when the button is not hovered over
                display.blit(back_dark, (305, 450))                                                                     # default color of the back icon is dark

        pygame.display.update()                                                                                         # updates the whole screen
    display.blit(image, (0, 0))                                                                                         # blits the clean image

icon_size = 50                                                                                                          # defines the size of the icons
next = pygame.image.load("icons/next.png")                                                                              # loads in the icon for next
next_dark = pygame.image.load("icons/next_dark.png")                                                                    # loads in the icon for dark next
next = pygame.transform.scale(next, (icon_size, icon_size))                                                             # scales the next icon size to the right size
next_dark = pygame.transform.scale(next_dark, (icon_size, icon_size))                                                   # scales the dark next icon to the right size

def intro_page():                                                                                                       # functions for the intro page
    main_button_intro = ("songs/main_button.mp3")                                                                       # the music for the intro page background
    main_button_intro_sound = pygame.mixer.Sound(main_button_intro)                                                     # loads the music into pygame

    next_button_intro = ("songs/next_button.mp3")                                                                       # the sound for next button
    next_button_intro_sound = pygame.mixer.Sound(next_button_intro)                                                     # loads the sound for next button into pygame

    flag_5 = [0]                                                                                                        # flag for about button
    flag_6 = [0]                                                                                                        # flag for leaderboard button
    flag_7 = [0]                                                                                                        # flag for quickplay button
    flag_8 = [0]                                                                                                        # flag for next button

    check = [0]

    display = pygame.display.set_mode((960, 540))                                                                       # sets the display size to 960 x 540

    about = pygame.image.load("icons/about.png")                                                                        # loads in the icon for about
    leaderboard = pygame.image.load("icons/leaderboard.png")                                                            # loads in the icon for leaderboard
    quickplay = pygame.image.load("icons/quickplay.png")                                                                # loads in the icon for quickplay

    about_dark = pygame.image.load("icons/about_dark.png")                                                              # loads in the icon for dark about
    leaderboard_dark = pygame.image.load("icons/leaderboard_dark.png")                                                  # loads in the icon for dark leaderboard
    quickplay_dark = pygame.image.load("icons/quickplay_dark.png")                                                      # loads in the icon for dark quickplay

    about = pygame.transform.scale(about, (icon_size, icon_size))                                                       # scales the about icon
    leaderboard = pygame.transform.scale(leaderboard, (icon_size, icon_size))                                           # scales the leaderboard idon
    quickplay = pygame.transform.scale(quickplay, (icon_size, icon_size))                                               # scales the quickplay icon


    about_dark = pygame.transform.scale(about_dark, (icon_size, icon_size))                                             # scales the dark about icon
    leaderboard_dark = pygame.transform.scale(leaderboard_dark, (icon_size, icon_size))                                 # scales the dark leaderboard icon
    quickplay_dark = pygame.transform.scale(quickplay_dark, (icon_size, icon_size))                                     # scales the dark quickplay icon

    offset = 100                                                                                                        # spacing between the icons

    pygame.display.update()                                                                                             # updates the screen

    font = pygame.font.SysFont('Corbel', 32)                                                                            # setting the font and the size of the characters

    input_box = pygame.Rect(390, 200, 140, 32)                                                                          # draws the input box

    color_inactive = pygame.Color(255, 255, 255)                                                                        # inactive color of the box(white)
    color_active = pygame.Color((77, 0, 120))                                                                           # active color of the box(purple)
    color = color_inactive                                                                                              # sets the initial color as inactive
    active = False                                                                                                      # initially status of clicking the box is false
    text = ''                                                                                                           # variable to store name entered
    names = []                                                                                                          #
    a = 0
    done = False
    display.fill((30, 30, 30))                                                                                          # sets initial color (this doesnt do anything since it gets overlapped)
    background = pygame.Surface((960, 540))                                                                             # sets up the background surface object
    background.fill((0, 0, 0))                                                                                          # fills the background with black color
    initial_image = pygame.image.load('wallpaper/wallpaper_intro_fadein.png')                                           # fade in image
    initial_image = pygame.transform.scale(initial_image, (960, 540))                                                   # sets the fade in image scale to size
    initial_image = initial_image.convert()                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster
    rect = initial_image.get_rect()                                                                                     # gets the coordinates for the box


    i = 0                                                                                                               # variable for interating fade

    intro_music = ("songs/intro_music.mp3")                                                                             # intro music file

    intro_music = pygame.mixer.Sound(intro_music)                                                                       # loads in the intro music
    pygame.mixer.Channel(0).set_volume(0.2)                                                                             # sets volume for intro music
    pygame.mixer.Channel(0).play(intro_music)                                                                           # plays the intro music
    image = pygame.image.load('wallpaper/wallpaper_intro_textselected.png')                                             # fade out image
    image = pygame.transform.scale(image, (960, 540))                                                                   # scale out image
    image = image.convert()                                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster
    while i != 255:                                                                                                     # fade
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                                                               # quits game if you click on close
                pygame.quit()                                                                                           # quits game if you click on close
                sys.exit()
        initial_image.set_alpha(i)                                                                                      # set brightness value of image
        display.blit(background, background.get_rect())                                                                 # blits backdrop image
        display.blit(initial_image, rect)                                                                               # blits the fade image
        pygame.time.delay(10)                                                                                           # sets a delay for the fade
        i += 5                                                                                                          # step value for the fade
        pygame.display.update()                                                                                         # updates the screen

    while not done:                                                                                                     # if you dont click on the button
        for event in pygame.event.get():                                                                                # check for the presence of any event in pygame
            mousepos = pygame.mouse.get_pos()                                                                           # get the position of the mouse
            if event.type == pygame.QUIT:                                                                               # if the close button is clicked it ends
                done = True                                                                                             # quits the pygame
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and a != 1:                                                         # checks if any key is pressed when there is name in textbox
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False

                color = color_active if active else color_inactive                                                      # Change the current color of the input box.
            if event.type == pygame.KEYDOWN:                                                                            # checks for the presence of a key pressdown
                display.blit(image, rect)                                                                               # blits image on the screen
                if active:
                    if event.key == pygame.K_RETURN and text != '':                                                     # allows you to click on enter
                        print(text)
                        display.blit(image, rect)
                        a = 1
                    elif event.key == pygame.K_BACKSPACE:                                                               # allows you to backspace on the textbox
                        text = text[:-1]
                    else:
                        text += event.unicode                                                                           # collects all the text that has been entered

            if text != '':                                                                                              # condition to prevent people from clicking on any button if there is no text in the text box
                a = 1
            else:
                a = 0

            about_x = 960 / 2 - (3 / 2) * offset - icon_size / 2                                                        # location of x coordinate of about icon
            leaderboard_x = 960 / 2 - (1 / 2) * offset - icon_size / 2                                                  # location of x coordinate of leaderboard icon
            quickplay_x = 960 / 2 + (1 / 2) * offset - icon_size / 2                                                    # location of x coordinate of quickplay icon
            next_x_2 = 960 / 2 + (3 / 2) * offset - icon_size / 2                                                       # location of x coordinate of next icon

            if about_x <= mousepos[0] <= about_x + 50 and 450 <= mousepos[1] <= 500:                                    # if mouse is over the about icon
                display.blit(about, (about_x, 450))                                                                     # make the about icon light colored
                if event.type == pygame.MOUSEBUTTONDOWN and a == 1:                                                     # checks if you pressed the button and if there is text in textbox
                    main_button_intro_sound = pygame.mixer.Sound(main_button_intro)                                     # sound for button sound
                    pygame.mixer.Channel(3).set_volume(1)                                                               # sets volume of button
                    pygame.mixer.Channel(3).play(main_button_intro_sound)                                               # plays the sound of button
                    i = 255                                                                                             # variable to fade

                    txt_surface_2 = font.render(text, True, color_inactive)                                             # text has been rendered into an image

                    display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                                     # blits the image onto the screen

                    clean_fadein = pygame.image.load("wallpaper/wallpaper_clean.png")                                   # backdrop for fade
                    clean_fadein = pygame.transform.scale(clean_fadein, (960, 540))                                     # scales the backdrop iamge properly
                    clean_fadein = clean_fadein.convert()                                                               # converts the pygame.surface to same pixel format as the one created by us, makes code faster
                    if flag_8[0] == 0:                                                                                  # sets the flag for preventing from running again and again
                        while i != 0:                                                                                   # fades the image to black
                            clean_fadein.set_alpha(255 - i)                                                             # fade for the image(jugaad)
                            txt_surface_2.set_alpha(i)                                                                  # fade for the text
                            display.blit(image, (0, 0))                                                                 # blits the image onto the screen
                            display.blit(clean_fadein, (0, 0))                                                          # backdrop image
                            display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                             # blits the text onto the screen
                            pygame.time.delay(1)                                                                        # delay between each iteration
                            i = i - 5                                                                                   # step value for the fade
                            pygame.display.update()                                                                     # updates the screen
                            flag_8[0] = 1                                                                               # sets the flag for preventing from running again and again
                    flag_8[0] = 0                                                                                       # resets the flag
                    about_func()                                                                                        # calls the about function
                    if flag_8[0] == 0:                                                                                  # uses the flag to prevent the fade from unning again and again
                        while i != 255:                                                                                 # fade till fully bright
                            clean_fadein.set_alpha(255 - i)                                                             # fade the iamge
                            txt_surface_2.set_alpha(i)                                                                  # fade the text
                            display.blit(image, (0, 0))                                                                 # blit the image
                            display.blit(clean_fadein, (0, 0))                                                          # blits the backdrop image
                            display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                             # blits the text
                            pygame.time.delay(1)                                                                        # defines the delay time
                            i = i + 5                                                                                   # step value for fade
                            pygame.display.update()                                                                     # updates the screen
                            flag_8[0] = 1                                                                               # changes flag value
                    flag_8[0] = 0                                                                                       # resets flag value

                elif event.type == pygame.MOUSEBUTTONDOWN and a != 1:                                                   # checks if button is clicked and if no text
                    message('Please type your name', (255, 255, 255), 390, 510, 25)                                     # enters text ENTER YOUR NAME
            else:                                                                                                       # if mouse is not on top of button
                display.blit(about_dark, (about_x, 450))                                                                # then icon is dark

            if leaderboard_x <= mousepos[0] <= leaderboard_x + 50 and 450 <= mousepos[1] <= 500:                        # checks if the mouse is over the leaderboard icon
                display.blit(leaderboard, (leaderboard_x, 450))                                                         # blits the light version of the leaderboard
                if event.type == pygame.MOUSEBUTTONDOWN and a == 1:                                                     # if button is clicked and name is there in textbox
                    main_button_intro_sound = pygame.mixer.Sound(main_button_intro)                                     # loads in button sound
                    pygame.mixer.Channel(3).set_volume(1)                                                               # sets volume of button sound
                    pygame.mixer.Channel(3).play(main_button_intro_sound)                                               # plays the button sound
                    i = 255                                                                                             # variable to iterate sound

                    txt_surface_2 = font.render(text, True, color_inactive)                                             # converts name to image

                    display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                                     # blits the text

                    clean_fadein = pygame.image.load("wallpaper/wallpaper_clean.png")                                   # backdrop image for fade
                    clean_fadein = pygame.transform.scale(clean_fadein, (960, 540))                                     # scale the image properly
                    clean_fadein = clean_fadein.convert()                                                               # converts the pygame.surface to same pixel format as the one created by us, makes code faster
                    if flag_7[0] == 0:                                                                                  # flag to prevent the fade from running again and again
                        while i != 0:                                                                                   # fade to black
                            clean_fadein.set_alpha(255 - i)                                                             # fade for image
                            txt_surface_2.set_alpha(i)                                                                  # fade for text
                            display.blit(image, (0, 0))                                                                 # blits the image onto the screen
                            display.blit(clean_fadein, (0, 0))                                                          # blits the backdrop image
                            display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                             # blits the text
                            pygame.time.delay(1)                                                                        # delay for the fade
                            i = i - 5                                                                                   # step value for the fade
                            pygame.display.update()                                                                     # updates the screen
                            flag_7[0] = 1                                                                               # flag to prevent fade from running again and again
                    flag_7[0] = 0                                                                                       # reset the flag
                    leaderboard_func()                                                                                  # calls the function for the leaderboard
                    i = 0                                                                                               # iteration variable for fade
                    if flag_7[0] == 0:                                                                                  # flag to prevent fade from running again and again
                        while i != 255:                                                                                 # fade back to full brightness
                            clean_fadein.set_alpha(255 - i)                                                             # fade of image
                            txt_surface_2.set_alpha(i)                                                                  # image fade
                            display.blit(image, (0, 0))                                                                 # blits the image
                            display.blit(clean_fadein, (0, 0))                                                          # blits the clean image
                            display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                             # blits the text onto the screen
                            pygame.time.delay(1)                                                                        # time delay for each iteration
                            i = i + 5                                                                                   # step value for each fade
                            pygame.display.update()                                                                     # updating the whole screen
                            flag_7[0] = 1                                                                               # flag to prevent fade from running again and again
                    flag_7[0] = 0                                                                                       # resets the flag

                elif event.type == pygame.MOUSEBUTTONDOWN and a != 1:                                                   # if button is clicked when you havnt typed any name
                    message('Please type your name', (255, 255, 255), 390, 510, 25)                                     # message to type name if you havn typed your name

            else:
                display.blit(leaderboard_dark, (leaderboard_x, 450))                                                    # if the person doesnt click on button it is dark

            if quickplay_x <= mousepos[0] <= quickplay_x + 50 and 450 <= mousepos[1] <= 500:                            # checks if the mouse is over the region of quickplay button
                display.blit(quickplay, (quickplay_x, 450))                                                             # blits the quickplay icon
                if event.type == pygame.MOUSEBUTTONDOWN and a == 1:                                                     # checks if button is pressed and if you have a name within the text
                    main_button_intro_sound = pygame.mixer.Sound(main_button_intro)                                     # sound for when you click on a button
                    pygame.mixer.Channel(3).set_volume(1)                                                               # sets the volume of the button click
                    pygame.mixer.Channel(3).play(main_button_intro_sound)                                               # plays the playing button
                    goto[0] = 1                                                                                         # this is a variable created if quickplay is clicked to bypass the choosing sreen 2
                    done = True                                                                                         # starts the game immediately with default values                                                 
                    i = 255                                                                                             # fade out variable

                    txt_surface_2 = font.render(text, True, color_inactive)                                             # renders the text entered by user into an image

                    display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                                     # blits the image of that text onto the screen

                    clean_fadein = pygame.image.load("wallpaper/wallpaper_clean.png")                                   # backdrop of the fade in
                    clean_fadein = pygame.transform.scale(clean_fadein, (960, 540))                                     # scale the image properly
                    clean_fadein = clean_fadein.convert()                                                               # converts the pygame.surface to same pixel format as the one created by us, makes code faster
                    if flag_6[0] == 0:
                        while i != 0:                                                                                   # fade to black
                            clean_fadein.set_alpha(255 - i)                                                             # fading of image
                            txt_surface_2.set_alpha(i)                                                                  # fading of text
                            display.blit(image, (0, 0))                                                                 # blits the image onto the display
                            display.blit(clean_fadein, (0, 0))                                                          # backdrop for the image
                            display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                             # blits the text onto the screen

                            pygame.time.delay(1)                                                                        # delay for the fade
                            i = i - 5                                                                                   # step value for the fade
                            pygame.display.update()                                                                     # updates the python screen
                            flag_6[0] = 1                                                                               # flag to prevent fade from running again and again
                elif event.type == pygame.MOUSEBUTTONDOWN and a != 1:                                                   # if button is pressed and the name is not entered then it shows message
                    message('Please type your name', (255, 255, 255), 390, 510, 25)                                     # please type your name message
            else:
                display.blit(quickplay_dark, (quickplay_x, 450))                                                        # if mouse is not over the image, it makes the icon dark

            if next_x_2 <= mousepos[0] <= next_x_2 + 50 and 450 <= mousepos[1] <= 500:                                  # if the mouse is over the next button
                display.blit(next, (next_x_2, 450))                                                                     # blits the icon onto the screen
                if event.type == pygame.MOUSEBUTTONDOWN and a == 1:                                                     # checks if the button is clicked as well as the name is entered
                    pygame.mixer.Channel(3).set_volume(1)                                                               # sets the volume of the button sound
                    pygame.mixer.Channel(3).play(next_button_intro_sound)                                               # play the button sound

                    done = True
                    i = 255                                                                                             # variable for iterating through the fade values

                    txt_surface_2 = font.render(text, True, color_inactive)                                             # converts the name into image

                    display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                                     # blits the text onto the screen

                    clean_fadein = pygame.image.load("wallpaper/wallpaper_clean.png")                                   # wallpaper for the backdrop
                    clean_fadein = pygame.transform.scale(clean_fadein, (960, 540))                                     # transform the image to corrrect scale
                    clean_fadein = clean_fadein.convert()                                                               # converts the pygame.surface to same pixel format as the one created by us, makes code faster
                    if flag_5[0] == 0:                                                                                  # flags to prevent the fade from running again and again
                        while i != 0:
                            clean_fadein.set_alpha(255 - i)                                                             # fade in for the image
                            txt_surface_2.set_alpha(i)                                                                  # fade in for the text
                            display.blit(image, (0, 0))                                                                 # blit the image to the screen
                            display.blit(clean_fadein, (0, 0))                                                          # blit the backdrop image
                            display.blit(txt_surface_2, (input_box.x + 5, input_box.y + 5))                             # blit the text onto the screen
                            pygame.time.delay(1)                                                                        # time delay for the fade in
                            i = i - 5                                                                                   # step value for the fade
                            pygame.display.update()                                                                     # updates the whole sreen

                            flag_5[0] = 1                                                                               # flag to prevent the fade from running again and again

                            check[0] = 1


                elif event.type == pygame.MOUSEBUTTONDOWN and a != 1:                                                   # ask to type name if you havnt typed name already
                    message('Please type your name', (255, 255, 255), 390, 510, 25)                                     # message type your name
            else:
                display.blit(next_dark, (next_x_2, 450))                                                                # if you dont click on the option make it dark in color

        if check[0] == 0:                                                                                               # take in the in the name
            message('Enter Your Name', (255, 255, 255), 400, 150, 30)                                                   # enter the message "enter your name"
            txt_surface = font.render(text, True, color_inactive)                                                       # render the image of the text name
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)                                                              # width increases if the name becomes too big
            input_box.w = width                                                                                         # finds the width of the input box
            # Blit the text.
            display.blit(txt_surface, (input_box.x + 5, input_box.y + 5))                                               # blit the new box onto the screen
            # Blit the input_box rect.
            pygame.draw.rect(display, color, input_box, 2)                                                              # drawing a rectangle
            names += text                                                                                               # enters the name onto a variable
            pygame.display.flip()                                                                                       # updates a part of screen
            pygame.display.update()                                                                                     # updates the whole screen

        if check[0] == 1:                                                                                               # if next has been clicking then it returns the text and goes onto next screen
            return text

    return text                                                                                                         # returns the text

pygame.display.set_caption('SNAKE GAME')                                                                                # heading for game window
icon = pygame.image.load("icons/logo.png")                                                                              # icon on the heading
pygame.display.set_icon(icon)                                                                                           # setting heading icon

name = intro_page()                                                                                                     # the name is the only thing returned from the intro page

desolate = pygame.image.load("wallpaper/wallpaper_wipe.png")                                                            # this image is the wipe image that is used after each reset
desolate = pygame.transform.scale(desolate, (960, 540))                                                                 # transforms image to the right size


color_inactive = pygame.Color((250, 90, 90))                                                                            # setting the color light red for regular use
color_active = pygame.Color((255, 0, 0))                                                                                # setting the color dark red for selected use
colorbox = color_inactive                                                                                               # initial color is active

snake_speed, snake_color, snake_wallpaper, snake_food, snake_song, snake_displaysize = -1, -1, -1, -1, -1, -1           # initial values of variable to store aspects of the program


def enter_sql(name, score, speed, size):                                                                                # function for entering new data in mysql
    if speed == 15:                                                                                                     # if value of speed is 15, it can enter slow
        speed = "slow"                                                                                                  # speed is assigned as slow
    elif speed == 30:                                                                                                   # if value of speed is 30, it can enter medium
        speed = "medium"                                                                                                # speed is assigned as medium
    elif speed == 50:                                                                                                   # if value of speed is 50, it can enter fast
        speed = "fast"                                                                                                  # speed is assigned as fast
    elif speed == 70:                                                                                                   # if value of speed is 70, it can enter plaid
        speed = "plaid"                                                                                                 # speed is assigned as plaid

    if size == 0:                                                                                                       # if size is 0, it can enter small
        size = "small"                                                                                                  # size is assigned as small
    elif size == 1:                                                                                                     # if size is 1, it can enter medium
        size = "medium"                                                                                                 # size is assigned as medium
    elif size == 2:                                                                                                     # if size is 2, it can enter large
        size = "large"                                                                                                  # size is assigned as large
    elif size == 3:                                                                                                     # if size is 3, it can enter colossal
        size = "colossal"                                                                                               # size is assigned as colossal

    cursor = mycon.cursor()                                                                                             # cursor is defined
                                                                                                                        # statement for entering new value

    statement_enter = "INSERT INTO scores(name, score, speed, size) values('{}','{}','{}','{}')".format(name, score, speed, size)

                                                                                                                        # statement for updating existing value

    statement_update = "UPDATE scores set score = '{}', speed = '{}' ,size = '{}'" \
                       "WHERE name = '{}'".format(score, speed, size, name)

    flag = -1                                                                                                           # flag to check if name already exists
    cursor.execute("select * from scores")                                                                              # selects all the scores
    data = cursor.fetchall()                                                                                            # collects all the data

    for i in data:                                                                                                      # iterates through the data
        if name == i[0]:                                                                                                # if name exists in the database,
            flag = -2
            if score > i[1]:                                                                                            # if the score is greater than the previous high score
                flag = 1                                                                                                # sets the flag

    if flag >= 0:
        cursor.execute(statement_update)                                                                                # updates the statement
        mycon.commit()                                                                                                  # fixes the thing into mysql
    elif flag == -1:
        cursor.execute(statement_enter)                                                                                 # enters new value into mysql
        mycon.commit()                                                                                                  # fixes the thign into mysql


def box(x, y, box_color=color_inactive):                                                                                # function to insert a box onto the display
    box_to_use = pygame.Rect(x, y, 120, 30)                                                                             # defines the location and size of the boxes
    pygame.draw.rect(display, box_color, box_to_use)                                                                    # inserts box onto display


def loading(x, y, color, length, fill):                                                                                 # function for loading bar
    if fill == False:                                                                                                   # fill is equal to False
        box_to_use = pygame.Rect(x, y, length, 20)                                                                      # draws a rectangle with a rectangle with width 2
        pygame.draw.rect(display, color, box_to_use, width=2)
    else:
        box_to_use = pygame.Rect(x, y, length, 20)                                                                      # if fill is equal to true
        pygame.draw.rect(display, color, box_to_use)                                                                    # draws a rectangle with fillerss


def wipe():                                                                                                             # wipes the full screen and puts back the main boxes after each selection
    display.blit(desolate, (0, 0))


def button(event, options, x_location, y_location, box_name, box_value):                                                # function for creating the sub options
    b = True
    pygame.draw.rect(display, color_active, box_name)                                                                   # if mouse is hovering over button the color changes
    if box_value != -1:
        for i in range(int(len(options) / 2)):
            if box_value == options[i]:
                message(options[i + int(len(options) / 2)], (0, 0, 0), x_location + 30, y_location + 10, 24)            # it allows you to put the name you selected on the main box
    else:
        message("Select", (0, 0, 0), x_location + 30, y_location + 10, 24)                                              # if you dont choose a option, it shows "select" on the main box
    sub_buttons = {}                                                                                                    # contains the sub buttons
    for i in range(int(len(options) / 2)):
        sub_buttons[i] = pygame.Rect(x_location, y_location + (30 * (i + 1)), 120, 30)                                  # stores the sub buttons

    if event.type == pygame.MOUSEBUTTONDOWN:                                                                            # checks if you have clicked anything
        global a
        a = True
        w = False
        if box_name.collidepoint(event.pos):                                                                            # checks if you clicked on the sub box
            main_button_sound = pygame.mixer.Sound(main_button)                                                         # loads in the sound for clicking the sub button
            pygame.mixer.Channel(1).set_volume(1)                                                                       # sets the volume of the button click
            pygame.mixer.Channel(1).play(main_button_sound)                                                             # plays the button click sound
            for i in range(int(len(options) / 2)):
                box(x_location, y_location + (30 * (i + 1)))                                                            # draws the box and the text of each sub box
                message(options[i + int(len(options) / 2)], (0, 0, 0), x_location + 30,
                        y_location + 10 + (30 * (i + 1)), 20)

            while a:
                for event in pygame.event.get():                                                                        # checks for the presence of any event in pygame

                    mousepos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:                                                                       # quits the pygame if you click on the close icon
                        pygame.quit()                                                                                   # quits pygame
                        a = False
                    for i in range(int(len(options) / 2)):                                                              # checks if you have clicked any of the sub options
                        if (x_location <= mousepos[0] <= x_location + 120) and (                                        # checks if x location matches
                                (y_location + (30 * (i + 1))) <= mousepos[1] <= (y_location + (30 * (i + 2)))):         # checks if the y location of mouse covers the box
                            pygame.draw.rect(display, color_active, sub_buttons[i])                                     # makes the box in darker color
                            message(options[i + int(len(options) / 2)], (0, 0, 0), x_location + 30,                     # puts the messages on the sub boxes
                                    y_location + 10 + (30 * (i + 1)), 20)
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                sub_button_sound = pygame.mixer.Sound(sub_button)                                       # loads in the sound for sub button
                                pygame.mixer.Channel(2).set_volume(1)                                                   # loads the volume of the sub button
                                pygame.mixer.Channel(2).play(sub_button_sound)                                          # play the sound for the button click
                                a = False
                                box_value = i
                                pygame.event.clear()                                                                    # clear all the values for the
                                w = True

                        else:
                            pygame.draw.rect(display, colorbox, sub_buttons[i])                                         # makes the box in regular color
                                                                                                                        # put the message on all sub buttons
                            message(options[i + int(len(options) / 2)], (0, 0, 0), x_location + 30,
                                    y_location + 10 + (30 * (i + 1)), 20)
                        if w:                                                                                           # if an option is clicked on wipe the screen
                            wipe()                                                                                      # functions to wipe
                    if (x_location <= mousepos[0] <= x_location + 120) and (                                            # code to make the drop down disappear when you click on another area other than the sub button
                            (y_location + (30 * (i + 1))) <= mousepos[1] <= (y_location + (30 * (i + 2)))):
                        pass
                    elif event.type == pygame.MOUSEBUTTONDOWN:                                                          # if mouse clicks somewhere else it wipes
                        wipe()                                                                                          # wipe function
                        a = False
                        break

        else:
            b = False
    return b, box_value


def else_button(options, x_location, y_location, box_name, box_value):                                                  # if an option is not clicked on
    pygame.draw.rect(display, colorbox, box_name)                                                                       # it draws a blank box
    if box_value != -1:                                                                                                 # if an option has already been selected
        for i in range(int(len(options) / 2)):                                                                          # make the option you have chosen appear on the main box
            if box_value == options[i]:
                message(options[i + int(len(options) / 2)], (0, 0, 0), x_location + 30, y_location + 10, 24)
    else:
        message("Select", (0, 0, 0), x_location + 30, y_location + 10, 24)                                              # make the word "select" appear on the top if no option has been chosen


def end_screen(display_width, display_height, size, speed, size_of_display, image, score):                              # screen shown when the game ends

    if size_of_display == 0:                                                                                            # sets up the screen depending on which size display has been chosen
        background = pygame.Surface((300, 200))                                                                         # if size of display is small
    elif size_of_display == 1:
        background = pygame.Surface((460, 300))                                                                         # if size of display is medium
    elif size_of_display == 2:
        background = pygame.Surface((1000, 600))                                                                        # if size of display is large
    elif size_of_display == 3:
        background = pygame.Surface((1300, 680))                                                                        # if size of display is colossal

    background.fill((0, 0, 0))                                                                                          # backdrop color
    pygame.display.update()                                                                                             # updates the screen
    image = image.convert()                                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster
    i = 255
    global flag                                                                                                         # defines flag

    if flag == False:                                                                                                   # flag prevents the running of fade again and again
        while i != 40:                                                                                                  # fade till brightness reaches 40,(max is 255)
            image.set_alpha(i)                                                                                          # sets the brightness value of iamge
            display.blit(background, (0, 30))                                                                           # blits the background image
            display.blit(image, (0, 30))                                                                                # blits the overlapping image
            pygame.time.delay(1)
            i = i - 1                                                                                                   # step values for the fade
            pygame.display.update()                                                                                     # updates the screen

            flag = True                                                                                                 # resets flag

    retry = pygame.image.load("icons/retry.png")                                                                        # loading retry icon into pygame
    exit = pygame.image.load("icons/exit.png")                                                                          # loading exit icon into pygame
    over = pygame.image.load("icons/game over.png")                                                                     # loading game over icon into pygame

    retry_dark = pygame.image.load("icons/retry_dark.png")                                                              # loading dark retry icon into pygame
    exit_dark = pygame.image.load("icons/exit_dark.png")                                                                # loading dark retry icon into pygame

    retry = pygame.transform.scale(retry, (size, size))                                                                 # scale retry icon
    exit = pygame.transform.scale(exit, (size, size))                                                                   # scale exit icon
    retry_dark = pygame.transform.scale(retry_dark, (size, size))                                                       # scale dark retry icon
    exit_dark = pygame.transform.scale(exit_dark, (size, size))                                                         # scale dark exit icon

    over = pygame.transform.scale(over, (size * 6, size * 6))                                                           # scale over icon

    single_star = pygame.image.load("icons/single_star.png")                                                            # loading single star icon into pygame
    triple_star = pygame.image.load("icons/triple_star.png")                                                            # loading triple star icon into pygame

    single_star = pygame.transform.scale(single_star, (size*6, size*6))                                                 # scale single star icon
    triple_star = pygame.transform.scale(triple_star, (size*6, size*6))                                                 # scale triple star icon

    lead = display_sql()                                                                                                # gets the data from sql
    players = len(lead)                                                                                                 # find the length of the sql table
    for i in range(players):                                                                                            # code to find top players
        for j in range(0, players - i - 1):
            if lead[j][1] < lead[j + 1][1]:
                lead[j], lead[j + 1] = lead[j + 1], lead[j]


    flag_100 = [0]                                                                                                      # flag to check which exit screen to show

    for i in lead:                                                                                                      # code to check if you beat your personal high score
        if name == i[0]:
            if score > i[1]:

                flag_100[0]= 1
    if score> lead[0][1]:                                                                                               # check if you beat the global highscore
        flag_100[0] = 2

    if flag_100[0] == 0:                                                                                                # if you did not beat any highscore
        display.blit(over, ((display_width) / 2 - (size * 6) / 2, display_height / 3))                                  # blits the game over icon
    elif flag_100[0] == 1:                                                                                              # if you beat personal highscore
        display.blit(single_star, ((display_width) / 2 - (size * 6) / 2, display_height / 3))                           # blits the single star icon
    elif flag_100[0] == 2:                                                                                              # if you beat the global highscore
        display.blit(triple_star,((display_width)/2 - (size*6) /2 , display_height/3))                                  # blits the triple star icon

    mousepos_exit = pygame.mouse.get_pos()                                                                              # get the mouse position

    exit_x = (display_width / 2 - (size * 5))                                                                           # x location  of exit icon
    exit_y = (display_height / 2 + size * 4)                                                                            # y location of exit icon
    retry_x = (display_width / 2 + (size * 4))                                                                          # x location of retry icon
    retry_y = (display_height / 2 + size * 4)                                                                           # y location of retry icon

    if exit_x <= mousepos_exit[0] <= (exit_x + size) and exit_y <= mousepos_exit[1] <= (exit_y + size):                 # if mouse is over the game over icon
        display.blit(exit, ((display_width / 2 - (size * 5)), display_height / 2 + size * 4))                           # makes the exit icon light if mouse hovers
        for event_2 in pygame.event.get():                                                                              # check for the presence of any event
            if event_2.type == pygame.MOUSEBUTTONDOWN:                                                                  # check for mouse button click
                enter_sql(name,score,speed,size_of_display)                                                             # enter the data of current game into mysql
                print(name, score, speed, size_of_display)                                                              # print this data of current game
                game_over[0] = True                                                                                     # full gme gets over
                game_close[0] = False
                flag_3[0] = 2
                return

    else:
        display.blit(exit_dark, ((display_width / 2 - (size * 5)), display_height / 2 + size * 4))                      # blits the dark image if mouse is not hovering

    if retry_x <= mousepos_exit[0] <= (retry_x + size) and retry_y <= mousepos_exit[1] <= (retry_y + size):             # checks if mouse is hovering over retry icon
        display.blit(retry, ((display_width / 2 + (size * 4)), display_height / 2 + size * 4))                          # makes icon light if it hovers
        for event_2 in pygame.event.get():                                                                              # checks for the presence of any event
            if event_2.type == pygame.MOUSEBUTTONDOWN:                                                                  # checks if button is pressed
                enter_sql(name, score, speed, size_of_display)                                                          # enters data in mysql
                flag = False                                                                                            # restarts the name
                flag_3[0] = 1
                return
    else:
        display.blit(retry_dark, ((display_width / 2 + (size * 4)), display_height / 2 + size * 4))                     # if mouse is not hovering over icon, it is dark

    pygame.display.update()                                                                                             # updates the screen


if goto[0] == 0:                                                                                                        # default game type(without quickplay)

    image = pygame.image.load("wallpaper/wallpaper_clean.png")                                                          # background iamge
    image = pygame.transform.scale(image, (960, 540))                                                                   # scales image correctly
    image = image.convert()                                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster

    main_fadein = pygame.image.load("wallpaper/wallpaper_main_fadein.png")                                              # image to fade in
    main_fadein = pygame.transform.scale(main_fadein, (960, 540))                                                       # scales image correctly
    main_fadein = main_fadein.convert()                                                                                 # converts the pygame.surface to same pixel format as the one created by us, makes code faster
    i = 0
    while i != 255:                                                                                                     # fades to bright full brightness
        main_fadein.set_alpha(i)                                                                                        # sets brightness
        display.blit(image, (0, 0))                                                                                     # blits the backdrop image
        display.blit(main_fadein, (0, 0))                                                                               # blits the fade in image
        pygame.time.delay(1)                                                                                            # delay for the fade
        i += 5                                                                                                          # step value
        pygame.display.update()                                                                                         # update the screen

    box_x = 270
    box_y = 140
    snake_speed_box = pygame.Rect(box_x, box_y, 120, 40)                                                                # snake speed box
    snake_color_box = pygame.Rect(box_x + 300, box_y, 120, 40)                                                          # snake color box
    wallpaper_box = pygame.Rect(box_x, box_y + 100, 120, 40)                                                            # wallpaper box
    food_type_box = pygame.Rect(box_x + 300, box_y + 100, 120, 40)                                                      # food box
    song_box = pygame.Rect(box_x, box_y + 200, 120, 40)                                                                 # song box
    display_size_box = pygame.Rect(box_x + 300, box_y + 200, 120, 40)                                                   # display size box

    pygame.display.update()                                                                                             # update display

    mousepos = ()
    run = True
    next_x, next_y = 610, 480                                                                                           # location of next button
    selected = 0

    main_button = ("songs/main_button.mp3")                                                                             # main button sound
    sub_button = ("songs/sub_button.mp3")                                                                               # sub button sound
    next_button = ("songs/next_button.mp3")                                                                             # next button sound

    while run:                                                                                                          # while the programming is running
        for event in pygame.event.get():                                                                                # checking for event in pygame

            mousepos = pygame.mouse.get_pos()                                                                           # find the position of mouse

            a = False
            if event.type == pygame.QUIT:                                                                               # quit pygame when close is clicked on
                pygame.quit()                                                                                           # quit pygame
                run = False

            if box_x <= mousepos[0] <= box_x + 120 and box_y <= mousepos[1] <= box_y + 40:                              # check if mouse is over speed box
                options = [0, 1, 2, 3, "Slow", "Medium", "Fast", "Plaid"]                                               # options for speed otpion
                x_location = box_x                                                                                      # x location of button
                y_location = box_y                                                                                      # y location of button
                returned = button(event, options, x_location, y_location, snake_speed_box, snake_speed)                 # find the value that has been chosen for speed
                if not returned[0]:
                    break
                snake_speed = returned[1]
                pygame.display.update()                                                                                 # update the screen
            else:
                options = [0, 1, 2, 3, "Slow", "Medium", "Fast", "Plaid"]                                               # options for speed option
                x_location = box_x                                                                                      # x location of button
                y_location = box_y                                                                                      # y location of button
                else_button(options, x_location, y_location, snake_speed_box, snake_speed)                              # if button hasnt been clicked
                pygame.display.update()                                                                                 # update the python screen

            if box_x + 300 <= mousepos[0] <= box_x + 420 and box_y <= mousepos[1] <= box_y + 40:                        # check if mouse is over color box
                options = [0, 1, 2, 3, 4, 5, 6, "Black", "Red", "White", "Yellow", "Green", "Blue", "Purple"]           # options for color option
                x_location = box_x + 300                                                                                # x location of button
                y_location = box_y                                                                                      # y location of button
                returned = button(event, options, x_location, y_location, snake_color_box, snake_color)                 # find the value that has been chosen for color
                if not returned[0]:
                    break
                snake_color = returned[1]
            else:
                options = [0, 1, 2, 3, 4, 5, 6, "Black", "Red", "White", "Yellow", "Green", "Blue", "Purple"]           # options for color option
                x_location = box_x + 300                                                                                # x loction of button
                y_location = box_y                                                                                      # y location of button
                else_button(options, x_location, y_location, snake_color_box, snake_color)                              # if button hasnt been clicked

            if box_x <= mousepos[0] <= box_x + 120 and box_y + 100 <= mousepos[1] <= box_y + 140:                       # checks if mouse is over the wallpaper box
                options = [0, 1, 2, 3, 4, 5, "Mars", "Forest", "City", "Ocean", "Microverse", "Milky Way"]          # options for wallpaper option
                x_location = box_x                                                                                      # x location of button
                y_location = box_y + 100                                                                                # y location of button
                returned = button(event, options, x_location, y_location, wallpaper_box, snake_wallpaper)               # find the value that has been chosen for wallpaper
                if not returned[0]:
                    break
                snake_wallpaper = returned[1]
            else:
                options = [0, 1, 2, 3, 4, 5, "Mars", "Forest", "City", "Ocean", "Microverse", "Milky Way"]       # options for wallpaper option
                x_location = box_x                                                                                      # x location of button
                y_location = box_y + 100                                                                                # y location of button
                else_button(options, x_location, y_location, wallpaper_box, snake_wallpaper)                            # if button hasnt been clicked

            if box_x + 300 <= mousepos[0] <= box_x + 420 and box_y + 100 <= mousepos[1] <= box_y + 140:                 # checks if the mouse is over the food icon
                options = [0, 1, 2, 3, 4, 5, 6, "Burger", "Taco", "Doritos", "Pizza", "Sushi", "Doughnut", "Cookie"]    # options for the food option
                x_location = box_x + 300                                                                                # x location of button
                y_location = box_y + 100                                                                                # y location of button
                returned = button(event, options, x_location, y_location, food_type_box, snake_food)                    # find the value that has been chosen for food
                if not returned[0]:
                    break
                snake_food = returned[1]
            else:
                options = [0, 1, 2, 3, 4, 5, 6, "Burger", "Taco", "Doritos", "Pizza", "Sushi", "Doughnut", "Cookie"]    # options for the food option
                x_location = box_x + 300                                                                                # x location of button
                y_location = box_y + 100                                                                                # y location of button
                else_button(options, x_location, y_location, food_type_box, snake_food)                                 # if button hasnt been clicked

            if box_x <= mousepos[0] <= box_x + 120 and box_y + 200 <= mousepos[1] <= box_y + 240:                       # checks if the mouse is over the music option
                options = [0, 1, 2, 3, 4, "Epic", "Extreme", "Racing", "Chase", "Doom"]                                 # options for the song option
                x_location = box_x                                                                                      # x location of button
                y_location = box_y + 200                                                                                # y location of button
                returned = button(event, options, x_location, y_location, song_box, snake_song)                         # find the value that has been chosen for song
                if not returned[0]:
                    break
                snake_song = returned[1]
            else:
                options = [0, 1, 2, 3, 4, "Epic", "Extreme", "Racing", "Chase", "Doom"]                                 # options for the song option
                x_location = box_x                                                                                      # x location of button
                y_location = box_y + 200                                                                                # y location of button
                else_button(options, x_location, y_location, song_box, snake_song)                                      # if the button hasnt been clicked

            if box_x + 300 <= mousepos[0] <= box_x + 420 and box_y + 200 <= mousepos[1] <= box_y + 240:                 # checks if the mouse is over the size option
                options = [0, 1, 2, 3, "Small", "Medium", "Large", "Colossal"]                                          # options for the size option
                x_location = box_x + 300                                                                                # x location of button
                y_location = box_y + 200                                                                                # y location of button
                returned = button(event, options, x_location, y_location, display_size_box, snake_displaysize)          # find the value that has been chosen for size
                if not returned[0]:
                    break
                snake_displaysize = returned[1]
            else:
                options = [0, 1, 2, 3, "Small", "Medium", "Large", "Colossal"]                                          # options for the size option
                x_location = box_x + 300                                                                                # x location of button
                y_location = box_y + 200                                                                                # y location of button
                else_button(options, x_location, y_location, display_size_box, snake_displaysize)                       # if the button hasnt been clicked

            if 605 <= mousepos[0] <= 655 and 450 <= mousepos[1] <= 500:                                                 # check if the mouse is over next button
                display.blit(next, (605, 450))                                                                          # make button light if mouse hovers

            else:
                display.blit(next_dark, (605, 450))                                                                     # make button dark if mouse is not hovering

            if snake_color != -1 and snake_speed != -1 and snake_song != -1 and snake_food != -1 and snake_wallpaper != -1 and snake_displaysize != -1:
                selected = 1

            if event.type == pygame.MOUSEBUTTONDOWN and selected == 1:                                                  # if button is pressed down
                # if the mouse is clicked on the button the game is terminated
                if 605 <= mousepos[0] <= 655 and 450 <= mousepos[1] <= 500:                                             # checks if mouse is over next icon
                    run = False
                    pygame.mixer.music.load(next_button)                                                                # loads music for button icon
                    pygame.mixer.music.set_volume(1)                                                                    # sets volume of button
                    pygame.mixer.music.play()                                                                           # plays the music
                    pygame.mixer.Channel(0).fadeout(2000)                                                               # fades the music in 2 seconds
                    loading(380, 465, (255, 255, 255), 200, fill=False)                                                 # loading icon is done here
                    for i in range(0, 200):
                        loading(380, 465, (255, 255, 255), i, fill=True)                                                # loading bar is moving
                        time.sleep(0.01)                                                                                # delay for loading bar
                        pygame.display.update()


            elif selected == 0 and pygame.MOUSEBUTTONDOWN and (                                                         # code for if everyone doesnt choose all options
                    605 <= mousepos[0] <= 655 and 400 <= mousepos[1] <= 500):                                           # ask them to select all the options
                message('Please select all options', (255, 255, 255), 380, 465, 25)                                     # message" sleect all options"
elif goto[0] == 1:                                                                                                      # if you click on quickplqy
    data = display_sql()                                                                                                # collect all data from mysql

    for i in data:                                                                                                      # iterating through mysql data
        if name == i[0]:                                                                                                # if name exists in database
            snake_speed = i[2]                                                                                          # sets speed to persons previous speed
            snake_displaysize = i[3]                                                                                    # sets display size to persons previous display size
            print("name exists in database")
            break
        else:
            snake_speed = "medium"                                                                                      # default speed is medium if person doesnt exist
            snake_displaysize = "medium"                                                                                # default size is medium if person doesnt exists
            print("name doesnt exist")
    if snake_speed == "slow":                                                                                           # setting code for speed as 0 if speed is slow
        snake_speed = 0
    elif snake_speed == "medium":                                                                                       # setting code for speed as 1 if speed is medium
        snake_speed = 1
    elif snake_speed == "fast":                                                                                         # setting code for speed as 2 if speed is fast
        snake_speed = 2
    elif snake_speed == "plaid":                                                                                        # setting code for speed as 3 if speed is plaid
        snake_speed = 3

    if snake_displaysize == "small":                                                                                    # setting code for size as 0 if size is small
        snake_displaysize = 0
    elif snake_displaysize == "medium":                                                                                 # setting code for size as 1 if size is medium
        snake_displaysize = 1
    elif snake_displaysize == "large":                                                                                  # setting code for size as 2 if size is large
        snake_displaysize = 2
    elif snake_displaysize == "colossal":                                                                               # setting code for size as 3 if size is colossal
        snake_displaysize = 3

    snake_color = 0                                                                                                     # setting default snake color
    snake_wallpaper = 2                                                                                                 # setting default snake wallpaper
    snake_food = 0                                                                                                      # setting default snake food
    snake_song = 0                                                                                                      # setting default snake background song

print("SNAKE SPEED = ", snake_speed)                                                                                    # print game settings
print("SNAKE COLOR = ", snake_color)
print("SNAKE WALLPAPER = ", snake_wallpaper)
print("SNAKE FOOD = ", snake_food)
print("SNAKE SONG = ", snake_song)
print("SNAKE DISPLAY SIZE = ", snake_displaysize)
print("CHARACTER NAME = ", name)
                                                                                                                        # dictionary to store the colors
colors = {0: (0, 0, 0), 1: (255, 0, 0), 2: (255, 255, 255), 3: (255, 255, 0),
          4: (0, 255, 0), 5: (0, 0, 255), 6: (255, 128, 0), 7: (153, 0, 153)}
# 0 = black
# 1 = red
# 2 = white
# 3 = yellow
# 4 = green                                                                                                             #
# 5 = blue
# 6 = purple

flag_4 = [False]
flag_3 = [0]
flag = False
game_over = [False]                                                                                                     #
game_close = [False]


def enter_game(speed, snake_color, size_of_display, wallpaper, food_type, music_type,
               name):                                                                                                   # function for the full game part
    print(size_of_display)
    if size_of_display == 0:                                                                                            # if we choose the display size "small"
        display_width, display_height = 300, 200                                                                        # pixel size of game window
    elif size_of_display == 1:                                                                                          # if we choose the display size "medium"
        display_width, display_height = 460, 300                                                                        # pixel size of game window
    elif size_of_display == 2:                                                                                          # if we choose the display size "large"
        display_width, display_height = 1000, 600                                                                       # pixel size of game window
    elif size_of_display == 3:
        display_width, display_height = 1300, 680                                                                       # backup display size

    food = pygame.image.load("food/" + str(food_type) + ".png")                                                         # loading the food image
    food = pygame.transform.scale(food, (30, 30))                                                                       # setting size of food to 30 by 30 pixels

    background = pygame.image.load("wallpaper/" + str(wallpaper) + ".png")                                              # loading the wallpaper to the code
    background = pygame.transform.scale(background, (display_width, display_height - 30))                               # setting size of wallpaper

    music = ("songs/background_song/" + str(music_type) + ".mp3")                                                       # file for game background music
    if speed == 0:                                                                                                      # settings speed as 15 if code is 0
        speed = 15
    elif speed == 1:                                                                                                    # setting speed as 30 if code is 1
        speed = 30
    elif speed == 2:                                                                                                    # setting speed as 50 if code is 2
        speed = 50
    elif speed == 3:                                                                                                    # setting speed as 70 if code is 3
        speed = 70
    snake_block, snake_speed = 10, speed                                                                                # setting thickness and speed of snake

    display = pygame.display.set_mode((display_width, display_height))                                                  # using earlier value to set display size
    pygame.display.set_caption('SNAKE GAME')                                                                            # heading for game window
    icon = pygame.image.load("icons/logo.png")                                                                          # icon on the top of the bar
    pygame.display.set_icon(icon)                                                                                       # setting icon on the top

    def snake(snake_block_function, snake_list_function):                                                               # function for drawing the snake
        for site in snake_list_function:                                                                                # loop for each individual block in the snake
            # pygame.draw.circle(display, colors[snake_color], [site[0]+5, site[1]+5], snake_block_function/2, width=3)
            pygame.draw.rect(display, colors[snake_color],
                             [site[0], site[1], snake_block_function, snake_block_function],
                             width=3)                                                                                   # actual drawing of snake(draws box by box)

    def message(msg, color, width_location, height_location, size):                                                     # function for putting messages in window
        mesg = pygame.font.SysFont("Corbel", size).render(msg, True,
                                                          color)                                                        # setting font and size and color of message
        display.blit(mesg, (width_location, height_location))                                                           # setting location of message in window

    def game():                                                                                                         # function for game play

        game_over[0] = False                                                                                            # variable for quitting whole game
        game_close[0] = False                                                                                           # window for GAME OVER
        x, y = display_width / 2, display_height / 2                                                                    # setting initial location of snake
        x_change, y_change = 0, 0                                                                                       # change in position of snake head
        snake_list = []                                                                                                 # list with each block in snake
        length_of_snake = 1                                                                                             # length of snake
        score = 0                                                                                                       # initial score

        foodx = (random.randint(0, round((display_width - snake_block * 3) / 10)) * 10)                                 # x coordinate of x
        foody = (random.randint(3, round((display_height - snake_block * 3) / 10)) * 10)                                # y coordinate of y

        if goto[0] == 1:                                                                                                # if quickplay is there dont change music
            pass
        elif goto[0] == 0:                                                                                              # if quickplay is not there then dont change the music
            pygame.mixer.music.load(music)                                                                              # loading in the music
            pygame.mixer.music.set_volume(0.3)                                                                          # setting volume of music
            pygame.mixer.music.play(-1)                                                                                 # loop the music

        while not game_over[0]:                                                                                         # loop for whole game

            while game_close[0]:                                                                                        # loop for each repeating of game
                if size_of_display == 0:                                                                                # condition if wallpaper is small
                    end_screen(display_width, display_height, 15, speed, size_of_display, background, score)            # shows the game over screen

                elif size_of_display == 1:                                                                              # condition if wallpaper is medium
                    end_screen(display_width, display_height, 22, speed, size_of_display, background, score)            # shows the game over screen

                elif size_of_display == 2:                                                                              # condition if wallpaper is large
                    end_screen(display_width, display_height, 35, speed, size_of_display, background, score)            # shows the game over screen

                elif size_of_display == 3:
                    end_screen(display_width, display_height, 40, speed, size_of_display, background, score)            # shows the game over screen

                    display_sql()                                                                                       # display all the data

                pygame.display.update()                                                                                 # updating display after each iteration

                if flag_3[0] == 1:
                    flag_3[0] = 0

                    if size_of_display == 0:                                                                            # if size of display code is 0
                        background_2 = pygame.Surface((300, 200))
                    elif size_of_display == 1:                                                                          # if size of display code is 1
                        background_2 = pygame.Surface((460, 300))
                    elif size_of_display == 2:                                                                          # if size of display code is 2
                        background_2 = pygame.Surface((1000, 600))
                    elif size_of_display == 3:                                                                          # if size of dissplay code is 3
                        background_2 = pygame.Surface((1300, 680))

                    image = pygame.image.load(
                        "wallpaper/" + str(wallpaper) + ".png")                                                         # loading the wallpaper to the code
                    image = pygame.transform.scale(image,
                                                   (display_width, display_height - 30))                                # setting size of wallpaper

                    background_2.fill((0, 0, 0))                                                                        # fill backdrop with black color
                    pygame.display.update()                                                                             # update the screen
                    image = image.convert()                                                                             # converts the pygame.surface to same pixel format as the one created by us, makes code faster
                    i = 40                                                                                              # bightness set to 40

                    if flag_4[0] == False:                                                                              # fade in for the game
                        while i < 254:                                                                                  # till max brightness
                            image.set_alpha(i)                                                                          # set brightness of wallpaper
                            display.blit(background_2, (0, 30))                                                         # set the backdrop image
                            display.blit(image, (0, 30))                                                                # set the fade in image
                            pygame.time.delay(1)                                                                        # delay for the fade
                            i = i + 4                                                                                   # step value for the fade
                            pygame.display.update()                                                                     # update the screen

                            flag_4[0] = True
                    flag_4[0] = False
                    game()                                                                                              # call the game

                for event in pygame.event.get():                                                                        # loop through key pressed
                    if event.type == pygame.KEYDOWN:                                                                    # checking if key is pressed
                        if event.key == pygame.K_q:                                                                     # checking if q is pressed
                            game_over[0] = True                                                                         # full game will QUIT
                            game_close[0] = False
                        if event.key == pygame.K_c:                                                                     # restart game if c is pressed
                            global flag
                            flag = False
                            flag_4[0] = False

                            game()                                                                                      # game function

            file = open("scores.txt", "r+")                                                                             # open SCORES file which has past highscores
            read_score = file.readline()                                                                                # read first line of SCORES file
            highscore = int(read_score[12:])                                                                            # reads the numerical part of file

            for event in pygame.event.get():                                                                            # loop to check if you click on close sign
                if event.type == pygame.QUIT:                                                                           # check if close is clicked

                    game_over[0] = True                                                                                 # full game closes

                if x_change == snake_block:                                                                             # prevents quit if u go left while going right
                    if event.type == pygame.KEYDOWN:                                                                    # check if key is pressed
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:                                       # check if DOWN is clicked
                            break                                                                                       # skip loop if u go left while going right
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:                                    # check if RIGHT is clicked
                            x_change = snake_block                                                                      # move 1 block right
                            y_change = 0                                                                                # move 0 block along y axis
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:                                       # check if UP is clicked
                            x_change = 0                                                                                # move 0 block along x axis
                            y_change = -snake_block                                                                     # move 1 block  up
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:                                     # check if DOWN is clicked
                            x_change = 0                                                                                # move 0 block along x axis
                            y_change = snake_block                                                                      # move 1 block down

                elif x_change == -snake_block:                                                                          # prevents quit if u go right while going left
                    if event.type == pygame.KEYDOWN:                                                                    # check if key is pressed
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:                                       # check if LEFT is clicked
                            x_change = -snake_block                                                                     # move 1 block left
                            y_change = 0                                                                                # move 0 block along y axis
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:                                    # check if RIGHT is clicked
                            break                                                                                       # skip loop if u go right while going left
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:                                       # check if UP is clicked
                            x_change = 0                                                                                # move 0 block along x axis
                            y_change = -snake_block                                                                     # move 1 block up
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:                                     # check if DOWN is clicked
                            x_change = 0                                                                                # move 0 block along x axis
                            y_change = snake_block                                                                      # move 1 block down

                elif y_change == snake_block:                                                                           # prevents quit if you go up while going down
                    if event.type == pygame.KEYDOWN:                                                                    # check if key is pressed
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:                                       # check if LEFT is clicked
                            x_change = -snake_block                                                                     # move 1 block left
                            y_change = 0                                                                                # move 0 block along y axis
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:                                    # check if RIGHT is clicked
                            x_change = snake_block                                                                      # move 1 block right
                            y_change = 0                                                                                # move 0 block along y axis
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:                                       # check if UP is clicked
                            break                                                                                       # skip loop if you got up while going down
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:                                     # check if DOWN is clicked
                            x_change = 0                                                                                # move 0 block along x axis
                            y_change = snake_block                                                                      # move 1 block down

                elif y_change == -snake_block:                                                                          # prevents quit if you go down while going up
                    if event.type == pygame.KEYDOWN:                                                                    # check if key is pressed
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:                                       # check if LEFT is clicked
                            x_change = -snake_block                                                                     # move 1 block left
                            y_change = 0                                                                                # move 0 along y axis
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:                                    # check if RIGHT is clicked
                            x_change = snake_block                                                                      # move 1 block along right
                            y_change = 0                                                                                # move 0 black along y axis
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:                                       # check if UP is clicked
                            x_change = 0                                                                                # move 0 block along x axis
                            y_change = -snake_block                                                                     # move 1 block up
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:                                     # check if DOWN is clicked
                            break                                                                                       # skip loop if you go down while going up

                else:                                                                                                   # to prevent block from moving initially
                    if event.type == pygame.KEYDOWN:                                                                    # check if key pressed
                        if event.key == pygame.K_LEFT:                                                                  # check if LEFT is clicked
                            x_change = -snake_block                                                                     # move 1 block down
                            y_change = 0                                                                                # move 0 block along y axis
                        elif event.key == pygame.K_RIGHT:                                                               # check if RIGHT is clicked
                            x_change = snake_block                                                                      # move 1 block right
                            y_change = 0                                                                                # move 0 block along y axis
                        elif event.key == pygame.K_UP:                                                                  # check if UP is clicked
                            x_change = 0                                                                                # move 0 block along x axis
                            y_change = -snake_block                                                                     # move 1 block up
                        elif event.key == pygame.K_DOWN:                                                                # check if DOWN is clicked
                            x_change = 0                                                                                # move 0 block along x axis
                            y_change = snake_block                                                                      # move 1 block down

            if x >= display_width or x < 0 or y >= display_height or y < 30:                                            # condition to check if snake hits border
                game_close[0] = True                                                                                    # close the game if snake hits border
            x += x_change                                                                                               # actual moving of snake along x axis
            y += y_change                                                                                               # actual moving of snake along y axis

            display.blit(background, (0, 30))                                                                           # setting location of wallpaper
            pygame.draw.rect(display, (211, 211, 211), (0, 0, display_width, 30))                                       # drawing the black box on the top
            display.blit(food, (foodx, foody))                                                                          # setting location of food
            message("Score = " + str(score) + "    Highscore = " + str(highscore), colors[1], 5, 5,
                    size=20)                                                                                            # putting the score and highscore on the top
            snake_head = [x, y]                                                                                         # location of snake head
            snake_list.append(snake_head)                                                                               # adding a block on top if it eats food
            if len(snake_list) > length_of_snake:
                del snake_list[0]                                                                                       # removing butt of snake when head moves

            for site in snake_list[:-1]:                                                                                # quitting the game if head hits itself
                if site == snake_head:
                    game_close[0] = True

            snake(snake_block, snake_list)                                                                              # function for drawing the snake
            pygame.display.update()                                                                                     # updating the display for each movement
            pygame.time.Clock().tick(speed)                                                                             # setting the speed of the snake
            if (x == foodx or x == foodx + 10 or x == foodx + 20) and (
                    y == foody or y == foody + 10 or y == foody + 20):                                                  # condition to check if snake eats food
                length_of_snake += 3                                                                                    # add block if it eats food
                score += 3                                                                                              # increase score by 3
                foodx = random.randint(0, round(
                    (display_width - snake_block * 3) / 10)) * 10                                                       # make a food block appear randomly(x axis)
                foody = random.randint(3, round(
                    (display_height - snake_block * 3) / 10)) * 10                                                      # make a food block appear randomly(y axis)
                print("score = " + str(score))                                                                          # printing the score
                if score > highscore:                                                                                   # check if you break the highscore
                    highscore = score                                                                                   # change the value of highscore
                    file = open("scores.txt", "w+")                                                                     # open file of highscores
                    file.write("HIGHSCORE = " + str(highscore))                                                         # change the value of highscore in SCORES file

        pygame.quit()                                                                                                   # quit the pygame
        quit()                                                                                                          # quit whole game


    game()                                                                                                              # calling the game function


enter_game(snake_speed, snake_color, snake_displaysize, snake_wallpaper, snake_food, snake_song,name)                   # calling the entire snake game function
