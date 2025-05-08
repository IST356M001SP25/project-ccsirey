# Reflection

Student Name:  name
Student Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

Over the course of developing the BART Travel Time comparer, I gained valuable experience in building a data-driven application using Python, Streamlit, and external APIs. The core functionality of the app allows users to compare estimated travel times between two BART stations in the San Francisco Bay Area, using both driving and public transit modes. Travel time data is retrieved through the Google Maps API displayed in a user-friendly web interface built with Streamlit. Users select a starting and ending station from dropdown menus, and the app returns real-time estimated travel durations.

A major goal of the project was to supplement these estimates with a dynamic map showing the two selected stations. I attempted to implement this using the Folium library, which can embed interactive maps in Streamlit via st.components.v1. However, I ran into several issues during this part of development. The first major challenge came from handling the API responses correctly. I initially encountered a TypeError that said “string indices must be integers, not 'str',” which was caused by an incorrect assumption about how the JSON response was structured. Later, I received a KeyError: 'status', which stemmed from forgetting to pass both the headers and params into the requests.get() function during an API call—this caused the response object to be missing expected fields. These errors required careful debugging, and I used a combination of print statements, response inspections, and try/except blocks to isolate where the logic was failing.

I also tried to improve the robustness of the app by implementing a local caching system that stores Google Place IDs in a JSON file. This reduced the number of API requests and prevented exceeding the usage limit on the free tier. Unit tests using pytest were written to verify the functionality of core components, including address-to-Place ID resolution and duration calculations between two known addresses. Setting up these tests also helped me learn how to configure import paths properly in VS Code, especially when working across code/, cache/, and tests/ folders.

Despite my efforts, I was not able to fully get the Folium map working in the final version. While I could generate the map and add markers for the selected stations, integrating this into Streamlit proved more difficult than expected, especially when debugging Streamlit's use of embedded HTML components. I spent considerable time tracing why map components failed to render and trying various ways to encode and pass HTML using folium._repr_html_() and components.html(), but persistent structure mismatches and unexpected exceptions prevented this part from being successfully completed.

Overall, this project challenged me to work through API errors, data formatting issues, and user interface integration. I improved not only my coding skills, but also my ability to debug, trace problems, and handle edge cases gracefully. Even though not every feature was implemented as planned, I now have a much better understanding of how APIs, data pipelines, and visualization tools fit together in an interactive application.