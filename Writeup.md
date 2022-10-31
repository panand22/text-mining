## Part 3: Project Writeup and Reflection

**1. Project Overview** [~1 paragraph]
What data source(s) did you use and what technique(s) did you use analyze/process them? What did you hope to learn/create?

I used the Project Gutenberg data source and used the following techniques to analyze/process them: 

**2. Implementation** [~1-2 paragraphs]
Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.

---
The data for this book was originally stored in a text file from the Project Gutenberg link. However, I stored it in a dictionary to track the frequency of the words that appear in the book. In this function, I removed the header and cleaned up the data. I also tracked the total words and number of different words in a histogram dictionary. I chose to use a dictionary, as it would be easy to track the frequency of the words and also iterate through them. Moreover, dictionaries allow for easy readibility and are also fast in looking up a key. 

I also used natural language processing to calculate a sentiment score of this book, 



**3. Results** [~2-3 paragraphs + figures/examples]
Present what you accomplished:

- If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
- If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.


**4. Reflection** [~1 paragraph]
From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

~~Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by task, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?~~

---
## Turning in your assignment

1. Push your completed code to GitGub repository (depending on which team member's repository is being used to work on the project).
2. Submit your Project Writeup/Reflection ~~(1 per team, not 1 per person)~~. This can be in the form of either:
    - a **Markdown** document pushed to GitHub, or
    - a **web page**.

    **Do not** use Word document or PDF file.
   
   Make sure there is a link to your reflection document in your _README.md_ file in your GitHub repo. Or you could use _README.md_ file to write reflection.
3. Create a pull request to the upstream repository. Learn [Creating a pull request](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/working-with-your-remote-repository-on-github-or-github-enterprise/creating-an-issue-or-pull-request).
4. **(This step is required for everyone)** Submit the URL of your project GitHub repository in the comment area on Canvas.

---
*updated: 10/19/2022*