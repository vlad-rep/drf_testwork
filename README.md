# Тестовое задание

Задача: спроектировать и разработать API для системы опросов пользователей

## Requirements

* python-3.7.9
* Django==2.2
* djangorestframework==3.12.2
* pytz==2020.5
* sqlparse==0.4.1

## Installation guide

  ```
  pip install -r requirements.txt
  
  cd api_testwork
    
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
 
  python manage.py runserver
  ```

## API documentation

### To get user token:

* Request method: GET
* URL: http://localhost:8000/api/users/
* Body:
    * username:
    * password:
* Example:

```
curl --request GET 'http://localhost:8000/api/users/' \
--form 'username=%username' \
--form 'password=%password'
```

### To create poll:

* Request method: POST
* URL: http://localhost:8000/api/polls/
* Header:
    * Authorization: Token userToken
* Body:
    * poll_name: name of poll
    * start_date: publication date can be set only when poll is created, format: YYYY-MM-DD HH:MM:SS
    * end_date: poll end date, format: YYYY-MM-DD HH:MM:SS
    * Poll_description: description of poll
* Example:

```
curl --request POST 'http://localhost:8000/api/polls/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### To update poll:

* Request method: PATCH
* URL: http://localhost:8000/api/polls/[poll_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id
* Body:
    * poll_name: name of poll
    * end_date: poll end date, format: YYYY-MM-DD HH:MM:SS
    * Poll_description: description of poll
* Example:

```
curl --request PATCH 'http://localhost:8000/api/polls/[poll_id]/' \
--form 'poll_name=%poll_name' \
--form 'end_date=%end_date \
--form 'poll_description=%poll_description'
```

### To delete poll:

* Request method: DELETE
* URL: http://localhost:8000/api/polls/[poll_id]
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id Example:

```
curl--request DELETE 'http://localhost:8000/api/polls/[poll_id]/' \
```

### To view all polls:

* Request method: GET
* URL: http://localhost:8000/api/polls/
* Header:
    * Authorization: Token userToken
* Example:

```
curl --request GET 'http://localhost:8000/api/polls/' \
```


* Request method: GET
* URL: http://localhost:8000/api/polls/active
* Header:
    * Authorization: Token userToken
* Example:

```
curl --request GET 'http://localhost:8000/api/polls/active/' \
--header 'Authorization: Token %userToken'
```

### To create question:

* Request method: POST
* URL: http://localhost:8000/api/questions/
* Body:
    * poll: id of poll
    * question_text:
    * question_type: can be only `one_choice`, `multiple_choices` or `text`
* Example:

```
curl --request POST 'http://localhost:8000/api/questions/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### To update question:

* Request method: PATCH
* URL: http://localhost:8000/api/questions/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Body:
    * poll: id of poll
    * question_text: question
    * question_type: can be only `one_choice`, `multiple_choices` or `text`
* Example:

```
curl --request PATCH 'http://localhost:8000/api/questions/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### To delete question:

* Request method: DELETE
* URL: http://localhost:8000/api/questions/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Example:

```
curl --request DELETE 'http://localhost:8000/api/questions/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### To create choice:

* Request method: POST
* URL: http://localhost:8000/api/choices/
* Header:
    * Authorization: Token userToken
* Body:
    * question: id of question
    * choice_text: choice
* Example:

```
curl --request POST 'http://localhost:8000/api/choices/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### To update choice:

* Request method: PATCH
* URL: http://localhost:8000/api/choices/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Body:
    * question: id of question
    * choice_text: choice
* Example:

```
curl --request PATCH 'http://localhost:8000/api/choices/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### To delete choice:

* Request method: DELETE
* URL: http://localhost:8000/api/choices/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Example:

```
curl --request DELETE 'http://localhost:8000/api/choices/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### To create answer:

* Request method: POST
* URL: http://localhost:8000/api/answers/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll
    * question: id of question
    * choice: if question type is one_choice or multiple_choices then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:

```
curl --request POST 'http://localhost:8000/api/answers/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### To update answer:

* Request method: PATCH
* URL: http://localhost:8000/api/answers/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * poll: id of poll
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:

```
curl --request PATCH 'http://localhost:8000/api/answers/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### To delete answer:

* Request method: DELETE
* URL: http://localhost:8000/api/answers/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:

```
curl --request DELETE 'http://localhost:8000/api/answers/[answer_id]' \
--header 'Authorization: Token %userToken'
```

### To view answers of user:

* Request method: GET
* URL: http://localhost:8000/api/answers/view/[user_id]/
* Param:
    * user_id
* Header:
    * Authorization: Token userToken
* Example:

```
curl --request GET 'http://localhost:8000/api/answers/view/[user_id]' \
--header 'Authorization: Token %userToken'
```

