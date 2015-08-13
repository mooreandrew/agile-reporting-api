from trello import TrelloClient
import os
import re
import time

from dateutil import parser

class Trello:
    client = None

    def __init__(self):
        self.client = TrelloClient(
            api_key=os.environ.get('trello_api_key'),
            api_secret=os.environ.get('trello_api_secret'),
            token=os.environ.get('trello_token')
        )

    def get_project_list(self):
        projects = []
        for b in self.client.list_boards():
            projects.append({'name': b.name.decode("utf-8"), 'id': b.id})
        return projects

    def get_sprints(self, trell_project):

        board = self.client.get_board(trell_project)

        sprints = []

        for l in board.all_lists():
            m = re.search('Sprint (.*?) - Done', l.name.decode("utf-8"))
            if m is not None:
                sprints.append({'sprint': m.group(1)})

        return sprints


    def get_story_list(self, trell_project, sprint):

        board = self.client.get_board(trell_project)

        stories = []

        list = board.all_lists()
        for l in board.all_lists():
            type = None
            if (l.name.decode("utf-8") == 'Sprint ' + sprint + ' - Backlog'):
                type = 'Backlog'
            elif (l.name.decode("utf-8") == 'Sprint ' + sprint + ' - Doing'):
                type = 'Doing'
            elif (l.name.decode("utf-8") == 'Sprint ' + sprint + ' - Done'):
                type = 'Done'

            if type is not None:
                for c in l.list_cards():
                    if type == 'Done':
                        if (len(c.listCardMove_date()) > 0):
                            #Convert DateTime to Epoch
                            card_date = time.mktime(parser.parse(str(c.latestCardMove_date)).timetuple())
                        else:
                            #Convert DateTime to Epoch
                            card_date = time.mktime(c.create_date().timetuple())
                    else:
                        card_date = None

                    split = c.name.decode("utf-8").split('(')
                    points = split[len(split) - 1].replace(')', '')
                    del split[len(split) - 1]
                    name = '('.join(split)

                    stories.append({'status': type, 'name': name, 'id': c.id, 'points': points, 'date_completed': card_date})

        return stories
