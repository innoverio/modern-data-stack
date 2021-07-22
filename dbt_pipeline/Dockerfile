FROM python:3.8-buster

RUN pip install -I dbt==0.20.0

RUN pip install git+https://github.com/mdesmet/dbt-presto.git@master

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagit and dagster-daemon, and to load the DagsterInstance

RUN pip install \
    dagster \
    dagster-postgres \
    dagster-docker \
    dagster-dbt

# Set $DAGSTER_HOME and copy dagster instance there

ENV DAGSTER_HOME=/opt/dagster/dagster_home

RUN mkdir -p $DAGSTER_HOME

COPY dagster.yaml $DAGSTER_HOME

# Add repository code

WORKDIR /opt/dagster/app

COPY repo.py /opt/dagster/app
ADD dbt_project /opt/dagster/app/

# Run dagster gRPC server on port 4000

EXPOSE 4000

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-f", "repo.py"]