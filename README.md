# Квантовый протокол Беннета (BB84)

Здесь представлен вариант программной реализации алгоритма распределения секретного ключа, используя квантовый протокол Беннета.
Программа имеет интерфейс пользователя. Интерфейс написан с помощью Tkinter.

## Очень кратко про протокол

Есть Алиса и Боб, которые хотят согласовать секретный ключ. В этом им может помешать Ева. Для передачи информации используются фотоны света, поляризованные по определенным правилам. Ссылки на правила приведены в источниках.

## Информация по проекту

* "model.py" - основная логика, где выполняются вызовы отображаемых окнон. Главный файл.
* "dialog.py" - логика отображаемых окон.

Для запуска программы необходим интерпретатор Python (использовался Python 3).
Программа выводит в консоли всю информацию, часть которой просто дублируется в интерфейс.

## Инструкция по применению

1. Выбирается точность извлечения бита из фотона.

![Точность приема фотона](https://github.com/iIyaPopov/bennett-protocol/blob/master/images/img1.png)

2. Выбирается количество "посылаемых" фотонов (в данной реализации от 0 до 100).

![Количество фотонов](https://github.com/iIyaPopov/bennett-protocol/blob/master/images/img2.png)

3. Выбираются режимы работы для Алисы, Евы и Боба

![Режимы работы](https://github.com/iIyaPopov/bennett-protocol/blob/master/images/img3.png)

***Алиса: Автоматический, ручной. Режимы посылки фотонов.***
Для выбора ручного режима для Алисы необходимо указать фотон и базис, через который Алиса будет извлекать бит.

![Выбор Алисы](https://github.com/iIyaPopov/bennett-protocol/blob/master/images/img4.png)

***Боб: Автоматический, ручной. Режимы перехвата фотонов.***
Для выбора ручного режима для Боба необходимо указать базис, через который Боб будет извлекать бит.

![Выбор Боба](https://github.com/iIyaPopov/bennett-protocol/blob/master/images/img5.png)

***Ева: не работает, Автоматический, ручной. Режимы перехвата фотонов.***
Действия Евы аналогичны действиям Боба.

4. Запуск симулятора.

5. Выводится информация: посланные и перехваченные фотоны, выбранные базисы, получившийся ключ.

![Точность приема фотона](https://github.com/iIyaPopov/bennett-protocol/blob/master/images/img7.png)

6. Если удалось передать более 8 бит, можно зашифровать текст.

![Ввод сообщения для шифрования](https://github.com/iIyaPopov/bennett-protocol/blob/master/images/img6.png)


## Список литературы:
* Википедия: <https://ru.wikipedia.org/wiki/BB84>
* Статья на хабре: <https://habr.com/ru/post/333952/>
