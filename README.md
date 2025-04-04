<h1>Financial Chatbot Powered by Gemini API for Stock and Other Investing Assistance</h1>

<p>This intelligent financial assistant is designed to provide seamless stock market insights and investing guidance. Leveraging advanced AI and real-time financial data, it offers a comprehensive toolset for traders, investors, and finance enthusiasts. Subsequently, it is also very useful for beginner investors.</p>

<h2>✨ Features </h2>
<ul>
  <li><strong>Generative AI:</strong> Google’s Gemini API (`gemini-2.0-flash`) for natural language understanding, image analysis, and resource suggestions.</li>
  <li><strong>Financial Data:</strong> `yfinance` for fetching live stock prices and historical trends.</li>
  <li><strong>Currency Conversion:</strong> `forex_python.converter` for real-time exchange rate calculations.</li>
  <li><strong>Web Scraping:</strong> `requests` and `BeautifulSoup` for searching ticker symbols when needed.</li>
  <li><strong>Visualization:</strong> `matplotlib` for plotting stock charts and indicators.</li>
  <li><strong>Frontend:</strong> `streamlit` for an interactive chatbot experience.</li>
  <li><strong>Image Processing</strong> `PIL` and `BytesIO` for handling uploaded images.</li>
  <li><strong>Core Language:</strong> Powered by Python, tying all components together seamlessly.</li>
</ul>

<p>This chatbot simplifies investment research, enhances decision-making, and provides personalized financial insights—all in an intuitive and accessible interface.</p>

<h2>✨ Installation </h2>
<ol>
  <li>Install python. Link: <a href="https://www.python.org/downloads"> https://www.python.org/download</a></li>
  <li>
    Create a virtual environment with help of <strong>'venv'</strong> package.
    <ol>
        <li>venv package is already installed in <strong>Python 3.3</strong> or higher. To you can check if venv packageis installed or not, by putting this code below in your command prompt: 
            <pre>
            <code>python -m venv --help</code>
            </pre> </li>
        <li>
            Go to your path of the project and copy the path. Then, put the code below and replace "path\to\your\project" with the copied path of your project in the command prompt:
            <pre>
            <code>
                cd path\to\your\project
            </code>
            </pre>
        </li>
        <li>
            Create your virtual environment. By running the code below in command prompt: 
            <pre>
            <code>
                # replace 'env1' with your environment name
                python -m venv env1
            </code>
            </pre>
        </li>
        <li>
            Go to 'Scripts' folder in your environment. Put the code below in command prompt: 
            <pre>
            <code>
                cd Scripts
            </code>
            </pre>
        </li>
        <li>Activate your virtual environment. Put this code in command prompt: 
          <pre>
            <code>
            # put your environment name by replacing 'env1'
            env1\Scripts\activate env1
            </code>
          </pre>
        </li>
    </ol>
  </li>
  <li>
    Download "finbot.py" and "requirements.txt" from this repository. Then keep those files in the 'Scripts' folder in your machine.
  </li>
  <li>
    Then go to this page: <a href="https://aistudio.google.com/apikey">https://aistudio.google.com/apikey</a> and sign in or sign up. Then create a gemini API key and copy the API key code. Therefore paste that code at 'API_key' in "finbot.py" as mention below: 
    <pre>
      <code>
            # Open finbot.py file
            # At the top of the code there will be a variable called 'API_KEY'
            import google.generativeai as genai
            import yfinance as yf
            import matplotlib.pyplot as plt
            import pandas as pd
            import streamlit as st
            from io import BytesIO
            from forex_python.converter import CurrencyRates, get_currency_name
            import re
            import requests
            from bs4 import BeautifulSoup
            from PIL import Image
            import cv2
            import numpy as np
            import os
            # Replace with your actual Gemini API key
            API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your actual Gemini API key
      </code>
    </pre>
  </li>
</ol>
  

