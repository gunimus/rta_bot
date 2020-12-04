import datetime
import requests
from script import common

prefix_url = 'https://www.speedrun.com/api/v1'
game_id = ''

def get_user(user_name):
    send_list = []
    user_id = get_user_id(user_name)
    if user_id == '':
        send_list.append(user_name + ' is not found')
        return send_list, user_id
    
    send_list.append('user name : ' + user_name)
    return send_list, user_id

def get_ranking(user_data):
    global game_id
    send_list = []
    game_id = ''
    for data in user_data:
        previous_id = game_id
        game_id = data.get('run').get('game')
        if previous_id != game_id:
            send_list.append('\n' + get_title(game_id))
        send_list.append(get_records(data))

    if len(send_list) == 1:
        send_list.append('\n' + 'records is not found')

    return send_list

def get_user_id(user_name):
    url = prefix_url + '/users?name=' + user_name
    json = requests.get(url).json()
    user_id = ''
    for data in json.get('data'):
        if data.get('names').get('international') == user_name:
            user_id = data.get('id')
    return user_id

def get_user_data(user_id):
    url = prefix_url + '/users/' + user_id + '/personal-bests'
    return sorted(requests.get(url).json().get('data'), key=lambda x: x['run']['game'])

def get_title(game_id):
    url = prefix_url + '/games/' + game_id
    return requests.get(url).json().get('data').get('names').get('international')

def get_records(data):
    place = common.get_place(data.get('place'))
    run_time = common.get_time(datetime.timedelta(seconds=data.get('run').get('times').get('primary_t')))
    run_values = data.get('run').get('values')
    for links in data.get('run').get('links'):
        if links.get('rel') == 'category':
            category_url = links.get('uri')
            category_data = requests.get(category_url).json()
            if category_data.get('data').get('type') == "per-game":
                category_name = category_data.get('data').get('name')
                if len(run_values) != 0: 
                    for category_links in category_data.get('data').get('links'):
                        if category_links.get('rel') == 'variables':
                            variables_url = category_links.get('uri')
                            variables_choices = requests.get(variables_url).json().get('data')[0].get('values').get('choices')
                            for variables_keys in variables_choices.keys():
                                for run_value in run_values.values():
                                    if run_value == variables_keys:
                                        variables_name = variables_choices.get(variables_keys)
                                        category_name = category_name + ' (' + variables_name + ')'
            else:
                return ''
    return '  ' + category_name + '\n' + '    ' + place + ' (' + run_time + ')'
