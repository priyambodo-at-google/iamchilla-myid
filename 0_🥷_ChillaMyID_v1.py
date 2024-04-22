import streamlit as st
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)

vNoLabel = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
html_code = """
    Choose your menu from the sidebar to start your experience.
    """

def run():
    st.set_page_config(page_icon="static/usd.ico")
    st.markdown(vNoLabel, unsafe_allow_html=True)
    st.header('🥷 :red[Chilla.MyID]-v1 - ":blue[Human-AI] :green[Collaboration]"', divider="rainbow")
    st.write(html_code)
   
    st.markdown(
        """
        **👈 Select the menu from the sidebar** to start your experience. 
        """
    )
    #st.image("static/penguin-logo.png", width=700)
    #st.sidebar.success("Select the use cases that you would like to see above.")
    st.write("_(The logo image above is created by Google AI using Imagen 2 model.)_")

    st.write("""
    <div style="text-align:center;padding:1em 0;"> 
        <table style="width: 100%;">
        <tr>
            <th style="color: gray; text-align: left;">Current local time in</th>
            <th style="text-align: left;">Jakarta, Indonesia</th>
        </tr>
        <tr>
            <td colspan="2">
            <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=en&size=medium&timezone=Asia%2FJakarta" width="100%" height="115" frameborder="0" seamless></iframe>
            </td>
        </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        This application is maintained by <b>Doddi Priyambodo and Chisiella Alzena</b> (doddi@bicarait.com)   
        """, unsafe_allow_html=True
    )
    
if __name__ == "__main__":
    run()
