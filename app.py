from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloudflare</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
            padding: 40px;
            max-width: 600px;
            width: 100%;
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .subtitle {
            color: #666;
            text-align: center;
            margin-bottom: 30px;
            font-size: 14px;
        }
        
        .card {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }
        
        .card h3 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .card p {
            color: #555;
            line-height: 1.6;
        }
        
        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 30px;
            justify-content: center;
        }
        
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s ease;
        }
        
        .btn-primary {
            background: #667eea;
            color: white;
        }
        
        .btn-primary:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        .info {
            background: #e7f3ff;
            border: 1px solid #b3d9ff;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
            font-size: 14px;
            color: #004085;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Cloudflare</h1>
        <p class="subtitle">A small Flask web application</p>
        
        <div class="card">
            <h3>Welcome!</h3>
            <p>This is a simple Flask web page served with HTML and CSS. You can use this as a starting point for your Cloudflare proof-of-concept.</p>
        </div>
        
        <div class="card">
            <h3>API Endpoint Available</h3>
            <p>You can also access the <code>/api/hello</code> endpoint to get JSON responses.</p>
        </div>
        
        <div class="button-group">
            <button class="btn-primary" onclick="fetchAPI()">Call API</button>
        </div>
        
        <div id="api-response" class="info" style="display: none;"></div>
    </div>
    
    <script>
        function fetchAPI() {
            fetch('/api/hello')
                .then(response => response.json())
                .then(data => {
                    const responseDiv = document.getElementById('api-response');
                    responseDiv.innerHTML = `<strong>API Response:</strong><br>` +
                                          `Message: ${data.message}<br>` +
                                          `Your IP: ${data.client_ip}`;
                    responseDiv.style.display = 'block';
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Failed to call API');
                });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!", 
                    "client_ip": request.remote_addr})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    

## run the cloudflare tunnel with the command:
# cloudflared tunnel --url http://localhost:5000