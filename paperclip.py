import pygame
import random
from random import randint
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Universal Paperclips")
clock = pygame.time.Clock()


class Market(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pc_amount = 0
        self.pc_ever = 0
        self.funds = 1000
        self.buyers = 1
        self.price = 15
        self.market_font = pygame.font.Font(None, 30)
        self.rival_font = pygame.font.Font(None, 23)
        self.seller_font = pygame.font.Font(None, 23)
        self.rival_title_font = pygame.font.Font(None, 27)
        self.dist = 0
        self.rival_avg = 15
        self.clip_it = 15
        self.the_clipatorium = 15
        self.twist_and_clip = 15
        self.paper_gripper = 15
        self.rival_list = ['clip_it', 'the_clipatorium', 'twist_and_clip', 'paper_gripper']
        self.sell_but_color = (255, 0, 0)
        self.sold_pc = 0
        self.new_buyer_chance = 0
        self.sell_amount = 500
        self.draw()
        
            
    def state(self, event_pos):
        if self.price_up_rect.collidepoint(event_pos):
            self.price += 0.5
        elif self.price_down_rect.collidepoint(event_pos) and self.price > 0:
            self.price -= 0.5
        elif self.sell_but_rect.collidepoint(event_pos):
            self.sell()
        elif self.sell_amount_up_rect.collidepoint(event_pos):
            self.sell_amount += 500
            self.price *= 2
        elif self.sell_amount_down_rect.collidepoint(event_pos) and self.sell_amount >= 1000:
            self.sell_amount -= 500
            self.price /= 2
            
    def update_pc(self):
        self.pc_amount += 5
        self.pc_ever += 5
        self.draw()
    
    def sell(self):
        if self.buyers > 0:
            if self.pc_amount >= self.sell_amount:
                self.funds += self.price
                self.pc_amount -= self.sell_amount
                self.sold_pc += self.sell_amount
                self.buyers -= (self.sell_amount // 500)
            else:
                pass
            
    def clients(self):
            self.dist = self.price - self.rival_avg
            if abs(self.dist) > 1:
                if self.dist > 0:
                    if self.buyers != 0:
                        self.buyers -= 1
                    seller.price_down(self)
                elif self.dist < 0:
                    self.buyers += 1
                    seller.price_up(self)
                #print('price not good')
            else:
                attraction = randint(1, 16)
                if self.buyers == 0 and attraction % 4 == 0:
                    self.buyers += 1
                else:
                    if attraction % 8:
                        self.buyers += self.pc_ever//1500
                
            self.new_buyer_chance = randint(1, 40)
            if self.new_buyer_chance == 1:
                self.buyers += 1                
            #print(f'dist: {self.dist}')
        
        
    def rivals(self):
        for rival in self.rival_list:
            evo_chance = randint(1, 32)
            evolution = 0
            if evo_chance % 8 == 0:
                evolution = random.choice([1, -1])
            if evo_chance == 30:
                #print("adapting")
                if self.dist > 0:
                    evolution = 1
                else:
                    evolution = -1
                
            if getattr(self, rival) <= 10:
                setattr(self, rival, getattr(self, rival) + 1)
            elif getattr(self, rival) >= 30:
                setattr(self, rival, getattr(self, rival) - 1)
            else:
                setattr(self, rival, getattr(self, rival) + evolution)
            
            
        self.rival_avg = (self.clip_it + self. the_clipatorium + self.twist_and_clip + self.paper_gripper) / 4
        #print(self.rival_avg)
        
    def draw(self):
        self.pc_surf = self.market_font.render(f'Paperclips: {self.pc_amount}', True, (128, 0, 128))
        self.pc_rect = self.pc_surf.get_rect(topleft = (900, 30))
        self.funds_surf = self.market_font.render(f'Funds: {self.funds}$', True, (128, 0, 128))
        self.funds_rect = self.funds_surf.get_rect(topleft = (900, 5))
        screen.blit(self.pc_surf, self.pc_rect)
        screen.blit(self.funds_surf, self.funds_rect)
        self.rival_title_surf = self.rival_title_font.render('Rivals:', True, (100, 100, 100))
        self.rival_title_rect = self.rival_title_surf.get_rect(topleft=(10, 150))
        screen.blit(self.rival_title_surf, self.rival_title_rect)
        y_offset = 175
        for rival in self.rival_list:
            rival_value = getattr(self, rival)  # Get the value of each rival
            rival_surf = self.rival_font.render(f'{rival}: {rival_value}$ / 500', True, (100, 100, 100))
            rival_rect = rival_surf.get_rect(topleft=(10, y_offset))
            screen.blit(rival_surf, rival_rect)
            y_offset += 20
        self.rival_avg_surf = self.rival_font.render(f'Rival avg: {self.rival_avg}', True, (160, 100, 100))
        self.rival_avg_rect = self.rival_avg_surf.get_rect(topleft=(10, 260))
        screen.blit(self.rival_avg_surf, self.rival_avg_rect)
        
        self.buyers_surf = self.rival_font.render(f'Buyers: {self.buyers}', True, (160, 100, 100))
        self.buyers_rect = self.buyers_surf.get_rect(topleft=(10, 280))
        screen.blit(self.buyers_surf, self.buyers_rect)
        if self.pc_amount >= self.sell_amount:
            self.sell_but_color = (0, 100, 0)
        else:
            self.sell_but_color = (255, 0, 0)
        self.sell_but_surf = self.market_font.render(f'Sell {self.sell_amount} paperclips for {self.price}$', True, self.sell_but_color)
        self.sell_but_rect = self.sell_but_surf.get_rect(topleft=(10, 83))
        screen.blit(self.sell_but_surf, self.sell_but_rect)
        
        self.price_up_surf = self.market_font.render('+', True, (0, 100, 0))
        self.price_up_rect = self.price_up_surf.get_rect(topleft=(280, 81))
        screen.blit(self.price_up_surf, self.price_up_rect)
        self.price_down_surf = self.market_font.render('-', True, (0, 100, 0))
        self.price_down_rect = self.price_down_surf.get_rect(topleft=(310, 82))
        screen.blit(self.price_down_surf, self.price_down_rect)
        
        self.sell_amount_up_surf = self.seller_font.render('+', True, (0, 120, 0))
        self.sell_amount_up_rect = self.sell_amount_up_surf.get_rect(topleft=(50, 103))
        screen.blit(self.sell_amount_up_surf, self.sell_amount_up_rect)
        self.sell_amount_down_surf = self.seller_font.render('-', True, (0, 120, 0))
        self.sell_amount_down_rect = self.sell_amount_down_surf.get_rect(topleft=(80, 103))
        screen.blit(self.sell_amount_down_surf, self.sell_amount_down_rect)
            

class Seller(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.seller_font = pygame.font.Font(None, 23)
        self.seller_state = 'inactive'
        self.seller_color = (255, 0, 0)
        self.seller_salaris = 2000
        self.sleep = True
        
    def price_down(self, market):
        if self.seller_state == 'active' and self.sleep == False and market.price > 0:
            market.price -= 0.5
    def price_up(self, market):
        if self.seller_state == 'active' and self.sleep == False:
            market.price += 0.5
    
    def state(self, event_pos):
        if self.seller_state == 'inactive' and market.funds >= self.seller_salaris:
            if self.seller_rect.collidepoint(event_pos):
                self.seller_state = 'active'
                market.funds -= self.seller_salaris
        elif self.seller_state == 'active':
            if self.seller_rect.collidepoint(event_pos):
                if self.sleep == True:
                    self.sleep = False
                else:
                    self.sleep = True
        
        
    def sell(self):
        if self.sleep == False:
            market.sell()
        
    def draw(self):
        if self.seller_state == 'inactive':
            if market.funds >= self.seller_salaris:
                self.seller_color = (0, 100, 0)
            else:
                self.seller_color = (255, 0, 0)
        else:
            self.seller_color = (100, 100, 100)
            
        if self.seller_state == 'active':
            if self.sleep == False:
                self.seller_surf = self.seller_font.render(f'Seller sold {market.sold_pc} paperclips', True, self.seller_color)
                self.seller_rect = self.seller_surf.get_rect(topleft=(10, 120))
                screen.blit(self.seller_surf, self.seller_rect)
            elif self.sleep == True:
                self.seller_surf = self.seller_font.render('Seller is sleeping', True, self.seller_color)
                self.seller_rect = self.seller_surf.get_rect(topleft=(10, 120))
                screen.blit(self.seller_surf, self.seller_rect)
        else:
            self.seller_surf = self.seller_font.render(f'Buy seller for {self.seller_salaris}$', True, self.seller_color)
            self.seller_rect = self.seller_surf.get_rect(topleft=(10, 126))
            screen.blit(self.seller_surf, self.seller_rect)
        
       
            
        #print(self.sleep)
class Factory(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.factory_font = pygame.font.Font(None, 40)
        self.factory_color = (0, 100, 0)
        self.factory_surf = self.factory_font.render("Factory", True, self.factory_color)
        self.factory_rect = self.factory_surf.get_rect(center = (550, 300))
        
    def state(self, event_pos, market):
        if self.factory_rect.collidepoint(event_pos):
            self.click()
            
        
    def click(self):
        if self.factory_color == (0, 100, 0):
            self.factory_color = (100, 150, 75)
        else:
            self.factory_color = (0, 100, 0)
        
        self.factory_surf = self.factory_font.render("Factory", True, self.factory_color)
        market.update_pc()
        
    def draw(self):
        screen.blit(self.factory_surf, self.factory_rect)
        
class Employee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.empl_font = pygame.font.Font(None, 30)
        self.potion_font = pygame.font.Font(None, 23)
        self.empl_num = 0
        self.empl_prod = 3
        self.hire_but_color = (255, 0, 0)
        self.empl_salaris = 0
        self.hire_but_surf = self.empl_font.render(f'Hire employee ({self.empl_salaris}$)', True, self.hire_but_color)
        self.hire_but_rect = self.hire_but_surf.get_rect(topleft = (250, 20))
        self.pot_cost = 50
        
        
        
    def state(self, event_pos):
        if self.hire_but_rect.collidepoint(event_pos):
            if market.funds >= self.empl_salaris:
                self.hire()
        elif self.potion_rect.collidepoint(event_pos) and market.funds > self.pot_cost:
            self.empl_prod *= 2
            self.pot_cost *= 2
            market.funds -= self.pot_cost
    
    def work(self):
        market.pc_amount += (self.empl_prod * self.empl_num)
        market.pc_ever += (self.empl_prod * self.empl_num)
        
    def hire(self):
        self.empl_num += 1
        market.funds -= self.empl_salaris
        if self.empl_num > 19:
            self.empl_salaris += 1
        
    def potion(self):
        self.empl_prod += 1
    
    def draw(self):
        if market.funds >= self.empl_salaris:
            self.hire_but_color = (0, 100, 0)
        else:
            self.hire_but_color = (255, 0, 0)
        self.empl_surf = self.empl_font.render(f'You have {self.empl_num} employees', True, (100, 100, 100))
        self.empl_rect = self.empl_surf.get_rect(topleft = (10, 20))
        screen.blit(self.empl_surf, self.empl_rect)
        self.hire_but_surf = self.empl_font.render(f'Hire employee ({self.empl_salaris}$)', True, self.hire_but_color)
        screen.blit(self.hire_but_surf, self.hire_but_rect)
        
        self.potion_surf = self.potion_font.render(f'Give potion ({self.pot_cost})$', True, (100, 100, 100))
        self.potion_rect = self.potion_surf.get_rect(topleft = (10, 45))
        screen.blit(self.potion_surf, self.potion_rect)
        
class Art(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pc_need = 20000
        self.art_title_font = pygame.font.Font(None, 30)
        self.art_font = pygame.font.Font(None, 23)
        self.art1_state = 'unmade'
        self.art2_state = 'unmade'
        self.art3_state = 'unmade'
        self.art1_need = 20000
        self.art2_need = 20000
        self.art3_need = 20000
        self.pc_need_color = (255, 0, 0)
        self.proposition = 1000
        
        
    def price_button_state(self, event_pos):
         if self.pc_need_up_rect.collidepoint(event_pos):
             self.pc_need += 5000
         elif self.pc_need_down_rect.collidepoint(event_pos):
             if self.pc_need > 20000:
                 self.pc_need -= 5000
         elif self.make_art1_rect.collidepoint(event_pos):
             if self.art1_state == 'unmade':
                 if self.pc_need <= market.pc_amount:
                     self.art1_state = 'made'
                     market.pc_amount -= self.pc_need
                     self.proposition = self.pc_need//4
                     print(self.proposition)
             else:
                 market.funds += self.proposition
                 self.art1_state = 'unmade'
             
    def art1(self):
            
        if self.art1_state == 'unmade':
            self.art1_surf = self.art_font.render(f'Art1({self.pc_need} paperclips)', True, (100, 100, 100))
            if market.pc_amount >= self.pc_need:
                self.pc_need_color = (0, 100, 0)
            else:
                self.pc_need_color = (255, 0, 0)
            self.make_art1_surf = self.art_font.render('Make', True, self.pc_need_color)
        else:
            self.pc_need_color = (0, 100, 0)
            self.art1_surf = self.art_font.render(f'Art1({self.pc_need}$)', True, (100, 100, 100))
            self.make_art1_surf = self.art_font.render('Sell', True, self.pc_need_color)
            
            infl_chance = randint(1, 3)
            if infl_chance != 3:
                inflation = random.choice([1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1])
                self.proposition += inflation
            
    def draw(self):
        self.art_title_surf = self.art_title_font.render('Metal art gallery', True, (100, 100, 100))
        self.art_title_rect = self.art_title_surf.get_rect(topleft = (10, 325))
        screen.blit(self.art_title_surf, self.art_title_rect)
        
        self.art1_rect = self.art1_surf.get_rect(topleft = (70, 350))
        screen.blit(self.art1_surf, self.art1_rect)
        self.make_art1_rect = self.make_art1_surf.get_rect(topleft = (10, 350))
        screen.blit(self.make_art1_surf, self.make_art1_rect)        
        
        self.art_value_surf = self.art_font.render('Art value:', True, (100, 100, 100))
        self.art_value_rect = self.art_value_surf.get_rect(topleft = (10, 375))
        screen.blit(self.art_value_surf, self.art_value_rect)        
        self.pc_need_up_surf = self.art_font.render('+', True, (0, 100, 0))
        self.pc_need_up_rect = self.pc_need_up_surf.get_rect(topleft = (100, 375))
        screen.blit(self.pc_need_up_surf, self.pc_need_up_rect)
        self.pc_need_down_surf = self.art_font.render('-', True, (0, 100, 0))
        self.pc_need_down_rect = self.pc_need_down_surf.get_rect(topleft = (130, 375))
        screen.blit(self.pc_need_down_surf, self.pc_need_down_rect)
        
        if self.art1_state == 'made':
            self.buyer_surf = self.art_font.render(f'buyer proposes {self.proposition}$', True, (0, 100, 0))
            self.buyer_rect = self.buyer_surf.get_rect(topleft = (200, 350))
            screen.blit(self.buyer_surf, self.buyer_rect)
    
    
    
    
factory = Factory()
market = Market()
employee = Employee()
seller = Seller()
art = Art()

last_work = pygame.time.get_ticks()
last_evo = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            factory.state(event.pos, market)
            employee.state(event.pos)
            market.state(event.pos)
            seller.state(event.pos)
            art.price_button_state(event.pos)
                
                
    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
            
    
    if (current_time - last_work) > 1000:
        employee.work()
        market.rivals()
        market.clients()
        if seller.seller_state == 'active':
            seller.sell()

        last_work = current_time
        #print(market.pc_ever)

    

    market.draw()
    factory.draw()   
    employee.draw()
    seller.draw()
    art.art1()
    art.draw()
    
    
    
    
    pygame.draw.line(screen, (200, 200, 200), (10, 310), (190, 310), 2)
    pygame.draw.line(screen, (200, 200, 200), (10, 68), (425, 68), 2)
    
    

    pygame.display.update()
    clock.tick(60)