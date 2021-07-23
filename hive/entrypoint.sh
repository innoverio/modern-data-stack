#!/bin/sh
export METASTORE_DB_HOSTNAME=${METASTORE_DB_HOSTNAME:-localhost}

echo "Waiting for database on ${METASTORE_DB_HOSTNAME} to launch on 3306 ..."

while ! nc -z ${METASTORE_DB_HOSTNAME} 3306; do
  sleep 1
done

echo "Database on ${METASTORE_DB_HOSTNAME}:3306 started"
echo "Init apache hive metastore on ${METASTORE_DB_HOSTNAME}:3306"

/opt/apache-hive-metastore-3.0.0-bin/bin/schematool -initSchema -dbType mysql
/opt/apache-hive-metastore-3.0.0-bin/bin/start-metastore