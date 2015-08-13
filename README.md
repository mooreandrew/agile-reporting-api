# agile-reporting-api
At the moment this service posts data to a postgres database.

##requirements:
- Vagrant
- Virtualbox
- git

##Environment Variables

The following environment variables need to be set:

- trello_api_key = Generated by visiting https://trello.com/app-key
- trello_api_secret = Generated by visting https://trello.com/app-key
- trello_token = Generated by visiting  https://trello.com/1/authorize?key=<your trello api key>&name=<application name>&expiration=never&response_type=token

##How to run

```
git clone https://github.com/mooreandrew/agile-reporting-api.git
```

```
cd agile-reporting-api
```

```
vagrant up
```

```
vagrant ssh
```

```
cd /vagrant
```

```
source ~/venvs/scrum-progress/bin/activate
```

```
source environment.sh
```

```
pip install -r requirements.txt
```

```
export trello_api_key="key here"
export trello_api_secret="secret here"
export trello_token="token here"
```

```
./run.sh
```

##How to use

To check if the application is running, go to:

```
http://localhost:5001/
```

This should return a response of "Ok"

To get a list of compatible tools:

```
http://localhost:5001/tools
```

This will return a list with an id of the tool (e.g. trello)

To return all of trello's projects:

```
http://localhost:5001/projects/trello
```

This will return a list of all projects in that tool.

Using the id of one of the projects to return all the sprints:

```
http://localhost:5001/sprints/trello/547703b1284f36366cd6c182
```

This returns a list of all identified sprints in the tool

Using the sprint we can now extract all the stories from that sprint:

```
http://localhost:5001/stories/trello/547703b1284f36366cd6c182/15
```

### modules

Currently there is only a module for Trello. This has the following functions:

- __init__() - Will make a connection to the api
- get_project_list() - Returns a list of projects in the tool
- get_sprints(project_id) - Return all the sprints for that project in the tool
- get_story_list(project_id, sprint) - Return all the stories for that project/sprint in the tool

New modules need to follow this format with the same functions and argument count.

### Issues

- This currently only supports Trello lists which are named "Sprint ## - Done". You can also replace Done with Backlog and Doing