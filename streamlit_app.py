import streamlit

streamlit.title("My Mom's New Healthy Diner")
   
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

from urllib.error import URLError
streamlit.header("Fruityvice Fruit Advice!")
try: 
fruit_choice=streamlit.text_input('What fruit would you like information about?','Kiwi')
if not Fruit_choice:
streamlit.error("please select a fruit to get a information.")
else:

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
# json files normalize code below
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
except URLError as e:
streamlit.error()


import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_rows)

streamlit.text("what Fruit would you like to add?")
add_my_fruit = streamlit.text_input('what Fruit would you like to add?','banana')
streamlit.write('Thanks for adding', add_my_fruit)

my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')");
