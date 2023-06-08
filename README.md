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
______________________________________________________________________________________

### Ajax Systems, Python developer in test for Application team
Для выполнения тестового задания Вам нужно установить приложение Ajax Systems на телефон (если у вас нет реального андроид устройства то вы можете использовать эмулятор).

### Задание
1) Написать базовый функционал для работы с приложением (поиск элемента, клик элемента и тд).
2) Написать тест логина пользователя в приложение (позитивный и негативные кейсы).
3) Использовать параметризацию.
4) Закомитить выполненное задание на гитхаб.

### Дополнительное задание (опционально)
1) *Реализовать логирование теста.
2) *Реализовать динамическое определение udid телефона через subprocess
3) **Написать на проверку элементов SideBar (выезжающее меню слева).

### Полезные ссылки
1) Приложение - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Работа с реальным телефоном - https://developer.android.com/studio/command-line/adb
3) Настройка эмулятора - https://developer.android.com/studio/run/emulator
4) Настройка аппиума - 
5) Инспектор приложения - https://appium.io/docs/en/drivers/android-uiautomator2/

### Login credentials
login - qa.ajax.app.automation@gmail.com
password - qa_automation_password
# ajax_app_test
