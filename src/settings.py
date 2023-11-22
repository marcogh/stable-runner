# result_backend = 'db+sqlite:///data/results.sqlite'
# broker_url = 'amqp://guest@localhost/'
broker='amqp://guest@localhost//',
backend='db+sqlite:///data/results.sqlite',
task_serializer = 'json'
broker_connection_retry_on_startup = True
