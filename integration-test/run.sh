#!/usr/bin/env bash

<<<<<<< HEAD
cd "$(dirname "$0")"

LOCAL_TAG=`date +"%Y-%m-%d-%H-%M"`
export LOCAL_IMAGE_NAME="stream-model-duration:${LOCAL_TAG}"
export PREDICTIONS_STREAM_NAME="ride_predictions"
export AWS_DEFAULT_REGION="us-east-1"

# yes | docker system prune -a --volumes

docker build -t ${LOCAL_IMAGE_NAME} ..

docker-compose up -d

sleep 1
=======
if [[ -z "${GITHUB_ACTIONS}" ]]; then
  cd "$(dirname "$0")"
fi

if [ "${LOCAL_IMAGE_NAME}" == "" ]; then
    LOCAL_TAG=`date +"%Y-%m-%d-%H-%M"`
    export LOCAL_IMAGE_NAME="stream-model-duration:${LOCAL_TAG}"
    export PREDICTIONS_STREAM_NAME="ride_predictions"
    export AWS_DEFAULT_REGION="us-east-1"
    echo "LOCAL_IMAGE_NAME is not set, building a new image with tag ${LOCAL_IMAGE_NAME}"
    docker build -t ${LOCAL_IMAGE_NAME} ..
else
    echo "no need to build image ${LOCAL_IMAGE_NAME}"
fi


# yes | docker system prune -a --volumes

docker-compose up -d

sleep 5
>>>>>>> 8c93d3a (Re-initialize repository without old history.)

aws --endpoint-url=http://localhost:4566 \
    kinesis create-stream \
    --stream-name ${PREDICTIONS_STREAM_NAME} \
    --shard-count 1

pipenv run python test_docker.py

ERROR_CODE=$?

if [ ${ERROR_CODE} != 0 ]; then
    docker-compose logs
    docker-compose down
    exit ${ERROR_CODE}
fi

pipenv run python test_kinesis.py

ERROR_CODE=$?

if [ ${ERROR_CODE} != 0 ]; then
    docker-compose logs
    docker-compose down
    exit ${ERROR_CODE}
fi

<<<<<<< HEAD
docker-compose down
=======
docker-compose down
>>>>>>> 8c93d3a (Re-initialize repository without old history.)
