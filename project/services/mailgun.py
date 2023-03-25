# -*- coding: utf-8 -*-
import json

import requests
from settings.logging import logger


class mailgun:
    def send(self, req):
        '''
        {
            "from": "example@example.in",
            "to": "shoaibmohd113@gmail.com",
            "subject": "test",
            "cc": [],
            "text": "This is Example Email for Testing"
        }
        '''

        data = json.loads(req)

        if not data.get("from"):
            return {"message": "from is not available"}, 400
        if not data.get("to"):
            return {"message": "to is not available"}, 400
        if not data.get("subject"):
            return {"message": "subject is not available"}, 400
        if not data.get("text"):
            return {"message": "text is not available"}, 400

        key = "find it in your mailgun profile"
        url = "you have to verify your domain on mailgun"

        # For more information: https://help.mailgun.com/hc/en-us/articles/203380100-Where-Can-I-Find-My-API-Key-and-SMTP-Credentials-

        response = requests.post(url, auth=("api", key), data=data, timeout=30)

        logger.info(
            "Email Send by Mailgun url: %s payload: %s status code: %s response: %s",
            url,
            data,
            response.status_code,
            response.text,
        )

        if response.status_code == 200:
            res = json.loads(response.text)
            return {"email_id": res.get("id"), "status_code": response.status_code}
        return {"message": response.text, "status_code": response.status_code}
