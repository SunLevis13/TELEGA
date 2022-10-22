from aiogram.utils.callback_data import CallbackData

start_callback = CallbackData('start') # создали экземпляр класса CallbackData, через него зашиваем данные - создаем заголовок start

navigation_callback = CallbackData('navigation_btn','for_data','id') # создаем класс с полями. Поле for_data, чтолбы понимать для какой табл. из нашей базы данных мы создаем навигацию
