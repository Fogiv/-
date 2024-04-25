import pygame
import random
import time 
pygame.init()


WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED = 5
PADDLE_SPEED = 5


FONT = pygame.font.SysFont(None, 30)


ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)


ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

score1 = 0
score2 = 0

def collision():
   
    global ball_speed_x, ball_speed_y, score1, score2
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        score2 += 1
        reset_ball()
    if ball.right >= WIDTH:
        score1 += 1
        reset_ball()
        
        


def reset_ball():
    
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))
    


def bot_control():
    if paddle1.centery < ball.centery:
        paddle1.y += PADDLE_SPEED
    elif paddle1.centery > ball.centery:
        paddle1.y -= PADDLE_SPEED


def main():
    global ball_speed_x, ball_speed_y, score1, score2

    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        bot_control()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle2.top > 0:
            paddle2.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle2.bottom < HEIGHT:
            paddle2.y += PADDLE_SPEED


        ball.x += ball_speed_x
        ball.y += ball_speed_y


        collision()

        
        WIN.fill(BLACK)

        
        pygame.draw.rect(WIN, WHITE, paddle1)
        pygame.draw.rect(WIN, WHITE, paddle2)
        pygame.draw.ellipse(WIN, WHITE, ball)

        
        score_text = FONT.render(f"{score1} - {score2}", True, WHITE)
        WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

       
        pygame.display.update()
        
       
        clock.tick(60)
       

    pygame.quit()

if __name__ == "__main__":
    main()