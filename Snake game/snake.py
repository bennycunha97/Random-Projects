#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:39:01 2024

@author: bernardo
"""

import pygame
import os

pygame.init()

my_clock = pygame.time.Clock()
main_dir = os.path.split(os.path.abspath(__file__))[0]


image = pygame.image.load(os.path.join(main_dir, "data", "placeholder.png"))
# pygame.image.load("placeholder.png")
apple_image = pygame.image.load(os.path.join(main_dir, "data", "apple.png"))

head_u = pygame.image.load(os.path.join(main_dir, "data", "head_t.png"))
head_d = pygame.image.load(os.path.join(main_dir, "data", "head_b.png"))
head_l = pygame.image.load(os.path.join(main_dir, "data", "head_l.png"))
head_r = pygame.image.load(os.path.join(main_dir, "data", "head_r.png"))

tail_u = pygame.image.load(os.path.join(main_dir, "data", "tail_t.png"))
tail_d = pygame.image.load(os.path.join(main_dir, "data", "tail_b.png"))
tail_l = pygame.image.load(os.path.join(main_dir, "data", "tail_l.png"))
tail_r = pygame.image.load(os.path.join(main_dir, "data", "tail_r.png"))

mid_h = pygame.image.load(os.path.join(main_dir, "data", "mid_hor.png"))
mid_v = pygame.image.load(os.path.join(main_dir, "data", "mid_vert.png"))

mid_ul = pygame.image.load(os.path.join(main_dir, "data", "mid_tl.png"))
mid_ur = pygame.image.load(os.path.join(main_dir, "data", "mid_tr.png"))
mid_dl = pygame.image.load(os.path.join(main_dir, "data", "mid_bl.png"))
mid_dr = pygame.image.load(os.path.join(main_dir, "data", "mid_br.png"))







class SnakePiece:
    def __init__(self,pos,lifetime,orient="lr",head_img=head_r,mid_img = mid_h,
                 tail_img = tail_r):
        self.position = pos
        self.lifetime = lifetime
        self.orientation = orient
        if orient == "lr": # There has to be a better way...
            self.head_img = head_r
            self.mid_img = mid_h
            self.tail_img = tail_r
        if orient == "rl":
            self.head_img = head_l
            self.mid_img = mid_h
            self.tail_img = tail_l
        if orient == "ud":
            self.head_img = head_d
            self.mid_img = mid_v
            self.tail_img = tail_d
        if orient == "du":
            self.head_img = head_u
            self.mid_img = mid_v
            self.tail_img = tail_u
        if orient == "ld":
            self.head_img = head_d
            self.mid_img = mid_dl
            self.tail_img = tail_d
        if orient == "lu":
            self.head_img = head_u
            self.mid_img = mid_ul
            self.tail_img = tail_u
        if orient == "rd":
            self.head_img = head_d
            self.mid_img = mid_dr
            self.tail_img = tail_d
        if orient == "ru":
            self.head_img = head_u
            self.mid_img = mid_ur
            self.tail_img = tail_u
        if orient == "ul":
            self.head_img = head_l
            self.mid_img = mid_ul
            self.tail_img = tail_l
        if orient == "ur":
            self.head_img = head_r
            self.mid_img = mid_ur
            self.tail_img = tail_d
        if orient == "dl":
            self.head_img = head_l
            self.mid_img = mid_dl
            self.tail_img = tail_l
        if orient == "dr":
            self.head_img = head_r
            self.mid_img = mid_dr
            self.tail_img = tail_r
            
        
    def update(self,orient):
        self.orientation = orient
        if orient == "lr": # There has to be a better way...
            self.head_img = head_r
            self.mid_img = mid_h
            self.tail_img = tail_r
        if orient == "rl":
            self.head_img = head_l
            self.mid_img = mid_h
            self.tail_img = tail_l
        if orient == "ud":
            self.head_img = head_d
            self.mid_img = mid_v
            self.tail_img = tail_d
        if orient == "du":
            self.head_img = head_u
            self.mid_img = mid_v
            self.tail_img = tail_u
        if orient == "ld":
            self.head_img = head_d
            self.mid_img = mid_dl
            self.tail_img = tail_d
        if orient == "lu":
            self.head_img = head_u
            self.mid_img = mid_ul
            self.tail_img = tail_u
        if orient == "rd":
            self.head_img = head_d
            self.mid_img = mid_dr
            self.tail_img = tail_d
        if orient == "ru":
            self.head_img = head_u
            self.mid_img = mid_ur
            self.tail_img = tail_u
        if orient == "ul":
            self.head_img = head_l
            self.mid_img = mid_ul
            self.tail_img = tail_l
        if orient == "ur":
            self.head_img = head_r
            self.mid_img = mid_ur
            self.tail_img = tail_r
        if orient == "dl":
            self.head_img = head_l
            self.mid_img = mid_dl
            self.tail_img = tail_l
        if orient == "dr":
            self.head_img = head_r
            self.mid_img = mid_dr
            self.tail_img = tail_r
        

class SnakeSprite:
    
    def __init__(self,pieces):
        self.pieces=pieces
        self.grow = False
        
    def update(self,direct,orient):
        if direct == "left":
            x = self.pieces[0].position[0]-1
            y = self.pieces[0].position[1]
            # orient="horiz"
        elif direct == "right":
            x = self.pieces[0].position[0]+1
            y = self.pieces[0].position[1]
            # orient="horiz"
        elif direct == "up":
            x = self.pieces[0].position[0]
            y = self.pieces[0].position[1]-1
            # orient="vert"
        else:
            x = self.pieces[0].position[0]
            y = self.pieces[0].position[1]+1
            # orient="vert"
            
        
        
        
        
        if not self.grow:
            for piece in self.pieces:
                piece.lifetime -= 1
                if piece.lifetime == 0:
                    self.pieces.remove(piece)
                # print(piece.position,piece.lifetime)
        else:
            self.grow = False
            
        
    
        newpiece = SnakePiece((x,y), len(self.pieces)+1, orient)
        self.pieces.insert(0,newpiece)
        self.pieces[1].update(orient)
        
    def draw(self,target_surface):
        for i,piece in enumerate(self.pieces):
            if i == 0:
                target_surface.blit(piece.head_img, 
                                (piece.position[0]*30,piece.position[1]*30))
            elif i == len(self.pieces)-1:
                target_surface.blit(piece.tail_img, 
                                (piece.position[0]*30,piece.position[1]*30))
            else:
                target_surface.blit(piece.mid_img, 
                                (piece.position[0]*30,piece.position[1]*30))

    def test_oob(self,size):
        head_pos = self.pieces[0].position
        if head_pos[0] <= 0 or head_pos[0] >= size:
            return True
        elif head_pos[1] <= 0 or head_pos[1] >= size:
                return True
        return False
    
    def test_self_collision(self):
        head_pos = self.pieces[0].position
        for piece in self.pieces[1:]:
            if head_pos == piece.position:
                return True
        return False

class AppleSprite:
    
    def __init__(self,pos):
        self.position=pos
        

        
    def draw(self,target_surface):
        target_surface.blit(apple_image,
                            (self.position[0]*30,self.position[1]*30))


def compute_orient(old_dir,new_dir):
        if old_dir == "right":
            fl = "l"
        elif old_dir == "left":
            fl = "r"
        elif old_dir == "up":
            fl = "d"
        elif old_dir == "down":
            fl = "u"
        orient = fl + new_dir[0]
        return orient


def snake(speed,size):
    import random
    
    maxcounter =10 - speed
    
    pygame.display.init()
    
    #inner_surface_sz = size*30
    surface_sz=size*31
    surface = pygame.display.set_mode((surface_sz, surface_sz))
    surface.fill("white")
    
    border = pygame.Rect(0, 0, size*31, size*31)
    pygame.draw.rect(surface,"black",border,30)
    # pygame.draw.rect(surface,"white",(size,size,
     #                              inner_surface_sz,inner_surface_sz))
    all_sprites = []
    
    # testblob0=SnakePiece((15,14), 3, "vert")
    # testblob=SnakePiece((15,15), 2, "vert")
    # testblob2=SnakePiece((15,16), 1, "vert")
    initial_size = 5
    
    
    blobs=[SnakePiece((size//2-n,size//2),initial_size-n,"lr")
           for n in range(1,initial_size)]
    snake1=SnakeSprite(blobs)
    
    
    prov_direct = "right"
    direct = "right"
    orient = "lr"
    
    all_sprites.append(snake1)
    
    apple_count = 0
    
    def collision(apple,snake):
        col = False
        for piece in snake.pieces:
            if piece.position == apple.position:
                col = True
                return col
        return col
    
    while apple_count == 0:
        a_x,a_y = random.randint(1, size-1),random.randint(1, size-1)
        apple = AppleSprite((a_x,a_y))
        if not collision(apple, snake1):
            all_sprites.append(apple)
            apple_count +=1
    
    
    counter = 0
    score = 0
    while True:
        counter += 1 
        old_direct = direct
        # dt=my_clock.tick(60)
        # Look for an event from keyboard, mouse, etc.
        events = pygame.event.get()
        for ev in events:
            if ev.type == pygame.QUIT:
                pygame.quit()
                break;
            if ev.type == pygame.KEYDOWN:
                key = ev.dict["key"]
                if key == 27:         
                    pygame.quit() # On Escape key ...
                    break                      #   leave the game loop.
                if key == pygame.K_LEFT and direct != "right":
                    prov_direct = "left"
                if key == pygame.K_RIGHT and direct != "left":
                    prov_direct = "right"
                if key == pygame.K_UP and direct != "down":
                    prov_direct = "up"
                if key == pygame.K_DOWN and direct != "up":
                    prov_direct = "down"
    
        
    
        
    
        if snake1.pieces[0].position == apple.position:
            # print("eaten!")
            score +=1
            all_sprites.remove(apple)
            apple_count -= 1
            snake1.grow = True
            
        



        # generate an apple
        

        while apple_count == 0:
            a_x,a_y = random.randint(1, size-1),random.randint(1, size-1)
            apple = AppleSprite((a_x,a_y))
            if not collision(apple, snake1):
                all_sprites.append(apple)
                apple_count +=1
            

            
           
        surface.fill("white")
        
        # pygame.draw.rect(surface,"white",(size,size,
        #            inner_surface_sz-size,inner_surface_sz-size))     
        
        # # Ask every sprite to update itself.
        # for sprite in all_sprites:
        #     sprite.update(direct)
        
        orient = compute_orient(old_direct, direct)
               
        
        # snake1.update(direct,orient)
               
        if counter == maxcounter:
              direct = prov_direct
              orient = compute_orient(old_direct, direct)
              snake1.update(direct,orient)
              # print("updated!")
              # print(snake1.pieces[1].position)
              counter =0                       
          
        
        apple.draw(surface)
        snake1.draw(surface)
        
        
        pygame.draw.rect(surface,"black",border,30)

        # Check for collisions or apple eaten    
        if snake1.test_oob(size) or snake1.test_self_collision():
            pygame.quit()
            break;
            
        pygame.display.update()
        my_clock.tick(60)
        
    print("You ate",score,"apples!")  
    

    
    
    
    
if __name__ == "__main__":
    snake(6,30)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    