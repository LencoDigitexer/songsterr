const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.use(express.json());

app.get('/api/meta/:songId/revisions', async (req, res) => {
  const songId = req.params.songId;
  try {
    const response = await axios.get(`https://www.songsterr.com/api/meta/${songId}/revisions`);
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
