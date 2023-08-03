import json
import os


class BodyExpected:
    path_list_users = f'.{os.sep}element_body_expected{os.sep}list_users.json'
    with open(path_list_users) as f:
        list_users_body = json.load(f)

    path_single_user = f'.{os.sep}element_body_expected{os.sep}single_user.json'
    with open(path_single_user) as f:
        single_user_body = json.load(f)

    path_list_resource = f'.{os.sep}element_body_expected{os.sep}list_resource.json'
    with open(path_list_resource) as f:
        list_resource_body = json.load(f)

    path_single_resource = f'.{os.sep}element_body_expected{os.sep}single_resource.json'
    with open(path_single_resource) as f:
        single_resource_body = json.load(f)

    path_create = f'.{os.sep}element_body_expected{os.sep}create.json'
    with open(path_create) as f:
        create_body = json.load(f)

    path_update = f'.{os.sep}element_body_expected{os.sep}update.json'
    with open(path_update) as f:
        update_body = json.load(f)

    path_register_successful = f'.{os.sep}element_body_expected{os.sep}register_successful.json'
    with open(path_register_successful) as f:
        register_successful_body = json.load(f)

    path_register_unsuccessful = f'.{os.sep}element_body_expected{os.sep}register_unsuccessful.json'
    with open(path_register_unsuccessful) as f:
        register_unsuccessful_body = json.load(f)

    path_login_successful = f'.{os.sep}element_body_expected{os.sep}login_successful.json'
    with open(path_login_successful) as f:
        login_successful_body = json.load(f)

    path_login_unsuccessful = f'.{os.sep}element_body_expected{os.sep}login_unsuccessful.json'
    with open(path_login_unsuccessful) as f:
        login_unsuccessful_body = json.load(f)

    path_list_users_delay = f'.{os.sep}element_body_expected{os.sep}list_users_delay.json'
    with open(path_list_users_delay) as f:
        list_users_delay_body = json.load(f)
