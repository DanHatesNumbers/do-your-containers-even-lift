from flask import Flask
from flask import render_template
from flask import Response
import time

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

frames = [
    "  /(˘ω˘)\\                /(˘ω˘)\\             ",
	" |       |    /(˘ω˘)\\   |       |    /(˘ω˘)\\ ",
    " ^       ^   ^       ^   ^       ^   ^       ^ ",
	"  /(˘ω˘)\\                /(˘ω˘)\\             ",
	" |       |    /(˘ω˘)\\   |       |    /(˘ω˘)\\ ",
    " ^       ^   ^       ^   ^       ^   ^       ^ ",
    "ᕦ(˘ω˘)ᕤ",
    " \\\    /   ",
	"  (*≧ω≦)   ",
    "     |     ",
    "   /   \\  ",
    "  (*≧ω≦)   ",
    "  -- | --  ",
    "    / \\   ",
    "   (*≧ω≦)   ",
    "   | | |   ",
    "    | |    ",
	" \\\    /   ",
	"  (*≧ω≦)   ",
    "     |     ",
    "   /   \\  ",
    "  (*≧ω≦)   ",
    "  -- | --  ",
    "    / \\   ",
    "   (*≧ω≦)   ",
    "   | | |   ",
    "    | |    ",
    " (ﾉ^ヮ^)ﾉ*:・ﾟ✧",

]

@app.route('/dance')
def dance():
    def generate():
        while True:
            for frame in frames:
                yield f"{frame}\n\n"
                time.sleep(0.5)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)

