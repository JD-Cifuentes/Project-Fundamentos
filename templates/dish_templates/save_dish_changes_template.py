from tkinter import *
from tkinter import ttk
import re
import utils.template_handler
import databases.db_dishes as db_dishes


global dish_name
global dish_price
global dish_description
global dish_availability

dish_name = ''
dish_price = ''
dish_description = ''
dish_availability = ''

def save_process(dynamic_frame, dish_to_update):
    global dish_name
    global dish_price
    global dish_description
    global dish_availability

    dish_to_update[1] = dish_name
    dish_to_update[2] = dish_price
    dish_to_update[3] = dish_description
    dish_to_update[4] = dish_availability
    list_index = dish_to_update[0]-1
    #!!!!!!!!!!!!!!!!!!llamar backend
    db_dishes.db_matrix[list_index] = dish_to_update
    utils.template_handler.templ_handler('update_dish', dynamic_frame)

def catch_dish_name(var):
    if len(var)>25:
        return False
    global dish_name
    dish_name = var
    return True

def catch_dish_price(var):  
    pattern = r'\d*'
    if re.fullmatch(pattern, var) is None or len(var)>6:
        return False
    global dish_price
    dish_price = var
    return True

def catch_dish_description(var):
    if len(var)>50:
        return False
    global dish_description
    dish_description = var
    return True

def catch_dish_availability(event):
    global dish_availability
    dish_availability = event.widget.get()
    return True

def save_dish_changes_template(dynamic_frame, dish_to_update):
    utils.template_handler.destroy_widgets(dynamic_frame)
    global dish_name
    global dish_price
    global dish_description
    global dish_availability

    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame,
                          text="Guardar cambios - plato",
                          font=("default",12, "bold"))
    lbl_dish_name = ttk.Label(dynamic_frame,
                              text="Nombre")
    lbl_dish_price = ttk.Label(dynamic_frame,
                               text="Precio")
    lbl_dish_description = ttk.Label(dynamic_frame,
                                     text="Descripción")
    lbl_dish_availability = ttk.Label(dynamic_frame,
                                      text="Disponibilidad")

    
    entry_dish_name = ttk.Entry(dynamic_frame,
                                width=entry_box_width,
                                validate="key", 
                                validatecommand=(dynamic_frame.register(catch_dish_name), '%P'))
    entry_dish_price = ttk.Entry(dynamic_frame,
                                 width=entry_box_width,
                                 validate="key", 
                                 validatecommand=(dynamic_frame.register(catch_dish_price), '%P'))
    entry_dish_description = ttk.Entry(dynamic_frame,
                                       width=entry_box_width, 
                                       validate="key", 
                                       validatecommand=(dynamic_frame.register(catch_dish_description), '%P'))
    
    options = ['Si', 'No']
    combobox_dish_availability =ttk.Combobox(dynamic_frame,
                                          width=(entry_box_width-3),
                                          values=options)
    combobox_dish_availability.bind("<<ComboboxSelected>>", catch_dish_availability)

    entry_dish_name.insert(0, dish_to_update[1])
    entry_dish_price.insert(0, dish_to_update[2])
    entry_dish_description.insert(0, dish_to_update[3])
    combobox_dish_availability.insert(0, dish_to_update[4])

    dish_name = dish_to_update[1]
    dish_price = dish_to_update[2]
    dish_description = dish_to_update[3]
    dish_availability = dish_to_update[4]
    
    button_add = ttk.Button(
        dynamic_frame,
        text="Guardar",
        style="Accent.TButton",
        command=lambda dynamic_frame=dynamic_frame, dish_to_update=dish_to_update: save_process(dynamic_frame, dish_to_update)) 

    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'update_dish', frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_dish_name.grid(column=0, row=1, sticky="w", padx=(20,0), pady=2)
    entry_dish_name.grid(column=0, row=2, padx=(20,10), pady=2)
    lbl_dish_price.grid(column=1, row=1, sticky="w", padx=(10,0), pady=2)
    entry_dish_price.grid(column=1, row=2, padx=(10,20), pady=2)
    lbl_dish_description.grid(column=0, row=3, sticky="w", padx=(20,0), pady=2)
    entry_dish_description.grid(column=0, row=4, padx=(20,10), pady=2)
    lbl_dish_availability.grid(column=1, row=3, sticky="w", padx=(10,0), pady=2)
    combobox_dish_availability.grid(column=1, row=4, padx=(10,20), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0,10), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(10,0), pady=15)