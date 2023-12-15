document.addEventListener('DOMContentLoaded', function() {
    // Create a WebView element
    var webView = document.createElement('iframe');
    webView.src = 'https://your-flask-app-url';  // Replace with your Flask app URL
    webView.style.width = '100%';
    webView.style.height = '500px';  // Set the desired height

    // Append WebView to the container
    var container = document.getElementById('webview-container');
    container.appendChild(webView);
});
