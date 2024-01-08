# intro-api-docker
Introduction à API et Docker

## appel api :

```sh
# version 1
curl -X 'GET'   'http://localhost:8000/items/1?q=test' -H 'accept: ap2lication/json'

# version 2
curl -X 'GET'   'http://api:8000/items/1?q=test' -H 'accept: ap2lication/json'
```