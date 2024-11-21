# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

## im.Composite looks a little nicer with ATL.

## View the sprite images in game/s/obody and game/s/owl to see the images used in the im.Composite layers.

###################### OWL SOFIA

image OSbase = "GUI/Parts/sidesprite.png" ## OWL SOFIA'S PORTRAIT BASE

### 


################ OWL 

image owl = im.Composite(
    (451, 250),
    (0, 0), im.AlphaMask(im.Crop("s/calista/texture.png", (0, 0, 451, 250)), "s/obody/sil01.png"),
    (0, 0), im.AlphaMask("s/obody/01.jpg", "s/obody/01-mask.png"),
    (0,0), "s/obody/eyes.png"
    )

image owl talk  = im.Composite(
    (451, 250),
    (0, 0), im.AlphaMask(im.Crop("s/calista/texture.png", (0, 0, 451, 250)), "s/obody/sil01.png"),
    (0, 0), im.AlphaMask("s/obody/01.jpg", "s/obody/01-mask.png"),
    (0,0), "s/obody/eyes.png",
    (0,0), "s/obody/Mopen.png"
    )

image owl 2 = im.Composite(
    (451, 250),
    (0, 0), im.AlphaMask(im.Crop("s/calista/texture.png", (0, 0, 451, 250)), "s/obody/sil01.png"),
    (0, 0), im.AlphaMask("s/obody/01.jpg", "s/obody/01-mask.png"),
    (0,0), "s/obody/eyes.png"
    )

image owl 2talk  = im.Composite(
    (451, 250),
    (0, 0), im.AlphaMask(im.Crop("s/calista/texture.png", (0, 0, 451, 250)), "s/obody/sil02.png"),
    (0, 0), im.AlphaMask("s/obody/02.jpg", "s/obody/02-mask.png"),
    (0,0), "s/obody/eyes.png",
    (0,0), "s/obody/Mopen.png"
    )


image side owl = im.Composite(
    (526, 448),
    (373, 0), "s/owl/shadow.png",
    (0, 0), im.AlphaMask("s/owl/01.jpg", "s/owl/01-mask.png"),
    (0,0), "s/owl/eyes.png"
    )

image side owl talk = im.Composite(
    (526, 448),
    (373, 0), "s/owl/shadow.png",
    (0, 0), im.AlphaMask("s/owl/01.jpg", "s/owl/01-mask.png"),
    (0,0), "s/owl/eyes.png",
    (0,0), "s/owl/Mopen.png"
    )

image side 2owl = im.Composite(
    (526, 448),
    (373, 0), "s/owl/shadow.png",
    (0, 0), im.AlphaMask("s/owl/01.jpg", "s/owl/01-mask.png"),
    (0,0), "s/owl/eyes.png"
    )

image side owl 2talk = im.Composite(
    (526, 448),
    (373, 0), "s/owl/shadow.png",
    (0, 0), im.AlphaMask("s/owl/01.jpg", "s/owl/01-mask.png"),
    (0,0), "s/owl/eyes.png",
    (0,0), "s/owl/Mopen.png"
    )

