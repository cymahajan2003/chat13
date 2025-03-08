from flask import Flask, render_template_string, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

translator = Translator()

LANG_CODES = {
    "Hindi": "hi", "Bengali": "bn", "Telugu": "te", "Marathi": "mr",
    "Tamil": "ta", "Urdu": "ur", "Gujarati": "gu", "Malayalam": "ml",
    "Odia": "or", "Punjabi": "pa", "Kannada": "kn", "Assamese": "as",
    "Maithili": "mai", "Santali": "sat", "Kashmiri": "ks", "Nepali": "ne",
    "Konkani": "kok", "Sindhi": "sd", "Manipuri": "mni", "Bodo": "brx",
    "Dogri": "doi", "Sanskrit": "sa"
}

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get("text", "")
    lang = data.get("lang", "")

    if not text or not lang:
        return jsonify({"error": "Missing text or language"}), 400

    if lang not in LANG_CODES:
        return jsonify({"error": "Invalid language"}), 400

    try:
        translated = translator.translate(text, dest=LANG_CODES[lang])
        return jsonify({"translation": translated.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Translator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
            margin-bottom: 10px;
        }
        select, button {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
        }
        .output {
            margin-top: 20px;
            font-weight: bold;
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Text Translator</h2>
    <textarea id="inputText" placeholder="Enter text..."></textarea>
    
    <select id="language">
        <option value="Hindi">Hindi</option>
        <option value="Bengali">Bengali</option>
        <option value="Telugu">Telugu</option>
        <option value="Marathi">Marathi</option>
        <option value="Tamil">Tamil</option>
        <option value="Urdu">Urdu</option>
        <option value="Gujarati">Gujarati</option>
        <option value="Malayalam">Malayalam</option>
        <option value="Odia">Odia</option>
        <option value="Punjabi">Punjabi</option>
        <option value="Kannada">Kannada</option>
        <option value="Assamese">Assamese</option>
        <option value="Maithili">Maithili</option>
        <option value="Santali">Santali</option>
        <option value="Kashmiri">Kashmiri</option>
        <option value="Nepali">Nepali</option>
        <option value="Konkani">Konkani</option>
        <option value="Sindhi">Sindhi</option>
        <option value="Manipuri">Manipuri</option>
        <option value="Bodo">Bodo</option>
        <option value="Dogri">Dogri</option>
        <option value="Sanskrit">Sanskrit</option>
    </select>

    <button onclick="translateText()">Translate</button>
    
    <div class="output" id="outputText"></div>
</div>

<script>
    function translateText() {
        let text = document.getElementById("inputText").value;
        let lang = document.getElementById("language").value;

        if (text.trim() === "") {
            alert("Please enter text to translate.");
            return;
        }

        fetch("/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text, lang: lang })
        })
        .then(response => response.json())
        .then(data => {
            if (data.translation) {
                document.getElementById("outputText").innerText = data.translation;
            } else {
                alert("Translation failed: " + data.error);
            }
        })
        .catch(error => console.error("Error:", error));
    }
</script>

</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
