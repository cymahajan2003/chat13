const translate = require('google-translate-api-x');

const text = "Hello, how are you?";  // Change this to the text you want to translate

const languages = {
    "as": "Assamese", "bn": "Bengali", "gu": "Gujarati", "hi": "Hindi", "kn": "Kannada",
    "ks": "Kashmiri", "ml": "Malayalam", "mr": "Marathi", "ne": "Nepali", "or": "Odia",
    "pa": "Punjabi", "sa": "Sanskrit", "sd": "Sindhi", "ta": "Tamil", "te": "Telugu",
    "ur": "Urdu", "kok": "Konkani", "mai": "Maithili", "mni": "Manipuri", "bodo": "Bodo",
    "doi": "Dogri", "sat": "Santali"
};

(async () => {
    for (const [code, lang] of Object.entries(languages)) {
        try {
            const res = await translate(text, { to: code });
            console.log(`${lang} (${code}): ${res.text}`);
        } catch (error) {
            console.log(`Error translating to ${lang}: ${error.message}`);
        }
    }
})();
