# Login

Used for log in user

### URL: `/api/auth/login`

### Method: `POST`
---

### Request body
```json
{
  "login": "string",
  "password": "string",
  "__secure_key": "string"
}
```
---
### Response

If login result is successful

```json
{
  "access_token": "string",
  "logout_hash": "string",
  "user_id": "number"
}
```
Otherwise

```json
{
  "error": "string",
  "error_code": "number"
}
```
