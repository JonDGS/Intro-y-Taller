class player():
    def __init__(self,d1,d2,d3,d4,Angle,speed,speed_change,x,y):
        self.d1 = k2
        self.d2 = k0
        self.d3 = k1
        self.d4 = k3
        self.Angle = Angle
        self.speed = speed
        self.speed_change = speed_change
        self.x = x
        self.y = y
    def movement(self):
        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    G_exit = True
                    pygame.quit()
                    quit()
                elif event.key == K_2:
                    n = 1
                    Angle = 0
                    speed_change = 1
                    if event.key == K_2 and event.key == K_3:
                        y_player_change = -speed
                        x_player_change = speed
                    elif event.key == K_2 and event.key == K_1:
                        y_player_change = -speed
                        x_player_change = -speed
                    else:
                        y_player_change = -speed
                        x_player_change = 0
                elif event.key == K_0:
                    n = 1
                    Angle = 180
                    speed_change = 1
                    if event.key == K_0 and event.key == K_3:
                        y_player_change = speed
                        x_player_change = speed
                    elif event.key == K_0 and event.key == K_1:
                        y_player_change = speed
                        x_player_change = -speed
                    else:
                        y_player_change = speed
                        x_player_change = 0
                elif event.key == K_3:
                    n = 1
                    Angle = 270
                    speed_change = 1
                    if event.key == K_3 and event.key == K_2:
                        x_player_change = speed
                        y_player_change = -speed
                    elif event.key == K_3 and event.key == K_0:
                        x_player_change = speed
                        y_player_change = speed
                    else:
                        x_player_change = speed
                        y_player_change = 0
                elif event.key == K_1:
                    n = 1
                    Angle = 90
                    speed_change = 1
                    if event.key == K_1 and event.key == K_2:
                        x_player_change = -speed
                        y_player_change = -speed
                    elif event.key == K_1 and event.key == K_0:
                        x_player_change = -speed
                        y_player_change = speed
                    else:
                        x_player_change = -speed
                        y_player_change = 0
            elif event.type == pygame.KEYUP:
                if event.key == K_2:
                    y_player_change = 0
                    x_player_change = 0
##                    speed_change = -1
                elif event.key == K_0:
                    y_player_change = 0
                    x_player_change = 0
##                    speed_change = -1
                elif event.key == K_3:
                    x_player_change = 0
                    y_player_change = 0
##                    speed_change = -1
                elif event.key == K_1:
                    x_player_change = 0
                    y_player_change = 0
##                    speed_change = -1
        x_player += x_player_change
        y_player += y_player_change
        if speed > -1:
            speed += speed_change
        else:
            speed = 0
            speed_change = 0
        
