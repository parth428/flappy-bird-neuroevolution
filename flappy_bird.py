# Machine Learning Flappy Bird Project
# Parth Patel
# pygame
# neat-python

# Objects(classes of objects): pipe, bird, ground 

import pygame 
import neat # NEAT is a method to train neural networks
import time
import os
import random
pygame.font.init() # Initialize the font

# Set the window size
WIN_WIDTH = 500  # CONSTANTS SO CAPS
WIN_HEIGHT = 800

# Set the generation to 0
GEN = 0

# Load the images. 2x the size of the original image
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), 
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), 
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

STAT_FONT = pygame.font.SysFont("calibri", 50, True) # Font for the score

# Bird class (bird objects moving)
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25  # How much the bird is rotated
    ROT_VEL = 20  # How much we rotate on each frame
    ANIMATION_TIME = 5  # How long each bird animation is shown

    def __init__(self, x, y): # x and y are the starting positions of the bird
        self.x = x 
        self.y = y
        self.tilt = 0 # 0 becuase bird starts flat
        self.tick_count = 0 # Physics of the bird
        self.vel = 0 # Velocity of the bird. Starting at still.
        self.height = self.y
        self.img_count = 0 # Which image we are showing
        self.img = self.IMGS[0] # Shows the bird image

    def jump(self):
        self.vel = -10.5 # Negative because top left corner is 0,0
        self.tick_count = 0 # When we last jumped
        self.height = self.y # Where the bird jumped from

    def move(self):
        self.tick_count += 1 # How many times we moved since we last jumped

        # Displacement: How many pixels we move up or down
        d = self.vel*self.tick_count + 1.5*self.tick_count**2 # Physics equation for displacement
        #-10.5*1 + 1.5*1 = -9.5 upwards velocity (upwards is negative)

        if d >= 16: # If we are moving down more than 16 pixels
            d = 16 # Cap the velocity at 16
        
        if d<0: # Improves the jump to be more smooth
            d -= 2

        self.y = self.y + d

        # Tilt the bird
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION: 
                self.tilt = self.MAX_ROTATION 
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1
        # Change the bird image based on the image count (animation)
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2: # 2nd image is shown
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3: # 3rd image is shown
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4: # 4th image is shown
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1: 
            self.img = self.IMGS[0]
            self.img_count = 0 # Reset the image count

        # When the bird is nose diving, we don't want the wings to flap
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        # Rotate the bird image
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center) # Rotate around the center instead of the top left corner
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    

class Pipe:
    GAP = 200 # Space between the pipes
    VEL = 5 # Velocity of the pipes
    
    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False # If the bird has passed the pipe for collision
        self.set_height() 

    def set_height(self):
        self.height = random.randrange(50, 450) # Random height of the pipe
        self.top = self.height - self.PIPE_TOP.get_height() # Top pipe
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win): # Draw the pipes
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird): # Pixel perfect collision/ hitbox method
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP) # Mask for the top pipe
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM) # Mask for the bottom pipe

        # Offset between the bird and the top pipe
        top_offset = (self.x - bird.x, self.top - round(bird.y)) 
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        # Point of collision
        b_point = bird_mask.overlap(bottom_mask, bottom_offset) 
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point: # If there is a collision
            return True

        return False

class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width() # Width of the base
    IMG = BASE_IMG 

    def __init__(self, y): # x does not need to be passed because the base moves horizontally
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH # 2nd base image starts at the end of the first base image

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0: # If the first base image goes off the screen
            self.x1 = self.x2 + self.WIDTH # Move it to the end of the 2nd base image so it looks like it is 1 moving object

        if self.x2 + self.WIDTH < 0: 
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win): # Draws the base
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
 
def draw_window(win, birds, pipes, base, score, gen): #Do the drawing from the object itself
    win.blit(BG_IMG, (0,0)) # Draw the background image

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255,0,0)) # Score text. 255 is the color.
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10)) # Position of the score text and keep moving it to the left

    text = STAT_FONT.render("Gen: " + str(gen), 1, (255,255,255)) 
    win.blit(text, (10, 10)) # Position of the generation

    base.draw(win)
    for bird in birds:
        bird.draw(win)
    pygame.display.update()

def main(genomes, config):
    global GEN
    GEN += 1
    nets = []
    ge = []
    birds = []

    # Create the population of birds
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config) # Create a neural network for each bird
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)
    
    base = Base(730)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock() # Clock object to control the speed of the game
    score = 0

    run = True
    while run: 
        clock.tick(30) # 30 frames per second
        for event in pygame.event.get(): # Check for events 
            if event.type == pygame.QUIT: # Quits pygame
                run = False    
                pygame.quit() # Quits the game when the window is closed
                quit()

        # Set pipe index to 0 by default
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break

        # Move the birds
        for x, bird in enumerate(birds):
            # Pass values to the neural network
            bird.move()
            ge[x].fitness += 0.1 # add fitness

            # Activiate the neural network
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom))) # distance between the bird and the top pipe, distance between the bird and the bottom pipe
            
            if output[0] > 0.5:
                bird.jump()

        add_pipe = False
        rem = [] # List of pipes to remove
        for pipe in pipes: # Move the pipes
            for x, bird in enumerate(birds): # Use for multiple birds
                if pipe.collide(bird):
                    ge[x].fitness -= 1 # If the bird hits the pipe, reduce 1 from the fitness score
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe) # Remove the pipe if it goes off the screen
            
            pipe.move() 
        
        if add_pipe: # If the bird passes the pipe add a new pipe and increase the score
            score += 1
            for g in ge: # if bird get through the pipe, increase the fitness score by 5
                g.fitness += 5 
            pipes.append(Pipe(600)) # 600 is the distance between the pipes
        
        for r in rem: # Remove the pipes that are off the screen
            pipes.remove(r)

        # If the bird hits the ground or the top of the screen, remove the bird
        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
    
        base.move() # Move the base
        draw_window(win, birds, pipes, base, score, GEN)


# NEAT ML Algorithm Setup to train the bird
# Load config file
def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    # Create the population
    p = neat.Population(config)

    # Stats reporter. Gives output of the stats of the population.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50) # Calls the main function 50 times

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)