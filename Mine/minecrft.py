from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()
Boxes = []

for z in range(30):
    for x in range(30):
        if z == 0 or z == 29:
            box = Button(color=color.white, model='cube', position=(x,0,z),
            texture='brick.png', parent=scene, origin_y=0)
            Boxes.append(box)
        elif x == 0 or x == 29:
            box = Button(color=color.white, model='cube', position=(x,0,z),
            texture='brick', parent=scene, origin_y=0)
            Boxes.append(box)
        else:
            box = Button(color=color.white, model='cube', position=(x,0,z),
            texture='grass.png', parent=scene, origin_y=0)
            Boxes.append(box)
        
bloque = 0

def input(key):
    global bloque
    for box in Boxes:
        if box.hovered:
            if key == "left mouse down":
                if bloque == 0:
                    new = Button(color=color.white,model='cube',position=box.position + mouse.normal,texture='grass', parent=scene, origin_y=0)
                elif bloque == 1:
                    new = Button(color=color.white,model='cube',position=box.position + mouse.normal,texture='Assets/Piedra.png', parent=scene, origin_y=0)
                elif bloque == 2:
                    new = Button(color=color.white,model='cube',position=box.position + mouse.normal,texture='block', parent=scene, origin_y=0)
                elif bloque == 3:
                    new = Button(color=color.white,model='cube',position=box.position + mouse.normal,texture='Assets/MAderaCheta.png', parent=scene, origin_y=0)
                elif bloque == 4:
                    new = Button(color=color.white,model='cube',position=box.position + mouse.normal,texture='Assets/Imagen.png', parent=scene, origin_y=0) 
                elif bloque == 5:
                    new = Button(color=color.white,model='cube',position=box.position + mouse.normal,texture='brick', parent=scene, origin_y=0)     
                Boxes.append(new)
            elif key == "right mouse down":
                Boxes.remove(box)
                destroy(box)
            if  key in ("1","2","3","4","5","6"):
                bloque = int(key)-1

app.run()

