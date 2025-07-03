'''
=================================================
Milestone 3

Nama  : Iriel Aureleo
Batch : FTDS-027-HCK

Program ini dibuat untuk melakukan automatisasi proses load data dari PostgreSQL, melakukan transformasi dan pembersihan data, lalu mengirimkan hasilnya ke Elasticsearch untuk keperluan visualisasi di Kibana.
Adapun dataset yang digunakan adalah IBM HR Analytics Attrition Dataset, yang berisi informasi terkait profil karyawan dan status attrition mereka, guna mendukung analisis retensi karyawan di IBM Indonesia.
=================================================
'''

import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from elasticsearch import Elasticsearch, helpers
import time

# Default args
default_args = {
    'owner': 'Iriel Aureleo',
    'start_date': datetime(2024, 11, 1)
}

# Define DAG
with DAG(
    'P2M3_iriel_aureleo_DAG',
    description='ETL from PostgreSQL to Elasticsearch - Milestone 3',
    schedule_interval='10,20,30 9 * * 6',  # Setiap Sabtu pukul 09:10, 09:20, 09:30
    default_args=default_args,
    catchup=False
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task
    def extract_from_postgresql():
        """Fetch from PostgreSQL: ambil data dan simpan ke CSV mentah."""
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        url = f'postgresql+psycopg2://{username}:{password}@{host}/{database}'
        engine = create_engine(url)
        conn = engine.connect()

        df = pd.read_sql_query("SELECT * FROM table_m3", conn)
        df.to_csv('/opt/airflow/data/P2M3_iriel_aureleo_data_raw.csv', sep=',', index=False)

    @task
    def data_cleaning():
        """Data Cleaning: bersihkan data dan simpan ke CSV clean."""
        df = pd.read_csv('/opt/airflow/data/P2M3_iriel_aureleo_data_raw.csv')

        # Hapus duplikat
        df = df.drop_duplicates()

        # Normalisasi nama kolom
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'[^0-9a-zA-Z_]', '', regex=True)

        # Buang baris yang memiliki >50% kolom kosong
        df = df.dropna(thresh=int(0.5 * df.shape[1]))

        # Imputasi missing values
        num_cols = df.select_dtypes(include='number').columns
        cat_cols = df.select_dtypes(include='object').columns

        df[num_cols] = df[num_cols].fillna(df[num_cols].median())
        for col in cat_cols:
            df[col] = df[col].fillna(df[col].mode()[0])

        df.to_csv('/opt/airflow/data/P2M3_iriel_aureleo_data_clean.csv', sep=',', index=False)

    @task
    def post_to_elasticsearch():
        '''Function ini berfungsi untuk mengupload data ke elasticsearch'''
        time.sleep(10)  # beri waktu agar ES siap menerima koneksi

        try:
            es = Elasticsearch(
                "http://elasticsearch:9200",
                timeout=60,
                max_retries=5,
                retry_on_timeout=True
            )

            # Hapus index lama jika sudah ada
            if es.indices.exists(index="p2m3_iriel_aureleo"):
                es.indices.delete(index="p2m3_iriel_aureleo")
                print("Index lama dihapus")

            # Baca data dan kirim ulang
            df = pd.read_csv('/opt/airflow/data/P2M3_iriel_aureleo_data_clean.csv')
            df = df.fillna('')
            print(f"Jumlah record yang akan dikirim: {len(df)}")

            records = df.to_dict(orient='records')
            actions = [
                {
                    "_index": "p2m3_iriel_aureleo",
                    "_source": record
                }
                for record in records
            ]

            helpers.bulk(es, actions, chunk_size=250)
            print("Data berhasil dikirim ke Elasticsearch")

        except Exception as e:
            print(f"Gagal mengirim data ke Elasticsearch: {e}")
            raise e

    start >> extract_from_postgresql() >> data_cleaning() >> post_to_elasticsearch() >> end
