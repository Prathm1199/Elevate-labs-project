from flask import Flask, render_template_string, request
from scanner import main
import sys
import io

app = Flask(__name__)

# HTML template for results
HTML_TEMPLATE = '''
<h2>Web App Vulnerability Scanner</h2>
<form method="post">
    Target URL: <input type="text" name="url" required>
    <input type="submit" value="Scan">
</form>
<hr>
{% if results %}
<h3>Scan Results:</h3>
<pre>{{ results }}</pre>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def index():
    results = ""
    if request.method == "POST":
        target_url = request.form['url']

        # Capture print output from scanner.main()
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        main(target_url)  # run your scanner exactly as it is

        sys.stdout = old_stdout
        results = new_stdout.getvalue()

    return render_template_string(HTML_TEMPLATE, results=results)

if __name__ == "__main__":
    app.run(debug=True)
