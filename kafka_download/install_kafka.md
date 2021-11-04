



Download kafka

mkdir kafka_download && cd kafka_download

set -e

curl -O https://dlcdn.apache.org/kafka/2.7.1/kafka_2.13-2.7.1.tgz
curl -O https://dlcdn.apache.org/kafka/2.7.1/kafka_2.13-2.7.1.tgz.sha512
gpg --print-md SHA512 kafka_2.13-2.7.1.tgz | diff - kafka_2.13-2.7.1.tgz.sha512
tar xvzf kafka_2.13-2.7.1.tgz


./kafka-consumer-groups.sh

--export                                Export operation execution to a CSV
                                          file. Supported operations: reset-
                                          offsets.
--from-file <String: path to CSV file>  Reset offsets to values defined in CSV
                                          file.


 Links:

 - https://dlcdn.apache.org/kafka/2.7.1/
 - https://www.apache.org/info/verification.html (it doesn't work. Apache Kafka uses GPG)
- https://linuxhandbook.com/bash-arguments/
- https://stackoverflow.com/a/6482403/1102761
- https://stackoverflow.com/a/255416/1102761
