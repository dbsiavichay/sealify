from botocore.exceptions import ClientError
from mypy_boto3_dynamodb.service_resource import Table

from src.core.app.exceptions import DynamoDBException


class AWSDynamoDBClient:
    def __init__(self, table: Table):
        self.table = table

    def put_item(self, item):
        try:
            return self.table.put_item(Item=item)
        except ClientError as e:
            raise DynamoDBException(f"PUT_ITEM: {e.response['Error']['Message']}")

    def get_item(self, key):
        try:
            return self.table.get_item(Key=key)
        except ClientError as e:
            raise DynamoDBException(f"GET_ITEM: {e.response['Error']['Message']}")

    def query(self, key, index_name=None):
        try:
            if not isinstance(key, dict) or len(key) != 1:
                raise ValueError(
                    "El parámetro 'key' debe ser un diccionario con un único atributo."
                )

            attribute_name, attribute_value = list(key.items())[0]

            key_condition_expression = f"{attribute_name} = :value"
            expression_attribute_values = {":value": attribute_value}
            response = self.table.query(
                KeyConditionExpression=key_condition_expression,
                IndexName=index_name,
                ExpressionAttributeValues=expression_attribute_values,
            )
            return response
        except ClientError as e:
            raise DynamoDBException(f"QUERY: {e.response['Error']['Message']}")

    def update_item(self, key, update_values):
        update_expression = "SET " + ", ".join(
            f"#{k} = :{k}" for k in update_values.keys()
        )
        expression_attribute_values = {f":{k}": v for k, v in update_values.items()}
        expression_attribute_names = {f"#{k}": k for k in update_values.keys()}

        try:
            response = self.table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ExpressionAttributeNames=expression_attribute_names,
                ReturnValues="ALL_NEW",
            )
            return response
        except ClientError as e:
            raise DynamoDBException(f"UPDATE_ITEM: {e.response['Error']['Message']}")

    def delete_item(self, key):
        try:
            response = self.table.delete_item(Key=key)
            return response
        except ClientError as e:
            raise DynamoDBException(f"DELETE_ITEM: {e.response['Error']['Message']}")

    def scan_items(self):
        try:
            return self.table.scan()
        except ClientError as e:
            raise DynamoDBException(f"SCAN_ITEMS: {e.response['Error']['Message']}")
