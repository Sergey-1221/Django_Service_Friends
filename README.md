# Django_Service_Friends
# Регистрация пользователя
Используется для регистрации нового пользователя

POST /register/

Body: 

{"username":"username","password":"password"}

# Получение токена
Используется для дальнейшей работы 

POST /api-token/

Body: 

{"username":"username","password":"password"}

# Использование токена
Для того чтобы использовать токен, нужно добавить заголовок.

Authorization: Token <Ваш_токен>

# Список друзей
Посмотреть пользователю список своих друзей (Необходима авторизация по токену)

GET /friend/

# Cписок исходящих заявок в друзья
Посмотреть пользователю список своих исходящих заявок в друзья (Необходима авторизация по токену)

GET /friend-request/sender/

# Cписок входящих заявок в друзья
Посмотреть пользователю список своих входящих заявок в друзья (Необходима авторизация по токену)

GET /friend-request/receive/

# Принять пользователю заявку в друзья
Принять пользователю заявку в друзья от другого пользователя (Необходима авторизация по токену)

GET friend-request/accept/?type=id&id=<id_user> 

GET friend-request/accept/?type=name&name=<name_user>

# Отклонить пользователю заявку в друзья
Отклонить пользователю заявку в друзья от другого пользователя (Необходима авторизация по токену)

GET friend-request/cancel/?type=id&id=<id_user> 

GET friend-request/cancel/?type=name&name=<name_user>

# Отклонить пользователю заявку в друзья
Отклонить пользователю заявку в друзья от другого пользователя (Необходима авторизация по токену)

GET friend-request/cancel/?type=id&id=<id_user> 

GET friend-request/cancel/?type=name&name=<name_user>

# Отправить заявку в друзья
Отправить одному пользователю заявку в друзья другому (Необходима авторизация по токену)

GET friend-request/send/?type=id&id=<id_user> 

GET friend-request/send/?type=name&name=<name_user>

*если пользователь1 отправляет заявку в друзья пользователю2, а пользователь2 отправляет заявку пользователю1, то они автоматом становятся друзьями, их заявки автоматом принимаются

# Удалить пользователя из своих друзей
Удалить пользователю другого пользователя из своих друзей (Необходима авторизация по токену)

GET friend/delete/?type=id&id=<id_user> 

GET friend/delete/?type=name&name=<name_user>

# Получить статус дружбы с другим пользователем
Получить пользователю статус дружбы с каким-то другим пользователем (Необходима авторизация по токену)

GET friend/status/?type=id&id=<id_user>

GET friend/status/?type=name&name=<name_user>








