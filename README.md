# Django_Service_Friends
# Регистрация пользователя
Используется для регистрации нового пользователя
POST /register/

Body: 
{"username":"username","password":"password"}

# Получение токена
Используется для дальнейшей работы 
/api-token/

Body: 
{"username":"username","password":"password"}
# Использование токена
Для того чтобы использовать токен, нужно добавить заголовок.
Authorization: Token <Ваш_токен>

