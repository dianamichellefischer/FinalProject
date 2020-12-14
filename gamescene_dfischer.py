import pygame
import random




class Gamescene(object):

    def __init__(self, w, h):
        pygame.init()

        self.width = w
        self.height= h
        self.scene = pygame.display.set_mode((w,h))
        self.caption = pygame.display.set_caption("Dirty Room Escape!!")
        self.points = '0'

        self.message = {'intro':'Welcome to the Dirty Room Escape Room', 'description':'\nYou are in a room standing on a dirty floor covered in toys. \nYou see dusty blinds, dirty shelves, a messy bed and a closed door.  \nYou have to have everything cleaned up and put together to leave.  What do you want to do first? \nType help or enter exit to quit.\n',
                        'descript1':'\nYou see dusty blinds, dirty shelves, a messy bed and a closed door.  \nYou have to have everything cleaned up and put together to leave.  What do you want to do first? \nType help or enter exit to quit.\n',
                        'descript2':'\nYou see a messy bed, dirty floor and a closed door.  \nYou have to have everything cleaned up and put together to leave.  What do you want to do first? \nType help or enter exit to quit.\n',
                        'descript3':'\nYou see a dirty floor and a closed door.  \nYou have to have everything cleaned up and put together to leave.  What do you want to do? \nType help or enter exit to quit.\n',
                        'descript4':'\nYou see a dirty floor and a closed door.  \nYou have to have everything cleaned up and put together to leave.  What do you want to do? \nType help or enter exit to quit.\n','descript5':'\nYou see a closed door.  \nYou have to have everything cleaned up and put together to leave.  What do you want to do? \nType help or enter exit to quit.\n','winner':'You won!'}
        self.gameloop = True

        self.bgimg = 'assets/dirtyroom.jpg'

      
        if(self.bgimg != ''):
            self.bg = pygame.image.load(self.bgimg)

        self.bgc = (51,51,51)

    def setBackground(self, points):
        self.points = points
        self.scene.fill(self.bgc)
        if(self.bg != None):
            self.scene.blit(self.bg, (0,0) )
            
        if (self.points == '1'):
            self.bgimg = 'assets/removedtoys.jpg'
            self.bg = pygame.image.load(self.bgimg)

        elif self.points == 2:
            self.bgimg = 'assets/dustedshelves.jpg'
            self.bg = pygame.image.load(self.bgimg)
        elif self.points == 3:
            self.bgimg = 'assets/madebeds.jpg'
            self.bg = pygame.image.load(self.bgimg)
        elif self.points == 4:
            self.bgimg = 'assets/vacumedroom.jpg'
            self.bg = pygame.image.load(self.bgimg)
        elif self.points == 5:
            self.bgimg = 'assets/opendoor.jpg'
            self.bg = pygame.image.load(self.bgimg)
        else:
            self.bgimg = 'assets/dirtyroom.jpg'
            self.bg = pygame.image.load(self.bgimg)




    def update(self, points):
        self.setScoreBoard(self.points)
   
        pygame.display.update()
    


    def setScoreBoard(self, points):
        font = pygame.font.Font('freesansbold.ttf',32)

        text = font.render('[ '+str(self.points)+' ]', True, (255,255,255) )
        self.scene.blit(text, (10, 10) )

    def setPoints(self, points):
        self.points = self.points + points



    def playGame(self, points):
        h = 600
        w = 800
        g = Gamescene(w,h)
        pickupToys = False
        dustShelf = False
        makeBeds = False
        vacumeFloor = False
        openDoor = False

        self.points = points

        
        if (self.points == '0'):
            print(self.message.get('description'))
        elif (self.points == '1'):
            print(self.message.get('descript1'))            
        elif (self.points == '2'):
            print(self.message.get('descript2'))
        elif (self.points == '3'):
            print(self.message.get('descript3'))
        elif (self.points == '4'):
            print(self.message.get('descript4'))
        else:
            print(self.message.get('descript5'))
            print(self.message.get('winner'))
            play = False
            

        command = input("Enter what you want to do now: ")
        
        if (command == 'help'):
            f = open("help.txt", 'r')
            while True:
                line = f.readline()
                if line =="":
                    break
                print(line)
                
        elif (command == 'exit'):
            print('You have exited the game')
            play = False
            
        elif (command == 'list'):
            print([self.itemsDone])
            
        elif (command == 'pickup'):
            cmdPickup = input("Enter what you want to pickup: ")
            if (cmdPickup == "toys"):
                if (pickupToys):
                    print ("You already did that....")
                else:
                    print(self.points)
                    print ("You have picked up the toys!  Step 1!")
                    self.points = '1'
                    pickupToys = True
                    
            elif (cmdPickup == "door"):
                print ("You didn't finish cleaning!!")
            else:
                print ("You can't do that.  \nEnter what you want to do: ")


        elif (command == 'dust'):
            cmddustShelf = input("Enter what you want to dust: ")
            if (cmddustShelf == "shelf"):
                if (pickupToys == False):
                    print ("You need to pick up toys first")
                else:
                    print ("You have dusted the blinds, Step 2!")
                    self.points = '2'
                    dustShelf = True
                    
            elif (cmddustShelf == "door"):
                print ("You didn't finish cleaning!!")
            else:
                print ("You can't do that.  \nEnter what you want to do: ")

        elif (command == 'make'):
            cmdmakeBeds = input("Enter what you want to make: ")
            if (cmdmakeBeds == "beds"):
                if (dustShelf == False):
                    print ("You need to dust the shelf first")
                else:
                    print ("You have made the beds, Step 3!")
                    self.points = '3'
                    makeBeds = True
                    
            elif (cmdmakeBeds == "door"):
                print ("You didn't finish cleaning!!")
            else:
                print ("You can't do that.  \nEnter what you want to do: ")


        elif (command == 'vacume'):
            cmdvacumeFloor = input("Enter what you want to vaume: ")
            if (cmdvacumeFloor == "floor"):
                if (makeBeds == False):
                    print ("You need to make the beds first")
                else:
                    print ("You have vacumed, Step 4!")
                    self.points = '4'
                    vacumeFloor = True
                    
            elif (cmdvacumeFloor == "door"):
                print ("You didn't finish cleaning!!")
            else:
                print ("You can't do that.  \nEnter what you want to do: ")


        elif (command == 'open'):
            cmdopenDoor = input("Enter what you want to vaume: ")
            if (cmdopenDoor == "floor"):
                if (vacumeFloor == False):
                    print ("You need to vacume the floor first")
                else:
                    print ("You won!!")
                    self.points = '5'
                    openDoor = True
                    play = False

            else:
                print ("You can't do that.  \nEnter what you want to do: ")

                       
        else:
            print ("What was that?")





            
            
            


       



