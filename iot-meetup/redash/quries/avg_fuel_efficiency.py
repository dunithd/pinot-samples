from pinotdb import connect

conn = connect(host='host.docker.internal', port=8099, path='/query/sql', scheme='http')
curs = conn.cursor()
curs.execute("""
select sensor_id, avg(fuel_efficiency) avg_fe
from readings 
group by sensor_id
order by avg_fe
""")

result = {}
result['columns'] = [
    {
      "name": "sensor_id",
      "type": "integer",
      "friendly_name": "sensor_id"
    },
    {
      "name": "avg_fe",
      "type": "integer",
      "friendly_name": "avg_fe"
    }
  ]

rows = []
for row in curs:
    record = {}
    record['sensor_id'] = row[0]
    record['avg_fe'] = row[1]
    
    rows.append(record)

result["rows"] = rows