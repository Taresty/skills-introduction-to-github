import random


def play_game():
    target = random.randint(1, 100)
    attempts = 0
    print("猜数字游戏！请输入 1 到 100 之间的数字。")
    while True:
        guess = input("你的猜测: ")
        try:
            guess_int = int(guess)
        except ValueError:
            print("请输入有效的数字！")
            continue

        attempts += 1
        if guess_int < target:
            print("太小了，再试一次。")
        elif guess_int > target:
            print("太大了，再试一次。")
        else:
            print(f"恭喜你，猜对了！答案就是 {target}。你一共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    play_game()
