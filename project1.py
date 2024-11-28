import pygame, math
from sys import exit
import random
from random import randint

 
pygame.init()
screen = pygame.display.set_mode((1200, 700))  # size screen
pygame.display.set_caption('MBC-project')  # name screen
clock = pygame.time.Clock()  # get time
font_1 = pygame.font.Font(None, 50)  # Check file path for the font
 
# starting_page
# images/surfaces
spring_touw_i_surf = pygame.image.load('graphics/spring_touw.jpg').convert_alpha()
spring_touw_i_surf = pygame.transform.scale(spring_touw_i_surf, (1300, 758))
spring_touw_i_rect = spring_touw_i_surf.get_rect(topleft=(-17, -10))
 
ski_i_surf = pygame.image.load('graphics/ski_view.jpg').convert_alpha()
ski_i_surf = pygame.transform.scale(ski_i_surf, (1300, 758))
ski_i_rect = ski_i_surf.get_rect(topleft=(-17, -10))
 
labyrinth_i_surf = pygame.image.load('graphics/labyrinth_view.jpg').convert_alpha()
labyrinth_i_surf = pygame.transform.scale(labyrinth_i_surf, (1300, 758))
labyrinth_i_rect = labyrinth_i_surf.get_rect(topleft=(-17, -10))
 
starttrans_surf = pygame.Surface((600, 500))
starttrans_surf.fill('pink')
starttrans_rect = starttrans_surf.get_rect(center=(600, 350))
 
# text
spring_touw_t_surf = font_1.render('spring touw', False, (251, 72, 196))
spring_touw_t_surf = pygame.transform.scale(spring_touw_t_surf, (250, 70))
spring_touw_t_rect = spring_touw_t_surf.get_rect(center=(250, 350))
 
ski_t_surf = font_1.render('Ski', False, (251, 72, 196))
ski_t_surf = pygame.transform.scale(ski_t_surf, (130, 70))
ski_t_rect = ski_t_surf.get_rect(center=(600, 350))
 
labyrinth_t_surf = font_1.render('Labyrinth', False, (251, 72, 196))
labyrinth_t_surf = pygame.transform.scale(labyrinth_t_surf, (250, 70))
labyrinth_t_rect = labyrinth_t_surf.get_rect(center=(900, 350))
 
play_surf = font_1.render('Start', False, (251, 72, 196))
play_surf = pygame.transform.scale(play_surf, (200, 70))
play_rect = play_surf.get_rect(center=(600, 600))
 
start_view = 'spring_touw'
game_status = 'unstarted'
screen_center = (600, 350)
game_ready = 'not_ready'
game_choice = 'not choosed yet'
rect_width, rect_height = 0, 0
growth_rate = 50
pink = (255, 105, 180)
underline_color = pink
underline_thickness = 3






def springtouw():
    global springtouw_achter, game_status
    screen_x = 1000
    screen_y = 500
    screen = pygame.display.set_mode((screen_x,screen_y))
    pygame.display.set_caption('game name')
    clock = pygame.time.Clock()
    none_font = pygame.font.Font(None,int(70))
    start_time = 0
    grond_hoogte = 373
    snelheid_touw = 0.04
    #False or True voor de 2 richtingen
    springtouw_draairichting = True
    springtouw_achter = True
    #starting_screen, playing, end_screen
    game_status = 'starting_screen'
    startup = True
    
    class Achtergrond:
        def __init__(self,achtergrond,x,y):
            self.image = pygame.image.load(achtergrond)
            self.image = pygame.transform.scale(self.image, (screen_x,screen_y))
            self.rect = self.image.get_rect(topleft = (x,y))
        def display_score(self):
            current_time = int(pygame.time.get_ticks()/1000 - start_time/1000)
            score_surf = none_font.render(f'score: {current_time}',True,(64,64,64))
            score_rect = score_surf.get_rect(center = (400,50))
            screen.blit(score_surf,score_rect)
            return current_time
        def blit(self):
            screen.blit(self.image,self.rect)
    
    class Grond(Achtergrond):
        def __init(self,achtergrond,x,y):
            super().__init__(achtergrond)
            self.image = pygame.transform.scale(self.image, (screen_x,screen_y/2))
            self.rect = self.image.get_rect(topleft = (x,y))
            
    class Obstacle:
        def __init__(self,obstacle_image,pos_x,pos_y):
            self.image = pygame.image.load(obstacle_image)
            self.image = pygame.transform.scale(self.image,(screen_x/4,screen_y/3))
            self.image.set_colorkey((255,255,255))
            self.rect = self.image.get_rect(center = (pos_x,pos_y))
            
    class Springtouw(Obstacle):
        def __init__(self,image,pos_x,pos_y):
            super().__init__(image,pos_x,pos_y)
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image,(300,10))
            self.image = pygame.transform.scale(self.image,(10,10))
            self.rect = self.image.get_rect(center = (pos_x,pos_y))
            
    class Player(Obstacle):
        def __init__(self,obstacle_image,pos_x,pos_y):
            super().__init__(obstacle_image,pos_x,pos_y)
            self.gravity = 0
            self.y_status = 'bestaan'
        def vallen(self):
            self.gravity -= 0.9
            self.rect.y -= self.gravity
        def staan(self):
            self.rect.y = self.rect.y - self.gravity
            if self.rect.bottom >= grond_hoogte: 
                self.rect.bottom = grond_hoogte
                self.y_status = 'staan'
            else: 
                self.vallen()
                self.y_status = 'vallen'
        def springen(self,hoogte):
            self.gravity = hoogte
            

    def draairichting_springtouw(richting):
        global springtouw_achter, game_status
        if springtouw_achter:
            screen.blit(player.image,player.rect)
        if springtouw_group[int(aantal_springtouwdelen/2)].rect.y >= 369:
            springtouw_achter = richting
            if richting:
                for springtouw in springtouw_group:
                    springtouw.image = pygame.transform.scale(springtouw.image,(9,9))
            else:
                for springtouw in springtouw_group:
                    springtouw.image = pygame.transform.scale(springtouw.image,(11,11))
            if player.y_status == 'staan':
                game_status = 'end_screen'
        elif springtouw_group[int(aantal_springtouwdelen/2)].rect.y <= 130:
            springtouw_achter = not richting
            if richting:
                for springtouw in springtouw_group:
                    springtouw.image = pygame.transform.scale(springtouw.image,(11,11))
            else:
                for springtouw in springtouw_group:
                    springtouw.image = pygame.transform.scale(springtouw.image,(9,9))
            if player.rect.top <= 130:
                game_status = 'end_screen'
                
                


    
    
    #maakt van de classes bruikbare objects
    player = Player('graphics/player2.png',screen_x/2,screen_y/2)
    player.rect.bottom = grond_hoogte
    grond = Grond('graphics/muur.png',0,grond_hoogte)
    begin_achtergrond = Achtergrond('graphics/muur.png',0,0)
         
    #bepaal de x pos voor elk sprintouwdeel
    springtouw_group = []
    aantal_springtouwdelen = 200
    pos_x = 0
    aantal_springtouw_gemaakt = 0
    for springtouw in range(aantal_springtouwdelen):
        pos_x = aantal_springtouw_gemaakt*math.pi/aantal_springtouwdelen + aantal_springtouw_gemaakt*(screen_x-3)/(aantal_springtouwdelen-1)
        springtouw = Springtouw('graphics/muur.png',pos_x, screen_y/2)
        springtouw_group.append(springtouw)
        aantal_springtouw_gemaakt += 1
        #print(aantal_springtouw_gemaakt)
    x = math.pi/2 + 0.5
    
    #startup_timer = pygame.USEREVENT + 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #if event.type == startup_timer:
             #   startup = True
            if game_status == 'starting_screen':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_status = 'playing'
                        
            elif game_status == 'playing':
                if player.y_status == 'staan':
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            player.springen(10)
                        
            elif game_status == 'end_screen':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.rect.bottom = grond_hoogte
                        springtouw_draairichting = True
                        springtouw_achter = True
                        startup = True
                        x = math.pi/2 + 0.5
                        game_status = 'playing'
        #print(game_status)
        #print(startup)
        if game_status == 'starting_screen':
            begin_achtergrond.blit()
            
        elif game_status == 'playing':
            screen.fill((255, 255, 255))
            screen.blit(grond.image,grond.rect)
    
            player.staan()
            
            #springtouw y positite berkenen
            if springtouw_achter == False:
                screen.blit(player.image,player.rect)
            for springtouw in springtouw_group:
                springtouw.rect.y = (screen_y/2 + (math.sin(x)*math.sin(springtouw.rect.center[0]*math.pi/screen_x)*120))
                screen.blit(springtouw.image,springtouw.rect)
                #pygame.draw.line(screen, (100,100,100), (100,screen_y/2), springtouw.rect.midleft,10)
            x += snelheid_touw
            draairichting_springtouw(springtouw_draairichting)
            if startup == True:
                pygame.display.update()
                pygame.time.wait(1000)
                startup = False
            
        elif game_status == 'end_screen':
            achtergrond = Achtergrond('graphics/muur.png',0,0)
            achtergrond.blit()
            end_tekst = none_font.render('je bent dood', True, (120,120,120))
            end_tekst_rect = end_tekst.get_rect(center = (500,100))
            screen.blit(end_tekst,end_tekst_rect)
            
        clock.tick(60)
        pygame.display.update()
 
 
def ski_game():
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption('Runner')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    
    class Sphere:
        def __init__(self):
            self.x = 300
            self.y = 0
            self.radius = 20
            self.color = (255, 255, 255)
            self.velocity_y = 0
            self.gravity = 0.22
            self.slow_fall_gravity = 0.04
            self.is_jumping = False
            self.is_space_held = False
            self.max_color_y = 700

        def update(self, points):
            if self.velocity_y > 0 and self.is_space_held:
                self.velocity_y += self.slow_fall_gravity
            else:
                self.velocity_y += self.gravity

            on_ground = False

            for point in points:
                if abs(point.rect.x - self.x) < 5:
                    if self.y + self.radius >= point.rect.y:
                        self.y = point.rect.y - self.radius
                        self.velocity_y = 0
                        on_ground = True

            if on_ground and self.is_jumping:
                self.velocity_y = -10
                self.is_jumping = False

            self.y += self.velocity_y
            
            normalized_height = max(0, min(self.max_color_y - self.y, self.max_color_y))
            red_intensity = int((normalized_height / self.max_color_y) * 255)
            self.color = (red_intensity, 100, 200)
            
            return on_ground

        def draw(self, surface):
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
    
    class Point(pygame.sprite.Sprite):
        def __init__(self, point_x, point_y):
            super().__init__()
            self.image = pygame.Surface((4, 1000))
            self.image.fill((100, 100, 100))
            self.rect = self.image.get_rect(topleft=(point_x, point_y))

        def update(self):
            self.rect.x -= 5
            
    class Snowflake:
        def __init__(self):
            self.x = random.randint(0, 1750)
            self.y = 0
            self.size = random.randint(2, 4)
            self.color = (255, 255, 255)
            self.speed = random.uniform(1, 3)
            self.horizontal_speed = random.uniform(-3,-3)

        def update(self):
            self.y += self.speed
            self.x += self.horizontal_speed
            
        def draw(self, surface):
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)
            
    class Deco:
        def __init__(self):
            #snoopy and woodstock
            self.sn_wo_width = 152
            self.sn_wo_hight = 96
            self.sn_wo_surf = pygame.image.load('graphics/snoopy_woodstock-removebg-preview.png').convert_alpha()
            self.sn_wo_surf = pygame.transform.scale(self.sn_wo_surf, (self.sn_wo_width, self.sn_wo_hight))
            self.sn_wo_y = 700
            self.sn_wo_x = 2000
            
            #snoopy on plane
            self.sn_pl_width = 115
            self.sn_pl_hight = 68
            self.sn_pl_surf = pygame.image.load('graphics/snoopy_plane-removebg-preview.png').convert_alpha()
            #self.sn_pl_surf = pygame.transform.flip(self.sn_pl_surf, True, False)
            self.sn_pl_surf = pygame.transform.scale(self.sn_pl_surf, (self.sn_pl_width, self.sn_pl_hight))
            self.sn_pl_y = 100
            self.sn_pl_x = -500
            
            #snoopy and snowman
            self.sn_sn_width = 85
            self.sn_sn_hight = 77
            self.sn_sn_surf = pygame.image.load('graphics/snoopy_snowman-removebg-preview.png').convert_alpha()
            self.sn_sn_surf = pygame.transform.scale(self.sn_sn_surf, (self.sn_sn_width, self.sn_sn_hight))
            self.sn_sn_y = 700
            self.sn_sn_x = 4000
            
            #snoopy and 3 woodstock
            self.sn_3wo_width = 115
            self.sn_3wo_hight = 68
            self.sn_3wo_surf = pygame.image.load('graphics/snoopy_3woodstock-removebg-preview.png').convert_alpha()
            self.sn_3wo_surf = pygame.transform.scale(self.sn_3wo_surf, (self.sn_3wo_width, self.sn_3wo_hight))
            self.sn_3wo_y = 700
            self.sn_3wo_x = 6000
            
            #snoopy and woodstock
            self.sn_ho_width = 152
            self.sn_ho_hight = 96
            self.sn_ho_surf = pygame.image.load('graphics/peanuts-snoopy-et-la-niche-du-chien-poster-poster-removebg-preview.png').convert_alpha()
            self.sn_ho_surf = pygame.transform.scale(self.sn_ho_surf, (self.sn_ho_width, self.sn_ho_hight))
            self.sn_ho_y = 700
            self.sn_ho_x = 8000
            
        def move(self):
            #snoopy and woodstock
            self.sn_wo_x -= 5
            if (self.sn_wo_x + self.sn_wo_width) < 0:
                self.sn_wo_x = randint(2000, 4000)
            self.sn_wo_rect = self.sn_wo_surf.get_rect(bottomleft=(self.sn_wo_x, self.sn_wo_y))
            
            #snoopy on plane
            self.sn_pl_x += 3
            if (self.sn_pl_x) > 1200:
                self.sn_pl_x = randint(-1000, -400)
                self.sn_pl_y = randint(60, 220)
            self.sn_pl_rect = self.sn_pl_surf.get_rect(bottomleft=(self.sn_pl_x, self.sn_pl_y))
            
            #snoopy and snowman
            self.sn_sn_x -= 5
            if (self.sn_sn_x + self.sn_sn_width) < 0:
                self.sn_sn_x = randint(2000, 4000)
            self.sn_sn_rect = self.sn_sn_surf.get_rect(bottomleft=(self.sn_sn_x, self.sn_sn_y))
            
            #snoopy and 3 woodstocks
            self.sn_3wo_x -= 5
            if (self.sn_3wo_x + self.sn_3wo_width) < 0:
                self.sn_3wo_x = randint(2000, 4000)
            self.sn_3wo_rect = self.sn_3wo_surf.get_rect(bottomleft=(self.sn_3wo_x, self.sn_3wo_y))
            
            #snoopy and woodstock
            self.sn_ho_x -= 5
            if (self.sn_ho_x + self.sn_ho_width) < 0:
                self.sn_ho_x = randint(2000, 4000)
            self.sn_ho_rect = self.sn_ho_surf.get_rect(bottomleft=(self.sn_ho_x, self.sn_ho_y))
            
        def draw(self):
            screen.blit(self.sn_wo_surf, self.sn_wo_rect)
            screen.blit(self.sn_pl_surf, self.sn_pl_rect)
            screen.blit(self.sn_sn_surf, self.sn_sn_rect)
            screen.blit(self.sn_3wo_surf, self.sn_3wo_rect)
            screen.blit(self.sn_ho_surf, self.sn_ho_rect)
    
    """def reset_game():
        global score, point_y, mountain_dir, sphere, points_group, last_point_time, was_on_ground, space_pressed, snowflakes
        score = 0
        point_y = 690
        mountain_dir = 'up'
        sphere = Sphere()
        points_group.empty()
        last_point_time = pygame.time.get_ticks()
        was_on_ground = True
        space_pressed = False
        snowflakes = []"""
        
        
    point_y = 1000
    points_group = pygame.sprite.Group()
    mountain_dir = 'up'
    sphere = Sphere()
    score = 0
    score_increment_timer = 0
    SCORE_INCREMENT_INTERVAL = 100

    deco = Deco()

    POINT_CREATION_INTERVAL = 40
    SNOWFLAKE_CREATION_INTERVAL = 1
    last_point_time = pygame.time.get_ticks()
    last_snowflake_time = pygame.time.get_ticks()

    snowflakes = []
    was_on_ground = True
    space_pressed = False
    game_state = 'playing'
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not sphere.is_jumping:
                        sphere.is_jumping = True 
                        space_pressed = True
                    sphere.is_space_held = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    sphere.is_space_held = False

        current_time = pygame.time.get_ticks()


        if game_state == 'playing':
            if sphere.velocity_y < 0:
                score_increment_timer += clock.get_time()
                if score_increment_timer >= SCORE_INCREMENT_INTERVAL:
                    score += 1
                    score_increment_timer = 0

            if current_time - last_point_time >= POINT_CREATION_INTERVAL:
                if mountain_dir == 'up':
                    point_y -= 2
                    
                    points_group.add(Point(1200, point_y))
                    if point_y < 570:
                        if random.random() < 0.028 or point_y < 450:
                            mountain_dir = 'down'
                elif mountain_dir == 'down':
                    point_y += 2
                    points_group.add(Point(1200, point_y))
                    if point_y > 600:
                        mountain_dir = 'up'


            if current_time - last_snowflake_time >= SNOWFLAKE_CREATION_INTERVAL:
                snowflakes.append(Snowflake())
                last_snowflake_time = current_time

            for snowflake in snowflakes[:]:
                snowflake.update()
                if snowflake.y > 700:
                    snowflakes.remove(snowflake)
                else:
                    for point in points_group:
                        if (snowflake.x >= point.rect.x and snowflake.x <= point.rect.x + point.rect.width) and \
                           (snowflake.y + snowflake.size >= point.rect.y and snowflake.y - snowflake.size <= point.rect.y + point.rect.height):
                            snowflakes.remove(snowflake)
                            break

            points_group.update()
            on_ground = sphere.update(points_group.sprites())

            if on_ground and not was_on_ground:
                if space_pressed:
                    ground_y_positions = []
                    for point in points_group:
                        if abs(point.rect.x - sphere.x) < 50:
                            ground_y_positions.append(point.rect.y)

                    if len(ground_y_positions) > 1:
                        slope = ground_y_positions[-1] - ground_y_positions[0]
                        if slope > 0:
                            print("The sphere has landed after jumping on falling ground!")
                        elif slope < 0:
                            print("GAME OVER")
                            print(f"Final Score: {score}")
                            game_state = 'over'
                        else:
                            print("The sphere has landed after jumping on flat ground!")
                    space_pressed = False

            was_on_ground = on_ground

            for point in points_group:
                if point.rect.x < 0:
                    points_group.remove(point)

            screen.fill((0, 0, 0))
            points_group.draw(screen)
            deco.move()
            deco.draw()
            
            if current_time >= 5000:
                sphere.draw(screen)
            elif 4970 <= current_time <=5030:
                print("GO!")
            else:
                print("Be ready!")
            

            # Draw each snowflake
            for snowflake in snowflakes:
                snowflake.draw(screen)

            score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
            screen.blit(score_surface, (10, 10))

        elif game_state == 'over':
            screen.fill((0, 0, 0))
            game_over_surface = font.render("GAME OVER", True, (255, 0, 0))
            score_surface = font.render(f'Final Score: {score}', True, (255, 255, 255))
            screen.blit(game_over_surface, (500, 300))
            screen.blit(score_surface, (500, 350))
            
            if space_pressed:
                points_group.empty()
                score = 0
                point_y = 690
                mountain_dir = 'up'
                sphere = Sphere()
                last_point_time = pygame.time.get_ticks()
                was_on_ground = True
                space_pressed = False
                snowflakes = []
                game_state = 'playing'
            
        
        pygame.display.update()
        clock.tick(60)
        
 
 
game_mode = None
 
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # to quit
            pygame.quit()
            exit()
 
    # Start page logic (before game starts)
    if game_ready == 'not_ready':
        mouse_x, mouse_y = pygame.mouse.get_pos()
 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if spring_touw_t_rect.collidepoint(mouse_x, mouse_y):
                start_view = 'spring_touw'
            elif ski_t_rect.collidepoint(mouse_x, mouse_y):
                start_view = 'ski'
            elif labyrinth_t_rect.collidepoint(mouse_x, mouse_y):
                start_view = 'labyrinth'
            elif play_rect.collidepoint(mouse_x, mouse_y):
                game_status = 'started'
 
        distance_x = mouse_x - screen_center[0]
        distance_y = mouse_y - screen_center[1]
 
        # Background image logic
        if start_view == 'spring_touw':
            spring_touw_i_rect.center = (screen_center[0] + distance_x / 20, screen_center[1] + distance_y / 20)
            screen.blit(spring_touw_i_surf, spring_touw_i_rect)
            underline_rect = pygame.Rect(spring_touw_t_rect.left, spring_touw_t_rect.bottom - 5, spring_touw_t_rect.width, underline_thickness)
            pygame.draw.rect(screen, underline_color, underline_rect)
            game_mode = 'spring_touw'
 
        elif start_view == 'ski':
            ski_i_rect.center = (screen_center[0] + distance_x / 20, screen_center[1] + distance_y / 20)
            screen.blit(ski_i_surf, ski_i_rect)
            underline_rect = pygame.Rect(ski_t_rect.left, ski_t_rect.bottom - 5, ski_t_rect.width, underline_thickness)
            pygame.draw.rect(screen, underline_color, underline_rect)
            game_mode = 'ski'
 
        elif start_view == 'labyrinth':
            labyrinth_i_rect.center = (screen_center[0] + distance_x / 20, screen_center[1] + distance_y / 20)
            screen.blit(labyrinth_i_surf, labyrinth_i_rect)
            underline_rect = pygame.Rect(labyrinth_t_rect.left, labyrinth_t_rect.bottom - 5, labyrinth_t_rect.width, underline_thickness)
            pygame.draw.rect(screen, underline_color, underline_rect)
            game_mode = 'labyrinth'
 
        # Text and button logic
        screen.blit(spring_touw_t_surf, spring_touw_t_rect)
        screen.blit(ski_t_surf, ski_t_rect)
        screen.blit(labyrinth_t_surf, labyrinth_t_rect)
        screen.blit(play_surf, play_rect)
 
        # Transition effect
        if game_status == 'started':
            rect_width += growth_rate
            rect_height += growth_rate
            if rect_width >= screen.get_width():
                game_ready = 'ready'
            elif rect_height >= screen.get_height():
                rect_height = screen.get_height()
 
            starttrans_surf = pygame.Surface((rect_width, rect_height))
            starttrans_surf.fill('pink')
            starttrans_rect = starttrans_surf.get_rect(center=screen_center)
            screen.blit(starttrans_surf, starttrans_rect)
 
    elif game_ready == 'ready':
        screen.fill('pink')
        print(game_mode)
        if game_mode == 'spring_touw':
            springtouw()
            
            print('playing spring touw')
        elif game_mode == 'ski':
            ski_game()
            print('playing ski')
        elif game_mode == 'labyrinth':

            print('playing labyrinth')

 
    pygame.display.update()
    clock.tick(60)