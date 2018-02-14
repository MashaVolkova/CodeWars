def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15 * human_years
        dog_years = 15 * human_years
        new_array = [human_years, cat_years, dog_years]
    if human_years == 2:
        cat_years = 9 * (human_years - 1) + 15
        dog_years = 9 * (human_years - 1) + 15
        new_array = [human_years, cat_years, dog_years]
    if human_years > 2:
        cat_years = 4 * (human_years - 2) + 15 + 9
        dog_years = 5 * (human_years - 2) + 15 + 9
        new_array = [human_years, cat_years, dog_years]
    return new_array
