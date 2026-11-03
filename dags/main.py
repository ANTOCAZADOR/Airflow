
from airflow.sdk import dag, task
import pendulum


@dag(
    dag_id="hola_mundo",
    description="Mi primer DAG con Apache Airflow",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["aprendizaje"],
)
def hola_mundo():

    @task
    def imprimir_mensaje():
        print("¡Hola Mundo desde Apache Airflow!")

    imprimir_mensaje()


hola_mundo()
