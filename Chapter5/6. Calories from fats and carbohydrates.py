def main():
    fat_grams = int(input("Enter the grams of the fat:"))
    carbogydrates_grams = int(input("Enter the grams of the carbohydrates:"))
    cal_fron_fats(fat_grams)
    cal_from_carbohydrates(carbogydrates_grams)



def cal_fron_fats(fat_grams):
    calories = fat_grams * 9
    print("The number of calories from fats are ",calories)


def cal_from_carbohydrates(carbohydrates_grams):
    calories = carbohydrates_grams * 4
    print("The number of calories from carbohydrates are ", calories)


main()
