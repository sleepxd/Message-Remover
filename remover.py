import requests, threading

TOKEN = ''

server = input('Server ID: ')
uid = input('User ID: ')

headers = {'Authorization':TOKEN}
while True:
    r = requests.get('https://discordapp.com/api/v6/guilds/%s/messages/search?author_id=%s&include_nsfw=true' % (server, uid), headers=headers)

    messages = []

    for block in r.json()['messages']:
        for message in block:
            if message['author']['id'] == uid:
                messages.append('%s:%s' % (message['channel_id'], message['id']))

    print('Deleting %s messages.' % (len(messages)))

    for message in messages:
        channel = message.split(':')[0]
        message_id = message.split(':')[-1]
        r = requests.delete('https://discordapp.com/api/v6/channels/%s/messages/%s' % (channel, message_id), headers=headers)