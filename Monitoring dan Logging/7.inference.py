import time
import random
from prometheus_client import start_http_server, Gauge

model_accuracy = Gauge('model_accuracy', 'Akurasi model')
request_count_total = Gauge('request_count_total', 'Jumlah request total')
request_latency_sum = Gauge('request_latency_sum', 'Total latency request')
request_latency_count = Gauge('request_latency_count', 'Jumlah request latency')

def simulate_metrics():
    while True:
        
        model_accuracy.set(random.uniform(0.7, 0.95))
        request_count_total.set(random.randint(50, 150))
        request_latency_sum.set(random.randint(1000, 6000))
        request_latency_count.set(random.randint(50, 150))
        time.sleep(5)

if __name__ == "__main__":
    
    start_http_server(8000)
    print("Prometheus metrics server running on http://localhost:8000")
    simulate_metrics()
