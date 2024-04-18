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
    VEL = 5  # กำหนดความเร็วในการเคลื่อนที่ของ paddle

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

# ฟังก์ชันสำหรับการเคลื่อนไหวของ paddle ของ AI
def handle_ai_movement(ball, right_paddle):
    # สร้าง AI ที่เรียนรู้พร้อมผลทำสมดุล
    target_y = ball.y - right_paddle.height / 2  # คำนวณตำแหน่งที่ paddle ของ AI ควรจะเคลื่อนไปเพื่อชนะลูกบอล
    if abs(right_paddle.y - target_y) > right_paddle.VEL:  # ถ้าความต่างระหว่างตำแหน่งปัจจุบันของ paddle กับตำแหน่งเป้าหมายมากกว่าความเร็วสูงสุดของ paddle
        if right_paddle.y < target_y:  # ถ้าตำแหน่งปัจจุบันของ paddle ต่ำกว่าตำแหน่งเป้าหมาย
            right_paddle.move(up=False)  # เคลื่อน paddle ขึ้น
        elif right_paddle.y > target_y:  # ถ้าตำแหน่งปัจจุบันของ paddle สูงกว่าตำแหน่งเป้าหมาย
            right_paddle.move(up=True)  # เคลื่อน paddle ลง
    else:
        # หากความแตกต่างเล็กมาก เคลื่อนไปที่ตำแหน่งเป้าหมายโดยตรง
        right_paddle.y = target_y  # กำหนดตำแหน่งปัจจุบันของ paddle ให้เป็นตำแหน่งเป้าหมายโดยตรง

# ฟังก์ชันหลักสำหรับการเรียกใช้งานเกม
def main():
    run = True  # ตัวแปรเพื่อตรวจสอบว่าเกมยังคงทำงานหรือไม่
    clock = pygame.time.Clock()  # สร้างอ็อบเจกต์ Clock เพื่อควบคุม FPS ของเกม

    # สร้าง paddle ทั้งสองข้างและลูกบอล
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)  # สร้าง paddle ทางซ้าย
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)  # สร้าง paddle ทางขวา
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)  # สร้างลูกบอลตรงกลางหน้าต่าง


    left_score = 0  # คะแนนของผู้เล่นทางซ้าย
    right_score = 0  # คะแนนของผู้เล่นทางขวา

    while run:
        clock.tick(FPS)  # กำหนด FPS ของเกม

        # วาดส่วนต่าง ๆ ของเกมและแสดงคะแนน
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():  # วนลูปเหตุการณ์ที่เกิดขึ้นในเกม
            if event.type == pygame.QUIT:  # ถ้ามีการคลิกปุ่มปิดหน้าต่าง
                run = False  # หยุดการทำงานของเกม
                break  # ออกจากลูป

        keys = pygame.key.get_pressed()  # รับคีย์ที่กด
        handle_user_movement(keys, left_paddle)  # จัดการการเคลื่อนไหวของ paddle ของผู้ใช้
        handle_ai_movement(ball, right_paddle)  # จัดการการเคลื่อนไหวของ paddle ของ AI

        ball.move()  # ย้ายลูกบอล
        handle_collision(ball, left_paddle, right_paddle)  # ตรวจสอบการชนของลูกบอลกับ paddle

        if ball.x < 0:  # ถ้าลูกบอลชนขอบซ้ายของหน้าต่าง
            right_score += 1  # เพิ่มคะแนนของผู้เล่นทางขวา
            ball.reset()  # รีเซ็ตตำแหน่งลูกบอล
        elif ball.x > WIDTH:  # ถ้าลูกบอลชนขอบขวาของหน้าต่าง
            left_score += 1  # เพิ่มคะแนนของผู้เล่นทางซ้าย
            ball.reset()  # รีเซ็ตตำแหน่งลูกบอล

        won = False  # ตัวแปรเพื่อตรวจสอบว่ามีผู้ชนะหรือไม่
        if left_score >= WINNING_SCORE:  # ถ้าผู้เล่นทางซ้ายชนะ
            won = True  # มีผู้ชนะ
            win_text = "Left Player Won!"  # ข้อความที่แสดงว่าผู้เล่นทางซ้ายชนะ
        elif right_score >= WINNING_SCORE:  # ถ้าผู้เล่นทางขวาชนะ
            won = True  # มีผู้ชนะ
            win_text = "Right Player Won!"  # ข้อความที่แสดงว่าผู้เล่นทางขวาชนะ

        if won:  # ถ้ามีผู้ชนะ
            text = SCORE_FONT.render(win_text, 1, WHITE)  # สร้างข้อความที่จะแสดงผล
            WIN.blit(text, (WIDTH//2 - text.get_width() // 2, HEIGHT//2 - text.get_height()//2))  # แสดงข้อความ
            pygame.display.update()  # อัปเดตหน้าต่างเกม
            pygame.time.delay(5000)  # รอเวลาสักครู่
            ball.reset()  # รีเซ็ตตำแหน่งลูกบอล
            left_paddle.reset()  # รีเซ็ตตำแหน่ง paddle ทางซ้าย
            right_paddle.reset()  # รีเซ็ตตำแหน่ง paddle ทางขวา
            left_score = 0  # รีเซ็ตคะแนนของผู้เล่นทางซ้าย
            right_score = 0  # รีเซ็ตคะแนนของผู้เล่นทางขวา

    pygame.quit()  # ปิด pygame

if __name__ == '__main__':
    main()  # เรียกใช้ฟังก์ชันหลัก
