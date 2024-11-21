## The OWL SPRITE (all images located in game/s/osbody/ and game/s/owlsofia/ and Lucky Sun Scribes logo (located in the game/logo folder) are licensed under a Creative Commons Attribution-NonCommercial license:
#https://creativecommons.org/licenses/by-nc/3.0/
## So you can use it for placeholders or testing, but not packaged in commercial games.

## The rest of the GUI art is licensed to the public domain.

## To the extent possible under law, ketskari ( http://sunlabyrinth.com ) has waived all copyright and related or neighboring rights to the Sunrise GUI Design & Art (all assets originally located in game/GUI/Parts, game/t/, and game/bg/ folders). This work is published from: United States. 

## CC0 1.0 Universal (CC0 1.0) Public Domain Dedication: http://creativecommons.org/publicdomain/zero/1.0/


##A persistent variable (for the Endings Gallery Extra):
if not persistent.Secret:
    $ persistent.Secret = False

define u = Character ('???', what_prefix="“", what_suffix="”", show_two_window=True, ctc="ctc", ctc_position="fixed", window_style = "adv", what_style="adv_text")

define s = Character ('Owl', what_prefix="“", what_suffix="”", show_two_window=True, ctc="ctc", ctc_position="fixed", window_style = "adv", what_style="adv_text")

define k = Character ('The Artist', what_prefix="“", what_suffix="”", show_two_window=True, ctc="ctc", ctc_position="fixed", window_style = "adv", what_style="adv_text")

## This is for choices. You need to use this speaker when making a choice menu
define mn = Character (None, color="#fdf4f5", what_prefix="(", what_suffix=")", what_font="GUI/Fonts/DejaVuSerif-BoldItalic.ttf")

###DEFAULT NARRATOR
define narrator = Character (None, color="#fdf4f5", what_prefix="(", what_suffix=")", show_two_window=True, ctc="ctc", ctc_position="fixed", window_style = "adv", what_style="adv2_text")

### NVL Defined
define n = Character(None, kind=nvl, ctc="nvl_ctc", ctc_position="fixed", style ="nvl_text")

##### OWL SOFIA ########
define os = Character ('Owl', image = "owl", window_style= "owlbox", what_style ="owlsofia", color="#fdf4f5", what_prefix="“", what_suffix="”", show_two_window=True, ctc="ctc", ctc_position="fixed")

## Owl Sofia's narrator:
define osN = Character ('Owl', image = "owl", window_style= "owlbox", what_style ="owlsofia", color="#fdf4f5", what_prefix="(", what_suffix=")", show_two_window=True, ctc="ctc", ctc_position="fixed")


## Owl Sofia's text styles:
style owlsofia is text:
    justify True

style owlbox:
    background im.AlphaMask("GUI/Parts/textbox/textbox-base.jpg", "GUI/Parts/textbox/textbox-mask.png")
    top_padding 100
    yminimum 273
    xfill True
    left_padding 290
    right_padding 200

## ADV Narrator text
style adv:
    background im.AlphaMask("GUI/Parts/textbox/textbox-base.jpg", "GUI/Parts/textbox/textbox-mask.png")
    top_padding 100
    yminimum 273
    xfill True
    left_padding 200
    right_padding 200

style adv_text is text:
    outlines [ (1, (248, 239, 238, 50), 0, 0) ]
    justify True
    text_align .5
    xalign .5
    xfill True

style adv2_text is text:
    justify True
    outlines [ (1, (248, 239, 238, 50), 0, 0) ]

### IMAGES

## im.MatrixColor and im.AlphaMask show up quite a bit. You can read more about these and other displayables in the documentation here:
## http://www.renpy.org/doc/html/displayables.html


## BASIC / CUSTOM BLACK AND WHITE BGS
image black = "bg/black.jpg" 
image white = "#f8efee"
image paper = "bg/paper.jpg"

## Optional border:
image border = im.AlphaMask (im.MatrixColor("bg/black.jpg", im.matrix.colorize("#7d5771", "#8786ae")), "t/border.png")

##INTRO
image intro = "bg/desert.jpg"
image plane01 = "bg/mdplane.png"
image plane02 = "bg/bgplane.png"
image plane03 = "bg/smplane.png"


## The seemingly endless variations on Shiye's work room, the purposes of which I cannot always remember, follow:

##SHIYE'S WORK ROOM:
image WRFG01 = im.AlphaMask ("bg/FG01.jpg", "bg/FG01-mask.png")
image WRFG02 = im.AlphaMask ("bg/FG02.jpg", "bg/FG02-mask.png")
image WRcage = im.AlphaMask ("bg/WRcage.jpg", "bg/WRcage-mask.png")
image WRdoor = im.AlphaMask ("bg/WRdoor.jpg", "bg/WRdoor-mask.png")
image plane = im.AlphaMask ("bg/plane.jpg", "bg/plane-mask.png")
image workroom = im.AlphaMask ("bg/shiyeroombase.jpg", "bg/shiyeroombase-mask.png")
image mtsWR = im.AlphaMask ("bg/Mts.jpg", "bg/Mts-mask.png")

## Shiye's work room with NO bird cage
image shiyeWR planeNBC = im.Composite(
    (1280, 720),
    (0, 0), im.AlphaMask ("bg/shiyeroombase.jpg", "bg/shiyeroombase-mask.png"),
    (0, 0), im.AlphaMask ("bg/WRdoor.jpg", "bg/WRdoor-mask.png"),
    (0, 0), im.AlphaMask ("bg/plane.jpg", "bg/plane-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG01.jpg", "bg/FG01-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG02.jpg", "bg/FG02-mask.png")
    )

##Shiye's work room WITH a bird cage
image shiyeWR planeBC = im.Composite(
    (1280, 720),
    (0, 0), im.AlphaMask ("bg/shiyeroombase.jpg", "bg/shiyeroombase-mask.png"),
    (0, 0), im.AlphaMask ("bg/WRdoor.jpg", "bg/WRdoor-mask.png"),
    (0, 0), im.AlphaMask ("bg/plane.jpg", "bg/plane-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG01.jpg", "bg/FG01-mask.png"),
    (24, 228), im.AlphaMask ("bg/WRcage.jpg", "bg/WRcage-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG02.jpg", "bg/FG02-mask.png")
    )

### Shiyes work room with a birdcage (foreground only)
image shiyeWRfg = LiveComposite(
    (1280, 720),
    (0, 411), im.AlphaMask ("bg/FG01.jpg", "bg/FG01-mask.png"),
    (0, 230), "bg/birdcageFG.png",
    (0, 411), im.AlphaMask ("bg/FG02.jpg", "bg/FG02-mask.png")
    )

image cagebg = "bg/birdcageBG.png"

image shiyeWRbg = LiveComposite(
    (1280, 720),
    (0, 0), im.AlphaMask ("bg/shiyeroombase.jpg", "bg/shiyeroombase-mask.png"),
    (0, 0), im.AlphaMask ("bg/WRdoor.jpg", "bg/WRdoor-mask.png"),
    (0, 0), im.AlphaMask ("bg/plane.jpg", "bg/plane-mask.png")
    )

##Shiye's workroom WITH a bird cage, but no plane
image shiyeWR noplaneBC = im.Composite(
    (1280, 720),
    (0, 0), im.AlphaMask ("bg/shiyeroombase.jpg", "bg/shiyeroombase-mask.png"),
    (0, 0), im.AlphaMask ("bg/WRdoor.jpg", "bg/WRdoor-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG01.jpg", "bg/FG01-mask.png"),
    (24, 228), im.AlphaMask ("bg/WRcage.jpg", "bg/WRcage-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG02.jpg", "bg/FG02-mask.png")
    )

##Shiye's workroom at NIGHT with a bird cage
image shiyeWR NplaneBC = im.Composite(
    (1280, 720),
    (0, 0), im.MatrixColor(im.AlphaMask ("bg/shiyeroombase.jpg", "bg/shiyeroombase-mask.png"), im.matrix.hue(250) * im.matrix.brightness(-.4) * im.matrix.saturation(.5) * im.matrix.contrast(.6)),
    (0, 0), im.MatrixColor(im.AlphaMask ("bg/WRdoor.jpg", "bg/WRdoor-mask.png"),  im.matrix.hue(250) * im.matrix.brightness(-.1) * im.matrix.saturation(.5)),
    (0, 0), im.MatrixColor(im.AlphaMask ("bg/plane.jpg", "bg/plane-mask.png"), im.matrix.hue(250) * im.matrix.brightness(-.2) * im.matrix.saturation(.2) * im.matrix.contrast(.8)),
    (0, 411), im.MatrixColor(im.AlphaMask ("bg/FG01.jpg", "bg/FG01-mask.png"), im.matrix.hue(250) * im.matrix.brightness(-.5) * im.matrix.saturation(.5) * im.matrix.contrast(.5)),
    (24, 228), im.MatrixColor(im.AlphaMask ("bg/WRcage.jpg", "bg/WRcage-mask.png"), im.matrix.hue(250) * im.matrix.brightness(-.5) * im.matrix.saturation(.5)),
    (0, 411), im.MatrixColor(im.AlphaMask ("bg/FG02.jpg", "bg/FG02-mask.png"), im.matrix.hue(250) * im.matrix.brightness(-.5) * im.matrix.saturation(.5) * im.matrix.contrast(.5)),
    (705, 0), im.MatrixColor("bg/shiyewall.jpg", im.matrix.hue(250) * im.matrix.brightness(-.8) * im.matrix.saturation(.2) * im.matrix.contrast(.5))
    )


##Shiye's work room sans plane and door but WITH a bird cage
image shiyeWR BC = im.Composite(
    (1280, 720),
    (0, 0), im.AlphaMask ("bg/shiyeroombase.jpg", "bg/shiyeroombase-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG01.jpg", "bg/FG01-mask.png"),
    (24, 228), im.AlphaMask ("bg/WRcage.jpg", "bg/WRcage-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG02.jpg", "bg/FG02-mask.png")
    )

## ???
image shiyeWR NBC = im.Composite(
    (1280, 720),
    (0, 0), im.AlphaMask ("bg/shiyeroombase.jpg", "bg/shiyeroombase-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG01.jpg", "bg/FG01-mask.png"),
    (0, 411), im.AlphaMask ("bg/FG02.jpg", "bg/FG02-mask.png")
    )

##Shiye's Plane
image shiplane = im.AlphaMask ("bg/shiyeplane.jpg", "bg/shiyeplane-mask.png")

image shiyeplane:
    "shiplane"
    xalign -0.3 yalign .3
    2.0
    rotate -15
    linear 5.0 align (.75, -.3) knot (0.1, .12)
    6.0
    rotate -5
    zoom .85
    xalign 0.0 yalign .05
    linear 15.0 align (20.0, 0.0) knot (.2, .05) knot (0.5, .0)
    
image shiyeplane02:
    "shiplane"
    xalign -0.3 yalign .3
    2.0
    rotate -15
    linear 5.0 align (.75, -.3) knot (0.1, .12)
    
image shiyewall:
    "bg/shiyewall.jpg"
    on show:
        xalign 1.2 yalign .5
        parallel:
            alpha 0.0
            linear .5 alpha 1.0
        parallel:
            easein .8 xalign 1.0 yalign .5
    on hide:
        xalign 1.0 yalign .5
        parallel:
            linear .9 alpha 0.0
        parallel:
            easeout .7 xalign 1.8 yalign .5

image wallstatic = "bg/shiyewall.jpg"
image bloodywall = "bg/bloodywall.jpg"

##Transforms
transform mist:
    on show:
        alpha 0.0
        linear .5 alpha 1.0
    on hide:
        linear .9 alpha 0.0
        
transform mist2:
    on show:
        alpha 0.0
        linear .5 alpha 1.0
    on hide:
        pause .3
        linear .3 alpha 0.0
    on replaced:
        alpha 1.0
        #pause .2
        linear .5 alpha 0.0
    on replace:
        pause .3
        linear .5 alpha 1.0


transform owlsofia_perch:
    xalign 0.05 yalign .62
    zoom .75
    xzoom 1
    on show:
        alpha 0.0
        linear .5 alpha 1.0
    on hide:
        pause .3
        linear .5 alpha 0.0
    on replaced:
        alpha 1.0
        #pause .2
        linear .5 alpha 0.0
    on replace:
        pause .3
        linear .5 alpha 1.0 

transform owlsofia_center:
    xalign 0.5 yalign .5
    zoom .75
    xzoom -1
    on show:
        alpha 0.0
        linear .5 alpha 1.0
    on hide:
        pause .3
        linear .5 alpha 0.0
    on replaced:
        alpha 1.0
        #pause .2
        linear .5 alpha 0.0
    on replace:
        pause .3
        linear .5 alpha 1.0 

transform owlsofia_anim:
    xalign 0.0 yalign 1.0
    zoom .55

        
##SPLASH SCREEN

image splashborder = im.AlphaMask (im.MatrixColor("bg/black.jpg", im.matrix.colorize("#5e2148", "#7b668e")), "t/border.png")
image splash = im.AlphaMask(im.Scale("GUI/Parts/textbox/nvl-base.jpg", 730, 730), im.Scale("GUI/Parts/textbox/nvl-mask.png", 730, 730))
image paper = "GUI/Parts/Paper.jpg"
image logo = im.AlphaMask("logo/base.png", "logo/mask.png")


        
label splashscreen:
    scene black
    $renpy.pause(1.5)
    scene paper
    show splashborder:
        alpha .6
    show splash at center:
        alpha .9
    show logo:
        alpha .65
        xalign .5 yalign .4
    with charcoal
    show text "{font=GUI/Fonts/Antonio-Bold.ttf}{size=+20}Your • Logo • Here{/size}{/font}":
        alpha 0.0
        xalign .5 yalign .65
        linear 3.0 alpha 1.0
    $renpy.pause(5.0)
    return
        
# The game starts here.

label start:
    show screen keymap_screen #keymapping for text history (t)

    queue music [ "st/WhenI.ogg", "st/WhenII.ogg" ]
    show intro:
        xalign .5 yalign 0.0
    show border onlayer foreground:
        alpha .6
    with charcoal
    show plane01:
        xalign 1.5 yalign .2
        linear 9.0 align (-3.0, .5) knot (.5, .3) knot (0.5, .2)
    show plane02:
        xalign 1.5 yalign .6
        linear 15.0 align (-3.0, .5) knot (.2, .7) knot (0.5, .2)
    show plane03:
        xalign 1.5 yalign .05
        linear 11.0 align (-3.0, .5) knot (.9, .1) knot (0.5, .2)
    $renpy.pause(6.0)

    show text "{font=GUI/Fonts/Antonio-Bold.ttf}{size=+50}The GUI{/size}{/font}":
        alpha 1.0
        xalign .5 yalign .45
        3.0
        linear 1.0 alpha 0.0
    $renpy.pause(1.0)
    show text "{i}{size=+5}“Here's some random text!”{/size}{/i}":
        alpha 1.0
        xalign .5 yalign .55
        4
        linear 3.0 alpha 0.0
    with charcoal

    show intro:
        subpixel True
        ease 15.0 xalign .5 yalign 1.0
    $ renpy.pause(17.0)


    n "{s}Once upon a time{/s} In 2015, during the {s}ides{/s} month of March, a writer, an artist and a programmer got together to work on a project for the NaNoRenO 2015 game jam."

    n "It was called {i}Sunrise{/i}, and much sleep was lost over it."

    n "But the GUI was kinda neat, and used a couple of features with the latest Ren'Py screen language."

    n "So the team decided to release it. {i}(Events exaggerated for narrative effect.){/i}"

    n "Right now we're demonstrating the NVL box, hence all this text."

    n "You can find the art for the NVL textbox and other GUI elements in the GUI/Parts/ folder."

    n "That's all for the NVL box."
    nvl clear

    play music "st/WhereI.ogg" fadein 1.0 fadeout 2.0
    show shiyeWR planeNBC at mist2
    with charcoal
    show shiyewall

    k "This layered background has several variations. You can see them defined in script.rpy."

    menu:
        mn "Oh, yeah, and here's what a choice menu looks like."

        "Choice #1":
            pass

        "Choice #2":
            pass

    os talk "Such creative choices."

    show owl 2talk at owlsofia_center

    os "Aghh!"

    show owl talk at owlsofia_perch

    os "I'll just perch here while we conduct a quick tour of the features of this GUI."

    show owl 2 at owlsofia_perch
    
    k "We have a couple different kinds of narrators aside from the choice menu narrator and the NVL box."

    show owl at owlsofia_perch

    osN "So I have parentheses around my thoughts ..."

    show owl talk at owlsofia_perch

    os "... and curly quotes for my speech."

    show shiyeWR planeBC at mist2

    os "And that magically appearing cage is part of another of the background variations."

    show owl 2talk at owlsofia_perch

    os "Also, if you click the history button, you'll see a history of all the text you've just read."

    show owl at owlsofia_perch

    k "That's the quick demonstration. Some more details are in the .rpy files."

    show owl talk at owlsofia_perch

    os "Finally, be sure to edit screens.rpy and customize things, such as putting your team's credits in places like the main menu!"

    show owl 2talk at owlsofia_perch
    os "We don't want to take credit for {i}everything{/i}."

    show owl at owlsofia_perch
    k "In all seriousness, it's public domain, so you don't have to even credit us! Please see script.rpy and license-README.txt for license details (the music and the owl sprite have different licenses)."

    $ persistent.Secret = True
    jump credits


label credits:
    scene paper
    show splash at center:
        alpha .9

    ## Credits text formatting
    show text "{font=GUI/Fonts/Antonio-Bold.ttf}{size=+20}Lucky • Sun • Scribes{/size}{/font}\n\nArt, Design, & Animation\n{i}by ketskari{/i}\n\nGUI Programming\n{i}by saguaro{/i}\n\n{i}Sunrise{/i} Writer\n {i}Hazel-Bun{/i}\n\nMusic (CC BY License):{i}\nSpin Day{/i}\n\nRen'Py Engine by Tom Rothamel":
        xalign .5 yalign .35
    with charcoal
    $renpy.pause()
    return

###########################

##A note here. There is a special Replay function that will allow you to turn off save mode when replaying an ending. Read more about that here:
##http://www.renpy.org/doc/html/rooms.html#replay

label secret:
    scene shiyeWR NplaneBC with charcoal
    k "This is a secret scene that you unlocked by finishing the demonstration."
    k "Since this demo doesn't have multiple endings, we just jumped to this secret scene instead."
    k "Making an ending gallery is a little easier if the endings are designed to be standalone labels."
    k "That's all."
    return
