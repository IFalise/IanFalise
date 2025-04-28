# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, request, render_template_string, send_file
from flask_cors import CORS
import io
# %%
app = Flask(__name__)
CORS(app)

def process_data(df):
    plt.style.use('_mpl-gallery')
    # grab your renamed columns:
    co2theta = df['Co 2(theta)']
    intensity = df['Intensity']

    # Excel formula in Python:
    #   H = ASIN(CU_RAD/(2*(CO_RAD/(2*SIN(co2theta*0.5*0.017453)))))*57.2958*2
    angle_half_rad = co2theta * 0.5 * 0.017453       # deg→rad
    H = np.arcsin(
            CU_RAD
            / (2 * (CO_RAD / (2 * np.sin(angle_half_rad))))) * 57.2958 * 2

    # now plot
    fig, ax = plt.subplots()
    ax.scatter(H, intensity)
    ax.set_xlabel('Cu 2θ (degrees)')
    ax.set_ylabel('Intensity')
    ax.set_title('PXRD: Cu 2θ vs Intensity')
    return fig
# %%
# Th
plt.style.use('_mpl-gallery')

# make data
# x = np.linspace(0, 10, 100)
# y = 4 + 1 * np.sin(2 * x)
# x2 = np.linspace(0, 10, 25)
# y2 = 4 + 1 * np.sin(2 * x2)

# plot
# fig, ax = plt.subplots()

# ax.plot(x2, y2 + 2.5, 'x', markeredgewidth=2)
# ax.plot(x, y, linewidth=2.0)
# ax.plot(x2, y2 - 2.5, 'o-', linewidth=2)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()
# %%

upload_page = '''
<!doctype html>
<title>Upload File</title>
<h1>Upload CSV File</h1>
<form action="/upload" method="post" enctype="multipart/form-data">
  <input type="file" name="file">
  <input type="submit" value="Upload">
</form>
'''

@app.route('/', endpoint='home')
def home():
    return render_template_string(upload_page)

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    df = pd.read_csv(uploaded_file)
    # Validate: require at least two columns for x and y
    if df.shape[1] < 2:
        return "Error: Uploaded CSV must contain at least two columns.", 400
    # Assign meaningful column names to the first two columns
    df = df.rename(columns={df.columns[0]: 'Co 2(theta)', df.columns[1]: 'Intensity'})
    fig = process_data(df)
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

# %%
