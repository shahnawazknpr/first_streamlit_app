import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parent New Healthy Diner')
streamlit.header('Breakfast Favourite')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale Spinach & Rocket Smoothie')
streamlit.text('🧀 Hard Biled Free-range eggs')
streamlit.text('🥑🥪Avacado Toast')
streamlit.header('🍓🍒Build your own Fruit Smoothie🥕🌽')

##import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section tp display fruityvice API responce
streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
  streamlit.error("Please select a fruit get the information.")
  else:
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)     
except URLError as e:
streamlit.error()



# stop execution 
streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit Load list contains:")
streamlit.dataframe(my_data_row)

# Allow end user to add fruit from the list
fruit_choice = streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('The user entered ', fruit_choice)

streamlit.write('Thanks for adding', fruit_choice)
my_cur.execute ("insert into pc_rivery_db.public.fruit_load_list values ('From Streamlt')")

