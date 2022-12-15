import streamlit

streamlit.title('My Parent New Healthy Diner')

streamlit.header('Breakfast Favourite')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale Spinach & Rocket Smoothie')
streamlit.text('🧀 Hard Biled Free-range eggs')
streamlit.text('🥑🥪Avacado Toast')

streamlit.header('🍓🍒Build your own Fruit Smoothie🥕🌽')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)


