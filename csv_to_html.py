from bs4 import BeautifulSoup
import urllib.parse
import os

def convert_to_faq_format(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    faq_items = []

    # Find all paragraphs (<p>) containing question and answer pairs.
    paragraphs = soup.find_all('p')
    for i in range(0, len(paragraphs), 2):
        question = paragraphs[i].get_text(strip=True)
        answer = paragraphs[i+1].get_text(strip=True)
        faq_items.append((question, answer))

    # Generate the HTML content in FAQ format.
    html = '<html>\n<head>\n<title>FAQs</title>\n</head>\n<body>\n<h1>Frequently Asked Questions</h1>\n<dl>\n'
    for question, answer in faq_items:
        html += f'<dt>{question}</dt>\n<dd>{answer}</dd>\n'
    html += '</dl>\n</body>\n</html>'
    return html

def save_html_file(html_content, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == '__main__':
    input_html_link = "file:///C:/Users/.html"
    output_file_path = "my_faq_page.html"  

    # Parse the file path from the input_html_link
    parsed_url = urllib.parse.urlparse(input_html_link)
    file_path = urllib.parse.unquote(parsed_url.path)

    # Convert 'file:///' to an absolute path on Windows
    if file_path.startswith('/'):
        file_path = file_path[1:]
    file_path = os.path.abspath(file_path)

    with open(file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    faq_page_html = convert_to_faq_format(html_content)
    save_html_file(faq_page_html, output_file_path)

    print(f"FAQ page HTML file generated successfully at '{output_file_path}'.")
