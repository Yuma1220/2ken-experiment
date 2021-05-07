import cv2
import pygame.mixer


deviceid = 0
cap = cv2.VideoCapture(deviceid)
max_time = 30 #持ち時間
teban = 0 #手番
count = 0 #手数

pygame.mixer.init() #初期化
pygame.mixer.music.load("秒読み.mp3") #読み込み

while True:
    if teban == 0:
        print("先手の番です。\n")
    else:
        print("後手の番です。\n")
    for t in range(max_time):
        print('残り{}秒'.format(max_time - t))
        if t == 11:
            pygame.mixer.music.play(1)
        ret, frame = cap.read()

        frame = cv2.line(frame, (630, 50), (650, 50), (0, 0, 255), 2)
        frame = cv2.line(frame, (640, 40), (640, 60), (0, 0, 255), 2)

        frame = cv2.line(frame, (620, 410), (640, 410), (0, 0, 255), 2)
        frame = cv2.line(frame, (630, 400), (630, 420), (0, 0, 255), 2)

        frame = cv2.line(frame, (895, 400), (915, 400), (0, 0, 255), 2)
        frame = cv2.line(frame, (905, 390), (905, 410), (0, 0, 255), 2)

        frame = cv2.line(frame, (885, 40), (905, 40), (0, 0, 255), 2)
        frame = cv2.line(frame, (895, 30), (895, 50), (0, 0, 255), 2)

        frame = cv2.line(frame, (1050, 30), (1070, 30), (0, 0, 255), 2)
        frame = cv2.line(frame, (1060, 20), (1060, 40), (0, 0, 255), 2)

        frame = cv2.line(frame, (1295, 30), (1315, 30), (0, 0, 255), 2)
        frame = cv2.line(frame, (1305, 20), (1305, 40), (0, 0, 255), 2)

        frame = cv2.line(frame, (1070, 390), (1090, 390), (0, 0, 255), 2)
        frame = cv2.line(frame, (1080, 380), (1080, 400), (0, 0, 255), 2)

        frame = cv2.line(frame, (1340, 390), (1360, 390), (0, 0, 255), 2)
        frame = cv2.line(frame, (1350, 380), (1350, 400), (0, 0, 255), 2)

        frame = cv2.line(frame, (660, 530), (680, 530), (0, 0, 255), 2)
        frame = cv2.line(frame, (670, 520), (670, 540), (0, 0, 255), 2)

        frame = cv2.line(frame, (1333, 510), (1353, 510), (0, 0, 255), 2)
        frame = cv2.line(frame, (1343, 500), (1343, 520), (0, 0, 255), 2)

        frame = cv2.line(frame, (648, 1055), (668, 1055), (0, 0, 255), 2)
        frame = cv2.line(frame, (658, 1045), (658, 1065), (0, 0, 255), 2)

        frame = cv2.line(frame, (1390, 1040), (1410, 1040), (0, 0, 255), 2)
        frame = cv2.line(frame, (1400, 1030), (1400, 1050), (0, 0, 255), 2)

        cv2.imshow("camera", frame)
        # キー入力を待つ
        k = cv2.waitKey(1000) & 0xff
        if k == 13:
            # Enterキーで画像を保存
            count = count + 1
            name = "img" + str(count) + ".png"
            cv2.imwrite(name, frame) # ファイル保存
            print("\n")
            teban = 1 - teban
            pygame.mixer.music.stop()
            break
        elif k == ord('q'):
            # 「q」キーが押されたら終了する
            exit()
