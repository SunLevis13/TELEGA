from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import start_callback, navigation_callback

# ПРОПИСЫВАЕМ клавиатуру для items (кнопки пролистывания)
def get_item_inline_keyboard(item_index='0', status='Small') -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup(row_width=2) # кладем в перемеменную созданную клавиатуру по экземпляру класса
    match status:
        case 'Big': # статус Big означает, что не выводим кнопку "вправо"
            index_left = str(int(item_index)-1) # если мы находимся на крайней правой границе, прописываем индекс левого эл-та, чтобы у нас был индекс товара, инф-ю о котором надо будет вывести - нужно знать индекс, чтобы знать какую инфу показать клиенту
            btn = InlineKeyboardButton(text='<<<', # СОЗДАЁМ КНОПКУ через метод add - добавляем кнопку
                                                          callback_data=navigation_callback.new(
                                                          for_data='items', # указываем, что именно для этой кнопки присвоено значение items под индексом ниже
                                                         id=index_left) # указываем индекс того товара, по которому надо вывести инфу
            )
            item_inline_keyboard.add()
            
        case 'Small': # статус Small означает, что не выводим кнопку "влево"
            index_right = str(int(item_index)+1)
            item_inline_keyboard.add(InlineKeyboardButton(text='>>>',
                                                          callback_data=navigation_callback.new(
                                                          for_data='items', # указываем, что именно для этой кнопки присвоено значение items под индексом ниже
                                                          id=index_right)
            ))
        case _: # любой другой статус сигнализирует, что можно выводить обе две кнопки "влево" и "вправо"
            index_left = str(int(item_index)-1)
            index_right = str(int(item_index)+1)
            item_inline_keyboard.add(InlineKeyboardButton(text='<<<',
                                                          callback_data=navigation_callback.new(
                                                          for_data='items',
                                                         id=index_left)))
            item_inline_keyboard.add(InlineKeyboardButton(text='>>>',
                                                          callback_data=navigation_callback.new(
                                                          for_data='items',
                                                          id=index_right)))
    return get_item_inline_keyboard

start_inline_keyboard = InlineKeyboardMarkup(row_width=1, # ширина строки - измеряется в количестве кнопок
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text='Главное меню', # создаем клавиатуру по аналогии с обычной клавой, также список = одстрока кнопок
                                                                        callback_data=start_callback.new()) # помещаем сюда наш заголовок из файла callback_data.py
                                                ]
                                            ])