import streamlit
import requests

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




def get_fruityvice_data(this_fruit_choice):
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen
return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
if not fruit choice:
   streamlit.write('The user entered ', fruit_choice)
else:
      back_from_function = get_fruityvice_data(fruit_choice)
     streamlit.dataframe(back_from_function)


   
# json files normalize code below
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

#import urllib.error 
#import urlError

streamlit.stop()

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

streamlit.header("The Fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
     my_cur.execute("SELECT * from fruit_load_list")
     return my_cur.fetchall()
     
 #adding a button function
     if streamlit.button('get fruit load list'):
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_fruit_load_list()
streamlit.dataframe(my_data_rows)



streamlit.text("what Fruit would you like to add?")
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor()as my_cur:
   my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')");
      Return "Thanks for adding", + new_fruit

add_my_fruit = streamlit.text_input('what Fruit would you like to add?')
if streamlit.button('add a fruit to the list'):
 my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
back_from_function = insert_row_snowflake(add my fruit)
   streamlit.text(back_from_function)


