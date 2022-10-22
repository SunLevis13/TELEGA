from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import start_callback, navigation_callback

def get_item_inline_keyboard(item_index='0', status='Small') -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup(row_width=2)
    match status:
        case 'Big':
            index_left = str(int(item_index)-1)
            item_inline_keyboard.add(InlineKeyboardButton(text='<<<',
                                                          callback_data=navigation_callback.new(
                                                          for_data='items',
                                                         id=index_left)
            ))
        case 'Small':
            index_right = str(int(item_index)+1)
            item_inline_keyboard.add(InlineKeyboardButton(text='>>>',
                                                          callback_data=navigation_callback.new(
                                                          for_data='items',
                                                          id=index_right)
            ))
        case _:
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