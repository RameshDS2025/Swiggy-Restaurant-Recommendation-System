import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import warnings
import base64
warnings.filterwarnings('ignore')


#To set the background image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()  #  only read on

# Path to your background image
image_base64 = get_base64_of_bin_file(r"images.png")

st.markdown(
    f"""
    <style>
    /* Main page background */
    [data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{image_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}
    /* MAIN CONTENT → background image */
    div[data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* SIDEBAR → keep green */
    section[data-testid="stSidebar"] {{
        background-color: #29d66e;
    }}

    /* Sidebar labels */
    section[data-testid="stSidebar"] label {{
        color: #1f2a44;
        font-weight: 600;
    }}

    /* Multiselect box */
    section[data-testid="stSidebar"]
    div[data-baseweb="select"] > div {{
        background-color: #9c3535 !important;
        border-radius: 8px !important;
    }}

    /* Multiselect text */
    section[data-testid="stSidebar"]
    div[data-baseweb="select"] span {{
        font-weight: 700 !important;
        color: #ffffff !important;
    }}

    /* Header transparent */
    header[data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    /* Reduce padding */
    .block-container {{
        padding-top: 0rem;
        padding-bottom: 1rem;
    }}

    /* Multiselect selected pill (Only city style) */
    div[data-baseweb="tag"] {{
    background-color: #e6e6e6 !important;
    color: #555 !important;
    font-style: italic;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SIDEBAR LOG
# --------------------------------------------------
st.sidebar.image("images1.png", width=150)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.markdown(
    """
    <h3 style="color:#3b0704; font-family:'Old English Text MT','Blackletter',serif;">
        🍴 Swiggy Restaurant Recommendation System
    </h3>
    """,
    unsafe_allow_html=True
)

About_us = st.sidebar.button("About us", type="primary")

Food = st.sidebar.button("Food Trends", type="primary")

india = st.sidebar.button("All Over India", type="primary")

Tech = st.sidebar.button("Food and Technology", type="primary")

Contact = st.sidebar.button("Contact Us", type="primary")

Locate = st.sidebar.button("Locate a Restaurant", type="primary")


if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True

# If any button is clicked, hide the welcome

if any([
    About_us, Food, india, Tech, Contact,
]):
    st.session_state.show_welcome = False
    st.session_state.show_welcome = True

if About_us:
    st.session_state.current_page = "about"
elif Food:
    st.session_state.current_page = "food"
elif india:
    st.session_state.current_page = "india"
elif Tech:
    st.session_state.current_page = "tech"
elif Contact:
    st.session_state.current_page = "contact"
elif Locate:
    st.session_state.current_page = "locate"

#  Animated Welcome Messag
if st.session_state.current_page == "home":
    st.markdown("""
        <style>
        @keyframes moveArrowLeft {
            0% {transform: translateX(0);}
            50% {transform: translateX(-15px);}
            100% {transform: translateX(0);}
        }
        .arrow {
            display: inline-block;
            color: #E63946;
            font-size: 48px;
            font-weight: bold;
            animation: moveArrowLeft 1.2s infinite ease-in-out;
            margin-right: 12px;
        }
        .welcome {
            text-align: center;
            margin-top: 20px;
            margin-bottom: 30px;
            font-family: 'Trebuchet MS', sans-serif;
            font-size: 36px;
            font-weight: bold;
            color: #4b064f;
        }
        .highlight {
            color: #274091;
        }
        </style>

        <div class="welcome">
            👋 Welcome to <span class="highlight">🍴 Swiggy Restaurant Recommendation System!</span><br>
            <span class="arrow">←</span> Explore insightful food recommendations from the sidebar
        </div>
    """, unsafe_allow_html=True)

# Left-align content below buttons
if st.session_state.current_page == "about":

    st.markdown("""
            <div style="background-color:transparent; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">About Us</h3>
            
            <p style="color:#180a29; font-size:16px; text-align:left;"> 
                This project is a Swiggy-based Restaurant Recommendation System designed to help users 
                discover restaurants and food options across India using data-driven insights. It 
                analyzes food trends, cuisines, ratings, and cost patterns to recommend the most 
                relevant restaurants based on user preferences. The system covers restaurants from 
                multiple cities all over India, providing location-specific insights and recommendations. 
                Machine learning techniques such as clustering and similarity analysis are used to group 
                restaurants and enhance recommendation accuracy. The project also highlights emerging 
                food trends by analyzing popular cuisines and high-demand areas. By combining food data 
                with modern technology, this application demonstrates how data science can improve food 
                discovery and customer experience in real-world platforms like Swiggy.
            </p>

            """, unsafe_allow_html=True)

if st.session_state.current_page == "food":
        st.markdown("""
            <div style="background-color:transparent; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">Food Trends</h3>
            
            <p style="color:#180a29; font-size:16px; text-align:left;"> 
                This section analyzes food consumption patterns across different cities in India using Swiggy 
                restaurant data. It explores how customer food preferences change based on location, cuisine 
                type, and price range. The system identifies popular cuisines and frequently ordered food items 
                across regions. By examining ratings, order volume, and cost trends, it highlights emerging 
                and declining food preferences. The analysis compares budget-friendly and premium dining trends 
                across cities. These insights help users understand changing food habits and discover trending 
                food options based on real customer data.
                
            <h4 style="color:#061f38;">Key Insights Provided</h4>

            <ul style="color:#061f38; font-size:15px; line-height:1.8;">
                <li>City-wise popular cuisines and food items</li>
                <li>Frequently ordered dishes across regions</li>
                <li>Emerging cuisine trends in different cities</li>
                <li>Budget-friendly vs premium dining preferences</li>
                <li>Rating and order-volume based popularity analysis</li>
            </ul>

            </p>

            """, unsafe_allow_html=True)

if st.session_state.current_page == "india":

    st.markdown("""
            <div style="background-color:transparent; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">All Over India</h3>
            
            <p style="color:#180a29; font-size:16px; text-align:left;"> 
            India’s food culture is highly diverse and deeply influenced by regional traditions and 
                local ingredients. Each region offers unique cuisines, flavors, and cooking styles 
                that reflect its cultural heritage. North Indian, South Indian, Mughlai, and regional 
                street foods contribute to a rich and varied food ecosystem. This project analyzes 
                restaurant data collected from cities across India to capture this diversity. It 
                examines how food preferences differ between regions and cities. The system identifies 
                popular cuisines and frequently ordered food items. Customer ratings and order volume 
                are used to understand demand patterns. The analysis highlights regional specialties 
                and local food favorites. It also tracks emerging food trends driven by changing 
                lifestyles. The project compares traditional food choices with modern dining preferences. 
                Pricing data helps analyze affordability across regions. Urban and semi-urban food 
                trends are compared for deeper insights. These patterns reflect shifts in customer 
                behavior over time. Data-driven insights help users explore food diversity effectively. 
                Overall, the system showcases India’s evolving food market through analytics.
            </p>

            """, unsafe_allow_html=True)
    
if st.session_state.current_page == "tech":

    st.markdown("""
            <div style="background-color:transparent; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">Food and Technology</h3>
            
            <p style="color:#180a29; font-size:16px; text-align:left;"> 
            Technology plays a vital role in transforming how people discover and order food in India. This 
                project demonstrates how data science and analytics can enhance food recommendation systems. 
                By using Swiggy restaurant data, the system processes large volumes of information efficiently. 
                Machine learning techniques are applied to analyze customer preferences and restaurant attributes. 
                Data preprocessing and feature engineering help improve data quality and accuracy. Recommendation 
                algorithms identify similar restaurants based on cuisine, location, and pricing. Clustering 
                techniques group restaurants with similar characteristics. Visualization tools are used to present 
                insights in an interactive manner. The Streamlit framework enables real-time user interaction 
                with the data. Users can filter restaurants based on their preferences easily. Technology helps 
                uncover hidden food trends across regions. Data-driven insights support smarter food discovery 
                decisions. The system bridges traditional food culture with modern digital platforms. It 
                highlights how technology improves customer experience. Overall, this project showcases the 
                power of technology in the food industry.
            </p>

            """, unsafe_allow_html=True)
    
if st.session_state.current_page == "contact":

    st.markdown("""
            <div style="background-color:transparent; padding:20px; border-radius:10px;">
            <h3 style="color:#800000;">Contact Us</h3>
            
            <p style="color:#180a29; font-size:16px; text-align:left;"> 
            #412, 5th Cross Road, <br>
            Bengaluru, Karnataka,  <br>
            India - 560038.
            </p>

            """, unsafe_allow_html=True)
    
# --------------------------------------------------
# LOAD DATA & MODEL
# --------------------------------------------------
df_clean = pd.read_csv("cleaned_with_clusters.csv")

encoder = pickle.load(open("encoder.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
kmeans = pickle.load(open("kmeans_model.pkl", "rb"))

# --------------------------------------------------
# RESTAURANT FILTERS
# --------------------------------------------------

# ---------------- CITY FILTER ----------------

if st.session_state.current_page == "locate":

    st.subheader("📍 Choose the below options to Locate a Restaurant")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        city = st.multiselect(
            "Select City",
            sorted(df_clean["city"].dropna().unique()),
            key="city_filter"
        )

        if not city:
            df_city = df_clean.copy()
        else:
            df_city = df_clean[df_clean["city"].isin(city)]

        st.write(f"🍽️ Restaurants found: {len(df_city)}")

    # ---------------- AREA FILTER ----------------
    with col2:
        if not city:
            st.markdown(
                "<p style='color:#6b6b6b; font-style:italic;'>Select city first</p>",
                unsafe_allow_html=True
            )
            df_area = df_city.copy()

        else:
            area_options = sorted(
                df_city.loc[df_city["Area"] != "Only city", "Area"]
                .dropna()
                .unique()
            )

            if len(area_options) == 0:
                st.markdown(
                    "<p style='color:#6b6b6b; font-weight:600;'>Only city</p>",
                    unsafe_allow_html=True
                )
                df_area = df_city.copy()

            else:
                area = st.multiselect(
                    "Select Area",
                    area_options,
                    key="area_filter"
                )

                if not area:
                    df_area = df_city.copy()
                else:
                    df_area = df_city[df_city["Area"].isin(area)]

    # ---------------- CUISINE FILTER ----------------
    with col3:
        cuisine = st.multiselect(
            "Select Cuisine",
            sorted(df_area["cuisine"].dropna().unique()),
            key="cuisine_filter"
        )

        if not cuisine:
            df_cuisine = df_area.copy()
        else:
            df_cuisine = df_area[df_area["cuisine"].isin(cuisine)]

        st.write(f"🍽️ Restaurants found: {len(df_cuisine)}")

    # ---------------- ITEM FILTER ----------------
    with col4:
        if not cuisine:
            st.markdown(
                "<p style='color:#6b6b6b; font-style:italic;'>Select cuisine first</p>",
                unsafe_allow_html=True
            )
            df_item = df_cuisine.copy()

        else:
            item_options = sorted(
                df_cuisine.loc[df_cuisine["Item"] != "Only cuisine", "Item"]
                .dropna()
                .unique()
            )

            if len(item_options) == 0:
                st.markdown(
                    "<p style='color:#6b6b6b; font-weight:600;'>Only Cuisine</p>",
                    unsafe_allow_html=True
                )
                df_item = df_cuisine.copy()

            else:
                item = st.multiselect(
                    "Select Area",
                    item_options,
                    key="item_filter"
                )

                if not item:
                    df_item = df_cuisine.copy()
                else:
                    df_item = df_cuisine[df_cuisine["Item"].isin(item)]

    col5, col6 = st.columns(2)

# ---------------- RATING SLIDER ----------------

    with col5:
        df_rating = df_item.copy()

        rating_range = None

        if df_rating.empty:
            st.info("No rating data available")

        else:
            min_rating = float(df_rating["rating"].min())
            max_rating = float(df_rating["rating"].max())

            if min_rating == max_rating:
                st.markdown(
                    f"<p><b>⭐ Rating:</b> {min_rating}</p>",
                    unsafe_allow_html=True
                )
                rating_range = (min_rating, max_rating)

            else:
                rating_range = st.slider(
                    "⭐ Rating",
                    min_value=0.0,
                    max_value=5.0,
                    value=(min_rating, max_rating),
                    step=0.1
                )

            df_rating = df_rating[
                (df_rating["rating"] >= rating_range[0]) &
                (df_rating["rating"] <= rating_range[1])
            ]

    # ---------------- COST SLIDER ----------------

    with col6:
        df_cost = df_rating.copy()

        # DEFAULT → always defined
        cost_range = None

        if df_cost.empty:
            st.info("No cost data available")

        else:
            min_cost = int(df_cost["cost"].min())
            max_cost = int(df_cost["cost"].max())

            # Case 1: only one unique cost
            if min_cost == max_cost:
                st.markdown(
                    f"<p><b>💰 Cost (₹):</b> {min_cost}</p>",
                    unsafe_allow_html=True
                )
                cost_range = (min_cost, max_cost)

            # Case 2: multiple values → slider
            else:
                cost_range = st.slider(
                    "💰 Cost (₹)",
                    min_value=min_cost,
                    max_value=max_cost,
                    value=(min_cost, max_cost),
                    step=50
                )

            #Apply filter safely
            df_cost = df_cost[
                (df_cost["cost"] >= cost_range[0]) &
                (df_cost["cost"] <= cost_range[1])
            ]


st.markdown("""
<style>
/* Recommendation section container */
.reco-container {
    background: rgba(230, 240, 255, 0.92);
    padding: 25px;
    border-radius: 16px;
    margin-top: 20px;
}

/* Recommendation cards */
.reco-card {
    background: linear-gradient(135deg, #a081e6, #ffffff);
    padding: 15px;
    border-radius: 14px;
    margin-bottom: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

if st.session_state.current_page == "home":
    
    st.markdown("""
    <div class="reco-container">
        <h2 style="color:#800000;">🍽️ Recommended Restaurants</h2>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.current_page == "locate":

    st.markdown("---")
    st.subheader("🎯 Recommended Restaurants")

    # Columns used during training
    cat_cols = ["Area", "city", "Item", "cuisine"]

    if "df_cost" not in locals():
        df_cost = df_clean.copy()

    final_df = df_cost.copy()

    if final_df.empty:
        st.warning("⚠️ No restaurants found for selected filters.")
    else:
        # ENCODE
        encoded_filtered = encoder.transform(final_df[cat_cols])
        encoded_filtered_df = pd.DataFrame(
            encoded_filtered,
            columns=encoder.get_feature_names_out(cat_cols)
        )

        # SCALE
        scaled_filtered = scaler.transform(encoded_filtered_df)

        # PREDICT CLUSTER
        final_df["cluster"] = kmeans.predict(scaled_filtered)
        target_cluster = final_df["cluster"].mode()[0]

        # RECOMMENDATIONS (SAFE)
        recommendations = df_clean[
            (df_clean["cluster"] == target_cluster) &
            (df_clean["city"].isin(city))
        ].copy()

        # Optional area filter
        if "area" in locals() and area:
            recommendations = recommendations[
                recommendations["Area"].isin(area)
            ]

        # Apply rating & cost filters
        recommendations = recommendations[
            (recommendations["rating"] >= rating_range[0]) &
            (recommendations["rating"] <= rating_range[1]) &
            (recommendations["cost"] >= cost_range[0]) &
            (recommendations["cost"] <= cost_range[1])
        ]

        recommendations = recommendations.sort_values(
            by=["rating", "rating_count"],
            ascending=False
        ).head(10)

        # DISPLAY
        cols = st.columns(2)
        for i, (_, row) in enumerate(recommendations.iterrows()):
            with cols[i % 2]:
                st.markdown(
                    f"""
                    <div style="background-color:#a081e6;
                                padding:15px;
                                border-radius:12px;
                                margin-bottom:15px;">
                        <h4>🍴 {row['name']}</h4>
                        <p><b>City:</b> {row['city']}</p>
                        <p><b>Area:</b> {row['Area']}</p>
                        <p><b>Item:</b> {row['Item']}</p>
                        <p><b>Cuisine:</b> {row['cuisine']}</p>
                        <p><b>Rating:</b> ⭐ {row['rating']}</p>
                        <p><b>Cost:</b> ₹ {row['cost']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
