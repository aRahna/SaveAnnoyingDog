# SaveAnnoyingDog
![Doge](https://raw.githubusercontent.com/aRahna/SaveAnnoyingDog/main/gif_help.gif)
### Описание
Игра по мотивам классической "виселицы". Цель - угадать* слово по буквам, но количество попыток ограничено.
***
### Что хотелось бы реализовать
- Большой список доступных слов (из-за этого, правда, деление слов по темам весьма затруднительно).
- Возможность выбрать режим игры - сложность или длину слова, чтобы игрок знал, на что идет.
- Подсказки, например в "Кто хочет стать миллионером" хорошая идея "50/50".
- Чтобы после завершения игры не приходилось ее закрывать, чтобы сыграть еще раз.
- Приемлемый дизайн, для этого надо лучше разобраться в среде разработки графики.
- Возможность прервать игру и выбрать режим заново.
- Было бы забавным добавить и другие языки, хотя бы английский.
***
### Техническое описание
- Для вызуализации был использован модуль [PyQt5](https://pypi.org/project/PyQt5/), а также среда [QtDesigner](https://doc.qt.io/qt-5/qtdesigner-manual.html).
- Список русских слов был взят из [словаря «Толковый словарь Ефремовой»](http://blog.harrix.org/article/3334), 51301 существительных; список английских слов был взят из [The Great Noun List](http://www.desiquintans.com/nounlist), 6699 слов после чистки (слова с тире/опострофами не подходят).
- Для работы с фоном и островом (и гифкой) использовалась программа [Aseprite](https://www.aseprite.org).
***
### Примерный план, которого я придерживалась
1. Написать основной код (висельник.py) виселицы, который генерировал бы слово, получал букву и выводил текущей прогресс и кол-во попыток в консоль.
2. Разобраться в интерфейсе и тонкостях QtDesigner (кто же знал, что картинку добавляют через элемент "текстовое поле").
3. Создать в QtDesigner внешнюю оболочку, внешний вид окна, в котором имелись бы элементарные функции, например исчезновение клавиши после ее нажатия.
4. Почистить код, так как он был создан автоматически и имел много лишнего.
5. Дописать функционал клавиш, которые уже частично разметил QtDesigner, интегрировать код игры.
6. Понять, что нужны костыли и замаскировать их, добавить ограничения на действия игрока, чтобы. например, во время выбора сложности игрок не мог уже сразу начать выбирать буквы/подсказки.
7. Придуть как реализовать остальной функционал - обновление прогресса (слово, жизни, сложность), добавление всплывающего окна с подсказкой, возможность начать игру заново после выигрыша/проигрыша или закончить ее.
***
### Как запустить?

Для работы необходимо установить модуль PyQt5 через командную строку:
 > pip install PyQt5

А также скачать папку с необходимыми изоражениеми и файлами для корректной работы, там запустить файл Save_dog.ру. В файле висельник.ру исходный код, с помощью которого можно играть в самой среде для Python.

**игра автоматически напечатает слово в консоли, чтобы убрать - удалите 548 строку кода.*
