#!/bin/bash
awslocal dynamodb create-table \
   --table-name certificates \
   --attribute-definitions \
      AttributeName=id,AttributeType=S \
   --key-schema \
      AttributeName=id,KeyType=HASH \
   --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
   --region us-east-1