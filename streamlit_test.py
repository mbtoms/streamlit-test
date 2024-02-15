# import module
import streamlit as st
import time 

# Title
st.title("Hello GeeksForGeeks !!!")


# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")
 
# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
	# display the text if the checkbox returns True value
	st.text("Showing the widget")



# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
	st.success("Male")
else:
	st.success("Female")


# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
					['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)


# multi select box

# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
						['Dancing', 'Reading', 'Sports'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')


# Create a simple button that does nothing
st.button("Click me for no reason")

print('Does this print?')

# Create a button, that when clicked, shows a text
if(st.button("About")):
	st.text("Welcome To GeeksForGeeks!!!")


# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = name.title()
	st.success(result)



# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(level))



@st.cache_data
def expensive_computation(input_data):
	print('in the expensive computation')
    # Perform some expensive computation here
	result = 20 * input_data
	return result

input_data = 2  # Define your input data here

# Use the expensive computation function
result = expensive_computation(input_data)

st.write('a')
st.progress(5)
st.write('b')
with st.spinner('Wait for it...'):    
	time.sleep(5)
	st.balloons()
	
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.line_chart(df)

import requests

response = requests.get('https://api.thecatapi.com/v1/images/search')
cat_url = response.json()[0]['url']
st.image(cat_url, caption='Random Cat Image')


import requests

response = requests.get('https://api.quotable.io/random')
quote = response.json()['content']
author = response.json()['author']
st.write(f'"{quote}" - {author}')


import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.area_chart(df)


import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
df = pd.DataFrame(   np.random.randn(500, 3),   columns=['x','y','z'])
c = alt.Chart(df).mark_circle().encode(   x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)


import pandas as pd
import numpy as np
import streamlit as st
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)