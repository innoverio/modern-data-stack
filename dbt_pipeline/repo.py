from dagster import pipeline, repository, schedule, solid, ModeDefinition
from dagster_dbt import dbt_cli_resource

my_dbt_resource = dbt_cli_resource.configured({"profiles_dir": "."})

@solid(required_resource_keys={"dbt"})
def run_all_models(context):
    context.resources.dbt.run()

@pipeline(mode_defs=[ModeDefinition(resource_defs={"dbt": my_dbt_resource})])
def my_dbt_pipeline():
    run_all_models()


@schedule(cron_schedule="0 * * * *", pipeline_name="my_dbt_pipeline", execution_timezone="US/Central")
def my_schedule(_context):
    return {}


@repository
def my_repository():
    return [my_dbt_pipeline, my_schedule]