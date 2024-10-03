from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Q&A Dictionary for keyword-based responses
# responses = {
#     'python': 'Python is a powerful programming language used for backend development, data analysis, and AI.',
#     'web scraping': 'Web scraping is the process of extracting data from websites using libraries like BeautifulSoup or Scrapy.',
#     'django': 'Django is a high-level Python web framework that encourages rapid development and clean design.'
# }
responses = {
    'greetings': {
        'hi': 'Hello! How can I help you today?',
        'hello': 'Hi there!',
        'hey': 'Hey! What can I do for you?',
    },
    'qa': {
        'flask': 'Flask is a micro web framework for Python that allows for building web applications quickly and easily.',
        'react': 'React is an open-source library for building user interfaces in web development.',
        'vue.js': 'Vue.js is an open-source JavaScript framework for building user interfaces.',
        'angular': 'Angular is an open-source web application framework for building single-page applications.',
        'leak': 'The leak detection instruments for quality manufacturing are designed to detect leaks in systems and equipment, ensuring that products are manufactured to the highest standards of quality and safety.',
        'what are the test instruments': '''
                    a. Sentinel Blackbelt Pro 

                    b. Sentinel Blackbelt 

                    c. Sentinel I28 

                    d. Sentinel LPC 528 

                    e. Sentinel C28WE 

                    f. Sentinel C20WE 

                    g. Sentinel MH 

                    h. Sentinel 3520  

                    i. TracerMate II 
                    

                    ''',
        'accurate testing for every application':
                    '''
                        Not every application is complex. There are times when a simple leak tester is the best fit. For basic applications, Cincinnati Test Systems has several simple, low-cost leak testing options that can accommodate single-test options. Despite their simplicity, these leak testers offer quick cycle time, superior performance and accuracy, and easy maintenance. 


                        Sentinel MH

                        Sentinel C20WE 

                        Sentinel C28WE 

                        LPC-528
                    ''',
        ('what types of leak test instruments does cts offer',
         'which leak testing products are available at cts',
         'what kinds of testers does cts provide',
         'can you list the main cts leak test instruments',
         'does cts offer instruments for multiple testing methods',
         'what models of leak testers does cts have'): 'CTS offers various leak test instruments, including Sentinel Blackbelt Pro, Sentinel I28, and TracerMate II. These instruments handle different testing methods such as pressure decay, vacuum testing, mass flow, and tracer gas detection, making them versatile for industries like automotive, medical, and electronics manufacturing.',

         ('how does cts improve product quality in manufacturing',
          'how do CTS testers enhance manufacturing quality',
           'can CTS help in reducing product defects',
            'why is CTS leak testing essential in quality control',
             'how does CTS contribute to product safety',
              'what role does CTS play in improving manufacturing quality' ):'CTS ensures high-quality manufacturing by providing precise leak detection, helping identify defects early in the production process. Their instruments are widely used in automotive, medical devices, and packaging industries, ensuring that products meet safety and reliability standards, reducing waste, and maintaining consistency.',
        
    }
}

# View for the chat interface
def index(request):
    return render(request, 'chat/index.html')

# Function to handle bot responses
def get_response(request):
    user_input = request.GET.get('message').lower()

    # Check for greetings
    for greet in responses['greetings']:
        if greet in user_input:
            return JsonResponse({'response': responses['greetings'][greet]})

    # Check for Q&A keywords
    for questions, answer in responses['qa'].items():
        if isinstance(questions, tuple):
            for question in questions:
                if all(word in user_input for word in question.split()):
                    return JsonResponse({'response': answer})
        elif questions in user_input:
            return JsonResponse({'response': answer})

    # Default response if no keyword is matched
    return JsonResponse({'response': "I'm not sure I understand. Can you ask something else?"})

    # If no match, perform web scraping as fallback
    scraped_data = scrape_data("https://example.com")
    return JsonResponse({'response': f"I couldn't find an answer, but here's some info: {scraped_data}"})

# Function to perform web scraping
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract relevant data from the page (example)
    data = soup.find('div', class_='info').text
    return data
