import pandas as pd
from pinotdb import connect
import matplotlib.pyplot as plt

conn = connect(host='host.docker.internal', port=8099, path='/query/sql', scheme='http')
curs = conn.cursor()

curs.execute("""
SELECT
 sensor_id,
 avg(speed) as avg_speed
FROM readings
GROUP BY sensor_id
LIMIT 200
""")

df = pd.DataFrame(curs, columns=[item[0] for item in curs.description])

plt.bar("sensor_id", "avg_speed", data = df, color = "blue")
plt.xlabel("Players")
plt.ylabel("Goal Scored")
plt.title("Highest goal scorers in the Premier league 2019-20 by mid-season")
plt.show()