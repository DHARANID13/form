const express = require('express');
const cors = require('cors');
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// POST endpoint for service request
app.post('/api/submit-request', (req, res) => {
    const { fullName, email, deviceType, message } = req.body;

    // Validate required fields
    if (!fullName || !email || !deviceType || !message) {
        return res.status(400).json({ error: 'All fields are required' });
    }

    // Log the request data
    console.log('📝 New Service Request Received:');
    console.log('  Name:', fullName);
    console.log('  Email:', email);
    console.log('  Device:', deviceType);
    console.log('  Message:', message);
    console.log('  Time:', new Date().toLocaleString());
    console.log('---');

    // Send success response
    res.status(200).json({
        success: true,
        message: 'Request received successfully',
        data: { fullName, email, deviceType }
    });
});

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.status(200).json({ status: 'Server is running' });
});

// Start server
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`✅ Server running at http://localhost:${PORT}`);
    console.log(`📍 Service request endpoint: http://localhost:${PORT}/api/submit-request`);
});
