from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font


# объявляем список ИД добавляемых картинок, и список самих картинок
images_id_list = []
photo_images_list = []


# Функция загрузки изображений из файла
def load_image(image_x=200, image_y=200):
    global images_id_list, photo_images_list
    file_name = filedialog.askopenfile()
    if file_name:
        print("имя файла:", file_name.name)
        photo_image = PhotoImage(file=file_name.name)
        photo_images_list.append(photo_image)
        image = canvas.create_image(image_x, image_y, image=photo_image)
        images_id_list.append(image)
        return image
    else:
        return 0

# Функция очистки холста
def erase_all():
    print('Очистка холста')
    canvas.delete('all')

# GUI
root = Tk()
root.geometry('600x400')
root.title('Рисовалка')

canvas = Canvas(root, bg='black')
canvas.place(relx=0, rely=0,
             relheight=1, relwidth=0.7)

fr1 = Frame(root, bd=3, relief=GROOVE)
fr1.place(relx=0.7, rely=0,
          relheight=1, relwidth=0.3)

fr1_1 = Frame(fr1, bd=3, relief=GROOVE)
fr1_1.place(relx=0, rely=0,
            relheight=0.5, relwidth=1)

fr1_2 = Frame(fr1, bd=3, relief=GROOVE)
fr1_2.place(relx=0, rely=0.5,
            relheight=0.5, relwidth=1)

btn_1 = Button(fr1_1, text=1)
btn_1.place(relx=0, rely=0,
            relheight=0.5, relwidth=0.5)

btn_2 = Button(fr1_1, text=2)
btn_2.place(relx=0.5, rely=0,
            relheight=0.5, relwidth=0.5)

btn_3 = Button(fr1_1, text=3)
btn_3.place(relx=0, rely=0.5,
            relheight=0.5, relwidth=0.5)

btn_4 = Button(fr1_1, text=4)
btn_4.place(relx=0.5, rely=0.5,
            relheight=0.5, relwidth=0.5)


btn2_1 = Button(fr1_2, text="Фон",)
btn2_1.place(relx=0, rely=0,
            relheight=0.25, relwidth=1)
btn2_2 = Button(fr1_2, text="Очистить", command=erase_all)
btn2_2.place(relx=0, rely=0.25,
            relheight=0.25, relwidth=1)
btn2_3 = Button(fr1_2, text="Рисунок", command=load_image)
btn2_3.place(relx=0, rely=0.5,
            relheight=0.25, relwidth=1)
btn2_4 = Button(fr1_2, text="Сохранить",)
btn2_4.place(relx=0, rely=0.75,
            relheight=0.25, relwidth=1)

root.mainloop()
