-- lists all cities contained in the database hbtn_0d_usa. 
-- usuing JOiN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.states_id = state.id
ORDER BY cities.id ASC;
