class SchemaError(Exception):
    '''
    Todo: 用途に応じて追加
    schemaはロードに失敗しない限り配列にネストした辞書
    '''
    def __init__(self, schema):
        self.schema = schema
    def __str__(self):
            return repr(self.schema)

