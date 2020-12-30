# WebScraping basics

Executive Summary

open webpage in chrome/firefox, select the section you want to explore, right click and choose "Inspect" this will open the source page and locate the tag for the section selected

Elements:tags, Properties, id,class

Libraries:  **import requests**: api to make requests to webpages (GET is one such reuest used to download webpage content)

**from bs4 import BeautifulSoup**: beautiful soup module

Steps:

1. download webpage: **page = requests.get(<webpage>)**
   1. status code: page.status_code  (200 is success)
   2. print html content: **page.content**
2. generate Bsoup object: **soup = BeautifulSoup(page.content, 'html.parser')**
   1. Nicely formated print: **print(soup.prettify())**
3. select all the elements at the top level of the page using the children property of soup. Note that children returns a list generator, so we need to call the list function on it:**list(soup.children)**
4.  what the type of each element in the list is: **[type(item) for item in list(soup.children)]**
   1. Tag object allows us to navigate through an HTML document, and extract other tags and text.
5. select the given tag and its children by taking the nth item in the list: **html = list(soup.children)[<n>]**
   1. html as returned is also a bs object so methods can further be applied on it ex:  **list(html.children)**
6. Find tag of interest div/p/a etc and build a bs object for it: 
   1. want to extract the text inside the p tag, so we’ll dive into the body: **body = list(html.children)[3]**
   2. **list(body.children)**: lists the contents of children, the contents can tags, text new line chars etc...
   3. get the elemnts of list which are  desired tag (ex p): **p = list(body.children)[1]**
7. Once we’ve isolated the tag, we can use the **get_text** method to extract all of the text inside the tag: **p.get_text()**
8. If we want to extract a single tag, we can instead use the find_all method, which will find all the instances of a tag on a page: **soup.find_all('p')**
   [<p>Here is some simple content for this page.</p>]
   1. If  instead only want to find the first instance of a tag, (return a single BeautifulSoup object) : **soup.find('p')**
9. Search using class and ids:
   1. search for any p tag that has the class outer-text: **soup.find_all('p', class_='outer-text')**
   2. **soup.find_all(class_="outer-text")**
   3. search for elements by id:**soup.find_all(id="first")**
10. CSS selection method can be used for selection as well using select method, look in the text for description

Example DWS website extract weather for tonight:

1. 

` page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168") `

`soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())`

`period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period, '  : ' ,short_desc,'  :  ', temp)
img = tonight.find("img") # find the title on the image
desc = img['title']
print(desc)`

2. CSS select method with tags

   ` period_tags = seven_day.select(".tombstone-container .period-name")
   periods = [pt.get_text() for pt in period_tags] `

   `short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
   temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
   descs = [d["title"] for d in seven_day.select(".tombstone-container img")] `







----





National weather service website scraping with BS and then analyzing with pandas



## The Components of a Web Page
When we visit a web page, our web browser makes a request to a web server. This request is called a GET request, since we’re getting files from the server. The server then sends back files that tell our browser how to render the page for us. The files fall into a few main types:

- HTML — contain the main content of the page.
- CSS — add styling to make the page look nicer.
- JS — Javascript files add interactivity to web pages.
- Images — image formats, such as JPG and PNG allow web pages to show pictures.



After our browser receives all the files, it renders the page and displays it to us. There’s a lot that happens behind the scenes to render a page nicely, but we don’t need to worry about most of it when we’re web scraping. When we perform web scraping, we’re interested in the main content of the web page, so we look at the HTML.

## HTML

Let’s take a quick tour through HTML so we know enough to scrape effectively. HTML consists of elements called tags. 

The most basic tag is the <html> tag. This tag tells the web browser that everything inside of it is HTML. We can make a simple HTML document just using this tag:

<html>
</html>

Right inside an html tag, we put two other tags, **the head tag, and the body tag**. The main content of the web page goes into the body tag. The head tag contains data about the title of the page, and other information that generally isn’t useful in web scraping:

<html>

<head>
</head>
<body>
</body>
</html>

You may have noticed above that we put the head and body tags inside the html tag. In HTML, tags are nested, and can go inside other tags.

We’ll now add our first content to the page, in the form of the **p tag**. The p tag defines a paragraph, and any text inside the tag is shown as a separate paragraph:

<html>
<head>
</head>
<body>

'<p>'

Here's a paragraph of text!

'</p>'

'<p>'


Here's a second paragraph of text!

'</p>'

</body>
</html>

Tags have commonly used names that depend on their position in relation to other tags:

- child — a child is a tag inside another tag. So the two p tags above are both children of the body tag.

- parent — a parent is the tag another tag is inside. Above, the html tag is the parent of the body tag.

- sibiling — a sibiling is a tag that is nested inside the same parent as another tag. For example, head and body are siblings, since they’re both inside html. Both p tags are siblings, since they’re both inside body.

- We can also add properties to HTML tags that change their behavior:

<html>

<head>
</head>
<body>

'<p>'

Here's a paragraph of text!
<a' href="https://www.dataquest.io">Learn Data Science Online'</a>'

'</p>'

'<p>'

Here's a second paragraph of text!
'<a' href="https://www.python.org">Python'</a>'

'</p>' 

</body></html>

In the above example, we added two **a tags**. **a tags are links**, and tell the browser to render a link to another web page. The href property of the tag determines where the link goes.

a and p are extremely common html tags. Here are a few others:

- div — indicates a division, or area, of the page.
- b — bolds any text inside.
- i — italicizes any text inside.
- table — creates a table.
- form — creates an input form.

For a full list of tags, look [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

Before we move into actual web scraping, let’s learn about the **class and id properties**. These special properties give HTML elements names, and make them easier to interact with when we’re scraping. 

.** Classes and ids are optional, and not all elements will have them.

We can add classes and ids to our example:

```python
<html>
<head>
</head>
<body>
<p class="bold-paragraph">  //p tag has single class
Here's a paragraph of text!
<a href="https://www.dataquest.io" id="learn-link">Learn Data Science Online</a> //a tag with 1 id
</p>
<p class="bold-paragraph extra-large"> //p tag has multiple classes
Here's a second paragraph of text!
<a href="https://www.python.org" class="extra-large">Python</a> // a tag with a class
</p>
</body>
</html>
```

 **Adding classes and ids doesn’t change how the tags are rendered at all.**

---

## The requests library
The first thing we’ll need to do to scrape a web page is to download the page. We can download pages using the Python requests library. The requests library will make a GET request to a web server, which will download the HTML contents of a given web page for us. There are several different types of requests we can make using requests, of which GET is just one. If you want to learn more, check out our API tutorial.

Let’s try downloading a simple sample website, http://dataquestio.github.io/web-scraping-pages/simple.html. We’ll need to first download it using the requests.get method.

**import requests**
**page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")**
**page**

<Response [200]>

After running our request, we get a Response object. This object has a status_code property, which indicates if the page was downloaded successfully:

**page.status_code**
200

A status_code of 200 means that the page downloaded successfully. We won’t fully dive into status codes here, but a status code starting with a 2 generally indicates success, and a code starting with a 4 or a 5 indicates an error.

We can print out the HTML content of the page using the content property:

**page.content**

## Parsing a page with BeautifulSoup
As you can see above, we now have downloaded an HTML document.

We can use the BeautifulSoup library to parse this document, and extract the text from the p tag. We first have to import the library, and create an instance of the BeautifulSoup class to parse our document:

**from bs4 import BeautifulSoup**



We can now print out the HTML content of the page, formatted nicely, using the prettify method on the BeautifulSoup object:

**print(soup.prettify())**

As all the tags are nested, we can move through the structure one level at a time. We can first select all the elements at the top level of the page using the children property of soup. Note that children returns a list generator, so we need to call the list function on it:

**list(soup.children)**
['html', 'n', <html> <head> <title>A simple example page</title> </head> <body> <p>Here is some simple content for this page.</p> </body> </html>]

The above tells us that there are two tags at the top level of the page — the initial <!DOCTYPE html> tag, and the <html> tag. There is a newline character (n) in the list as well. Let’s see what the type of each element in the list is:

**[type(item) for item in list(soup.children)]**
[bs4.element.Doctype, bs4.element.NavigableString, bs4.element.Tag]

As you can see, all of the items are BeautifulSoup objects. The first is a Doctype object, which contains information about the type of the document. The second is a NavigableString, which represents text found in the HTML document. The final item is a Tag object, which contains other nested tags. The most important object type, and the one we’ll deal with most often, is the Tag object.

The Tag object allows us to navigate through an HTML document, and extract other tags and text. You can learn more about the various BeautifulSoup objects [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-objects)..

We can now select the html tag and its children by taking the third item in the list:

**html = list(soup.children)[2]**

Each item in the list returned by the children property is also a BeautifulSoup object, so we can also call the children method on html.

Now, we can find the children inside the html tag:

**list(html.children)**
['n', <head> <title>A simple example page</title> </head>, 'n', <body> <p>Here is some simple content for this page.</p> </body>, 'n']

As you can see above, there are two tags here, head, and body. We want to extract the text inside the p tag, so we’ll dive into the body:

**body = list(html.children)[3]**

Now, we can get the p tag by finding the children of the body tag:

**list(body.children)**
['n', <p>Here is some simple content for this page.</p>, 'n']

We can now isolate the p tag:

**p = list(body.children)[1]**
Once we’ve isolated the tag, we can use the **get_text** method to extract all of the text inside the tag:

**p.get_text()**
'Here is some simple content for this page.'

### Finding all instances of a tag at once
What we did above was useful for figuring out how to navigate a page, but it took a lot of commands to do something fairly simple. If we want to extract a single tag, we can instead use the find_all method, which will find all the instances of a tag on a page.

**soup = BeautifulSoup(page.content, 'html.parser')**
**soup.find_all('p')**
[<p>Here is some simple content for this page.</p>]

If you instead only want to find the first instance of a tag, you can use the find method, which will return a single BeautifulSoup object:

**soup.find('p')**

<p>Here is some simple content for this page.</p>
## Searching for tags by class and id
We introduced classes and ids earlier, but it probably wasn’t clear why they were useful. **Classes and ids are used by CSS to determine which HTML elements to apply certain styles to**. We can also use them when scraping to specify specific elements we want to scrape. To illustrate this principle, we’ll work with the following page:

```python
<html>
<head>
<title>A simple example page</title>
</head>
<body>
<div>
<p class="inner-text first-item" id="first"> //p tag class and id
First paragraph.
</p>
<p class="inner-text"> //ptag class
Second paragraph.
</p>
</div>
<p class="outer-text first-item" id="second"> //p tag 2 classes and a id
<b>
First outer paragraph.
</b>
</p>
<p class="outer-text">  //p tag 1 class
<b>
Second outer paragraph.
</b>
</p>
</body>
</html>
```

We can access the above document at the URL http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html. Let’s first download the page and create a BeautifulSoup object:

**page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")**
**soup = BeautifulSoup(page.content, 'html.parser')**
**soup**

Now, we can use the find_all method to search for items by class or by id. In the below example, we’ll search for any p tag that has the class outer-text:

**soup.find_all('p', class_='outer-text')**
[<p class="outer-text first-item" id="second"> <b> First outer paragraph. </b> </p>, <p class="outer-text"> <b> Second outer paragraph. </b> </p>]

In the below example, we’ll look for any tag that has the class outer-text:

**soup.find_all(class_="outer-text")**

<p class="outer-text first-item" id="second">
<b>
First outer paragraph.
</b>
</p>, <p class="outer-text">
<b>
Second outer paragraph.
</b>
</p>]

We can also search for elements by id:

**soup.find_all(id="first")**
[<p class="inner-text first-item" id="first">
First paragraph.
</p>]

## Using CSS Selectors

You can also search for items using [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started/Selectors). These selectors are how the CSS language allows developers to specify HTML tags to style. Here are some examples:

- `p a` — finds all `a` tags inside of a `p` tag.
- `body p a` — finds all `a` tags inside of a `p` tag inside of a `body` tag.
- `html body` — finds all `body` tags inside of an `html` tag.
- `p.outer-text` — finds all `p` tags with a class of `outer-text`.
- `p#first` — finds all `p` tags with an id of `first`.
- `body p.outer-text` — finds any `p` tags with a class of `outer-text` inside of a `body` tag.

You can learn more about CSS selectors [here](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started/Selectors).

`BeautifulSoup` objects support searching a page via CSS selectors using the `select` method. We can use CSS selectors to find all the `p` tags in our page that are inside of a `div` like this:

**soup.select("div p")**

[<p class="inner-text first-item" id="first">
First paragraph.
</p>, <p class="inner-text">
Second paragraph.
</p>]

Note that the select method above returns a list of BeautifulSoup objects, just like find and find_all.

---

## Downloading weather data

We now know enough to proceed with extracting information about the local weather from the National Weather Service website. The first step is to find the page we want to scrape. We’ll extract weather information about downtown San Francisco from [this page](http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168).

![img](https://www.dataquest.io/wp-content/uploads/2019/01/extended_forecast.png)

We’ll extract data about the extended forecast.

As you can see from the image, the page has information about the extended forecast for the next week, including time of day, temperature, and a brief description of the conditions.

## Exploring page structure with Chrome DevTools

The first thing we’ll need to do is inspect the page using [Chrome Devtools](https://developer.chrome.com/devtools). If you’re using another browser, [Firefox](https://developer.mozilla.org/en-US/docs/Tools/Web_Console/Opening_the_Web_Console) and [Safari](https://developer.apple.com/safari/tools/) have equivalents. It’s recommended to use Chrome though.

You can start the developer tools in Chrome by clicking `View -> Developer -> Developer Tools`. You should end up with a panel at the bottom of the browser like what you see below. Make sure the `Elements` panel is highlighted:

![img](https://www.dataquest.io/wp-content/uploads/2019/01/devtools.png)

Chrome Developer Tools.

The elements panel will show you all the HTML tags on the page, and let you navigate through them. It’s a really handy feature!

By right clicking on the page near where it says “Extended Forecast”, then clicking “Inspect”, we’ll open up the tag that contains the text “Extended Forecast” in the elements panel:

![img](https://www.dataquest.io/wp-content/uploads/2019/01/ex_selected.png)

The extended forecast text.

We can then scroll up in the elements panel to find the “outermost” element that contains all of the text that corresponds to the extended forecasts. In this case, it’s a div tag with the id seven-day-forecast:

![img](https://www.dataquest.io/wp-content/uploads/2019/01/div.png)

The div that contains the extended forecast items.

If you click around on the console, and explore the div, you’ll discover that each forecast item (like “Tonight”, “Thursday”, and “Thursday Night”) is contained in a `div` with the class `tombstone-container`  (3 div levels down from id seven-day-forecast) .

We now know enough to download the page and start parsing it. In the below code, we:

- Download the web page containing the forecast.
- Create a `BeautifulSoup` class to parse the page.
- Find the `div` with id `seven-day-forecast`, and assign to `seven_day`
- Inside `seven_day`, find each individual forecast item.
- Extract and print the first forecast item.

**page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")**
**soup = BeautifulSoup(page.content, 'html.parser')**
**seven_day = soup.find(id="seven-day-forecast")**
**forecast_items = seven_day.find_all(class_="tombstone-container")**
**tonight = forecast_items[0]**
**print(tonight.prettify())**

## Extracting information from the page
As you can see, inside the forecast item tonight is all the information we want. There are 4 pieces of information we can extract:

- The name of the forecast item — in this case, Tonight.
- The description of the conditions — this is stored in the title property of img.
- A short description of the conditions — in this case, Mostly Clear.
- The temperature low — in this case, 49 degrees.
  We’ll extract the name of the forecast item, the short description, and the temperature first, since they’re all similar:

**period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()**
**temp = tonight.find(class_="temp").get_text()**
**print(period)**
**print(short_desc)**
**print(temp)**

Now, we can extract the title attribute from the img tag. To do this, we just treat the BeautifulSoup object like a dictionary, and pass in the attribute we want as a key:

**img = tonight.find("img")**
**desc = img['title']**
**print(desc)**

## Extracting all the information from the page

Now that we know how to extract each individual piece of information, we can combine our knowledge with css selectors and list comprehensions to extract everything at once.

In the below code, we:

- Select all items with the class `period-name` inside an item with the class `tombstone-container` in `seven_day`.
- Use a list comprehension to call the `get_text` method on each `BeautifulSoup` object.

**period_tags = seven_day.select(".tombstone-container .period-name")**
**periods = [pt.get_text() for pt in period_tags]**
**periods**
['Tonight',
'Thursday',
'ThursdayNight',
'Friday',
'FridayNight',
'Saturday',
'SaturdayNight',
'Sunday',
'SundayNight']

As you can see above, our technique gets us each of the period names, in order. We can apply the same technique to get the other 3 fields:

**short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]**
**temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]**
**descs = [d["title"] for d in seven_day.select(".tombstone-container img")]**

**print(short_descs)**

**print(temps)**

**print(descs)**
['Mostly Clear', 'Sunny', 'Mostly Clear', 'Sunny', 'Slight ChanceRain', 'Rain Likely', 'Rain Likely', 'Rain Likely', 'Chance Rain']
['Low: 49 °F', 'High: 63 °F', 'Low: 50 °F', 'High: 67 °F', 'Low: 57 °F', 'High: 64 °F', 'Low: 57 °F', 'High: 64 °F', 'Low: 55 °F']
['Tonight: Mostly clear, with a low around 49. West northwest wind 12 to

## Combining our data into a Pandas Dataframe
We can now combine the data into a Pandas DataFrame and analyze it. A DataFrame is an object that can store tabular data, making data analysis easy. If you want to learn more about Pandas, check out our free to start course [here](https://www.dataquest.io/course/data-analysis-intermediate)..

In order to do this, we’ll call the DataFrame class, and pass in each list of items that we have. We pass them in as part of a dictionary. Each dictionary key will become a column in the DataFrame, and each list will become the values in the column: