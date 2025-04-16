from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()
Boxes = []
Bloques_Gui = []

GUI_BORDER = Entity(model="quad",scale_y=0.11,scale_x=1.1,position=(0,-0.45,0),parent=camera.ui,color=color.hex('#494949'))
GUI = Entity(model="quad",scale_y=0.9,scale_x=0.98,parent=GUI_BORDER,color=color.hex('#a0a0a0'))
GUI_controles = Entity(model="quad",scale_x=0.2,scale_y=0.3,parent=GUI_BORDER,position=(-0.38,0.64,0),color=color.hex('#494949'))
text_controles = Text(text="E: Ayuda",position=(-0.5,-0.37,0))

Bloque_Gui2_1 = Entity(model="quad",scale_x=0.1,scale_y=0.8,position=(-0.42,0,0),color=color.hex('#494949'),parent=GUI)
Bloque_Gui2_2 = Entity(model="quad",scale_x=0.1,scale_y=0.8,position=(-0.3,0,0),color=color.hex('#737373'),parent=GUI)
Bloque_Gui2_3 = Entity(model="quad",scale_x=0.1,scale_y=0.8,position=(-0.18,0,0),color=color.hex('#737373'),parent=GUI)
Bloque_Gui2_4 = Entity(model="quad",scale_x=0.1,scale_y=0.8,position=(-0.06,0,0),color=color.hex('#737373'),parent=GUI)
Bloque_Gui2_5 = Entity(model="quad",scale_x=0.1,scale_y=0.8,position=(0.06,0,0),color=color.hex('#737373'),parent=GUI)
Bloque_Gui2_6 = Entity(model="quad",scale_x=0.1,scale_y=0.8,position=(0.18,0,0),color=color.hex('#737373'),parent=GUI)

Bloque_Gui_1 = Entity(model="quad",scale_x=0.85,scale_y=0.85,texture='grass',color=color.white,parent=Bloque_Gui2_1)
Bloque_Gui_2 = Entity(model="quad",scale_x=0.85,scale_y=0.85,texture='Assets/Piedra.png',color=color.white,parent=Bloque_Gui2_2)
Bloque_Gui_3 = Entity(model="quad",scale_x=0.85,scale_y=0.85,texture='block',color=color.white,parent=Bloque_Gui2_3)
Bloque_Gui_4 = Entity(model="quad",scale_x=0.85,scale_y=0.85,texture='Assets/MAderaCheta.png',color=color.white,parent=Bloque_Gui2_4)
Bloque_Gui_5 = Entity(model="quad",scale_x=0.85,scale_y=0.85,texture='Assets/Imagen.png',color=color.white,parent=Bloque_Gui2_5)
Bloque_Gui_6 = Entity(model="quad",scale_x=0.85,scale_y=0.85,texture='brick',color=color.white,parent=Bloque_Gui2_6)

Bloques_Gui.append(Bloque_Gui2_1)
Bloques_Gui.append(Bloque_Gui2_2)
Bloques_Gui.append(Bloque_Gui2_3)
Bloques_Gui.append(Bloque_Gui2_4)
Bloques_Gui.append(Bloque_Gui2_5)
Bloques_Gui.append(Bloque_Gui2_6)


# Crear mapa

for z in range(30):
    for x in range(30):
        if z in (0,29):
            box = Button(color=color.white, model='cube', position=(x,0,z),
            texture='brick.png', parent=scene, origin_y=0)
            Boxes.append(box)
        elif x in (0,29):
            box = Button(color=color.white, model='cube', position=(x,0,z),
            texture='brick', parent=scene, origin_y=0)
            Boxes.append(box)
        else:
            box = Button(color=color.white, model='cube', position=(x,0,z),
            texture='grass.png', parent=scene, origin_y=0)
            Boxes.append(box)

# Crear Casa en el mapa         
for x in range(5):
    for z in range(5):
        for y in range(5):
            if x in (0,4) and z in (0,4):
                box = Button(color=color.white,model='cube',position=(x+10,y+1,z+10),texture='Assets/Piedra.png', parent=scene, origin_y=0)
                Boxes.append(box)
            elif x in (0,4) and z in (1,3) or x in (1,3) and z in (0,4):
                if y in (0,1,2,3):
                    box = Button(color=color.white,model='cube',position=(x+10,y+1,z+10),texture='Assets/MAderaCheta.png', parent=scene, origin_y=0)
                    Boxes.append(box)
                elif y == 4:
                    box = Button(color=color.white,model='cube',position=(x+10,y+1,z+10),texture='Assets/Piedra.png', parent=scene, origin_y=0)
                    Boxes.append(box)
            elif x == 0 and z == 2 or x == 2 and z in (0,4):
                if y in (0,1,3):
                    box = Button(color=color.white,model='cube',position=(x+10,y+1,z+10),texture='Assets/MAderaCheta.png', parent=scene, origin_y=0)
                    Boxes.append(box)
                elif y == 4:
                    box = Button(color=color.white,model='cube',position=(x+10,y+1,z+10),texture='Assets/Piedra.png', parent=scene, origin_y=0)
                    Boxes.append(box)
            elif x == 4 and z == 2:
                if y == 3:
                    box = Button(color=color.white,model='cube',position=(x+10,y+1,z+10),texture='Assets/MAderaCheta.png', parent=scene, origin_y=0)
                    Boxes.append(box)
                elif y == 4:
                    box = Button(color=color.white,model='cube',position=(x+10,y+1,z+10),texture='Assets/Piedra.png', parent=scene, origin_y=0)
                    Boxes.append(box)
            elif y == 4:
                box = Button(color=color.white,model='cube',position=(x+10,y+1,z+10),texture='Assets/Piedra.png', parent=scene, origin_y=0)
                Boxes.append(box)
                        
# INPUT -------- Poder construir y borrar bloques                   
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
                for bloque in Bloques_Gui:
                    if bloque.color == color.hex('#494949'): bloque.color=color.hex('#737373')
                bloque = int(key)-1
                Bloques_Gui[int(key)-1].color=color.hex('#494949')

app.run()

