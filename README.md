<h1>GenAI-Powered Financial Assistant for Better Investing Decisions</h1>

<p>This intelligent financial assistant is designed to provide seamless stock market insights and investing guidance. Leveraging advanced AI and real-time financial data, it offers a comprehensive toolset for traders, investors, and finance enthusiasts. Subsequently, it is also very useful for beginner investors.</p>
</hr>
<img src="https://github.com/Prithwish-18/Financial_chatbot/blob/main/images/Output_1.png" alt="Financial chatbot"/>
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
        <li>venv package is already installed in <strong>Python 3.3</strong> or higher. To you can check if venv package is installed or not, by putting this code below in your command prompt: 
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
    Download "finbot.py" and "requirements.txt" in 'source_code' folder from this repository. Then keep those files in the 'Scripts' folder in your virtual environment folder you created before.
  </li>
  <li>
    Then go to this page: <a href="https://aistudio.google.com/apikey">https://aistudio.google.com/apikey</a> and sign in or sign up. Then create a gemini API key and copy the API key code. Therefore paste that API key code at 'API_key' in "finbot.py" as mention below: 
    <pre>
      <code>
            # Open finbot.py file
            # At the top of the code there will be a variable called 'API_KEY'
            # Replace with your actual Gemini API key
            API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # paste here
      </code>
    </pre>
  </li>
  <li>
    Now open command prompt and follow the steps below: 
    <ol>
      <li>Go to 'Scripts' folder in your virtual environment folder by putting this in command prompt: 
        <pre>
          <code>
            cd path/to/Scripts
          </code>
        </pre>
      </li>
      <li>
        Activate your virtual environment.
        <pre>
          <code>
            # replace 'env1' with your virtual environment name
            activate env1
          </code>
        </pre>
      </li>
      <li>
        Then install all required dependencies. Put the code below in command prompt: 
        <pre>
          <code>
            pip install -r requirements.txt
          </code>
        </pre>
      </li>
    </ol>
  </li>
  <li>Now in the same command prompt put the code below: 
    <pre>
      <code>
        streamlit run finbot.py
      </code>
    </pre>
    At first time you have to give your any email id and press 'Enter'.
  </li>
  <li>Then It will open a local server where the chatbot is shown. You can ask whatever you want know about investment, it will give your desired answers. 🤗</li>
</ol>

  </br>

<h2>✨ Some examples </h2>

<ul>
  <li>
    <strong>Prompt:  <em>"Show the graph of stock price of [ company_name ] for [ duration (1 month, 6 months, 1 year, 5 years, max) ]"</em></strong></br></br>
  <img src="https://github.com/Prithwish-18/Financial_chatbot/blob/main/images/output_2.png"/></br></br>
  </li>
  <li>
    <strong>Prompt: <em>"I have 4,00,000 rupees and I am a student. So I want to invest that money. Can you guide me which type of investment will be better for me at my situation ?"</em></strong></br></br>
  <img src="https://github.com/Prithwish-18/Financial_chatbot/blob/main/images/output_3.png"/></br></br>
  </li>
  <li>
    <strong>Prompt: <em>"convert 132 INR to EUR"</em></strong></br></br>
  <img src="https://github.com/Prithwish-18/Financial_chatbot/blob/main/images/output_4.png"/></br></br>
  </li>
  <li>
    <strong>Graph analysis from a uploaded image.</strong></br></br>
    <ol>
      <li>
        <strong>Uploading the image of the graph</strong></br></br>
        <img src="https://github.com/Prithwish-18/Financial_chatbot/blob/main/images/output_5.png"/></br></br>
      </li>
      <li>
        <strong>Prompt: <em>"How would you identify a false breakout in a stock price graph, and what indicators would you use to confirm it ?"</em></strong></br></br>
        <img src="https://github.com/Prithwish-18/Financial_chatbot/blob/main/images/output_6.png"/></br></br>
      </li>
      <li>
        <strong>Reply from the chatbot</strong></br></br>
        <img src="https://github.com/Prithwish-18/Financial_chatbot/blob/main/images/output_7.png"/></br></br>
      </li>
    </ol>
  </li>
</ul>

