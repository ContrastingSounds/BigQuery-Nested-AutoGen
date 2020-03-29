from collections import namedtuple


ViewFromTable = namedtuple('ViewFromTable', 'name partition_column')

project = 'gcp-project-name'
dataset = 'dataset_name'
tables = [
    ViewFromTable('table_one', 'created_date'),
    ViewFromTable('table_two', 'event_date'),
    ViewFromTable('table_three_no_partition', ''),
]