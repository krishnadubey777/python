					 
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/createJira', methods=['POST'])
def createJira():
    data = request.json
    comment = data.get('comment', '')

    if '/jira' in comment:

        url = "https://krishnadubey777.atlassian.net/rest/api/3/issue"

        API_TOKEN = ""
        EMAIL = ""
        auth = HTTPBasicAuth(EMAIL, API_TOKEN)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields": {
                "description": {
						
				 
                    "content": [
                        {
                            "content": [
                                {
                                    "text": comment.replace('/jira', '').strip(),
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
					 
				  
						  
                    "version": 1
                },
                "project": {
                    "key": "product-A"
                },
                "issuetype": {
                    "id": "10006"  # Replace with your issue type ID
                },
                "summary": "Main order flow broken" 
	  
				
            }
        })

        response = requests.post(
            url,
            data=payload,
            headers=headers,
            auth=auth
        )


        return jsonify(json.loads(response.text))

    return jsonify({"message": "No /jira command found, no ticket created."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
