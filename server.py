from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/api/submit-request', methods=['POST'])
def submit_request():
    try:
        data = request.get_json()
        
        # Extract form data
        full_name = data.get('fullName')
        email = data.get('email')
        device_type = data.get('deviceType')
        message = data.get('message')
        
        # Validate required fields
        if not all([full_name, email, device_type, message]):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Log the request
        print('\n📝 New Service Request Received:')
        print(f'  Name: {full_name}')
        print(f'  Email: {email}')
        print(f'  Device: {device_type}')
        print(f'  Message: {message}')
        print(f'  Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print('---\n')
        
        # Return success response
        return jsonify({
            'success': True,
            'message': 'Request received successfully',
            'data': {
                'fullName': full_name,
                'email': email,
                'deviceType': device_type
            }
        }), 200
    
    except Exception as e:
        print(f'❌ Error: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'Server is running'}), 200

if __name__ == '__main__':
    print('✅ Server running at http://localhost:5000')
    print('📍 Service request endpoint: http://localhost:5000/api/submit-request')
    print('Press Ctrl+C to stop the server\n')
    app.run(debug=True, port=5000)
