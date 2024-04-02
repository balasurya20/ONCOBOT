from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def return_response():
    if request.method == "POST":
        text_input = request.form.get('text_input')
        image_file = request.files.get('image_file')
        
        # Process the text_input and image_file as needed
        
        return "Text Input: {}<br>Image File Name: {}".format(text_input, image_file.filename if image_file else "No image uploaded")
    
    return render_template_string("""
   <!DOCTYPE html>
<html>
<head>
    <title>LLM Bot</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://t3.ftcdn.net/jpg/02/01/38/00/360_F_201380017_cNP9520EXzGG3xPUsGkSZvqxcFQsB5Ae.jpg');
            background-size: cover;
            background-position: center;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            width: 400px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px; /* Add space between the container and the bottom of the page */
        }

        .chat-history {
            padding: 20px;
            border-bottom: 1px solid #ccc;
            overflow-y: scroll;
            max-height: 300px;
        }

        .chat-history p {
            margin: 5px 0;
        }

        .query-processing {
            display: flex;
            align-items: center;
            justify-content: space-between; /* Adjusted to space between input and buttons */
            padding: 20px;
            border-top: 1px solid #ccc;
        }

        .query-processing input[type="text"],
        .query-processing input[type="file"] {
            flex: 1;
            padding: 10px;
            margin-right: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }

        .query-processing .button-container {
            display: flex;
            align-items: center;
        }

        .query-processing button {
            width: 40px; /* Adjust width to make it square */
            height: 40px; /* Adjust height to make it square */
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px; /* Adjust border-radius to make it square */
            cursor: pointer;
        }

        .camera-icon {
            width: 40px; /* Adjust width to make it square */
            height: 40px; /* Adjust height to make it square */
            background-color: #007bff;
            border: none;
            border-radius: 5px; /* Adjust border-radius to make it square */
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .camera-icon i {
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Chat history -->
        <div class="chat-history">
            <!-- Chat history content goes here -->
        </div>
        <!-- Query processing box -->
        <div class="query-processing">
            <form action="/process_query" method="post" enctype="multipart/form-data">
                <input type="text" name="user_query" placeholder="Enter your query...">
                <div class="button-container">
                    <button type="submit"><i class="fas fa-arrow-alt-circle-right"></i></button>
                    <label for="image_file" class="camera-icon">
                        <i class="fas fa-camera"></i>
                    </label>
                    <input type="file" id="image_file" name="image_file" style="display:none;">
                </div>
            </form>
        </div>
        <!-- Navigation pane -->
        <div class="navigation">
            <!-- Navigation buttons go here -->
        </div>
    </div>
</body>
</html>

    """)

if __name__ == "__main__":
    app.run(port=4001)
