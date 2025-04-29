import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class PrintFn(beam.DoFn):
    def process(self, element):
        print(f"Received: {element}")
        return [element]

def run():
    options = PipelineOptions(
        runner='FlinkRunner',
        flink_master='flink-jobmanager:8081',
        streaming=True
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | 'ReadFromKafka' >> beam.io.ReadFromKafka(
                consumer_config={'bootstrap.servers': 'kafka:9092'},
                topics=['test_topic']
            )
            | 'PrintToConsole' >> beam.ParDo(PrintFn())
        )

if __name__ == '__main__':
    run()
