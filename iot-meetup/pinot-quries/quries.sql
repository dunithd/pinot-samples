--active trucks
select count(distinct sensor_id) as active_trucks
from readings
where ts > ToEpochSeconds(now()- 5000)

--speeding trucks
select sensor_id, avg(speed) as avg_speed
from readings
where ts > ToEpochSeconds(now()- 5000)
group by sensor_id
having avg_speed > 80

--with lookup table
select 
sensor_id,
lookup('sensors','truck_name','sensor_id',sensor_id) as truck_name,
lookup('sensors','driver_name','sensor_id',sensor_id) as driver_name
from readings
where ts > ToEpochSeconds(now()- 5000)

select 
sensor_id,
latitude,
longitude
from readings
where ts > ToEpochSeconds(now()- 5000)
group by sensor_id
order by ts desc

--stationary trucks
select 
sensor_id,
count(distinct STPOINT(latitude, longitude)) as movements
from readings
where ts > ToEpochSeconds(now()- 5000)
group by sensor_id

--distance
select ST_Distance(ST_POINT(latitude, longitude), ST_POINT(37.68916,-122.39051)) AS distanceInMetres
from readings
WHERE ts > ToEpochSeconds(now()- 5000)

