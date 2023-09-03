import psycopg2

try:
    connection = psycopg2.connect(
                                  database="amjh_spp",
                                  user='amjh_spp_user', 
                                  password='YAaeYsk9BRASYglVLOYxGuqbuzO1K19u',
                                  host='dpg-c97u22397ej8dpgdvim0-a.oregon-postgres.render.com',
                                  port= '5432'
                                 )
    cursor = connection.cursor()
    print("Connection OK") 

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)