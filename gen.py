# Welcome to the simple captcha gen by R8QE! The max you want to make your captchas is 8 digits and lowest is 6!
import random
import string
import os
from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280, height=90)

def generate_captcha_text():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_captchas(limit):
    os.makedirs("captchas", exist_ok=True)
    existing_captchas = set(os.listdir("captchas"))
    count = 0

    while limit == 0 or count < limit:
        captcha_text = generate_captcha_text()
        file_name = f"{captcha_text}.png"

        if file_name in existing_captchas:
            continue

        full_path = os.path.join("captchas", file_name)
        print(f"Generating CAPTCHA: {captcha_text}")
        image.write(captcha_text, full_path)
        existing_captchas.add(file_name)
        count += 1
        print(f"Generated: {count}")

if __name__ == "__main__":
    try:
        limit = int(input("How many do you want to gen? "))
        input("Press Enter to start generating CAPTCHAs...")
        generate_captchas(limit)
    except ValueError:
        print("Invalid input. Please enter a number.")