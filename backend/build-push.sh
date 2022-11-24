#!/bin/bash

set -e

[ -f .env ] && . ./.env
[ -f .env.local ] && . ./.env.local

if [ -z ${PRIVATE_DOCKER_REGISTRY} ]; then
    cat ./.docker_pass | docker login -u $USERNAME --password-stdin
    image_name=${USERNAME}/${DOCKER_IMAGE}
else
    image_name=${PRIVATE_DOCKER_REGISTRY}/${DOCKER_IMAGE} 
fi

full_image_name=${image_name}:${DOCKER_IMAGE_TAG}
echo "docker image - ${full_image_name}"

current_branch=$(git branch --show-current)
branch_image_name=${image_name}:${current_branch}
echo "docker image branch - ${branch_image_name}"

commit_hash=$(git log -1 --format=%h)
commit_image_name=${image_name}:${commit_hash}
echo "docker image commit hash - ${commit_image_name}"

docker build \
    --platform linux/arm/v6 \
    --platform linux/amd64 \
    -t ${full_image_name} \
    -t ${branch_image_name} \
    -t ${commit_image_name} .

docker push ${full_image_name} 
docker push ${branch_image_name} 
docker push ${commit_image_name} 

exit 0