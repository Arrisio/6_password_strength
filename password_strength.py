import re
import getpass
import string
import argparse


def validate_password(typed_password):
    if re.search(r'[^ -~]+', typed_password):
        raise ValueError(
            'password must contain only English characters,'
            ' numbers and punctuation'
        )
    elif not typed_password:
        raise ValueError('You should enter password')
    else:
        return


def get_password_from_keyboard():
    while True:
        typed_password = getpass.getpass(prompt='Enter password: ')
        try:
            validate_password(typed_password)
            return typed_password
        except ValueError as e:
            print(str(e))


def calc_penalty_by_pers_data(typed_password, person_data):
    penalty = 0

    if person_data:
        for word in re.sub(r'[^a-z]', ' ', person_data.lower()).split():
            if word in re.sub(r'[^a-z]', '', typed_password.lower()):
                penalty += len(word)

        for digit in re.sub(r'[\D]', ' ', person_data).split():
            if digit in re.sub(r'[\D]', '', typed_password):
                penalty += len(digit)

    return penalty


def calc_difficult_score_by_inclusion(typed_password):
    inclusion_score = 0

    if re.search(r'[' + string.punctuation + ']', typed_password):
        inclusion_score += 1

    if re.search(r'[' + string.ascii_uppercase + ']', typed_password):
        inclusion_score += 1

    if re.search(r'[' + string.ascii_lowercase + ']', typed_password):
        inclusion_score += 1

    if re.search(r'[' + string.digits + ']', typed_password):
        inclusion_score += 1

    return inclusion_score


def get_password_strength(typed_password, blacklist, person_data=None):

    if typed_password in blacklist:
        return 1

    score = len(typed_password) - 6
    if score < 0:
        score = 0
    if score > 6:
        score = 6

    score += calc_difficult_score_by_inclusion(typed_password)

    if person_data:
        score -= calc_penalty_by_pers_data(typed_password, person_data)

    if score < 1:
        score = 1
    if score > 10:
        score = 10
    return score


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-b', action='store',
        dest='blacklist',
        help='Filepath with passwords blacklist',
        default=None
    )

    return parser.parse_args()


if __name__ == '__main__':
    params = parse_arguments()

    if params.blacklist:
        try:
            with open(params.blacklist, 'r') as file_handler:
                blacklist = file_handler.read().split()
        except (OSError, ValueError):
            print('failed load blacklist')
            blacklist = []
    else:
        blacklist = []

    person_data = input(
        'Enter the personal data that will be used to verify the password: '
    )

    typed_password = get_password_from_keyboard()
    password_strength = get_password_strength(
        typed_password, blacklist, person_data
    )
    print('Password strength: ', password_strength)
