# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo Araújo - ledharaujo@gmail.com, April 2022.

# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# Core.
import os
import email
import imaplib
import datetime as dt

# Libs.
import dotenv
import google.oauth2 as go
import googleapiclient.discovery as gd


dotenv.load_dotenv()

# Constants.
SP = [os.getenv('SP')]
EMAIL = os.getenv('EMAIL')
PASSWORD_EMAIL = os.getenv('PASSWORD_EMAIL')
NAME_RANGE = os.getenv('NAME_RANGE')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')


def main():
    '''Main func responsible for run project.'''

    m = imaplib.IMAP4_SSL('imap.gmail.com')
    m.login(EMAIL, PASSWORD_EMAIL)

    m.select('inbox')

    rs, dt = m.search(None, '(UNSEEN FROM "VOE MILHAS")')

    for em in dt[0].split():
        rs, dt = m.fetch(em, '(RFC822)')
        bd = email.message_from_string(dt[0][1].decode('utf-8'))

        ms, _ = bd.get_payload()
        lst = ms.get_payload().split('---')[0].strip().split('\r\n')
        vls = []

        for v in lst:
            vls.append(v.split(': ')[1] or 'Nenhum')

        ist_dt(vls)

def ist_dt(vls):
    '''Responsible for insert data in sheet.'''

    # Insert data in first column.
    vls.insert(0, str(dt.date.today()))

    rows = [vls]

    cdtls = go.service_account.Credentials.from_service_account_file('credentials.json', scopes=SP)
    service = gd.build('sheets', 'v4', credentials=cdtls)

    args = {'body': {}}

    args['spreadsheetId'] = SPREADSHEET_ID
    args['range'] = NAME_RANGE
    args['valueInputOption'] = 'USER_ENTERED'

    args['body']['majorDimension'] = 'ROWS'
    args['body']['values'] = rows

    service.spreadsheets().values().append(**args).execute()


if __name__ == '__main__':
    main()

