import requests, time

#Edit token
TOKEN = ''

mode = input('[1] DM\n[2] Server\n')
uid = input('User ID to purge: ')
headers = {'Authorization':TOKEN}

class Deleter:
    def something(self, stuff):
        messages = []
        for block in stuff:
            for message in block:
                if message['author']['id'] == uid:
                    messages.append('%s:%s' % (message['channel_id'], message['id']))
        self.something_else(messages)
    def something_else(self, messages):
        print('Deleting %s messages.' % (len(messages)))
        for message in messages:
            channel = message.split(':')[0]
            message_id = message.split(':')[-1]
            r = requests.delete('https://discordapp.com/api/v6/channels/%s/messages/%s' % (channel, message_id), headers=headers)
            time.sleep(0.2)
obj = Deleter()
if mode == '1':
    channel_id = input('Channel ID: ')
    while True:
        r = requests.get('https://discordapp.com/api/v6/channels/%s/messages/search?author_id=%s' % (channel_id, uid), headers=headers)
        obj.something(r.json()['messages'])
else:
    server = input('Server ID: ')
    while True:
        r = requests.get('https://discordapp.com/api/v6/guilds/%s/messages/search?author_id=%s&include_nsfw=true' % (server, uid), headers=headers)
        obj.something(r.json()['messages'])
