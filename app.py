from flask import Flask, render_template

app = Flask(__name__, static_folder='./static')

@app.route('/submit', methods=['POST'])
def submit():
    return f"""hello Dasha"""

@app.route('/delete', methods=['DELETE'])
def delete():
    return f""""""

@app.route('/delete_all', methods=['DELETE'])
def delete_all():
    return ""

@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def main():
    return render_template('/index.html')

@app.get('/about')
def about():
    return 'This is a rendered about HTML'

@app.get('/login')
def login():
    return f'''
    <form class="header_link">
        <input>Email</input>
        <input>Password</input>
    </form>
'''

@app.get('/home')
def home():
    return f'''
    <svg
                width="120mm"
                height="40mm"
                viewBox="0 0 140.65233 44.767521"
                version="1.1"
                id="svg1"
                xml:space="preserve"
                xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
                xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:svg="http://www.w3.org/2000/svg"><sodipodi:namedview
                    id="namedview1"
                    pagecolor="#ffffff"
                    bordercolor="#000000"
                    borderopacity="0.25"
                    inkscape:showpageshadow="2"
                    inkscape:pageopacity="0.0"
                    inkscape:pagecheckerboard="0"
                    inkscape:deskcolor="#d1d1d1"
                    inkscape:document-units="mm" /><defs
                    id="defs1" /><g
                    inkscape:label="Layer 1"
                    inkscape:groupmode="layer"
                    id="layer1"
                    transform="translate(-304.91941,-166.77337)"><text
                    xml:space="preserve"
                    style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;font-family:Jura;-inkscape-font-specification:Jura;white-space:pre;inline-size:129.012;fill:#2a2065;fill-opacity:1;stroke-width:0.665001;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:0.535714"
                    x="317.37866"
                    y="184.9174"
                    id="text22"><tspan
                        x="317.37866"
                        y="184.9174"
                        id="tspan2"><tspan
                        style="stroke-width:0.665"
                        id="tspan1">New platform for your </tspan></tspan><tspan
                        x="317.37866"
                        y="199.02854"
                        id="tspan4"><tspan
                        style="stroke-width:0.665"
                        id="tspan3">projects</tspan></tspan></text><text
                    xml:space="preserve"
                    style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:52.9167px;font-family:Jura;-inkscape-font-specification:Jura;white-space:pre;inline-size:188.974;fill:#2a2065;fill-opacity:1;stroke-width:0.665001;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:0.535714"
                    x="351.34305"
                    y="165.85959"
                    id="text23"
                    transform="translate(-49.625794,36.6061)"><tspan
                        x="351.34305"
                        y="165.85959"
                        id="tspan6"><tspan
                        style="font-weight:600;-inkscape-font-specification:'Jura Semi-Bold';stroke-width:0.665"
                        id="tspan5">[        ]</tspan></tspan></text></g>
            </svg>'''

@app.get('/contact')
def contact():
    return ''