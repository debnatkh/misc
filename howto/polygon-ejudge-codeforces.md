## Заливка задач на полигон из собранного в polygon архива

**На Linux:**

0. Установить [polygon-cli](https://github.com/kunyavskiy/polygon-cli) как сказано в репозитории. 
После этого команда `polygon-cli` должна работать из терминала. Если не работает, можно сделать 
`alias polygon-cli="<path-to-polygon-cli.run.py>""`
1. Скачать polygon-пакет, например, с [neerc.ifmo.ru/school/archive/...](neerc.ifmo.ru/school)
2. Разархивировать этот пакет в какую-нибудь папку
3. Создать задачу, в которую вы будете заливать на своём полигоне, например, `stolen-problem`, 
начать её редактирование а полигоне (кнопка Start)
4. В папке с распакованной задачей (там ещё должен лежать `problem.xml`) выполнить `polygon-cli
init stolen-problem`. При первом запуске `polygon-cli` потребует API-ключи и логин-пароль от полигона. 
Первое можно получить в настройках полигона
5. В папке с распакованной задачей выполнить `polygon-cli import_package .`
6. Теперь задачу можно продолжить редактировать/закоммитить/собрать из интерфейса полигона.

**На Windows:**

Вроде должно работать то же самое, но мной это не проверялось
