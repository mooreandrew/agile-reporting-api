from application import app
from application.modules.trello import Trello
import json

@app.route('/')
def login():
    return 'ok'

# This returns 'tool_id'
@app.route('/tools', methods=['GET'])
def get_tools():
    tools = []
    tools.append({'name': 'Trello', 'id': 'trello'})
    return json.dumps(tools)

# This returns 'project_id'
@app.route('/projects/<tool_id>', methods=['GET'])
def get_projects(tool_id):
    try:
        tool = toolmap(tool_id)
        return json.dumps(tool.get_project_list())
    except Exception as e:
        return json.dumps({'error': str(e)})

# This returns 'sprint'
@app.route('/sprints/<tool_id>/<project_id>', methods=['GET'])
def get_sprints(tool_id, project_id):
    try:
        tool = toolmap(tool_id)
        return json.dumps(tool.get_sprints(project_id))
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/stories/<tool_id>/<project_id>/<sprint>', methods=['GET'])
def get_stories(tool_id, project_id, sprint):
    try:
        tool = toolmap(tool_id)
        return json.dumps(tool.get_story_list(project_id, sprint))
    except Exception as e:
        return json.dumps({'error': str(e)})

# Function used to list all agile product apis
def toolmap(tool_id):
    if tool_id == 'trello':
        return Trello()
    else:
        raise Exception('Unknown Tool')
