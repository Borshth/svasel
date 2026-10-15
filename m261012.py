import cv2
import numpy as np


def main():
    # Загружаем исходное изображение
    img = cv2.imread('img.jpg')

    if img is None:
        print("Ошибка: не удалось загрузить imp.jpg")
        return

    # OpenCV загружает изображения в формате BGR
    # Разделяем на каналы
    b, g, r = cv2.split(img)

    # Создаём изображение с порядком каналов BRG
    # Исходный RGB -> BRG: меняем местами R и G (в терминах BGR: B, R, G)
    img_brg = cv2.merge([r, b, g])
    cv2.imwrite('p1.jpg', img_brg)
    print("Сохранено p1.jpg (BRG)")

    # Создаём изображение с порядком каналов GBR
    # Исходный RGB -> GBR: циклический сдвиг
    img_gbr = cv2.merge([g, r, b])
    cv2.imwrite('p2.jpg', img_gbr)
    print("Сохранено p2.jpg (GBR)")


if __name__ == '__main__':
    main()