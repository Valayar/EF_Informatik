request = { "args": { "match": "data%'" } }

match = request['args'].get('match')
sql = f"""
SELECT * 
FROM comics 
WHERE title ILIKE '%{match}%';
"""
print(sql)