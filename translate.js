const express = require('express');
const cors = require('cors');
const translate = require('@vitalets/google-translate-api');

const app = express();
app.use(express.json());
app.use(cors());

app.post('/translate', async (req, res) => {
    const { text, lang } = req.body;

    if (!text || !lang) {
        return res.status(400).json({ error: "Text or language missing" });
    }

    try {
        const result = await translate(text, { to: lang });
        res.json({ translation: result.text });
    } catch (error) {
        console.error("Translation Error:", error);
        res.status(500).json({ error: "Translation failed. Try again later." });
    }
});

app.listen(3000, () => console.log("Server running on port 3000"));
