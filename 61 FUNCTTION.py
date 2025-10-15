def greet():
    print("HELLO ")
    print("HOW DO YOU DO")
    print("Is n't the weather nice?")

def greet_with_name(NAME):
    print(f"HELLO {NAME}")
    print(f"HOW DO YOU DO {NAME}")

greet_with_name("kiran")


def life_in_weeks(age):
    # total years we assume to live
    total_years = 90

    # calculate remaining years
    years_left = total_years - age

    # 1 year = 52 weeks
    weeks_left = years_left * 52

    # output message using f-string
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(89)