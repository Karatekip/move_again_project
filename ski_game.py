import pygame
from sys import exit
import random
from random import randint

pygame.init()
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
    
def reset_game():
    global score, point_y, mountain_dir, sphere, points_group, last_point_time, was_on_ground, space_pressed, snowflakes
    score = 0
    point_y = 690
    mountain_dir = 'up'
    sphere = Sphere()
    points_group.empty()
    last_point_time = pygame.time.get_ticks()
    was_on_ground = True
    space_pressed = False
    snowflakes = []

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
            reset_game()
            game_state = 'playing'
        
    
    pygame.display.update()
    clock.tick(60)
