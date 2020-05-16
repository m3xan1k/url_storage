# url_storage
Small API based on fastAPI and redis


To run project locally you need **docker** and **docker-compose** installed,

then

```
git clone git@github.com:m3xan1k/url_storage.git
cd url_storage
docker-compose up --build -d
```

Service will be running locally on port **tcp/8000**

Resources

```
POST /visited_links
```
Takes json like this

```
{"links": ["https://ya.ru","https://ya.ru?q=123","funbox.ru","https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"]}
```

```
GET /visited_domains
need params:
from(numeric) timestamp
to(numeric) timestamp
```

You may test it like this

check timestamp

```
date '+%s'
```

make POST request

```
curl http://localhost:8000/visited_links -X POST -H 'Content-Type: Aplication/json' -d '{"links": ["https://ya.ru","https://ya.ru?q=123","funbox.ru","https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"]}' -L
```

check timestamp one more time and place this timestamps into GET request params

```
curl 'http://localhost:8000/visited_domains?from=1589571773&to=1589571873'
```
