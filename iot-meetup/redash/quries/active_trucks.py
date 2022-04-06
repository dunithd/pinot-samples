from pinotdb import connect

conn = connect(host='host.docker.internal', port=8099, path='/query/sql', scheme='http')
curs = conn.cursor()
curs.execute("""
   select count(distinct sensor_id) as active_trucks
from readings 
where ts > ToEpochSeconds(now()- 5000)
""")

result = {}
result['columns'] = [
    {
      "name": "active_trucks",
      "type": "integer",
      "friendly_name": "active_trucks"
    }
  ]

rows = []
for row in curs:
    record = {}
    record['active_trucks'] = row[0]
    
    rows.append(record)

result["rows"] = rows