from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x, hand_y = [random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)]
# -1 hand가 화면 밖을 벗어나는 것을 방지
frame = 0
character_direction = 1  # 1은 오른쪽, -1은 왼쪽
hide_cursor()
def handle_events():
    global running
    global character_x, character_y, character_direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def random_move_boy(p1, p2):
    global character_x, character_y, frame, character_direction
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    t = frame / 100
    character_x = (1 - t) * x1 + t * x2
    character_y = (1 - t) * y1 + t * y2

    if x2 > x1:
        character_direction = -1  # 왼쪽을 보게 함
    else:
        character_direction = 1  # 오른쪽을 보게 함

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    #hand_x, hand_y = random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)
    hand.draw(hand_x, hand_y)
    if character_direction == 1:
        character.clip_draw(frame * 100, 0, 100, 100, character_x, character_y)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, ' ', character_x, character_y, 100, 100)
    random_move_boy((character_x, character_y), (hand_x, hand_y))
    frame = (frame + 1) % 8
    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()




