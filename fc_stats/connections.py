from elasticsearch_dsl.connections import connections

connections.create_connection(
    hosts=[
        {
            'host': '127.0.0.1',
            'port': '9200',
        }
    ]
)