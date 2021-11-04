#!/bin/bash

set -e

if [ -z "$1" ]
  then
    echo "Please enter the directory name where to install the kafka in."
    return 1
fi

# echo -n "Please enter a directory name: "                                            master ✭ ✚ ◼
# read kafka_dir

mkdir -p $kafka_dir  && cd $kafka_dir

curl -O https://dlcdn.apache.org/kafka/2.7.1/kafka_2.13-2.7.1.tgz

curl -O https://dlcdn.apache.org/kafka/2.7.1/kafka_2.13-2.7.1.tgz.sha512

gpg --print-md SHA512 kafka_2.13-2.7.1.tgz | diff - kafka_2.13-2.7.1.tgz.sha512

tar xvzf kafka_2.13-2.7.1.tgz


