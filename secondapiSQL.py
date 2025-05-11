import requests
import json

url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"

payload = json.dumps({
  "finalQuery": "SELECT e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME, COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT FROM EMPLOYEE e1 JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID LEFT JOIN EMPLOYEE e2 ON e1.DEPARTMENT = e2.DEPARTMENT AND e2.DOB > e1.DOB GROUP BY e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME ORDER BY e1.EMP_ID DESC;"
})
headers = {
  'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdDUzIyMTAyMiIsIm5hbWUiOiJBa3NoYXQgU2F4ZW5hIiwiZW1haWwiOiJha3NoYXRzYXhlbmEyMjAxNzdAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYxMTU5LCJleHAiOjE3NDY5NjIwNTl9.uruMmxYkMFfzv-AHJgXc1Bvjgr45i3uZVPYqSfas7Ak',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
