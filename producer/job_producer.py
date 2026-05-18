from kafka import KafkaProducer
import json
import time

# ----------------------------------
# Kafka Producer Configuration
# ----------------------------------
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# ----------------------------------
# Job Posting Events
# ----------------------------------
jobs = [

    {
        "job_id": 9001,
        "company": "TechNova",
        "designation": "Data Engineer",
        "city": "Bangalore",
        "salary_range": "12-18 LPA",
        "required_skills": "Python,PySpark,Kafka",
        "experience_required": 2,
        "posted_time": "2025-01-01 09:00:00",
        "impressions": 2500,
        "clicks": 620
    },

    {
        "job_id": 9002,
        "company": "CloudAxis",
        "designation": "Data Analyst",
        "city": "Hyderabad",
        "salary_range": "8-12 LPA",
        "required_skills": "SQL,PowerBI,Python",
        "experience_required": 1,
        "posted_time": "2025-01-01 09:05:00",
        "impressions": 1800,
        "clicks": 450
    },

    {
        "job_id": 9003,
        "company": "AIWorks",
        "designation": "Data Scientist",
        "city": "Pune",
        "salary_range": "15-22 LPA",
        "required_skills": "ML,Python,TensorFlow",
        "experience_required": 3,
        "posted_time": "2025-01-01 09:10:00",
        "impressions": 3200,
        "clicks": 890
