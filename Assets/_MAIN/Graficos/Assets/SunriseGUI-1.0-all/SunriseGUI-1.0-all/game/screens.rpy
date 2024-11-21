# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

#CHARACTER FORMATS
#define e = Character('Eileen', show_two_window=True, ctc="ctc", ctc_position="fixed")

## WITH SIDE SPRITE, add left padding 270
# define s = Character ('Sofia', color="#fdf4f5", image="sofia", what_prefix="“", what_suffix="”", window_left_padding=270, show_two_window=True, ctc="ctc", ctc_position="fixed")
# image side sofia = "GUI/Parts/sidesprite.png"

screen say(who, what, side_image=None, two_window=False):
    # Decide if we want to use the one-window or two-window variant.
    if not two_window:
        # The one window variant.
        window:
            id "window"
            has vbox:
                style "say_vbox" xalign 0.5 ##to center menu dialogue
            if who:
                text who id "who"
            text what id "what"

    else:
        # The two window variant.
        vbox:
            style "say_two_window_vbox"
            window:
                id "window"
                has vbox:
                    style "say_vbox"
                text what id "what"  
                
        if who:  #Layer namebox over ADV window
            window:
                style "say_who_window"
                text who:
                    id "who" xalign 0.5 ##to center name
        
        use rollback    
        use quick_menu                     

    # If there's a side image, display it above the text.
    if side_image:
        add side_image at owlsofia_anim
    else:
        add SideImage() at owlsofia_anim # xalign 0.0 yalign 1.0  


## ADV CTC ##
image ctc:
    xpos 750 ypos 500  ##unfortunately fixed pos required
    "glowing_arrow"       
    
#ctc glowing transform for right-pointing arrow
image glowing_arrow:
    contains:
        "GUI/Parts/textbox/arrow_normal.png"
    contains:        
        "GUI/Parts/textbox/arrow_hover.png"  
        alpha 0.5
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0.5
        repeat            
            
## ROLLBACK ICON ##
screen rollback(xp=500, yp=500): #default pos for ADV screen
    imagebutton:
        idle (im.Flip("GUI/Parts/textbox/arrow_normal.png", horizontal=True))      
        hover (im.Flip("GUI/Parts/textbox/arrow_hover.png", horizontal=True))
        action Rollback()
        xpos xp ypos yp #unfortunately ctc has a fixed pos so this must be fixed as well  

## ADV STYLES ##
style window:
    background im.AlphaMask("GUI/Parts/textbox/textbox-base.jpg", "GUI/Parts/textbox/textbox-mask.png")         
    top_padding 100
    yminimum 273
    xfill True

style say_label:
    bold False
    size 25
    font "GUI/Fonts/DejaVuSerif-BoldItalic.ttf" 
    color "#f8efee"
    outlines [ (1, (248, 239, 238, 50), 0, 0) ]   

style say_who_window:
    is default
    ypos 505
    xalign 0.5
        
##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice
        
screen choice(items):
    window:
        style "menu_window"

        hbox:
            style "menu"
            spacing 30 #spacing between buttons

            for caption, action, chosen in items:
                if action:
                    button:
                        action action
                        style "menu_choice_button"
                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"

#expanding the choice button bg so the squiggle will center properly
image choice_button_bg = Fixed(Solid("#FFF0", width=250), Transform("GUI/Parts/ChoiceMenus/button_bg.png",xalign=(0.5)))  
                    
init -2:
    ## CHOICE MENU STYLES ##
    $ config.narrator_menu = True

    style menu_window is default:
        xalign 0.5
        yalign 0.85    
        
    style menu_choice is button_text:
        clear
        color "#f8efee"
        hover_color "e87d34"  
        font "GUI/Fonts/Antonio-Bold.ttf" 
        size 25       

    style menu_choice_button is button:
        xsize 250
        background "choice_button_bg"
        
##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if who is not None:
                    text who id who_id
                text what id what_id

        # Display a menu, if given.
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"

                    else:
                        text caption style "nvl_dialogue"
            
    #add SideImage() xalign 0.0 yalign 1.0
    use rollback(xp=125, yp=600)
    use quick_menu(xa=0.15, ya=0.95)  

#BG for NVL and Text History screens
image nvlbg = im.AlphaMask("GUI/Parts/textbox/nvl-base.jpg", "GUI/Parts/textbox/nvl-mask.png") 

image nvl_ctc:
    xpos 610 ypos 600
    "glowing_arrow"  

## NVL STYLES ##
style nvl_window:
    background "nvlbg"
    xmaximum 780
    xpadding 130
    ypadding 60
    
style nvl_text:
    color "#f8efeee6"
    
##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu

    window:
        background "GUI/Parts/main menu/mm_ground.jpg"

    ## EXTRAS ICON ##
    vbox:
        imagebutton:
                at icon_rotate
                idle "GUI/Parts/main menu/extra.png"
                hover "GUI/Parts/main menu/extra_hovered.png"
                insensitive "GUI/Parts/main menu/extra_grayed.png"
                action ShowMenu("extras")
                xpos 1000 ypos 25                 
    
    ## TEAM SUBMENU ##
    frame:
        style_group "submenu"        
        vbox:
            label "Presented by"
            textbutton "CHERUBIM SCRIBES" action OpenURL("http://www.cherubimscribes.com/")
            textbutton "LUCKY SPECIAL GAMES" action OpenURL("http://www.luckyspecialgames.com")
            textbutton "SUN LABYRINTH" action OpenURL("http://sunlabyrinth.com")

    ## MM NAV ##
    frame:
        style_group "mm" 
        has hbox xalign 0.5              
        textbutton _("Load") action ShowMenu("load")
        text u"\u272D" ypos 7
        textbutton _("Settings") action ShowMenu("preferences")
        text u"\u272D" ypos 7
        textbutton _("Start") action Start()            
        text u"\u272D" ypos 7
        textbutton _("Help") action Help()
        text u"\u272D" ypos 7
        textbutton _("Quit") action Quit() 
                
# ROTATE EXTRAS ICON
transform icon_rotate:
    rotate 10     

## MAIN MENU AND NAVBAR STYLES ##
style mm_frame:
    background im.AlphaMask("GUI/Parts/navi-base.jpg", "GUI/Parts/navi-mask.png")        
    yalign 0.8
    xfill True
    
style mm_hbox:
    spacing 20
    ypos 70      
    
style mm_text:        
    font "DejaVuSans.ttf"
    size 40
    color "#ead8d7B3"  #this is correct hex  

style mm_button:
    background None     
    
style mm_button_text:
    font "GUI/Fonts/Antonio-Bold.ttf"
    size 45      
    color "#ead8d7B3"  
    hover_color "#e97e35E6"  

## SUBMENU STYLES ##
style submenu_frame:
    xalign 0.03 yalign 0.6 background None
    
style submenu_label_text:
    font "GUI/Fonts/DejaVuSerif-Bold.ttf"
    color "#601d47BF" 
    italic True
    size 20
    
style submenu_text:
    font "DejaVuSans.ttf" 
    color "#601d47BF"       
    yalign 0.5
    
style submenu_button:
    background None  
    xpadding 0  
    ypadding 0

style submenu_button_text:
    font "GUI/Fonts/Antonio-Bold.ttf"
    size 35
    color "#601d47BF"
    hover_color "#e97e35E6"
    selected_color "#7e617d"  
    insensitive_color "#4448"        

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation

screen navigation(bg="GUI/Parts/save-load/sl_ground.jpg"):

    window:
        background bg  #workaround for concept art screen, which needs to be layered differently

    frame:
        style_group "mm" 
        has hbox xalign 0.5 spacing 10
        textbutton _("Return") action Return()
        text u"\u272D" ypos 6
        textbutton _("Save") action ShowMenu("save")
        text u"\u272D" ypos 6
        textbutton _("Load") action ShowMenu("load")
        text u"\u272D" ypos 6
        textbutton _("Main") action MainMenu()
        text u"\u272D" ypos 6
        textbutton _("Settings") action ShowMenu("preferences")
        text u"\u272D" ypos 6
        textbutton _("Help") action Help()
        text u"\u272D" ypos 6
        textbutton _("Quit") action Quit()

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():
    $ columns = 3
    $ rows = 2     

    ## FILE PICKER, FILE PICKER NAV INHERITS FROM SUBMENU STYLE
    frame:
        style "file_picker_frame"
        hbox:
            style_group "file_picker_nav"
            textbutton _("< Previous"):
                action FilePagePrevious()

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next >"):
                action FilePageNext()

    ## SAVE LOAD SUBMENU ##
    frame:
        style_group "submenu"
        vbox:
            hbox:   
                spacing 10
                label "Save":
                    if renpy.get_screen("save"):
                        text_color "#e87d34"
                text "/"
                label "Load":
                    if renpy.get_screen("load"):
                        text_color "#e87d34"
            
            textbutton _("Autosaves"):
                action FilePage("auto")

            textbutton _("Quick-saves"):
                action FilePage("quick")    
                
            textbutton _("Normal"):
                action FilePage(1)

    ## GRID FOR GAME SAVES
    grid columns rows:
        style_group "saveload"   

        # Display ten file slots, numbered 1 - 10.
        for i in range(1, columns * rows + 1):

            # Each file slot is a button.
            button:                       
                action FileAction(i)
                xfill True
                has fixed      

                $ file_name = FileSlotName(i, columns * rows)
                $ file_time = FileTime(i, empty=_("Empty Slot"))
                $ save_name = FileSaveName(i)  
                text "[file_name]. [file_time!t]\n[save_name!t]" style "filename_text"

                # Add the screenshot.
                add FileScreenshot(i) at thumb_offset #adjusting slightly smaller screenshot behind slot frame, looks nicer this way
                key "save_delete" action FileDelete(i)

screen save():
    # This ensures that any other menu screen is replaced.
    tag menu
    use navigation
    use file_picker

screen load():
    # This ensures that any other menu screen is replaced.
    tag menu
    use navigation
    use file_picker

image grid_selected:
    "GUI/Parts/save-load/slot_selected.png"
    alpha 0.5

## FILE PICKER STYLES
style file_picker_button is large_button
style file_picker_text is large_button_text

style file_picker_frame:
    background None        
    xalign 0.9
    yalign 0.05
    
## FILE PICKER NAV STYLES    
style file_picker_nav_button is submenu_button        
style file_picker_nav_button_text is submenu_button_text   
style file_picker_nav_text is submenu_button_text
style file_picker_nav_hbox:
    spacing 15

##SAVE LOAD GRID STYLING, for image layer box over slightly smaller screenshot
style saveload_button is default:
    background None
    foreground "GUI/Parts/save-load/slot.png"
    hover_foreground "GUI/Parts/save-load/slot_hovered.png"
    selected_foreground "grid_selected"
    selected_hover_foreground "GUI/Parts/save-load/slot_selected.png"
    maximum (236,135)
    minimum (236,135)
    
style saveload_grid:
    xpos 315
    ypos 150
    spacing 50

style filename_text:
    font "GUI/Fonts/DejaVuSerif-Bold.ttf"
    size 18
    italic True
    color "#f8efee80"
    yoffset -25
    xoffset -10
        
init python:
    config.thumbnail_width =  230
    config.thumbnail_height = 130             
        
##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():
    tag menu
    use navigation
    add "GUI/Parts/Settings/settings.png" xpos 150 ypos 50
            
    frame:
        style_group "prefs"
        hbox:
            vbox:            
                vbox:                
                    style_group "pref"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    null height 10
                    style_group "pref"
                    label _("Transitions")
                    textbutton _("All") action Preference("transitions", "all")
                    textbutton _("None") action Preference("transitions", "none")

            vbox:
                vbox:                
                    style_group "pref"
                    label _("Skip")
                    textbutton _("Seen Messages") action Preference("skip", "seen")
                    textbutton _("All Messages") action Preference("skip", "all")

                vbox:
                    null height 10
                    style_group "pref"
                    label _("After Choices")
                    textbutton _("Stop Skipping") action Preference("after choices", "stop")
                    textbutton _("Keep Skipping") action Preference("after choices", "skip")
            vbox:
                style_group "prefbars"
                vbox:                
                    style_group "pref"
                    textbutton _("Start Skipping") action Skip()
                    
                hbox:
                    vbox: 
                        label _("Text Speed")
                        bar value Preference("text speed") 
                    vbox: 
                        label _("Soundtrack")
                        bar value Preference("music volume")
                hbox:
                    vbox:
                        label _("Auto-Forward")
                        bar value Preference("auto-forward time")
                    vbox:
                        label _("Sound Effects")
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test"):
                                action Play("sound", config.sample_sound)
                                style "soundtest_button"

## MAIN SETTINGS FRAME STYLE ##
style prefs_frame: 
    is default
    xpos 325
    ypos 180      
    
style prefs_hbox:
    spacing 40
    
style prefs_vbox:
    spacing -25

## SETTINGS SUBSECTIONS STYLE ##
style pref_label:
    yoffset 10


style pref_label_text:
    font "GUI/Fonts/DejaVuSerif-Bold.ttf"
    size 20
    italic True
    color "#f8efee"  
    
style pref_button_text:
    font "GUI/Fonts/Antonio-Bold.ttf"
    size 40
    color "#f8efee"
    hover_color "#e87d34"
    selected_color "#f8efee66"
    insensitive_color "#f8efee66"

style pref_button is submenu_button

##SETTING SLIDER STYLES##
style prefbars_vbox:        
    spacing 20   
    
style prefbars_hbox:
    spacing 25

style prefbars_label_text is pref_label_text

style prefbars_slider:
    xmaximum 175
    ymaximum 26
    xalign 1.0   
    right_bar (im.MatrixColor("GUI/Parts/Settings/empty_bar.png", im.matrix.opacity(0.5)))
    left_bar (im.MatrixColor("GUI/Parts/Settings/full_bar.png", im.matrix.opacity(0.5)))
    hover_right_bar "GUI/Parts/Settings/empty_bar.png"
    hover_left_bar "GUI/Parts/Settings/full_bar.png"
    hover_thumb "GUI/Parts/Settings/selected.png" 
    thumb "GUI/Parts/Settings/idle.png"  
    thumb_shadow None
    thumb_offset 18
        
##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):
    modal True
    zorder 999 #fix - resolves ctc/window close issue
    frame:
        style_group "yesno" 
        
        add "yesnobox"
        
        vbox:
            xalign 0.5
            yalign 0.3
            spacing 30            
            add "GUI/Parts/YesNo/deco.png" xalign 0.5 ##top bracket

            label _(message):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
                
            add "GUI/Parts/YesNo/deco.png" xalign 0.5 yzoom -1.0 ##bottom bracket

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init python: ##fix - for window close / no bg issue
    config.quit_action = Quit()
    
# yesno box bg is nvl box scaled horizontally
image yesnobox:
    im.AlphaMask(im.Crop("GUI/Parts/textbox/nvl-base.jpg",(0,0,624,864)), im.FactorScale("GUI/Parts/textbox/nvl-mask.png", 0.8, 1.0))
    xalign 0.5 yalign 0.5
    
init -2:
    $ layout.MAIN_MENU = "Are you sure you want to return to the main menu? This will lose unsaved progress." ##fix - remove newline from message

    ## YES NO STYLES ##    
    style yesno_button is submenu_button:
        size_group "yesno"
        
    style yesno_button_text is submenu_button_text:
        color "#f8efeee6"  
        hover_color "#e87d34e6"

    style yesno_label:
        xmaximum 300
        
    style yesno_label_text:
        text_align 0.5
        layout "subtitle"        
        bold False
        font "GUI/Fonts/DejaVuSerif-BoldItalic.ttf" 
        color "#f8efee"           
        
    style yesno_frame:
        background im.AlphaMask("GUI/Parts/YesNo/yesnoscreen-base.png", "GUI/Parts/YesNo/yesnoscreen-mask.png") #full screen texture
        xfill True

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu(xa=0.95, ya=0.935): #default pos for adv
    hbox:
        style_group "quick"
        spacing 3
        xalign xa
        yalign ya

        textbutton "History" action ShowMenu("text_history")
        textbutton _("Q. Save") action QuickSave()
        textbutton _("Q. Load") action QuickLoad()
        hbox:
            textbutton _("Save") action ShowMenu('save')
            text "/"
            textbutton _("Load") action ShowMenu('load')
        textbutton _("Settings") action ShowMenu('preferences')
        textbutton _("Fast Skip") action Skip(fast=True, confirm=True)       
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")

## QUICK MENU STYLES ##
style quick_button:
    is default
    background None
    xpadding 5

style quick_button_text:
    is default
    size 18
    kerning .5
    font "GUI/Fonts/Antonio-Bold.ttf"
    idle_color "#f8efee90"
    hover_color "#e87d3490"
    selected_idle_color "#cc08"
    selected_hover_color "#cc0"
    insensitive_color "#4448"
    
style quick_text is quick_button_text:
    color "#f8efee"

## READBACK SCREEN - pulled from readback.rpy## 
screen text_history:
    tag menu   
    modal True
    zorder 9999999
    
    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []
        
    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]
        
    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):  
        $ lines_to_show = readback_buffer + [current_line]
        
    else:
        $ lines_to_show = readback_buffer
    
    $ adj = NewAdj(changed = store_yvalue, step = 300)
    
    frame:
        style_group "readback" 
        background "nvlbg"
        xmaximum 781        
    
        side "c r":  
            frame:                 
                ypadding 50            
                
                has viewport:
                    mousewheel True
                    draggable True
                    yinitial yvalue
                    yadjustment adj
                    
                    vbox:
                        null height 10
                        
                        for line in lines_to_show:
                            hbox:
                                if line[0] and line[0] != " ":
                                    label line[0] + "  "# name

                                # if there's no voice just log a dialogue
                                if not line[2]:
                                    text line[1]
                                    
                                # else, dialogue will be saved as a button of which plays voice when clicked
                                else: 
                                    textbutton line[1] action Play("voice", line[2] )
                            null height 20
            bar adjustment adj style 'readback_vscrollbar' 
        textbutton _("Return") action Return() align (0.5, 0.95)
        key "t" action Return()
        
screen keymap_screen():
    key "t" action ShowMenu('text_history')   
    
## READBACK STYLES ##
style readback_frame:
    xalign 0.5
    yalign 0.5
    background None
    
style readback_text:
    size 18    
    
style readback_label_text:
    font "GUI/Fonts/DejaVuSerif-BoldItalic.ttf"
    size 18
        
style readback_side:
    xalign 0.5
    yalign 0.5
    xmaximum 500
    ymaximum 600
   
style readback_vscrollbar:
    hover_thumb "GUI/Parts/Settings/selected.png" 
    thumb im.MatrixColor("GUI/Parts/Settings/selected.png", im.matrix.opacity(0.5))  
    thumb_shadow None
    thumb_offset 18
    ymaximum 553
    xmaximum 36
    right_bar Fixed(Solid("#FFF0", width=36),Transform("GUI/Parts/TextHistory/texthistory_bar.png", xalign=(0.5)))
    left_bar Fixed(Solid("#FFF0", width=36),Transform("GUI/Parts/TextHistory/texthistory_bar.png", xalign=(0.5)))
    yalign 0.5
    
style readback_button_text is mm_button_text
style readback_button is submenu_button  
        
############################ CUSTOM SCREENS #########################

## EXTRAS SCREENS LEFT SIDE SUBMENU ##
screen extras_menu():
    frame:
        style_group "submenu"
        vbox:
            label "Extras"            
            textbutton _("Concept Art"):
                action ShowMenu("conceptart")
            #textbutton _("Art Gallery"):
                #action ShowMenu("artgallery")   
            textbutton _("Endings"):
                action ShowMenu("endings")                   
            textbutton _("Credits"):
                action ShowMenu("extras") 

## EXTRAS SCREENS RIGHT CORNER SUBMENU ##
screen credits_menu():                
    frame:
        style_group "extras"
        xalign 0.9 yalign 0.05
        hbox:
            textbutton "Team" action ShowMenu("extras")
            text u"\u272D" font "DejaVuSans.ttf" color "#601d47BF"
            textbutton "Sound Credits" action ShowMenu("soundcredits") 
        
## MAIN EXTRAS/CREDITS SCREEN ##
screen extras():
    tag menu
    use navigation
    use extras_menu
    use credits_menu
    frame:
        style_group "extras"       
        vbox:
            label "Credits"
            text "Sunrise GUI ................................... ketskari and saguaro"
            null height 20
            label "In Association With...."
            hbox:
                textbutton "Contributor 1" action OpenURL("http://www.renpy.org")
                text u"\u272D" font "DejaVuSans.ttf" 
                textbutton "Contributor 2" action OpenURL("http://www.renpy.org")
                text u"\u272D" font "DejaVuSans.ttf" 
                textbutton "Contributor 3" action OpenURL("http://renpy.org")

screen endings():
    $persistent.endings = False
    tag menu
    use navigation
    use extras_menu
    #use credits_menu
    frame:
        style_group "extras"       
        vbox:
            label "Endings"
            ## The ending gallery here is really basic. Basically you just Start the game from an ending's label:

            if persistent.Secret:
                hbox:
                    text "Secret ......................................................................"
                    textbutton "Play" action Start("secret")

            else:
                text "Locked ....................................................................... Play"


                
## SOUND CREDITS SCREEN ##                
screen soundcredits():
    tag menu
    use navigation
    use extras_menu
    use credits_menu
    frame:
        style_group "extras"
        vbox:
            label "Credits"
            text "Spin Day............................................................ CC BY 4.0"   
            
## CONCEPT ART GALLERY ##       
screen conceptart():
    tag menu     
    default page = 1
    add "GUI/Parts/save-load/sl_ground.jpg"
    use extras_menu     
    
    ## ART DISPLAY, LAYERED UNDER NAV BAR
    frame:
        style_group "extras"        
        xpos 290 ypos 76
        showif page == 1: 
            add "GUI/Parts/Extras/concept art/01.png" at quick_dissolve
        elif page == 2:
            add "GUI/Parts/Extras/concept art/01.png" at quick_dissolve
        else:           
            add "GUI/Parts/Extras/concept art/01.png" at quick_dissolve
    use navigation(bg=None) 
    use navigation(bg=None) 
    use page_picker(3, page)    

transform quick_dissolve:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0
    on hide:
        alpha 1.0
        linear 1.0 alpha 0.0
    
##### GALLERY DATA ######
init python:
    g = Gallery()    
    # each button requires at least one scene unlocked to 'open' and will show each of the 3 after it is unlocked    
    
    g.button("Intro")
    g.condition("persistent.introextra01 or persistent.introextra02 or persistent.introextra03")
    g.image("introextra01")
    g.condition("persistent.introextra01")    
    g.image("introextra02")
    g.condition("persistent.introextra02")
    g.image("introextra03")
    g.condition("persistent.introextra03") 
    
    g.button("Hall")
    g.condition("persistent.hallextra01 or persistent.hallextra02 or persistent.hallextra03")
    g.image("hallextra01")
    g.condition("persistent.hallextra01")    
    g.image("hallextra02")
    g.condition("persistent.hallextra02")
    g.image("hallextra03")
    g.condition("persistent.hallextra03")
    
    g.button("Dreams")
    g.condition("persistent.dreamsextra01 or persistent.dreamsextra02 or persistent.dreamsextra03")
    g.image("dreamsextra01")
    g.condition("persistent.dreamsextra01")    
    g.image("dreamsextra02")
    g.condition("persistent.dreamsextra02")
    g.image("dreamsextra03")
    g.condition("persistent.dreamsextra03") 

    g.button("Work Room")
    g.condition("persistent.workroomextra01 or persistent.workroomextra02 or persistent.workroomextra03")
    g.image("workroomextra01")
    g.condition("persistent.workroomextra01")    
    g.image("workroomextra02")
    g.condition("persistent.workroomextra02")
    g.image("workroomextra03")
    g.condition("persistent.workroomextra03")

    g.button("Courtyard")
    g.condition("persistent.courtyardextra01 or persistent.courtyardextra02 or persistent.courtyardextra03")
    g.image("courtyardextra01")
    g.condition("persistent.courtyardextra01")    
    g.image("courtyardextra02")
    g.condition("persistent.courtyardextra02")
    g.image("courtyardextra03")
    g.condition("persistent.courtyardextra03")  
    
    g.button("Quarters")
    g.condition("persistent.quartersextra01 or persistent.quartersextra02 or persistent.quartersextra03")
    g.image("quartersextra01")
    g.condition("persistent.quartersextra01")    
    g.image("quartersextra02")
    g.condition("persistent.quartersextra02")
    g.image("quartersextra03")
    g.condition("persistent.quartersextra03")

    g.button("Desert")
    g.condition("persistent.desertextra01 or persistent.desertextra02 or persistent.desertextra03")
    g.image("desertextra01")
    g.condition("persistent.desertextra01")    
    g.image("desertextra02")
    g.condition("persistent.desertextra02")
    g.image("desertextra03")
    g.condition("persistent.desertextra03")   

    g.button("Ending I: Heart")
    g.condition("persistent.ending01extra01 or persistent.ending01extra02 or persistent.ending01extra03")
    g.image("ending01extra01")
    g.condition("persistent.ending01extra01")    
    g.image("ending01extra02")
    g.condition("persistent.ending01extra02")
    g.image("ending01extra03")
    g.condition("persistent.ending01extra03")    

    g.button("Ending II: Sunrise")
    g.condition("persistent.ending02extra01 or persistent.ending02extra02 or persistent.ending02extra03")
    g.image("ending02extra01")
    g.condition("persistent.ending02extra01")    
    g.image("ending02extra02")
    g.condition("persistent.ending02extra02")
    g.image("ending02extra03")
    g.condition("persistent.ending02extra03")    
    
    g.button("Ending III: Witch-Brother")
    g.condition("persistent.ending03extra01 or persistent.ending03extra02 or persistent.ending03extra03")
    g.image("ending03extra01")
    g.condition("persistent.ending03extra01")    
    g.image("ending03extra02")
    g.condition("persistent.ending03extra02")
    g.image("ending03extra03")
    g.condition("persistent.ending03extra03") 
    
    g.locked_button = im.MatrixColor("GUI/Parts/Extras/locked.png", im.matrix.opacity(0.45))
    g.hover_border = "GUI/Parts/save-load/slot_hovered.png"
    g.idle_border = "GUI/Parts/save-load/slot.png"
    
## MAIN GALLERY SCREEN ## 
screen artgallery():
    tag menu
    use navigation
    use extras_menu  
    default page = 1     
        
    grid 3 2:
        style_group "extras"
        $ button_x = 230
        $ button_y = 130  
        if page == 1:        
            add g.make_button("Intro", At("introextra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)      
            add g.make_button("Hall", At("hallextra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)
            add g.make_button("Dreams", At("dreamsextra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)
            add g.make_button("Work Room", At("workroomextra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)
            add g.make_button("Courtyard", At("courtyardextra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)           
            add g.make_button("Quarters", At("quartersextra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)    
            at quick_dissolve
        else:        
            add g.make_button("Desert", At("desertextra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)
            add g.make_button("Ending I: Heart", At("ending01extra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)
            add g.make_button("Ending II: Sunrise", At("ending02extra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)
            add g.make_button("Ending III: Witch-Brother", At("ending03extra01", thumb_size, thumb_crop, thumb_offset), xpadding=0, ypadding=0, background=None)
            add Null()   
            add Null()                
    use page_picker(2, page)
    
## top right corner page picker, args are total pages (range) and page screen variable
screen page_picker(r, page):
    frame:   
        style_group "extras"
        xalign 0.9 yalign 0.05
        hbox:    
            textbutton "< Previous" action [SetScreenVariable("page", page-1), SensitiveIf(page>1)]
            for i in range (1,r+1):
                textbutton str(i) action [SetScreenVariable("page", i), SelectedIf(i==page)]
            textbutton "Next >" action [SetScreenVariable("page", page+1), SensitiveIf(page<r)]
        
## animated thumbnail transforms, these must be applied in this order to get the image to scale and crop correctly
transform thumb_size:
    zoom 0.25
    
transform thumb_crop:
    crop (0,0,230,130)
    
transform thumb_offset:
    xoffset 3
    yoffset 3        
        
### EXTRAS STYLING  ##  
style extras_grid is saveload_grid:
    ypos 135
          
style extras_label_text:
    font "GUI/Fonts/DejaVuSerif-BoldItalic.ttf"
    color "#ead8d7"
    
style extras_text:
    font "GUI/Fonts/Antonio-Bold.ttf"
    size 35
    color "#ead8d7"
    
style extras_frame:
    background None
    xpos 325
    ypos 150
    
style extras_vbox:
    spacing 10
    
style extras_hbox:
    spacing 10
    
style extras_button is submenu_button    
style extras_button_text is submenu_button_text:
    size 35   
    
init python:
    config.window_icon = "icon.png"
    
##TODO
# shadows etc to main fonts
## sfx
# all styles are set up under the respective screen -- i.e. textbox styles under say screen.
