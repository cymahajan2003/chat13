const express = require('express');
const cors = require('cors');
const translate = require('@vitalets/google-translate-api');

const app = express();
app.use(express.json());
app.use(cors());

app.post('/translate', async (req, res) => {
    const { text, lang } = req.body;

    try {
        const result = await translate(text, { to: lang });
        res.json({ translation: result.text });
    } catch (error) {
        res.status(500).json({ error: "Translation failed" });
    }
});

app.listen(3000, () => console.log("Server running on port 3000"));
