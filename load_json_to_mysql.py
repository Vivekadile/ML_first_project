import json
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jiraiya@106",
    database="college"
)

cursor = conn.cursor()

with open("/Users/apple/Downloads/student_performance_1000_rows.json", "r") as f:
    data = json.load(f)

query = """
INSERT INTO students
(gender, race_ethnicity, parental_level_of_education,
 lunch, test_preparation_course,
 math_score, reading_score, writing_score)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

for row in data:
    cursor.execute(query, (
        row["gender"],
        row["race_ethnicity"],
        row["parental_level_of_education"],
        row["lunch"],
        row["test_preparation_course"],
        row["math_score"],
        row["reading_score"],
        row["writing_score"]
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully")
