# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Model Name: CoolSongRecommender
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for.  

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

My recommender is designed to generate the top 5 songs that best matches the user's song preferences. This is intended for testing and seeing whether the model would be ready to make predictions on users preferences. This uses multiple features to find user's preference songs and give a score with the reasons as to why the user would prefer this song lyrics.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The features I used were genre, mood, energy, tempo_bpm, valence, danceability and acousticness. My dataset had 18 rows that also mention the title and artist of the song. The model turns this into a score by checking whether the recommendation matches the users preferred genre, mood and numeric ranges. Each match would add points to the recommended song score and the top 5 songs with the highest scores are displayed as recommendations. I added more features to the code to check to make sure that the there wasn't a dominant feature that would display the song recommendations. I also alternated the score like making genre match 1 point instead of 2 to see if the ranking behavior would change.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
The model used the songs.csv dataset. There were 10 songs and later I added 8 more songs to the dataset. There was pop, lofi, rock, ambient, jazz, etc for genre feature and happy, chill, intense, relaxed, etc for mood feature. I don't see anything really missing from the dataset.
## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

Most users prefer chill and excited mood songs as well as pop and lofi for genre and for this the recommended song choices were really good choices that fit well with this criteria. The score is successfully counting and number of matches from the recommended song to the users preferences giving high scores with explanations to the reason for that score.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

During my experiments I noticed how the feature energy is dominating and the score given for the songs closely relates to that. Users are also getting the same style since genre and mood are technically around the same for most users in the dataset. Some preference fields like artist_preferences and target_energy are not always used for scoring so the results may be inaccurate. It seems like the scoring is overrepresenting some features and underrepresenting the others. 

## 7. Evaluation  

How you checked whether the recommender behaved as expected.   

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---


I created a songsTest.py file and wrote different edge cases to check whether my rankings made sense. For user profile did 2 experiments as well to where I doubled the points for energy and reduced the points for genre to see if a feature was being more dominate than the other. What surprised me was that energy had a stronger impact on the scoring and some preference fields had little to no effect for the scoring criteria.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

I would try to balance the metric for the users preference for songs so that way the model can successfully find the recommended songs that fits the full criteria for the user. I would have the model go through testing and test edge cases and if there's failure in the edge cases I may add another feature or make changes to the model so the edge case works successfully. 
## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learnt how even though it may seem that the system worked successfully and the top 5 song recommendations came out with good explanations for the scoring, there may be some bias the model undergoes when looking through the features. I noticed that the energy was the most dominant feature and the model would mostly rely on that to find top recommendations. This has made me realized that it is important to create test cases for the model in which creating edge cases helps to make sure the model is fairly selecting top recommendation songs. If the edge cases fail, this proves that the model didn't do the scoring properly.