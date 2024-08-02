teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")

validate_users(['purplecat'])