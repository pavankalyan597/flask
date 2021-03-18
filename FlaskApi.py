import flask
import sqlite3

app = flask.Flask(__name__)

def get_field_names(table):
    con = sqlite3.connect('flask.db')
    cursor = con.cursor()
    columns = cursor.execute(f'PRAGMA table_info({table})')
    keys = columns.fetchall()
    return keys,cursor,con

#endpoint to see tables in db
@app.route('/api/db/tables/',methods = ['GET'])
def show_tables():
    con = sqlite3.connect('flask.db')
    cursor = con.cursor()
    result = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {}
    count = 0
    for table, in result.fetchall():
        if table not in ['sqlite_master','sqlite_sequence','sqlite_stat1']:
            tables['table' + str(count)] = table
            count += 1
    con.close()
    return flask.jsonify(tables)

@app.route('/api/db/tables/<string:table>/',methods = ['GET'])
def table_details(table):
    keys,cursor,con = get_field_names(table)
    query = flask.request.args
    data = []
    if not query:
        rows = cursor.execute(f'select * from {table}')
        values = rows.fetchall()
        for tup in values:
            result = {}
            for num in range(len(keys)):
                result[keys[num][1]] = tup[num]
            data.append(result)
    else:
        query_keys = query.keys()
        for key in list(query_keys):
            result = cursor.execute(f"select * from {table} where {key} = '{query[key]}'")
            values = result.fetchall()
        for tup in values:
            result = {}
            for num in range(len(keys)):
                result[keys[num][1]] = tup[num]
            data.append(result)
    con.close()
    return flask.jsonify(data)

@app.route('/api/tables/<string:table>/<string:name>',methods = ['DELETE' ])
def delete_row(table,name):
    keys, cursor, con = get_field_names(table)
    cursor.execute(f'delete from {table} where name = "{name}"')
    con.commit()
    rows = cursor.execute(f'select * from {table}')
    values = rows.fetchall()
    data = []
    for tup in values:
        result = {}
        for num in range(len(keys)):
            result[keys[num][1]] = tup[num]
        data.append(result)
    return flask.jsonify(data)

@app.route('/api/db/tables/<string:table>/add',methods = ['POST'])
def add_item(table):
    keys, cursor, con = get_field_names(table)
    query = f'insert into {table} values('
    for key in keys:
        query += '"'+ f"{str(flask.request.json[key[1]])}" + '",'
    query = query[:len(query) - 1] + ')'
    cursor.execute(f'{query}')
    con.commit()
    rows = cursor.execute(f'select * from {table}')
    values = rows.fetchall()
    data = []
    for tup in values:
        result = {}
        for num in range(len(keys)):
            result[keys[num][1]] = tup[num]
        data.append(result)
    return flask.jsonify(data)

app.run(debug=True)