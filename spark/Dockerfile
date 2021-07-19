ARG OPENJDK_VERSION=8
FROM openjdk:${OPENJDK_VERSION}-jre-slim

ARG BUILD_DATE
ARG SPARK_VERSION=3.0.2
ARG HADOOP_VERSION=3.2

LABEL org.label-schema.name="Apache Spark ${SPARK_VERSION}" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.version=$SPARK_VERSION      
      
ENV SPARK_HOME /usr/spark
ENV PATH="/usr/spark/bin:/usr/spark/sbin:${PATH}"
  
RUN apt-get update && \
    apt-get install -y wget netcat procps libpostgresql-jdbc-java && \
    wget -q "http://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    tar xzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    mv "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}" /usr/spark && \
    ln -s /usr/share/java/postgresql-jdbc4.jar /usr/spark/jars/postgresql-jdbc4.jar && \
    wget -q https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/0.11.1/iceberg-spark3-runtime-0.11.1.jar -O iceberg-spark3-runtime-0.11.1.jar && \
    mv iceberg-spark3-runtime-0.11.1.jar /usr/spark/jars/ && \ 
    apt-get remove -y wget && \
    apt-get autoremove -y && \
    apt-get clean

COPY conf/spark-defaults.conf /usr/spark/conf/spark-defaults.conf

# COPY entrypoint.sh /scripts/
# RUN chmod +x /scripts/entrypoint.sh
# ENTRYPOINT ["/scripts/entrypoint.sh"]

CMD ["start-master.sh"]