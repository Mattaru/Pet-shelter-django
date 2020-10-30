# Pet shelter
Проект уже готов для деплоя на Heroku. Вам потребуется выполнить всего пару простых шагов:
1. Клонируйте репозиторий командой `git clone`
1. Зайдите под своим логином на **heroku** и создать новый проект.
1. Добавте postgres в **heroku resources**:
   + Зайдите в раздел **resources**
   + Нажмите **find mor add-ons**
   + В разделе **Data stores** найдите **Heroku Postgres**
   + Добавьте его к своему проекту
1. В разделе **settings**:
   + В разделе **Config vars** нажмите  **Reveal Config vars**
   + В свободную левую колонку добавьте переменную **SECRET_KEY**, а в праую значение ключа из **animal_shelter/settings.py**
   + Добавьте эти настройки и сохраните.
1. Откройте **animal_shelter/settings.py** и в переменную **ALLOWED_HOSTS** добавьте линк своего проекта.
1. Отключите автоматическую загрузку статики `heroku config:set DISABLE_COLLECTSTATIC=1`
1. Сделайте `git commit`
1. Выполните `git push heroku master`
1. Загрузите фикстуры `heroku run python manage.py loaddata myfixtures.json`
1. Соберите статику без дополнительных настроек `heroku run python manage.py collectstatic --noinput`
##### Ниже ссылка на рабочий проект:
##### Heroku link https://fathomless-lake-87191.herokuapp.com/
