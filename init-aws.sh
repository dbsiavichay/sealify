#!/bin/bash
awslocal dynamodb create-table \
   --table-name users \
   --attribute-definitions \
      AttributeName=email,AttributeType=S \
   --key-schema \
      AttributeName=email,KeyType=HASH \
   --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
   --region us-east-1