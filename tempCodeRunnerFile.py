
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                frogY_change=-frogY_change
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_SPACE:
                frogY_change *= -1j
        
    #check if the frog is on the rock or not
    if distance(frogX,rocksX, frogY, rocksY)<50:
        frogX_change=0
        frogY_change=0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: