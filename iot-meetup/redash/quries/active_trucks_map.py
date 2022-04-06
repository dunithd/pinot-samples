from pinotdb import connect

conn = connect(host='host.docker.internal', port=8099, path='/query/sql', scheme='http')
curs = conn.cursor()
curs.execute("""
select sensor_id,latitude,longitude,max(ts)
from readings 
where ts > ToEpochSeconds(now()- 5000)
group by sensor_id
having avg_speed > 80
""")

result = {}
result['columns'] = [
    {
      "name": "sensor_id",
      "type": "integer",
      "friendly_name": "sensor_id"
    },
    {
      "name": "avg_speed",
      "type": "integer",
      "friendly_name": "avg_speed"
    }
  ]

rows = []
for row in curs:
    record = {}
    record['sensor_id'] = row[0]
    record['avg_speed'] = row[1]
    
    rows.append(record)

result["rows"] = rows