import random
import time
import json
from kafka import KafkaProducer
import datetime

# Configuration
KAFKA_BROKER = 'kafka:9092'  # Kafka broker
TOPIC = 'share_prices'       # Kafka topic to publish data

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulating stock prices for companies
companies = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']

def generate_random_data():
    """Generate random stock data with random price between 100 and 1500."""
    stock_data = {}
    for company in companies:
        stock_data[company] = round(random.uniform(100, 1500), 2)  # Generate a random stock price between 100 and 1500
    return stock_data

def send_to_kafka(data):
    """Send the stock data to Kafka."""
    producer.send(TOPIC, data)
    producer.flush()  # Ensure the message is sent

def main():
    while True:
        data = generate_random_data()
        timestamp = datetime.datetime.now().isoformat()
        data['timestamp'] = timestamp  # Add timestamp for the generated data
        send_to_kafka(data)
        print(f"Data sent to Kafka: {data}")
        time.sleep(5)  # Wait for next data generation

if __name__ == '__main__':
    main()
