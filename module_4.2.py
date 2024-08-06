def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()        #здесь ничего не возвращает

#inner_function()  # ЗДЕСЬ НЕ РАБОТАЕТ! (ошибка)
# Вызов функци inner_function() вне функции test_function приводит к появлению ошибки -
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# вследствие различия пространства имён

test_function()     # Здесь работает!!!