import pygame 

class Game:
    def __init__(self):
        # Intialize game variables
        pygame.init()
        pygame.display.set_caption("Snake") # Name window title to Snake
        # Set screen dimensions
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 500
        # Set display resolution (w x h)
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT]) 
        
        # Initialize clock for game ticks
        self.clock = pygame.time.Clock() 
 
        #Group and add sprites
        self.all_sprites_list = pygame.sprite.Group()
        """ self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        self.all_sprites_list.add(self.ball)"""
        
        self.isRunning = True # Set isRunning state of the game to True
        self.MainLoop() # Start main loop
    
    def ProcessInput(self): # Responsible for game event such as input, prog
        for event in pygame.event.get():
            keys = pygame.key.get_pressed() # Get the key currently being pressed
            if event.type == pygame.QUIT: # Did the user exit the game?
                self.isRunning = False
            # Take keyboard input to control paddle
            """else:
                if keys[pygame.K_w]:
                    self.paddleA.moveUp(10)
                if keys[pygame.K_s]:
                    self.paddleA.moveDown(10)
                if keys2[pygame.K_UP]:
                    self.paddleB.moveUp(10)
                if keys2[pygame.K_DOWN]:
                    self.paddleB.moveDown(10)"""
            
        
    def UpdateGame(self): # Updates game variables/conditions
        
        self.all_sprites_list.update() # Updates all sprites in list
        self.clock.tick(60) # Frame rate control

    def GenerateOutput(self): # Updates the graphics in the game
        self.screen.fill("BLACK") # Fill the background with black 
        # Render paddle score texts
       
        self.all_sprites_list.draw(self.screen) # Render sprites in game
        
        pygame.display.flip() # Flip the display
        
    def MainLoop(self): # Runs in game processes in a loop
        while self.isRunning: # Keep on doing these proccess until the game exits
            self.ProcessInput()
            self.UpdateGame()
            self.GenerateOutput()
        pygame.quit() # Close the game
