from flask import Flask
app = Flask(__name__)
@app.route(&#39;/&#39;)
def hello_world():
return &#39;Hello World!&#39;
if __name__ == &quot;__main__&quot;:
app.run(host=&#39;0.0.0.0&#39;, port=80)
