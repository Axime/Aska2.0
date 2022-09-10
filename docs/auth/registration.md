# Registration

Execute registration of new user

---
### URL: `/api/auth/registration`
### Method: `POST`
---

### Request body
```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "password": "string",
  "password_repeat": "string",
  "__secure_key": "string"
}
```
---


### Response
If result is successful
```json
{
  "access_token": "string",
  "user_id": "number",
  "logout_hash": "string"
}
```

Otherwise
```json
{
  "error": "string",
  "error_code": "string"
}
```