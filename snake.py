import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("my game")
running = True
snake_x = 80
snake_y = 100
direction = 'RIGHT'
speed = 0
counter = 0

while running:
    counter+=1
    print (counter)
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'UP'
                snake_y -= 5
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
                snake_y += 5
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'  
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
                snake_x -= 5
                
    if direction == 'RIGHT':
         snake_x += 5   
    if direction == 'LEFT':
        snake_x -= 5
    if direction == 'UP':
        snake_y -= 5
    if direction == 'DOWN':
        snake_y += 5
    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, (58, 123, 208), (snake_x, snake_y, 100, 50))
    pygame.draw.circle(screen, (255,0,0), (300, 300), 10)
    pygame.draw.circle(screen, (255, 255, 255), (92, 140), 7)
    pygame.draw.circle(screen, (255, 255, 255), (92, 115), 7)
    pygame.display.flip()
    pygame.time.delay(100-speed)
    if counter == 10:
        speed += 1
        counter = 0
    
    
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         direction  ='UP'
        # elif event.key == pygame.K_DOWN:
        #     direction ='DOWN'
        # elif event.key == pygame.K_LEFT:
        #     direction ='LEFT'
        # elif event.key == pygame.K_RIGHT:
        #     direction ='RIGHT'
        # if event.type == pygame.K_UP:
        #     snake_y -= 200

    # screen.fill((50,50,50))
    # import pygame

    # pygame.init()
    # screen = pygame.display.set_mode((600, 600))
    # pygame.display.set_caption("my game")
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             running = False
