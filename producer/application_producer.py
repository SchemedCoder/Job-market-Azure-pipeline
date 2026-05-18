from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

applications = [
    {
        "application_id": 1001,
        "candidate_id": 501,
        "job_id": 9001,
        "city": "Bangalore",
        "designation": "Data Engineer",
        "skills": "Python,PySpark,Kafka",
        "experience": 2,
        "salary_expected": 1400000,
        "application_time": "2025-01-01 10:05:00",
        "status": "Applied"
    }
]

for app in applications:

    producer.send("job_applications", value=app)

    print("Sent:", app)

    time.sleep(2)
