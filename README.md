# Retroplay

Fullstack Frameworks with Django Project - Code Institute  


Retroplay is a ficticious e-commerce website that sells retro video games. It also contains the latest news in the retro gaming world and is a central hub for users to access information about any video game.  
Overview of features:
* A large inventory of games, categorised by brand and console.
* The ability to add games to a cart, update the cart, and checkout.
* A news section where users can read articles about retro gaming.
* Users can leave comments on news articles.
* Users can update and delete their comments.
* A 'Game Bible' section where users can make use of the IGDB api to search for information about any game.
* Information area for shipping info, contact and FAQs.

It was built in Python3 using the Django framework.

### This project is for educational purposes only

### A live version is hosted [here](https://mpark-django-retroplay.herokuapp.com/)  

## UX

I have been developing an interst in retro video games over the last couple of years. Because of this I often visit online stores selling retro games.  
I find a lot of these sites to be relatively simplistic without many features.  
My aim for this project was to make a retro gaming site more visually appealing while also offering some more features on top of the standard e-commerce functionality.  
For this reason I also included the news and bible apps.  
Originally I had intended to also include a 'gaming lounge' section where users could play versions of retro games that could be built with javascript (eg. pong) directly in the browser.  
Unfortunately time constraints meant I could not pursue this.  
I intend to add it at a future date to give the site a feeling of a full experience to visit.  

The visual theme for the site is intended to evoke a nostagic view of gaming.  
To achieve this there are three separate full screen iconic images on the home screen, as well as iconic sprites that would appeal to a user of this site. 
The full screen images use a parallax effect. However this effect is removed on mobile size screens and the images are changed as the originals are too big for mobile size.  
There is also a color motif that runs throughtout the site of a 5 color stripe, which is intended to mimic the classic lines and colors on the commodore 64 logo.  
[canva.com](https://www.canva.com/) was used to create this color pattern.  

Site navigation is designed to be as intuitive as possible. The navbar contains links to the seperate main apps.  
The navbar link for the game shop gives a dropdown menu to choose an individual brand.  
A side navigation menu also exists on nearly all screens except the index page and cart/checkout pages, which contains a search field to search all products at any time.  
The side navigation menu allows users to drill down further from brands to individual consoles. This is achieved through dropdown menus.  

No Template was used for this site.  


## Technologies Used
* HTML
* CSS
* Bootstrap
* Python3
* Django2 Framework
* Javascript
* Jquery
* lightbox
    * A javascript library used to overlay images on the current page. Used for viewing screenshots from games in the bible app.
* Hover.css
    * A library for creating effects on hovering over an image. Used throughout the site.
* CSS3 Animate it
    * A library for creating animations. Used in the bible app.
* Beautiful Soup
    * Used for the initial scraping of data to populate the database with games as products.
* IGDB API
    * Used to retrieve game data from the Internet Game Database and display it in the bible app.
* Stripe
    * Used for processing payments.


### Wireframing

Wireframes were made using the pencil application and can be found in the wireframes folder

## Background and features per app

### Accounts App

The accounts app is used for user authentication.  Currently the only benefit to creating an account is being able to comment on news articles.  
I would like to expand the features on offer to registered users.  

#### Existing Features
* Users can easily register, log in and log out.
* A user can comment on articles in the news app.
* A user can edit and delete their comments.
* A user cannot edit or delete another user's comment.
* A user must be logged in to comment.

#### Features left to implement
* Enable users to view previous purchases.
* Enable users to create an address book so they do not have to enter address information every time they purchase items.
* Similarly allow users to store multiple credit cards.
* Allow users to request password reset emails.
* Allow users to reply directly to comments in the news app.


### Bible App

The bible app is used to search the Internet Game Database and return information about games.  
The app makes use of this [python wrapper](https://github.com/igdb/igdb_api_python), designed for working with the IGDB API in python.  
The information retrieved gives a games' name, cover image, a selection of screenshots, aggregate rating, date released, a summary, and a link to the IGDB page for the game to get more information.  
Originally the cover images and screenshots sent through the api linked to small thumbnail images. These did not display well on the site due to the small sizes so in the view for retrieving the data I edited the string of the returned url to link instead to where a full size image was hosted:  
```
if 'cover' in game:
    game['cover']['url']=game['cover']['url'].replace("t_thumb","t_cover_big")

if 'screenshots' in game:
    for i in game['screenshots']:
        i['url']=i['url'].replace("t_thumb","t_original")
```

#### Existing Features
* Users can use the bible to search for information about any game.
* Information is presented in a simple layout, which gives the users access to screenshots, summary, rating, release date and link to get more information.
* In the case of the rating the animated color progress bar will show a color appropriate to the rating: green, orange, or red.
* The instances of no information for some of the returned values are handled in the following ways:
    * In the even a game has no cover image a default image will display instead.
    * No rating will display a grey animated progress bar stating no rating available.

#### Features left to implement
* Enable users to search for a game they discovered in the bible in the sites' products directly, without having to enter the title in the search products bar. This should be relatively easy to implement.


### Cart App

The cart app is used for adding products to a cart session and updating the cart. 

#### Existing Features
* Users can easily add items to a cart
* Users can easily update the number of items in a cart and delete items from a cart.
* The image for the cart in the navbar will display the amount of items currently in the cart


### Checkout App

The checkout app is used for making purchases with stripe. 

#### Existing Features
* Users can enter address and card information for making purchases.
* While making payment the order details are available on screen with an edit button should the user want to edit their cart before finalising purchases.
* When purchases are complete users will be redirected to a confirmation screen where they can view their order details. Billing information is also available on screen.

#### Features left to implement
* Sending email confirmation upon succesful purchases.


### Info App

The info app exists to create a sense of authenticity to the project as a whole.  
Rather than having dead links in the nav and footer I created the info app and filled the individual urls with dummy data. 

#### Existing Features
* working links to contact, FAQ and shipping information.
* Filled with dummy data.
* The contact form redirects to the FAQ via a get request.


### News App

The news app contains news articles sourced from the internet. Here the users can read and comment on the news articles.  

#### Existing Features
* Users can comment on news articles.

#### Features left to implement
* The ability to like articles.
* Number of views displayed on article.
* When users edit or delete a comment the page is reloaded, I would like this to happen dynamically without needing to reload the page.


### Products App

The products app contains all the information relating to the game products found on the site.  
For this project I wanted to work with a large ammount of data in order to learn how to present it to users in an easily consumable/navigatable manner.  
To this end there are over 1500 products in the database for users to look through. This is too much to render in a view all display.  
It was important to consider how to construct the models in order to make the data easy to deal with and present to the user.  
In the end there are three different models: Brand, Console and Game. Giving the console model a foreign key to the brand model and giving the Game model a foreign key to both Console and Brand made the data easy to work with and present in an intuitive fashion.  

To source the products I used Beautiful soup to scrape data from [consolemad.co.uk](https://www.consolemad.co.uk/), an online retro gaming store.  
The original site uses pagination in displaying their results. As a result I had to write a scrape function for multiple urls where it could look for paginated pages and deal with them accordingly.  
Originally, due to the amount of data, I chose not do download images for products, but rather linked them via url to the original image.  
This caused issue however as when the origianl site sold an item, they took down the image link.  As a result a product on my site would display no image if the corresponding product on theirs was sold.  
To overcome this I attempted to write it into the view for retreiveing and rendering products that, when filtering Game objects to be rendered, the view would check to see if the image link was returning a 404 status code. If it did then the game object with the broken image link would be deleted from the database before it could be rendered.  
This slowed the process of filtering and returning games down too much, and also meant that my inventory of games would slowly decrease.  
In the end I elected to expand the scrape function to also download images.  


#### Existing Features
* Users can easily navigate through the products via brand and console.
* There is also an ever present search bar in the side navigation menu where users can search for games by title.
* Each product, when hovered on, will display two buttons; one to add the item to the cart, and the other to search for the item in the game bible where the user can get information about the product.
* Product pages are paginated in order to load the pages quicker and present an easily consumable chunk of games on screen at one time.

#### Features left to implement
* Several test users have noted that they would like to be able to include a console in the search bar when searching for a game (for example someone wanting to search for a Fifa game only on playstation 2 would like to search using 'fifa playstation 2'). This is a feature I plan to implement.


## Run locally

1. Clone the [github repository](https://github.com/mparkcode/django-retroplay)
2. install requirements:
```
pip3 install -r requirements.txt
```
3. Get a secret key and set it as an environment variable. You can get one at https://www.miniwebtool.com/django-secret-key-generator/
4. set as an environment variable DJANGO\_SETTINGS\_MODULE equal to retroplay.settings.local:
5. migrate:
```
python3 manage.py migrate
```
6. create a superuser:
```
python3 manage.py createsuperuser
```
7. You will need to update your allowed hosts in base.py.
7. The site will now run locally. There will be no products or news articles. 
8. If you wish to use the game bible you will need to get an API key from [IGDB](https://www.igdb.com/api) and set it as an environment variable called IGDB\_API\_KEY.


## Testing
[![Build Status](https://api.travis-ci.org/mparkcode/django-retroplay.svg)]
Automated testing was done using Travis-CI. Currently it holds an 86% coverage rate for the site's apps. 80 tests were written, however many of these were needless. At a later stage I would like to remove these and write more tests to achieve 100% coverage.  
To run the tests, when you have the project running locally, enter:
```
python3 manage.py test
```

The site was tested on 21" monitors, 15" and 13" laptop screens and on an iPhone SE and iPhone 8 screen to test responsiveness.  
It was also tested using chrome, firefox and safari.  
There is an issue on very small screen sizes (iPhone SE size) where the large images on the home screen resize slightly when scrolling. This issue is not there on larger mobile screen sizes.  

Manual tests were also done to ensure links/form submissions/model relationships/purchases/IGDB api usage worked correctly and that the site was defensively designed.  

Manual testing was done to ensure:
* The site works as intended.
* User entered information was handled correctly (adding/editing/deleting comments, adding to and updating the cart, purchases etc).
* Logging in and out and registering works as intended.
* The Bible retrieves and displays data as intended.
* Defensive design:
    * The checkout page is not accessible if no items are in the cart.
    * The checkout confirmation is only accessible when payment is complete.
    * Users can only enter comments on news articles when logged in.
    * Only a user who creates a comment can edit or delete it.


## Issues

Due to the time constraints in creating this project I have not had time to satisfactorily refactor the code.  
As a result there is some repeated code and some 'messy' code with needless complexity.  
For example any view that checks for a search query (which is a majority of views) via a get request has the same code to redirect to the search_results view, as per below:  
```
search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
```
I attempted to place this within its own function but it would not work. I would like to go back and get this working to reduce the ammount of code.  
This is just an example of various issues I have. I also must make time to include comments on code blocks where it is not immediately clear what is going on.  

In addition to this the custom.css file where I wrote most of the custom styles for the site is not what I would consider to be best practice for writing css.  I definitely wish to clean this up.  


## Deployment
The site is hosted on heroku.  
Static assets are hosted on Amazon S3. 

## Credits

### Media
Static images on this site that do not represent a product were all sourced from google images.  
Products and their images were sourced from [consolemad.co.uk](https://www.consolemad.co.uk/)  
Font awesome was used for the various icons in the site.  
Google fonts used - Press Start 2P, Libre Barcode 39 Extended Text & Orbitron.  

### Acknowledgements
Corey Schafer's [video on web scraping with beautiful soup](https://www.youtube.com/watch?v=ng2o98k983k).  
WDTutorials [video on Django pagination](https://www.youtube.com/watch?v=Z8MDdDyB_6A)
Code for the smooth scrolling effect on the animated arrow on the home screen was taken from [css tricks](https://css-tricks.com/snippets/jquery/smooth-scrolling/).  