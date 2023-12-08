import databases.db_dishes as dishes


def add_dish(dish_to_create):
    dishes.db_id += 1
    new_dish_id = dishes.db_id
    dish_to_create[0] = new_dish_id
    dishes.db_matrix.append(dish_to_create)


def list_dishes():
    return dishes.db_matrix


def actualize_dish(dish_to_update):
    database = list_dishes()
    list_index = dish_to_update[0] - 1
    for row in database:
        if row[0] == list_index:
            dishes.db_matrix[list_index] = dish_to_update
            break


def erase_dish(dish_id):
    database = list_dishes()

    for row in database:
        if row[0] == dish_id:
            dishes.db_matrix.remove(row)
            break
