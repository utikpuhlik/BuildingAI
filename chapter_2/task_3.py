def bot8(pbot, p8_bot, p8_human):
    # Find a probability for p_8:
    # Вероятность быть роботом * вероятность быть роботом с 8 числами + быть человеком * 8 чисел у человека
    p_8 = pbot * p8_bot + p8_human * (1 - pbot)
    print(f"Probability to have 8 digit in name is {round(p_8, 3)}")

    # Find a probability for pbot_8:
    # Вероятность быть роботом * вероятность быть роботом / общая вероятность иметь 8 чисел в никнейме
    pbot_8 = p8_bot * pbot / p_8
    print(pbot_8)


# you can change these values to test your program with different values
pbot = 0.1
p8_bot = 0.8
p8_human = 0.05

bot8(pbot, p8_bot, p8_human)
