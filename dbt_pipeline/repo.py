from dagster import pipeline, repository, schedule
from dagster_dbt import dbt_cli_run, dbt_cli_seed

config = {"profiles-dir": "."}
run_all_models = dbt_cli_run.configured(config, name="run_all_models")
run_all_seeds = dbt_cli_seed.configured(config, name="run_all_seeds")

@pipeline
def my_dbt_pipeline():
    run_all_models(start_after=run_all_seeds())


@schedule(cron_schedule="0 * * * *", pipeline_name="my_dbt_pipeline", execution_timezone="US/Central")
def my_schedule(_context):
    return {}


@repository
def my_repository():
    return [my_dbt_pipeline, my_schedule]