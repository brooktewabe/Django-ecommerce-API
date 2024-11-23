## Django ecommerce API
- Django rest framework (DRF)
- Token authentication 

Basic endpoint examples(make sure to set Auth as API Key -> Authorization: Token your_token_here )

(POST) http://127.0.0.1:8000/api-token-auth/ //to login to django admin

{

    "username": "user",
    
    "password": "1234"
}

(GET) http://127.0.0.1:8000/item/

(GET) http://127.0.0.1:8000/item/uuid

(GET) http://127.0.0.1:8000/order

(GET) http://127.0.0.1:8000/order/uuid

(POST)http://127.0.0.1:8000/order 

{

    "item": "1726025d-cbd7-40d8-ba06-1141bb14c7c4", //item uuid
    
    "quantity": "1"
}

(POST) http://127.0.0.1:8000/contact/

{

    "name": "Bobby",
    
    "message": "test",
    
    "email": "bobby@example.com"
}
