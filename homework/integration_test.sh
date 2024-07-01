#!/usr/bin/env bash



docker-compose up -d

sleep 10

export INPUT_FILE_PATTERN="s3://nyc-duration-8663/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration-8663/out/{year:04d}-{month:02d}.parquet"
export S3_ENDPOINT_URL="http://localhost:4566"


aws --endpoint-url="${S3_ENDPOINT_URL}" s3 mb s3://nyc-duration-8663

pipenv run python integration_test.py

ERROR_CODE=$?

if [ ${ERROR_CODE} != 0 ]; then
    docker-compose logs
    docker-compose down
    exit ${ERROR_CODE}
fi

echo "yay tests work!"

# docker-compose down