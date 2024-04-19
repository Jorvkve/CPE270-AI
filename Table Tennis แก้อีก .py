# ใช้ pip เพื่อติดตั้งโมดูล pygame ก่อนเริ่มต้น
# pip install pygame ก่อนนะจร้ะ
import pygame  # นำเข้าโมดูล pygame เพื่อใช้งาน
import random  # นำเข้าโมดูล random เพื่อสุ่มตัวเลข
import numpy as np  # นำเข้าโมดูล numpy เพื่อใช้งาน

# กำหนดขนาดหน้าต่างและชื่อเกม
pygame.init()  # เริ่มต้นใช้งานโมดูล pygame
WIDTH, HEIGHT = 700, 500  # กำหนดความกว้างและความสูงของหน้าต่าง
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # สร้างหน้าต่างโดยใช้ความกว้างและความสูงที่กำหนด
pygame.display.set_caption("Table Tennis")  # กำหนดชื่อของหน้าต่างเกมเป็น "Table Tennis"

# กำหนด Frames Per Second (FPS) และสีต่าง ๆ
FPS = 60  # กำหนด Frames Per Second (FPS) ให้มีค่าเท่ากับ 60 เฟรมต่อวินาที
WHITE = (255, 255, 255)  # กำหนดสีขาวโดยใช้รหัสสี RGB (255, 255, 255)
BLACK = (0, 0, 0)  # กำหนดสีดำโดยใช้รหัสสี RGB (0, 0, 0)
RED = (255, 0, 0)  # กำหนดสีแดงโดยใช้รหัสสี RGB (255, 0, 0)

# กำหนดขนาดและรูปแบบของ paddle และลูกบอล
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100  # กำหนดขนาดของ paddle ให้มีความกว้าง 20 พิกเซลและความสูง 100 พิกเซล
BALL_RADIUS = 7  # กำหนดรัศมีของลูกบอลให้มีค่าเท่ากับ 7 พิกเซล

# กำหนดรูปแบบและขนาดของตัวหนังสือสำหรับคะแนนและคะแนนที่จะชนะ
SCORE_FONT = pygame.font.SysFont("comicsans", 50)  # กำหนดรูปแบบและขนาดของตัวหนังสือที่ใช้แสดงคะแนนในเกม
WINNING_SCORE = 10  # กำหนดคะแนนที่จะใช้ในการชนะเกม

# คลาสสำหรับ paddle
class Paddle:
    COLOR = WHITE  # กำหนดสีของ paddle เป็นสีขาว
    VEL = 3  # กำหนดความเร็วในการเคลื่อนที่ของ paddle

    def __init__(self, x, y, width, height):  # กำหนดค่าเริ่มต้นสำหรับ paddle
        self.x = self.original_x = x  # กำหนดตำแหน่งเริ่มต้นและตำแหน่งปัจจุบันของ paddle ในแนวแกน x
        self.y = self.original_y = y  # กำหนดตำแหน่งเริ่มต้นและตำแหน่งปัจจุบันของ paddle ในแนวแกน y
        self.width = width  # กำหนดความกว้างของ paddle
        self.height = height  # กำหนดความสูงของ paddle

    def draw(self, win):  # วาด paddle บนหน้าต่าง
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.width, self.height))  # วาดสี่เหลี่ยมผืนผ้าลงบนหน้าต่าง

    def move(self, up=True):  # ย้าย paddle ขึ้นหรือลง
        if up:
            self.y -= self.VEL  # ย้าย paddle ขึ้น
        else:
            self.y += self.VEL  # ย้าย paddle ลง

    def reset(self):  # รีเซ็ตตำแหน่ง paddle กลับไปยังตำแหน่งเริ่มต้น
        self.x = self.original_x  # ตั้งค่าตำแหน่ง x ของ paddle เป็นตำแหน่งเริ่มต้น
        self.y = self.original_y  # ตั้งค่าตำแหน่ง y ของ paddle เป็นตำแหน่งเริ่มต้น

# คลาสสำหรับลูกบอล
class Ball:
    MAX_VEL = 5  # กำหนดค่าสูงสุดของความเร็วในการเคลื่อนที่ของลูกบอล
    COLOR = RED  # กำหนดสีของลูกบอลเป็นสีแดง

    def __init__(self, x, y, radius):  # กำหนดค่าเริ่มต้นสำหรับลูกบอล
        self.x = self.original_x = x  # กำหนดตำแหน่งเริ่มต้นและตำแหน่งปัจจุบันของลูกบอลในแนวแกน x
        self.y = self.original_y = y  # กำหนดตำแหน่งเริ่มต้นและตำแหน่งปัจจุบันของลูกบอลในแนวแกน y
        self.radius = radius  # กำหนดรัศมีของลูกบอล
        self.x_vel = self.MAX_VEL  # กำหนดความเร็วในแนวแกน x ของลูกบอล
        self.y_vel = 0  # กำหนดความเร็วในแนวแกน y ของลูกบอลเป็น 0

    def draw(self, win):  # วาดลูกบอลบนหน้าต่าง
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)  # วาดวงกลมลงบนหน้าต่าง

    def move(self):  # เคลื่อนที่ลูกบอล
        self.x += self.x_vel  # เคลื่อนที่ลูกบอลในแนวแกน x
        self.y += self.y_vel  # เคลื่อนที่ลูกบอลในแนวแกน y

    def reset(self):  # รีเซ็ตตำแหน่งลูกบอลกลับไปยังตำแหน่งเริ่มต้น
        self.x = self.original_x  # ตั้งค่าตำแหน่ง x ของลูกบอลเป็นตำแหน่งเริ่มต้น
        self.y = self.original_y  # ตั้งค่าตำแหน่ง y ของลูกบอลเป็นตำแหน่งเริ่มต้น
        self.y_vel = 0  # ตั้งค่าความเร็วในแนวแกน y ของลูกบอลเป็น 0
        self.x_vel *= -1  # เปลี่ยนทิศทางของความเร็วในแนวแกน x ให้กลับสู่ทิศตรงข้าม

# ฟังก์ชันสำหรับวาดส่วนต่าง ๆ ของเกม
def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)  # เติมพื้นหลังของหน้าต่างเกมด้วยสีดำ

    # วาดข้อความคะแนนบนหน้าต่างเกม
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)  # สร้างข้อความคะแนนของผู้เล่นทางซ้าย
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)  # สร้างข้อความคะแนนของผู้เล่นทางขวา
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))  # วางข้อความคะแนนของผู้เล่นทางซ้ายลงบนหน้าต่างเกม
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))  # วางข้อความคะแนนของผู้เล่นทางขวาลงบนหน้าต่างเกม

    # วาด paddle ทั้งสองข้าง
    for paddle in paddles:
        paddle.draw(win)

    # วาดเส้นกึ่งกลางแยกสนามเกม
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:  # ถ้า i เป็นเลขคี่ ข้ามไปเลย
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))  # วาดเส้นกึ่งกลาง

    ball.draw(win)  # วาดลูกบอลบนหน้าต่างเกม
    pygame.display.update()  # อัปเดตหน้าต่างเกม

# ฟังก์ชันสำหรับจัดการการชนของลูกบอลกับ paddle
def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:  # หากลูกบอลชนขอบล่างของหน้าต่าง
        ball.y_vel *= -1  # เปลี่ยนทิศทางความเร็วในแนวแกน y ของลูกบอลให้กลับสู่ทิศตรงข้าม
    elif ball.y - ball.radius <= 0:  # หากลูกบอลชนขอบบนของหน้าต่าง
        ball.y_vel *= -1  # เปลี่ยนทิศทางความเร็วในแนวแกน y ของลูกบอลให้กลับสู่ทิศตรงข้าม

    if ball.x_vel < 0:  # ถ้าลูกบอลกำลังเคลื่อนที่ไปทางซ้าย
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:  # ถ้าลูกบอลชน paddle ทางซ้าย
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:  # ถ้าลูกบอลชนไปทางซ้ายของ paddle
                ball.x_vel *= -1  # เปลี่ยนทิศทางความเร็วในแนวแกน x ของลูกบอลให้กลับสู่ทิศตรงข้าม

                middle_y = left_paddle.y + left_paddle.height / 2  # หาค่าตำแหน่งกึ่งกลางของ paddle ทางซ้าย
                difference_in_y = middle_y - ball.y  # หาความต่างของตำแหน่ง y ระหว่างลูกบอลกับตำแหน่งกึ่งกลางของ paddle
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL  # คำนวณหารายการลดขนาด
                y_vel = difference_in_y / reduction_factor  # คำนวณความเร็วในแนวแกน y ของลูกบอล
                ball.y_vel = -1 * y_vel  # กำหนดความเร็วในแนวแกน y ของลูกบอล

    else:  # ถ้าลูกบอลกำลังเคลื่อนที่ไปทางขวา
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:  # ถ้าลูกบอลชน paddle ทางขวา
            if ball.x + ball.radius >= right_paddle.x:  # ถ้าลูกบอลชนไปทางขวาของ paddle
                ball.x_vel *= -1  # เปลี่ยนทิศทางความเร็วในแนวแกน x ของลูกบอลให้กลับสู่ทิศตรงข้าม

                middle_y = right_paddle.y + right_paddle.height / 2  # หาค่าตำแหน่งกึ่งกลางของ paddle ทางขวา
                difference_in_y = middle_y - ball.y  # หาความต่างของตำแหน่ง y ระหว่างลูกบอลกับตำแหน่งกึ่งกลางของ paddle
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL  # คำนวณหารายการลดขนาด
                y_vel = difference_in_y / reduction_factor  # คำนวณความเร็วในแนวแกน y ของลูกบอล
                ball.y_vel = -1 * y_vel  # กำหนดความเร็วในแนวแกน y ของลูกบอล

# ฟังก์ชันสำหรับการเคลื่อนไหวของ paddle ของผู้ใช้
def handle_user_movement(keys, left_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:  # ถ้าปุ่ม w ถูกกดและ paddle ยังไม่ชนขอบบนของหน้าต่าง
        left_paddle.move(up=True)  # เคลื่อน paddle ขึ้น

    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:  # ถ้าปุ่ม s ถูกกดและ paddle ยังไม่ชนขอบล่างของหน้าต่าง
        left_paddle.move(up=False)  # เคลื่อน paddle ลง

# นิยามฟังก์ชัน handle_ai_movement() เพื่อควบคุมการเคลื่อนที่ของ AI โดยใช้ตำแหน่งของลูกบอล
def handle_ai_movement(ball, right_paddle, player_vel):
    # คำนวณตำแหน่งที่ AI ควรจะเคลื่อนที่เพื่อให้หน่วยความเร็วเท่ากับผู้เล่น
    target_y = ball.y - right_paddle.height / 2
    
    # ตรวจสอบความแตกต่างในตำแหน่งระหว่าง paddle ของ AI และตำแหน่งที่ต้องการจะไป
    if abs(right_paddle.y - target_y) > player_vel:
        if right_paddle.y < target_y:
            right_paddle.move(up=False)  # ขยับลง
        elif right_paddle.y > target_y:
            right_paddle.move(up=True)  # ขยับขึ้น
    else:
        right_paddle.y = target_y  # ขยับตามตำแหน่งที่ต้องการ


def main():
    run = True
    clock = pygame.time.Clock()

    # สร้าง paddle สำหรับผู้เล่นทั้งสองข้างและลูกบอล
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    player_vel = left_paddle.VEL  # ใช้ความเร็วของผู้เล่นเป็นค่าเริ่มต้น

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_user_movement(keys, left_paddle)

        # ปรับความเร็วของ AI ให้เท่ากับความเร็วของผู้เล่น
        handle_ai_movement(ball, right_paddle, player_vel)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        # ตรวจสอบการชนของลูกบอลกับขอบกระดานและนับคะแนน
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        # ตรวจสอบการชนของลูกบอลกับกระดานและเมื่อมีผู้ชนะ
        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        # แสดงผลข้อความผู้ชนะและรีเซ็ตเกมเมื่อมีผู้ชนะ
        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == '__main__':
    main()
