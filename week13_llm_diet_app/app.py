from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # replace with your key

def generate_plan(bmi, age, gender):
    prompt = f"""
    A {age}-year-old {gender} has a BMI of {bmi}.
    Based on this information, generate a detailed one-month diet plan
    and one-month exercise plan tailored to their needs.
    Be specific with weekly meal suggestions and workout routines.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    plan = None
    if request.method == 'POST':
        bmi = request.form['bmi']
        age = request.form['age']
        gender = request.form['gender']
        plan = generate_plan(bmi, age, gender)
    return render_template('index.html', plan=plan)

if __name__ == '__main__':
    app.run(debug=True)

from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

def generate_plan(bmi, age, gender):
    prompt = f"""
    A {age}-year-old {gender} has a BMI of {bmi}.
    Generate a detailed one-month diet plan and one-month exercise plan for them.
    Be specific with weekly meal suggestions and workout routines.
    """
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
