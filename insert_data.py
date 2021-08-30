import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()


def package_read_csv(csv_filepath1, csv_filepath2):
    data_file = []

    with open(csv_filepath1, 'r') as reader:
        raw_data_1 = reader.readlines()

    with open(csv_filepath2, 'r') as reader:
        raw_data_2 = reader.readlines()

    for string_data in raw_data_1[1:]:
        raw_list_data = string_data.split(",")

        data_file.append({
            "id": raw_list_data[0] or -1,
            "category": raw_list_data[1] or "No Category",
            "name": raw_list_data[2].replace("\"", "") or "No Name",
            "price": raw_list_data[3] or "No Price",
            "rating": raw_list_data[4] or "No Rating",
            "tour_length": raw_list_data[5] or "No Tour Length",
            "thumbnail_url": raw_list_data[6].replace("/", "\/") or "No Thumbnail URL",
            "start": raw_list_data[7][:-1] or "No Start"
        })

    [data.update(promo=promo_data.replace("\"", "").replace("\'", "")) for data, promo_data in
     zip(data_file, raw_data_2[1:])]

    return data_file


def package_permission_read_csv(csv_filepath):
    data_file = []

    with open(csv_filepath, 'r') as reader:
        raw_data = reader.readlines()

    for string_data in raw_data[1:]:
        raw_list_data = string_data.split(",")

        data_file.append({
            "id": raw_list_data[0] or -1,
            "is_owner": True if raw_list_data[1] == 1 else False,
            "package_id": raw_list_data[2] or -1,
            "user_id": raw_list_data[3][:-1] or -1
        })

    return data_file


def package_insert(config, data, selector=""):
    conn = psycopg2.connect(f"dbname='{config.get('db')}'"
                            f" user='{config.get('user')}' "
                            f"password='{config.get('password')}' "
                            f"host='{config.get('host')}' "
                            f"port='{config.get('port')}'")
    cur = conn.cursor()

    if selector in ['package', 'package_permission']:
        table_name = "tour_api_package"

        if selector == "package_permission":
            table_name = "api_packagepermission"

        sql_string = f"INSERT INTO {table_name} VALUES {data}"

        cur.execute(sql_string)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    db_config = {
        "db": os.getenv("host_db"),
        "user": os.getenv("postgresql_username"),
        "password": os.getenv("postgresql_password"),
        "host": os.getenv("postgresql_host"),
        "port": os.getenv("postgresql_port")
    }

    data_csv = package_read_csv("api_package_selected.csv", "api_package_promo.csv")

    processed_data = [f"({data.get('id')}, '{data.get('category')}', '{data.get('name')}'," \
                      f" '{data.get('promo')}', {data.get('price')}, '{data.get('rating')}'," \
                      f" {data.get('tour_length')}, '{data.get('start')}', '{data.get('thumbnail_url')}')"
                      for data in data_csv]

    processed_data_string = ", ".join(processed_data)

    package_insert(db_config, processed_data_string, selector="package")

    # data_csv = package_permission_read_csv("api_packagepermission.csv")
    #
    # processed_data = [f"({data.get('id')}, {data.get('is_owner')}, {data.get('package_id')}, {data.get('user_id')})"
    #                   for data in data_csv]
    #
    # processed_data_string = ", ".join(processed_data)
    #
    # package_insert(db_config, processed_data_string, selector="package_permission")
