import json
import psycopg2
import os

def lambda_handler(event, context):
    user = event['request']['userAttributes']

    print("user Atributies")
    print(user)

    user_display_name= user['name']
    user_email= user['email']
    user_handle= user["preferred_username"]
    cognito_user_id= user['sub']
    try:
      conn = psycopg2.connect(os.getenv('CONNECTION_URL'))
      cur = conn.cursor()
      sql= f"""
        INSERT INTO public.users (display_name, handle, email, cognito_user_id)
          VALUES(
            '{user_display_name}',
            '{user_email}',
            '{user_handle}',
            '{cognito_user_id}'
              )
        """
      print("SQL-----")
      print(sql)
      cur.execute (sql)        
      conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
        
    finally:
      if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')

    return event