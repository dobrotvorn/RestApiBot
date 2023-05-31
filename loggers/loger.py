def log(func):
    def _log_func(*args, **kwargs):
        try:
            print('начинаем логирование')
            message, *ostalnuye = args
            print(f" имя Юзера: {message.from_user.username}",
                  f" айдишник чата: {message.message_id}",
                  f" тип сообщения: {message.content_type}",
                  f" контент: {message.text}")
            print('заканчиваем логирование')

            func(*args, **kwargs)
        except:
            print('Логгер не работает')
    return _log_func


