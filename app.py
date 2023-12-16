from flask import Flask, render_template, request,jsonify
import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def redirectUser():
    return render_template('user.html')

@app.route('/driver')
def redirectDriver():
    return render_template('driver.html')


@app.route('/process_data', methods=['POST'])
def process_data():
    try:
        data_from_js = request.get_json()
        lattitude = data_from_js.get('lattitude')
        longitude = data_from_js.get('longitude')
        print(f'lattitude: {lattitude}, longitude: {longitude}')
        map(lattitude,longitude)
        return jsonify({'status': 'success'})
        
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)})
        




def map(lattitude,longitude):
    mymap = folium.Map(location=[lattitude, longitude], zoom_start=15)
    folium.Marker(
    location=[lattitude, longitude],
    popup='Your Marker Popup Text',  # Replace with your desired popup text
    icon=folium.Icon(color='red', icon='info-sign')  # Customize the marker icon
    ).add_to(mymap)
    mymap.save("./static/map.html")




if __name__ == '__main__':
    app.run(debug=True)
