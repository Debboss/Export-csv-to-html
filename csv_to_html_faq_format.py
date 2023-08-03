import csv
import os

downloads_folder = f"C:\\Users\\your_name\\folder_name"

input_csv_file = os.path.join(downloads_folder, "input_csv_file.csv")
output_html_file = os.path.join(downloads_folder, "output_faq.html")


with open(input_csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    faq_list = [{"Question": row["Question"], "Answer": row["Answer"]} for row in reader]

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>FAQ Page</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }}
        h1 {{
            text-align: center;
        }}
        .question {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }}
        .answer {{
            font-size: 16px;
            color: #555;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <h1>Frequently Asked Questions</h1>
"""

for faq in faq_list:
    question = faq['Question']
    answer = faq['Answer']


    answer = answer.replace('\n', '<br>')  


    html_content += f"""
    <div class="question">{question}</div>
    <div class="answer">{answer}</div>
    """


html_content += """
</body>
</html>
"""


with open(output_html_file, 'w', encoding='utf-8') as htmlfile:
    htmlfile.write(html_content)

print("Conversion to HTML complete!")
