from app import client


def get_user_info(query):
    d, a = {}, []

    for rowproxy in query:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)

    for row in a:
        response = client.users_info(user=row['rateder'])
        row['rateder'] = response.get('user').get('name')

    return a
