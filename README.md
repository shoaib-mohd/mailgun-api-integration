# Mailgun API Integration


## About

In this project, you can use Mailgun API's to send email to anyone easily.

- APIS
    - http://localhost:8000/mailgun/status/
    - http://localhost:8000/mailgun/email/

## Paulod

```json
{
    "from": "email of the sender",
    "to": "email of the recipient",
    "subject": "subject of the email",
    "cc": [],
    "text": "message that will be sent"
}
```

### Project Start Guide:

- First of all, clone the project
- Install the dependencies by using ""pip install -r requirements.txt" command
- "python project/app.py -p 8000" command to start the project
- Then you can use the project api's and integrate in your project as well
