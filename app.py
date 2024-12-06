import streamlit as st


# App Title

st.set_page_config(

    page_title="🌍 Global Environmental Data Dashboard",

    page_icon="🌍",

    layout="wide",

    initial_sidebar_state="expanded",

)


st.title("🌍 Global Environmental Data Dashboard")


# Sidebar Navigation

st.sidebar.title("🌿 Navigation Menu")

page = st.sidebar.radio(

    "📜 Choose a section:",

    ["🏠 Home", "🌡️ Temperature", "🌧️ Precipitation", "🛰️ NDVI"],

    help="Navigate between the different data visualization reports.",

)


# Footer

def footer():

    st.markdown(

        """

        ---

        <div style="text-align: center;">

            Developed with ❤️ by [Sinwar team ] | 

            🌐 [GitHub] • 🐦 [Twitter]

        </div>

        """,

        unsafe_allow_html=True,

    )


# Define dynamic page content

if page == "🏠 Home":

    st.subheader("🌍 Tableau de bord interactif sur les données météorologiques")

    st.markdown(

        """

        <div style="font-size: 1.2rem; line-height: 1.8; color: #444;">

        🌟 Bienvenue sur le tableau de bord des données météorologiques interactif !
        Cette application vous permet d'explorer en profondeur des variables météorologiques 
        critiques grâce à des visualisations innovantes et interactives. Découvrez les tendances 
        et les patterns météorologiques à travers plusieurs dimensions :

       🌡️ Température : Suivez les fluctuations de température à l'échelle globale 
          et régionale pour mieux comprendre les variations climatiques.

       🌧️ Précipitations : Analysez les tendances de la pluie et des autres 
          formes de précipitations sur différentes périodes et zones géographiques.

       🌬️ Conditions Météorologiques en Temps Réel : Visualisez les conditions 
          actuelles à travers des animations interactives basées sur les API météorologiques.

       🛰️ Prévisions à Court Terme : Suivez les prévisions météorologiques pour les jours à venir, adaptées à vos 
           besoins en matière de planification et de prise de décision.

        

        Leverage these insights to make data-driven decisions, whether you're a policymaker, researcher, or environmental enthusiast!

        </div>

        """,

        unsafe_allow_html=True,

    )

    # st.image("https://source.unsplash.com/1024x400/?nature,environment", caption="Environmental Insights at Your Fingertips 🌎")


elif page == "🌡️ Temperature":

    st.subheader("🌡️ Global Temperature Trends")

    st.markdown(

        """

        Dive into interactive visualizations to analyze historical and recent temperature changes. Understand how global warming and regional climate changes are shaping the planet.

        """,

        unsafe_allow_html=True,

    )

    st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; height: auto;">
        <iframe title="Global Temperature Trends"
                width="1024" 
                height="800" 
                src="https://app.powerbi.com/view?r=eyJrIjoiZmY3Y2QzMTctZGNhZC00YTI4LWJhYmItZThiMTFlMzJlYzEzIiwidCI6IjZkOTIxZjkyLWY0Y2UtNGNlMC1hY2ZhLTkyNjg3ODUxMDc4MCJ9"
                frameborder="0" 
                allowFullScreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

    st.info("💡 Tip: Use the interactive filters within the embedded report to explore specific regions or time periods!")


elif page == "🌧️ Precipitation":

    st.subheader("🌧️ Rainfall Patterns and Insights")

    st.markdown(

        """

        Explore rainfall trends across different geographical regions. Understand how precipitation impacts ecosystems, agriculture, and urban planning.

        """,

        unsafe_allow_html=True,

    )

    st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; height: auto;">
        <iframe title="Global Precipitation Trends"
                width="1024" 
                height="800" 
                src="https://app.powerbi.com/view?r=eyJrIjoiZTQ1ZmMwNzItZDUxZC00NDNiLTllMTAtOTYwOTlmY2Q4NjE1IiwidCI6IjZkOTIxZjkyLWY0Y2UtNGNlMC1hY2ZhLTkyNjg3ODUxMDc4MCJ9"
                frameborder="0" 
                allowFullScreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

    st.success("📊 Insights: Correlate rainfall patterns with NDVI trends to understand vegetation growth dynamics.")


elif page == "🛰️ NDVI":

    st.subheader("🛰️ Vegetation Health Monitoring (NDVI)")

    st.markdown(

        """

        Analyze satellite-derived NDVI data to monitor vegetation health, agricultural productivity, and land cover changes.

        """,

        unsafe_allow_html=True,

    )

    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: auto;">
            <iframe title="NDVI Monitoring"
                    width="1024" 
                    height="800" 
                    src="https://app.powerbi.com/view?r=eyJrIjoiM2UxZDBjMzItNmYzMi00MjEyLTkwNTItZTJkMjZmYmNiOTgzIiwidCI6IjZkOTIxZjkyLWY0Y2UtNGNlMC1hY2ZhLTkyNjg3ODUxMDc4MCJ9"
                    frameborder="0" 
                    allowFullScreen="true">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.warning("🌍 Key Insight: NDVI trends are a crucial indicator of environmental health and agricultural sustainability.")


# Add Footer

footer()

