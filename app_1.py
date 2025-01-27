import streamlit as st
from PIL import Image

# Set the title of the website
st.title('Fashion Store')

# Add a description
st.write("""
    Welcome to our fashion store. Browse through our latest collections of trendy outfits, shoes, and accessories.
""")

# Create a sidebar menu for different categories
st.sidebar.title("Categories")
categories = ["Men's Clothing", "Women's Clothing", "Accessories", "Shoes"]

# Let the user select a category
category = st.sidebar.radio("Select a category", categories)

# Display different content based on the selected category
if category == "Men's Clothing":
    st.header("Men's Clothing")
    st.write("Check out our latest men's fashion collection!")
    img = Image.open('jk.jpg')  # Add appropriate image path
    st.image(img, caption="Men's Clothing Collection", use_column_width=True)

elif category == "Women's Clothing":
    st.header("Women's Clothing")
    st.write("Explore the latest trends in women's fashion!")
    img = Image.open('hh.jpg')  # Add appropriate image path
    st.image(img, caption="Women's Clothing Collection", use_column_width=True)

elif category == "Accessories":
    st.header("Accessories")
    st.write("Accessorize your outfit with the best accessories!")
    img = Image.open('pop2.jpg')  # Add appropriate image path
    st.image(img, caption="Accessories Collection", use_column_width=True)

elif category == "Shoes":
    st.header("Shoes")
    st.write("Step up your fashion game with our stylish shoes!")
    img = Image.open('OIP2.jpg')  # Add appropriate image path
    st.image(img, caption="Shoe Collection", use_column_width=True)

# Add a footer
st.markdown("""
    <hr>
    <p style="text-align: center;">&copy; jemzy Fashion Store. All Rights Reserved.</p>
    """, unsafe_allow_html=True)