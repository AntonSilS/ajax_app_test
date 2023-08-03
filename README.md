Для тестування був вибраний девайс з Andriod studio: Pixel_3a_API_33_x86_64.
!!! Цей код написаний під Pixel_3a_API_33_x86_64 з andriod 13.0 Tiramisu.

Необхідні кроки для перевірки завдання:
1. Встановіть pipenv
2. Створіть новие віртуальне оточення за домогою pipenv python --3.10
3. Активуйте оточення pipenv shell
4. Встановіть усі залженості за допомогою pipenv install
5. Встановіть Andriod studio. Створіть емулятор Pixel_3a_API_33_x86_64 з andriod 13.0 Tiramisu
6. Запустіть емулятор
7. З корневої пакпи пропишіть команду в терміналі pytest
- Зроблено динамічне визначення udid телефону через subprocess
- Додаток ajax.system встановлюється автоматично на емулятор з папки appium_ajax_apk
!!! На гіт не вдалось загрузити цей файл, тому треба скачати його по https://drive.google.com/drive/folders/16rOBYr1qheHzPgCyj0XD3Lv7DDCKhIxA?usp=sharing
та покласти в корінь разом з папкою appium_ajax_apk, так як логіка програми працює таким чином.

