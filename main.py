import env, sensors
import math
import pygame

environment = env.buildEnvironment((600,1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200, environment.originalMap, uncertainty=(0.5, 0.01))
environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()

running = True
sensorOn = False

while running:
    #sensorOn = False
   
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorOn = True
        elif not pygame.mouse.get_focused():
            sensorOn = False     
    
    if sensorOn: 
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense_obstacles()
        environment.dataStorage(sensor_data)
        environment.show_sensorData()
    
    environment.map.blit(environment.infomap, (0,0))
    pygame.display.update()

pygame.quit()


