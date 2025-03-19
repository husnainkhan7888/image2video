const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Endpoint to remove background
app.post('/remove-bg', async (req, res) => {
  try {
    const response = await axios.post(
      'https://api.remove.bg/v1.0/removebg',
      req.body,
      {
        headers: {
          'X-Api-Key': '35TWwUxkvoHGgPnVDR2JM7Qp', // Replace with your Remove.bg API key
          'Content-Type': 'application/json'
        },
        responseType: 'arraybuffer'
      }
    );
    res.type('image/png').send(response.data);
  } catch (error) {
    res.status(500).send('Error processing image');
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));