# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

##This was for the extras gallery that we didn't finish in time for Sunrise.

transform intro_anim:
    xalign .5 yalign 0.0
    12.0
    ease 15.0 xalign .5 yalign 1.0

transform plane01_anim:
    xalign 1.5 yalign .2
    linear 9.0 align (-3.0, .5) knot (.5, .3) knot (0.5, .2)

transform plane02_anim:
    xalign 1.5 yalign .6
    linear 15.0 align (-3.0, .5) knot (.2, .7) knot (0.5, .2)

transform plane03_anim:
    xalign 1.5 yalign .05
    linear 11.0 align (-3.0, .5) knot (.9, .1) knot (0.5, .2)

image introextra01:
    contains:
        "intro"
        intro_anim
    contains:
        "plane01"
        plane01_anim
    contains:
        "plane02"
        plane02_anim
    contains:
        "plane03"
        plane03_anim

transform cloud01_anim:
    xalign -1.5 yalign .6
    easeout 75.0 align (3.0, .6) knot (.5, .3) knot (0.5, .2)
    15.0
    repeat

transform cloud02_anim:
    xalign -1.5 yalign .2
    10.0
    ease 85.0 align (3.0, .2) knot (.2, .3) knot (0.5, .1)
    15.0
    repeat

transform cloud03_anim:
    xalign 32. yalign .05
    easein 60.0 align (-39.0, .5) knot (.9, .1) knot (0.5, .45)
    40.0
    repeat

transform wall:
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

image workroomextra01:
    contains:
        "daysky"
    contains:
        "shiyeWR planeNBC"
        mist2
    contains:
        "shiyewall"
        wall
    contains:
        "shiye_base P3"
        shiyeB_scn4
    contains:
        "shiye 03neutral"
        shiye_scn4
    contains:
        "cageBG"
        yalign 1.0
    contains:
        "owlsofia neuTupMopeEnoL"
        owlsofia_scn4
    contains:
        "cageFG"
        yalign 1.0
        
transform shiyeplane_anim:
    xalign -0.3 yalign .3
    2.0
    rotate -15
    linear 5.0 align (.75, -.3) knot (0.1, .12)
    6.0
    rotate -5
    zoom .85
    xalign 0.0 yalign .05
    linear 15.0 align (20.0, 0.0) knot (.2, .05) knot (0.5, .0)

image workroomextra02:
    contains:
        "shiplane"
        shiyeplane_anim
    contains:
        "daysky"
    contains:
        "mtsWR"
        mist2
    contains:
        "shiyeWR BC"
        mist2
        
image workroomextra03:
    contains:
        "evesky"
    contains:
        "mtsWR"
    contains:
        "shiyeWR NBC"
    contains:
        "bloodywall"
        right
    contains:
        "shiye_base P"
        shiyeB_scn10
    contains:
        "shiye C01EcloMneu"
        shiye_scn10


