from prometheus_client import start_http_server, Summary, Counter, Gauge
import random, time

REQUEST_COUNT = Counter('request_count', 'Total permintaan prediksi')
LATENCY = Summary('request_latency_seconds', 'Waktu proses prediksi')
ACCURACY = Gauge('model_accuracy', 'Akurasi model')
REQUEST_LATENCY_COUNT = Counter('request_latency_count', 'Total request latency count')

CPU_USAGE = Gauge('cpu_usage', 'Persentase penggunaan CPU')
MEMORY_USAGE = Gauge('memory_usage', 'Penggunaan memori dalam MB')
DISK_IO = Gauge('disk_io', 'Aktivitas disk IO dalam KB/s')
REQUEST_SUCCESS = Counter('request_success_count', 'Total request berhasil')
REQUEST_FAILURE = Counter('request_failure_count', 'Total request gagal')
REQUEST_AVG_LATENCY = Gauge('request_avg_latency', 'Rata-rata waktu request')
NETWORK_LATENCY = Gauge('network_latency', 'Simulasi latency jaringan dalam ms')
ERROR_RATE = Gauge('error_rate', 'Persentase error yang terjadi')
QUEUE_LENGTH = Gauge('queue_length', 'Jumlah request yang sedang menunggu dalam antrean')
CACHE_HIT_RATIO = Gauge('cache_hit_ratio', 'Rasio cache hit dari sistem')

@LATENCY.time()
def process_request():
    time.sleep(random.uniform(0.1, 0.3))
    REQUEST_COUNT.inc()
    ACCURACY.set(random.uniform(0.85, 0.95))
    REQUEST_LATENCY_COUNT.inc()

    CPU_USAGE.set(random.uniform(20, 80))
    MEMORY_USAGE.set(random.uniform(500, 1500))
    DISK_IO.set(random.uniform(50, 200))
    REQUEST_SUCCESS.inc()
    if random.random() < 0.1:  
        REQUEST_FAILURE.inc()
    avg_latency = random.uniform(0.1, 0.3)
    REQUEST_AVG_LATENCY.set(avg_latency)
    NETWORK_LATENCY.set(random.uniform(10, 100))
    ERROR_RATE.set(random.uniform(0, 5))
    QUEUE_LENGTH.set(random.randint(0, 10))
    CACHE_HIT_RATIO.set(random.uniform(0.7, 1.0))

if __name__ == '__main__':
    start_http_server(8000)
    print("Exporter berjalan di http://localhost:8000")
    while True:
        process_request()
        time.sleep(2)
