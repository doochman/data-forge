FROM apache/beam_python3.10_sdk:latest

WORKDIR /app
COPY pipeline /app

CMD ["python", "beam_job.py", "--runner=FlinkRunner", "--flink_master=flink-jobmanager:8081"]
