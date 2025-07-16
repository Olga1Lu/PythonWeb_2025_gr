# базовый синтаксис
```
SELECT перечень_полей (*)
FROM имя_таблицы
WHERE условие
```
# выборка по году выпуска
```
SELECT * 
FROM films
WHERE year = 2010
```

# выборка названия по году выпуска
```
SELECT title
FROM films
WHERE year = 2010
```

# выборка названия и года выпуска в диапазоне с сортировкой по году выпуска
```
SELECT title, year
FROM films
WHERE year > 2005  
AND year < 2010
AND duration < 90
ORDER BY year
```
# выборка названия и года выпуска в диапазоне (используя BETWEEN - ВКЛЮЧАЯ ГРАНИЦЫ) с сортировкой по году выпуска
```
SELECT title, year
FROM films
WHERE year BETWEEN 2005 AND 2010
AND duration < 90
ORDER BY year
```
#######################################
# пример не совсем корр. запроса
```
SELECT title
FROM films
WHERE genre = 8
```

# исправленный составной запрос
```


```

# выборка по перечню значений с сортировкой по убыванию (в обратном порядке)
```
SELECT title, duration FROM films
WHERE duration IN (45, 60, 90)
ORDER BY duration DESC
```

# выборка с группировкой по ID
```
SELECT * FROM films
WHERE year >= 2001
AND duration BETWEEN 45 AND 90
ORDER BY id
```

# оператор  LIKE, "%"-любое кол-во символов, "_"-любой символ
```
SELECT title FROM films
WHERE title LIKE 'А_к%'
```

# оператор  ILIKE - непохоже на... (не работает в SQLite)
```
SELECT title FROM films
WHERE title LIKE 'А_к%'
```

# оператор  NOT LIKE - непохоже на... 
```
SELECT title FROM films
WHERE title NOT LIKE 'А_к%'
```

# вывод без повторов
```
SELECT DISTINCT year FROM films
```

# выборка с объединением двух и вывод в два столбца с названиями столбцов
```
SELECT 
films.title as Фильм, 
genres.title as Жанр
FROM films JOIN genres WHERE films.genre = genres.id

```

# выборка с объединением двух таблиц и вывод в два столбца с названиями столбцов
```
SELECT 
films.title as Фильм, 
genres.title as Жанр
FROM films, genres WHERE films.genre = genres.id

```

# выборка сколько фильмов каждого года в базе данных
```
SELECT year, count(*) as Кол_во
FROM films
GROUP BY year
ORDER BY Кол_во DESC

```

# выборка сколько фильмов каждого года в базе данных, взять только те года, где фильмов более 500
```
SELECT year, count(*) as Кол_во
FROM films
GROUP BY year HAVING Кол_во > 500
ORDER BY Кол_во DESC

```

# добавление записей в таблицу
```
INSERT INTO users (name, age)
VALUES('Sim', 25),
('Rom', 41)

```

# изменение данных в поле "age"
```
update users 
SET age = 22 WHERE id = 2

```

# изменение данных в двух полях одной записи
```
update users 
SET name = "Billy", age = 23 WHERE id = 2

```

# удаление данных тех, кто старше 30 лет
```
DELETE from users 
WHERE age>30

```

```
CREATE TABLE IF NOT EXISTS users (

trip_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT    NOT NULL,
    city       TEXT    NOT NULL,
    per_diem   REAL    NOT NULL,
    date_first DATE    NOT NULL,
    date_last  DATE    NOT NULL
);
```

# ДЗ

```
CREATE TABLE IF NOT EXISTS users (

    trip_id    INTEGER     PRIMARY KEY AUTOINCREMENT,
    name       TEXT (30)   NOT NULL,
    city       TEXT (25)   NOT NULL,
    per_diem   REAL (8, 2) NOT NULL,
    date_first DATE        NOT NULL,
    date_last  DATE        NOT NULL
);
```

```
SELECT city, count(*) as Кол_во
FROM users
GROUP BY city
ORDER BY Кол_во DESC
Limit 2
```

