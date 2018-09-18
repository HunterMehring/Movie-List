from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

movies = []

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies *
add_form = """
    <form action="/add" method="post">
        <label for="new-movie">
            I want to add
            <input type="text" id="new-movie" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""
# TODO:
# Create the HTML for the form below so the user can check off a movie from their list 
# when they've watched it.
# Name the action for the form '/crossoff' and make its method 'post'.
# a form for crossing off watched movies *
crossoff_form = """ 
    <form action="/crossoff" method="post">
        <select name="crossed-off-movie">
            {dropdown_items}
        </select>
        <button type="submit">Crossoff movie</button>
    </form>

"""

return_to_index = """<a href="http://127.0.0.1:5000/"> Return to main page</a>
    """

# TODO:
# Finish filling in the function below so that the user will see a message like:
# "Star Wars has been crossed off your watchlist".
# And create a route above the function definition to receive and handle the request from 
# your crossoff_form.
@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']  
    crossed_off_movie_html = "<strike>"+crossed_off_movie+"</strike> has been crossed off your watchlist"
    #Now i want to delete the movie from the list, but I cannot acess the list because it says that I can't access the list before I assign a value to it, but I have. 
    #I think the problem is that i need to specifically request that data like line 60 did, but I don't know how to do that with a list. Not sure though. I could be wrong. 

    
    return page_header + "<p>" + crossed_off_movie_html + "</p>" + return_to_index + page_footer

# TODO:
# modify the crossoff_form above to use a dropdown (<select>) instead of
# an input text field (<input type="text"/>)

@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']
    movies.append(new_movie)

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>"+ return_to_index + page_footer

    return content

@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    #build the response string
    content = page_header + edit_header + add_form + crossoff_form.format(dropdown_items = get_dropdown_options()) + page_footer

    return content

def get_dropdown_options():
    dropdown = ""
    option_html = "<option>{movie_choice}</option>"
    for movie in movies:
        dropdown += option_html.format(movie_choice=movie)
    return dropdown

app.run()