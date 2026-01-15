---
guest: Dr. Fei Fei Li
title: The Godmother of AI on jobs, robots & why world models are next | Dr. Fei-Fei
  Li
youtube_url: https://www.youtube.com/watch?v=Ctjiatnd6Xk
video_id: Ctjiatnd6Xk
description: Dr. Fei-Fei Li is known as the “godmother of AI.” She’s been at the center
  of AI’s biggest breakthroughs for over two decades. She spearheaded ImageNet, the
  dataset that sparked the...
duration_seconds: 4774.0
duration: '1:19:34'
view_count: 139609
channel: Lenny's Podcast
keywords:
- experimentation
- hiring
- culture
- vision
- mission
- competition
- market
- persona
- design
- ui
- prototype
- founder
- investors
- platform
- ai
---

# The Godmother of AI on jobs, robots & why world models are next | Dr. Fei-Fei Li

## Transcript

Lenny Rachitsky (00:00:00):
A lot of people call you the godmother of AI. The work you did actually was the spark that brought us out of AI winter.

Dr. Fei Fei Li (00:00:07):
In the middle of 2015, middle of 2016, some tech companies avoid using the word AI because they were not sure if AI was a dirty word. 2017-ish was the beginning of companies calling themselves AI companies.

Lenny Rachitsky (00:00:22):
There's this line, I think, this was when you were presenting to Congress. There's nothing artificial about AI. It's inspired by people. It's created by people, and most importantly, it impacts people.

Dr. Fei Fei Li (00:00:30):
It's not like I think AI will have no impact on jobs or people. In fact, I believe that whatever AI does, currently or in the future, is up to us. It's up to the people. I do believe technology is a net positive for humanity, but I think every technology is a double-edged sword. If we're not doing the right thing as a society, as individuals, we can screw this up as well.

Lenny Rachitsky (00:00:56):
You had this breakthrough insight of just, okay, we can train machines to think like humans, but it's just missing the data that humans have to learn as a child.

Dr. Fei Fei Li (00:01:03):
I chose to look at artificial intelligence through the lens of visual intelligence because humans are deeply visual animals. We need to train machines with as much information as possible on images of objects, but objects are very, very difficult to learn. A single object can have infinite possibilities that is shown on an image. In order to train computers with tens and thousands of object concepts, you really need to show it millions of examples.

Lenny Rachitsky (00:01:36):
Today, my guest is Dr. Fei-Fei Li, who's known as the godmother of AI. Fei-Fei has been responsible for and at the center of many of the biggest breakthroughs that sparked the AI revolution that we're currently living through. She spearheaded the creation of ImageNet, which was basically her realizing that AI needed a ton of clean-labeled data to get smarter, and that data set became the breakthrough that led to the current approach to building and scaling AI models. She was chief AI scientist at Google Cloud, which is where some of the biggest early technology breakthroughs emerged from. She was director at SAIL, Stanford's Artificial Intelligence Lab, where many of the biggest AI minds came out of. She's also co-creator of Stanford's Human-Centered AI Institute, which is playing a vital role in a direction that AI is taking. She's also been on the board of Twitter. She was named one of Time's 100 Most Influential People in AI. She's also United Nations advisory board. I could go on.

(00:02:29):
In our conversation, Fei-Fei shares a brief history of how we got to today in the world of AI, including this mind-blowing reminder that 9 to 10 years ago, calling yourself an AI company was basically a death knell for your brand because no one believed that AI was actually going to work. Today, it's completely different. Every company is an AI company. We also chat about her take on how she sees AI impacting humanity in the future, how far current technologies will take us, why she's so passionate about building a world model and what exactly world models are, and most exciting of all, the launch of the world's first large world model, Marble, which just came out as this podcast comes out. Anyone can go play with this at marble.worldlabs.ai. It's insane. Definitely check it out. Fei-Fei is incredible and way too under the radar for the impact that she's had on the world, so I am really excited to have her on and to spread her wisdom with more people.

(00:03:22):
A huge thank you to Ben Horowitz and Condoleezza Rice for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. With that, I bring you Dr. Fei-Fei Li after a short word from our sponsors.

(00:03:37):
This episode is brought to you by Figma, makers of Figma Make. When I was a PM at Airbnb, I still remember when Figma came out and how much it improved how we operated as a team. Suddenly, I can involve my whole team in the design process, give feedback on design concepts really quickly and it just made the whole product development process so much more fun. But Figma never felt like it was for me. It was great for giving feedback and designs, but as a builder, I wanted to make stuff. That's why Figma built Figma Make. With just a few prompts, you can make any idea or design into a fully functional prototype or app that anyone can iterate on and validate with customers.

(00:04:15):
Figma Make is a different kind of vibe coding tool. Because it's all in Figma, you can use your team's existing design building blocks, making it easy to create outputs that look good and feel real and are connected to how your team builds. Stop spending so much time telling people about your product vision and instead show it to them. Make code-back prototypes and apps fast with Figma Make. Check it out at figma.com/lenny.

(00:04:40):
Did you know that I have a whole team that helps me with my podcast and with my newsletter? I want everyone on that team to be super happy and thrive in the roles. Justworks knows that your employees are more than just your employees; they're your people. My team is spread out across Colorado, Australia, Nepal, West Africa, and San Francisco. My life would be so incredibly complicated to hire people internationally, to pay people on time and in their local currencies, and to answer their HR questions 24/7. But with Justworks, it's super easy. Whether you're setting up your own automated payroll, offering premium benefits, or hiring internationally, Justworks offer simple software and 24/7 human support from small business experts for you and your people. They do your human resources right so that you can do right by your people. Justworks, for your people.

(00:05:31):
Fei-Fei, thank you so much for being here and welcome to the podcast.

Dr. Fei Fei Li (00:05:34):
I'm excited to be here, Lenny.

Lenny Rachitsky (00:05:36):
I'm even more excited to have you here. It is such a treat to get to chat with you. There's so much that I want to talk about. You've been at the center of this AI explosion that we're seeing right now for so long. We're going to talk about a bunch of the history that I think a lot of people don't even know about how this whole thing started, but let me first read a quote from Wired about you just so people get a sense, and in the intro I'll share all of the other epic things you've done. But I think this is a good way to just set context. "Fei-Fei is one of a tiny group of scientists, a group perhaps small enough to fit around a kitchen table, who are responsible for AI's recent remarkable advances."

(00:06:10):
A lot of people call you the godmother of AI, and unlike a lot of AI leaders, you're an AI optimist. You don't think AI is going to replace us. You don't think it's going to take all our jobs. You don't think it's going to kill us. So I thought it'd be fun to start there, just what's your perspective on how AI is going to impact humanity over time?

Dr. Fei Fei Li (00:06:30):
Yeah, okay, so Lenny, let me be very clear. I'm not a utopian, so it's not like I think AI will have no impact on jobs or people. In fact, I'm a humanist. I believe that whatever AI does, currently or in the future, is up to us. It's up to the people. So I do believe technology is a net positive for humanity. If you look at the long course of civilization, I think we are, and fundamentally, we're an innovative species that we... If you look at from written record thousands of years ago to now, humans just kept innovating ourselves and innovating our tools, and with that, we make lives better, we make work better, we build civilization, and I do believe AI is part of that. So that's where the optimism comes from. But I think every technology is a double-edged sword, and if we're not doing the right thing as a species, as a society, as communities, as individuals, we can screw this up as well.

Lenny Rachitsky (00:07:47):
There's this line, I think, this was when you were presenting to Congress, "There's nothing artificial about AI. It's inspired by people. It's created by people, and most importantly, it impacts people." I don't have a question there, but what a great line.

Dr. Fei Fei Li (00:07:59):
Yeah, I feel pretty deeply. I started working AI two and a half decades ago, and I've been having students for the past two decades and almost every student who graduates, I remind them when they graduate from my lab that your field is called artificial intelligence, but there's nothing artificial about it.

Lenny Rachitsky (00:08:23):
Coming back to the point you just made about how it's kind of up to us about where this all goes, what is it you think we need to get right? How do we set things on a path? I know this is a very difficult question to answer, but just what's your advice? What do you think we should be keeping in mind?

Dr. Fei Fei Li (00:08:36):
Yeah, how many hours do we have?

Lenny Rachitsky (00:08:39):
How do we align AI? There we go. Let's solve it.

Dr. Fei Fei Li (00:08:41):
So I think people should be responsible individuals no matter what we do. This is what we teach our children, and this is what we need to do as grownups as well. No matter which part of the AI development or AI deployment or AI application you are participating in, and most likely many of us, especially as technologists, we're in multiple points. We should act like responsible individuals and care about this. Actually, care a lot about this. I think everybody today should care about AI because it is going to impact your individual life. It is going to impact your community, it's going to impact the society and the future generation. And caring about it as a responsible person is the first, but also the most important step.

Lenny Rachitsky (00:09:37):
Okay, so let me actually take a step back and kind of go to the beginning of AI. Most people started hearing and caring about AI, as what it's called today, just like, I don't know, a few years ago when ChatGPT came out. Maybe it was like three years ago.

Dr. Fei Fei Li (00:09:51):
Three years ago, almost one more month, three years ago.

Lenny Rachitsky (00:09:55):
Wow, okay. And that was ChatGPT coming out. Is that the milestone you have in mind?

Dr. Fei Fei Li (00:09:56):
Yes.

Lenny Rachitsky (00:09:57):
Okay, cool. That's exactly how I saw it. But very few people know there was a long, long history of people working on, it was called machine learning back then and there's other terms, and now it's just everything's AI and there was kind of a long period of just a lot of people working on it. And then there's this what people refer to as the AI winter where people just gave up almost, most people did, and just, okay, this idea isn't going anywhere. And then the work you did actually was essentially the spark that brought us out of AI winter and is directly responsible for the world where now of just AI is all we talk about. As you just said, it's going to impact everything we do. So I thought it'd be really interesting to hear from you just the brief history of what the world was like before ImageNet and just the work you did to create ImageNet, why that was so important, and then just what happened after.

Dr. Fei Fei Li (00:10:44):
It is, for me, hard to keep in mind that AI is so new for everybody when I lived my entire professional life in AI. There's a part of me that is just, it's so satisfying to see a personal curiosity that I started barely out of teenagehood and now has become a transformative force of our civilization. It generally is a civilizational level technology. So that journey is about 30 years or 20 something, 20 plus years, and it's just very satisfying. So where did it all start? Well, I'm not even the first generation AI researcher. The first generation really date back to the '50s and '60s, and Alan Turing was ahead of his time in the '40s by asking, daring humanity with the question, "Is there thinking machines?" And of course he has a specific way of testing this concept of thinking machine, which is a conversational chatbot, which to his standard we now have a thinking machine.

(00:12:02):
But that was just a more anecdotal inspiration. The field really began in the '50s when computer scientists came together and look at how we can use computer programs and algorithms to build these programs that can do things that have been only capable by human cognition. And that was the beginning. And the founding fathers the Dartmouth workshop in the 1956, we have Professor John McCarthy who later came to Stanford who coined the term artificial intelligence. And between the '50s, '60s, '70s, and '80s, it was the early days of AI exploration and we had logic systems, we had expert systems, we also had early exploration of neural network. And then it came to around the late '80s, the '90s, and the very beginning of the 21st century. That stretch about 20 years is actually the beginning of machine learning, is the marriage between computer programming and statistical learning.

(00:13:23):
And that marriage brought a very, very critical concept into AI, which is that purely rule-based program is not going to account for the vast amount of cognitive capabilities that we imagine computers can do. So we have to use machines to learn the patterns. Once the machines can learn the patterns, it has a hope to do more things. For example, if you give it three cats, the hope is not just for the machines to recognize these three cats. The hope is the machines can recognize the fourth cat, the fifth cat, the sixth cat, and all the other cats. And that's a learning ability that is fundamental to humans and remaining animals. And we, as a field, realized, "We need machine learning." So that was up till the beginning of the 21st century. I entered the field of AI literally in the year of 2000. That's when my PhD began at Caltech.

(00:14:33):
And so I was one of the first generation machine learning researchers and we were already studying this concept of machine learning, especially neural network. I remember that was one of my first courses at Caltech is called neural network, but it was very painful. It was still smack in the middle of the so-called AI winter, meaning the public didn't look at this too much. There wasn't that much funding, but there was also a lot of ideas flowing around. And I think two things happened to myself that brought my own career so close to the birth of modern AI is that I chose to look at artificial intelligence through the lens of visual intelligence because humans are deeply visual animals. We can talk a little more later, but so much of our intelligence is built upon visual, perceptual, spatial understanding, not just language per se. I think they're complementary.

(00:15:37):
So I choose to look at visual intelligence and my PhD and my early professor years, my students and I are very committed to a north star problem, which is solving the problem of object recognition because it's a building block for the perceptual world, right? We go around the world interpreting reasoning and interacting with it more or less at the object level. We don't interact with the world at the molecular level. We don't interact with the world as... We sometimes do, but we rarely, for example, if you want to lift a teapot, you don't say, "Okay, the teapot is made of a hundred pieces of porcelain and let me work on this a hundred pieces." You look at this as one object and interact with it. So object is really important. So I was among the first researchers to identify this as a north star problem, but I think what happened is that as a student of AI and a researcher of AI, I was working on all kinds of mathematical models including neural network, including Bayesian network, including many, many models.

(00:16:53):
And there was one singular pain point is that these models don't have data to be trained on. And as a field, we were so focusing on these models, but it dawned on me that human learning as well as evolution is actually a big data learning process. Humans learn with so much experience constantly. In the evolution, if you look at time, animals evolve with just experiencing the world. So I think my students and I conjectured that a very critically-overlooked ingredient of bringing AI to life is big data. And then we began this ImageNet project in 2006, 2007. We were very ambitious. We want to get the entire internet's image data on objects. Now granted internet was a lot smaller than today, so I felt like that ambition was at least not too crazy. Now, it's totally delusional to think a couple of graduate student and a professor can do this.

(00:18:05):
And that's what we did. We curated very carefully, 15 million images on the internet, created a taxonomy of 22,000 concepts, borrowing other researchers' work like linguists work on WordNet, and it's a particular way of dictionarying words. And we combine that into ImageNet and we open-sourced that to the research community. We held an annual ImageNet challenge to encourage everybody to participate in this. We continue to do our own research, but 2012 was the moment that many people think was the beginning of the deep learning or birth of modern AI because a group of Toronto researchers led by Professor Geoff Hinton, participated in ImageNet Challenge, used ImageNet big data and two GPUs from NVIDIA and created successfully the first neural network algorithm that can...

(00:19:12):
It didn't totally solve, but made a huge progress towards solving the problem of object recognition. And that combination of the trio technology, big data, neural network, and GPU was kind of the golden recipe for modern AI. And then fast-forward, the public moment of AI, which is the ChatGPT moment, if you look at the ingredients of what brought ChatGPT to the world technically still use these three ingredients. Now, it's internet-scale data mostly texts is a much more complex neural network architecture than 2012, but it's still neural network and a lot more GPUs, but it's still GPUs. So these three ingredients are still at the core of modern AI.

Lenny Rachitsky (00:20:16):
Incredible. I have never heard that full story before. I love that it was two GPUs was the first. I love that. And now it's, I don't know, hundreds of thousands, right, that are orders of magnitude more powerful.

Dr. Fei Fei Li (00:20:30):
Yep.

Lenny Rachitsky (00:20:31):
And those two GPUs where they just bought, they were like gaming GPUs, they just went to the-

Dr. Fei Fei Li (00:20:34):
Yes.

Lenny Rachitsky (00:20:35):
... GameStar that people use for playing games. As you said, this continues to be in a large way, the way models get smarter. Some of the fastest growing companies in the world right now, I've had them all mostly on the podcast, Mercor and Surge and Scale. They continue to do this for labs, just give them more and more label data of the things they're most excited and interested in.

Dr. Fei Fei Li (00:20:53):
Yeah, I remember Alex Wang from Scale very early days. I probably still has his emails when he was starting Scale. He was very kind. He keeps sending me emails about how image that inspired Scale. I was very pleased to see that.

Lenny Rachitsky (00:21:08):
One of my other favorite takeaways from what you just shared is just such an example of high agency and just doing things that's kind of a meme on Twitter. Just you can just do things. You're just like, okay, this is probably necessary to move AI. And it's called machine learning back then, right? Was that the term most people used?

Dr. Fei Fei Li (00:21:25):
I think it was interchangeably. It's true. I do remember the companies, the tech companies, I am not going to name names, but I was in a conversation in one of the early days, I think is in the middle of 2015, middle of 2016, some tech companies avoid using the word AI because they were not sure if AI was a dirty word. And I remember I was actually encouraging everybody to use the word AI because to me that is one of the most audacious question humanity has ever asked in our quest for science and technology, and I feel very proud of this term. But yes, at the beginning some people were not sure.

Lenny Rachitsky (00:22:12):
What year was that roughly when AI was a dirty word?

Dr. Fei Fei Li (00:22:14):
2016, I think because that was-

Lenny Rachitsky (00:22:15):
2016, less than 10 years ago.

Dr. Fei Fei Li (00:22:18):
That was the changing. Some people start calling it AI, but I think if you look at the Silicon Valley tech companies, if you trace their marketing term, I think 2017-ish was the beginning of companies calling themselves AI companies.

Lenny Rachitsky (00:22:40):
That's incredible. Just how the world has changed.

Dr. Fei Fei Li (00:22:43):
Yes.

Lenny Rachitsky (00:22:43):
Now, you can't not call yourself an AI company.

Dr. Fei Fei Li (00:22:46):
I know.

Lenny Rachitsky (00:22:46):
Just nine-ish years later.

Dr. Fei Fei Li (00:22:48):
Yeah.

Lenny Rachitsky (00:22:49):
Oh, man. Okay. Is there anything else around the history, that early history that you think people don't know that you think is important before we chat about where you think things are going and the work that you're doing?

Dr. Fei Fei Li (00:23:01):
I think as all histories, I'm keenly aware that I am recognized for being part of the history, but there are so many heroes and so many researchers. We're talking about generations of researchers. In my own world, there are so many people who have inspired me, which I talked about in my book, but I do feel our culture, especially Silicon Valley, tends to assign achievements to a single person. While I think it has value, but it's just to be remembered. AI is a field of, at this point, 70 years old and we have gone through many generations. Nobody, no one could have gotten here by themselves.

Lenny Rachitsky (00:23:54):
Okay, so let me ask you this question. It feels like we're always on this precipice of AGI, this kind of vague term people throw around, AGI is coming, it's going to take over everything. What's your take on how far you think we might be from AGI? Do you think we're going to get there on the current trajectory we're on? Do you think we need more breakthroughs? Do you think the current approach will get us there?

Dr. Fei Fei Li (00:24:13):
Yeah, this is a very interesting term, Lenny. I don't know if anyone has ever defined AGI. There are many different definitions, including some kind of superpower for machines all the way to machines can become economically viable agent in the society. In other words, making salaries to live. Is that the definition of AGI? As a scientist, I take science very seriously and I enter the field because I was inspired by this audacious question of, can machines think and do things in the way that humans can do? For me, that's always the north star of AI. And from that point of view, I don't know what's the difference between AI and AGI.

(00:25:10):
I think we've done very well in achieving parts of the goal, including conversational AI, but I don't think we have completely conquered all the goals of AI. And I think our founding fathers, Alan Turing, I wonder if Alan Turing is around today and you ask him to contrast AI versus AGI, he might just shrugged and said, "Well, I asked the same question back in 1940s," so I don't want to get onto a rabbit hole of defining AI versus AGI. I feel AGI is more a marketing term than a scientific term as a scientist than technologist. AI is my north star, is my field's north star, and I'm happy people call it whatever name they want to call it.

Lenny Rachitsky (00:26:05):
So let me ask you maybe this way, like you described, there's kind of these components that from ImageNet and AlexNet took us to where we're today, GPUs essentially, data, label data, just like the algorithm of the model. There's also just the transformer feels like an important step in that trajectory. Do you feel like those are the same components that'll get us to, I don't know, 10 times smarter model, something that's like life-changing for the entire world? Or do you think we need more breakthroughs? I know we're going to talk about world models, which I think is a component of this, but is there anything else that you think is like, oh, this will plateau, or okay, this will take us just need more data, more compute, more GPUs?

Dr. Fei Fei Li (00:26:44):
Oh no, I definitely think we need more innovations. I think scaling loss of more data, more GPUs, and bigger current model architecture is there's still a lot to be done there, but I absolutely think we need to innovate more. There's not a single deeply scientific discipline in human history that has arrived at a place that says we're done, we're done innovating and AI is one of the, if not the youngest discipline in human civilization in terms of science and technology, we're still scratching the surface. For example, like I said, we're going to segue into world models. Today, you take a model and run it through a video of a couple of office rooms and ask the model to count the number of chairs. And this is something a toddler could do or maybe an elementary school kid could do, and AI could not do that, right?

(00:27:50):
So there's just so much AI today could not do, then let alone thinking about how did someone like Isaac Newton look at the movements of the celestial bodies and derive an equation or a set of equations that governs the movement of all bodies, that level of creativity, extrapolation, abstraction. We have no way of enabling AI to do that today. And then let's look at emotional intelligence. If you look at a student coming to a teacher's office and have a conversation about motivation, passion, what to learn, what's the problem that's really bothering you. That conversation, as powerful as today's conversational bots are, you don't get that level of emotional cognitive intelligence from today's AI. So there's a lot we can do better, and I do not believe we're done innovating.

Lenny Rachitsky (00:29:00):
Demis had this really interesting interview recently from DeepMind slash Google where someone asked him just like, "What do you think, how far are we from AGI? What does it look like going through there?" He had a really interesting way of approaching it is if we were to give the most cutting-edge model all the information until the end of the 20th century, see if it could come up with all the breakthroughs Einstein had and so far we're nowhere near that, but they could just-

Dr. Fei Fei Li (00:29:22):
No, we're not. In fact, it's even worse. Let's give AI all the data including modern instruments data of celestial bodies, which Newton did not have, and give it to that and just ask AI to create the 17th century set of equations on the laws of bodily movements. Today's AI cannot do that.

Lenny Rachitsky (00:29:49):
All right. We're ways away is what I'm hearing.

Dr. Fei Fei Li (00:29:50):
Yeah.

Lenny Rachitsky (00:29:51):
Okay, so let's talk about world models. To me, this is just another really amazing example of you being ahead of where people end up. So you were way ahead on, okay, we just need a lot of clean data for AI and neural networks to learn. You've been talking about this idea of world models for a long time. You started a company to build, essentially there's language models. This is a different thing. This is a world model. We'll talk about what that is. And now, as I was preparing for this Elon's talking about world models, Jensen's talking about world models, I know Google's working on this stuff. You've been at this for a long time and you actually just launched something that's going, we're going to talk about right before this podcast airs. Talk about what is a world model? Why is it so important?

Dr. Fei Fei Li (00:30:33):
I'm very excited to see that more and more people are talking about world models like Elon, like Jensen. I have been thinking about really how to push AI forward all my life and the large language models that came out of the research world and then OpenAI and all this, for the past few years, were extremely inspiring even for a researcher like me. I remembered when GPT2 came out, and that was in, I think, late 2020. I was co-director, I still am, but I was at that time full-time co-director of Stanford's Human-Centered AI institute, and I remember it was... The public was not aware of the power of the large language model yet, but as researchers, we were seeing it, we're seeing the future, and I had pretty long conversations with my natural language processing colleagues like Percy Liang and Chris Manning. We were talking about how critical this technology is going to be and the Stanford AI Institute, Human-Centered AI Institute, HAI, was the first one to establish a full research center foundation model.

(00:31:59):
We were, Percy Liang, and many researchers led the first academic paper foundation model. So it was just very inspiring for me. Of course, I come from the world of visual intelligence and I was just thinking there's so much we can push forward beyond language because humans, humans use our sense of spatial intelligence, a world understanding to do so many things and they are beyond language. Think about a very chaotic first responder scene, whether it's fire or some traffic accident or some natural disaster. And if you immerse yourself in those scene and think about how people organize themselves to rescue people, to stop further disasters, to put down fires, a lot of that is movements is spontaneous understanding of objects, worlds, human situational awareness. Language is part of that, but a lot of those situations, language cannot get you to put down the fire.

(00:33:21):
So that is, what is that? I was thinking a lot. And in the meantime, I was doing a lot of robotics research and it dawned on me that the linchpin of connecting the additional intelligence, in addition to language embodied AI, which are robotics, connecting visual intelligence, is the sense of spatial intelligence about understanding the world. And that's when I think it was 2024, I gave a TED talk about spatial intelligence at world models. And I start formulating this idea back in 2022 based on my robotics and computer vision research. And then one thing that was really clear to me is that I really want to work with the brightest technologists and move as fast as possible to bring this technology to life. And that's when we founded this company called World Labs. And you can see the word world is in the title of our company because we believe so much in world modeling and spatial intelligence.

Lenny Rachitsky (00:34:41):
People are so used to just chatbots and that's a large language model. A simple way to understand a world model is you basically describe a scene and it generates an infinitely explorable world. We'll link to the thing you launched, which we'll talk about, but just is that a simple way to understand it?

Dr. Fei Fei Li (00:34:56):
That's part of it, Lenny. I think a simple way to understand a world model is that this model can allow anyone to create any worlds in their mind's eye by prompting whether it's an image or a sentence. And also be able to interact in this world whether you are browsing and walking or picking objects up or changing things as well as to reason within this world, for example, if the person consuming, if the agent consuming this output of the world model is a robot, it should be able to plan its path and help to tidy the kitchen, for example. So world model is a foundation that you can use to reason, to interact, and to create worlds.

Lenny Rachitsky (00:36:00):
Great. Yeah. So robots feels like that's potentially the next big focus for AI researchers and just the impact on the world. And what you're saying here is this is a key missing piece of making robots actually work in the real world, understanding how the world works.

Dr. Fei Fei Li (00:36:17):
Yeah. Well, first of all, I do think there's more than robots. That's exciting. But I agree with everything you just said. I think world modeling and spatial intelligence is a key missing piece of embodied AI. I also think let's not underestimate that humans are embodied agents and humans can be augmented by AI's intelligence. Just like today, humans are language animals, but we're very much augmented by AI helping us to do language tasks including software engineering. I think that we shouldn't underestimate or maybe we tend not to talk about how humans, as an embodied agents, can actually benefit so much from world models and spatial intelligence models as well as robots can.

Lenny Rachitsky (00:37:15):
So the big unlocks here, robots, which a huge deal if this works out, imagine each of us has robots doing a bunch of stuff for us, they help us with disasters, things like that. Games obviously is a really cool example, just like infinitely playable games that you just invent out of your head. And then creativity feels like just like being fun, having fun, being creative, thinking of magic, wild new worlds, and environments.

Dr. Fei Fei Li (00:37:39):
And also design, humans design from machines to buildings to homes and also scientific discovery. There is so much. I like to use the example of the discovery of the structure of DNA. If you look at one of the most important piece in DNA's discovery history is the x-ray diffraction photo that was captured by Rosalind Franklin, and it was a flat 2D photo of a structure that it looks like a cross with diffractions. You can google those photos. But with that 2D flat photo, the humans, especially two important humans, James Watson and Francis Crick, in addition to their other information, was able to reason in 3D space and deduce a highly three-dimensional double helix structure of the DNA. And that structure cannot possibly be 2D. You cannot think in 2D and deduce that structure. You have to think in 3D spatial, use the human spatial intelligence. So I think even in scientific discovery, spatial intelligence or AI-assisted spatial intelligence is critical.

Lenny Rachitsky (00:39:08):
This is such an example of, I think it was Chris Dixon that had this line that the next big thing is going to start off feeling like a toy. When ChatGPT just came out, I remember Sam Altman just tweeted it as like, "Here's a cool thing we're playing with, check it out." Now, it's the fastest growing product to all of history, changed the world. And it's oftentimes the things that just look like, okay, this is cool, that it's a fun to play with that end up changing the world most.

(00:39:33):
This episode is brought to you by Sinch, the customer communications cloud. Here's the thing about digital customer communications. Whether you're sending marketing campaigns, verification codes, or account alerts, you need them to reach users reliably. That's where Sinch comes in. Over 150,000 businesses, including 8 of the top 10 largest tech companies globally use Sinch's API to build messaging, email, and calling into their products. And there's something big happening in messaging that product teams need to know about, Rich Communication Services or RCS. Think of RCS as SMS2.0. Instead of getting texts from a random number, your users will see your verified company name and logo without needing to download anything new.

(00:40:16):
It's a more secure and branded experience. Plus you get features like interactive carousels and suggested replies. And here's why this matters, US carriers are starting to adopt RCS. Sinch is already helping major brands send RCS messages around the world and they're helping Lenny's podcast listeners get registered first before the rush hits the US market. Learn more and get started at sinch.com/lenny. That's S-I-N-C-H.com/lenny.

(00:40:45):
I reached out to Ben Horowitz, who loves what you're doing, a big fan of yours. They're investors I believe in...

Dr. Fei Fei Li (00:40:51):
Yeah, we've known each other for many years, but yes, right now they're investors of World Labs.

Lenny Rachitsky (00:40:57):
Amazing. Okay, so I asked him what I should ask you about and he suggested ask you why is the bitter lesson alone not likely to work for robots? So first of all, just explain what the bitter lesson was in the history of AI and then just why that won't get us to where we want to be with robots.

Dr. Fei Fei Li (00:41:17):
Well, first of all, there are many bitter lessons, but the bitter lessons everybody refers to is a paper written by Richard Sutton who won the Turing Award recently, and he does a lot of reinforcement learning. And Richard has said, if you look at the history, especially the algorithmic development of AI, it turns out simpler model with a ton of data always win at the end of the day instead of the more complex model with less data. I mean, that was actually... This paper came years after ImageNet. That to me was not bitter; it was a sweet lesson. That's why I built ImageNet because I believe that big data plays that role. So why can't bitter lesson work in robotics alone? Well, first of all, I think we need to give credit to where we are today. Robotics is very much in the early days of experimentation.

(00:42:25):
The research is not nearly as mature as say language models. So many people are still experimenting with different algorithms and some of those algorithms are driven by big data. So I do think big data will continue to play a role in robotics, but what is hard for robotics, there are a couple of things. One is that it's harder to get data. It's a lot harder to get data. You can say, well, there's web data. This is where the latest robotics research is using web videos. And I think web videos do play a role. But if you think about what made language model worth a very... As someone who does computer vision and spatial intelligence and robotics, I'm very jealous of my colleagues in language because they had this perfect setup where their training data are in words, eventually tokens, and then they produce a model that outputs words.

(00:43:36):
So you have this perfect alignment between what you hope to get, which we call objective function and what your training data looks like. But robotics is different. Even spatial intelligence is different. You hope to get actions out of robots, but your training data lacks actions in 3D worlds, and that's what robots have to do, right? Actions in 3D worlds. So you have to find different ways to fit a, what do they call, a square in a round hole, that what we have is tons of web videos. So then we have to start talking about adding supplementing data such as teleoperation data or synthetic data so that the robots are trained with this hypothesis of bitter lesson, which is large amount of data. I think there's still hope because even what we are doing in world modeling will really unlock a lot of this information for robots.

(00:44:53):
But I think we have to be careful because we're at the early days of this and bitter lesson is still to be tested because we haven't fully figured out the data for. Another part of the bitter lesson of robotics I think we should be so realistic about is again, compared to language models or even spatial models, robots are physical systems. So robots are closer to self-driving cars than a large language model. And that's very important to recognize. That means that in order for robots to work, we not only need brains, we also need the physical body. We also need application scenarios. If you look at the history of self-driving car, my colleague Sebastian Thrun took Stanford's car to win the first DARPA challenge in 2006 or 2005. It's 20 years since that prototype of a self-driving car being able to drive 130 miles in the Nevada desert to today's Waymo and on the street of San Francisco.

(00:46:17):
And we're not even done yet. There's still a lot. So that's a 20-year journey. And self-driving cars are much simpler robots, they're just metal boxes running on 2D surfaces, and the goal is not to touch anything. Robot is 3D things running in 3D world, and the goal is to touch things. So the journey is going to be, there's many aspects, elements, and of course one could say, well, the self-driving car, early algorithm were pre deep learning era. So deep learning is accelerating the brains. And I think that's true. That's why I'm in robotics, that's why I'm in spatial intelligence and I'm excited by it. But in the meantime, the car industry is very mature and productizing also involves the mature use cases, supply chains, the hardware. So I think it's a very interesting time to work in these problems. But it's true, Ben is right. We might still be subject to a number of bitter lessons.

Lenny Rachitsky (00:47:28):
Doing this work, do you ever just feel awe for the way the brain works and is able to do all of this for us? Just the complexity just to get a machine to just walk around and not hit things and fall, does just give you more respect for what we've already got?

Dr. Fei Fei Li (00:47:44):
Totally. We operate on about 20 watts. That's dimmer than any light bulb in the room I'm in right now. And yet we can do so much. So I think actually the more I work in AI, the more I respect humans.

Lenny Rachitsky (00:48:03):
Let's talk about this product you just launched. It's called Marble, a very cute name. Talk about what this is, why this is important. I've been playing with it, it's incredible. We'll link to it for folks to check it out. What is Marble?

Dr. Fei Fei Li (00:48:14):
Yeah, I'm very excited. So first of all, Marble is one of the first product that World Labs has rolled out. World Labs is a foundation frontier model company. We are founded by four co-founders who have deep technical history. My co-founders, Justin Johnson, Christoph Lassner, and Ben Mildenhall. We all come from the research field of AI, computer graphics, computer vision, and we believe that spatial intelligence and world modeling is as important, if not more, to language models and complementary to language models. So we wanted to seize this opportunity to create deep tech research lab that can connect the dots between frontier models with products. So Marble is an app that's built upon our frontier models. We've spent a year and plus building the world's first generative model that can output genuinely 3D worlds. That's a very, very hard problem.

(00:49:30):
And it was a very hard process and we have a team of incredible, founding team of incredible technologists from incredible teams. And then around just a month or two ago, we saw the first time that we can just prompt with a sentence and the image and multiple images and create worlds that we can just navigate in. If you put it on Google, which we have an option to let you do that, you can even walk around. Even though we've been building this for quite a while, it was still just awe-inspiring and we wanted to get into the hands of people who need it. And then we know that so many creators, designers, people who are thinking about robotic simulation, people who are thinking about different use cases of navigable interactable, immersive worlds game developers will find this useful. So we developed Marble as a first step. It's again, still very early, but it's the world's first model doing this, and it's the world's first product that allows people to just prompt, we call it prompt to worlds.

Lenny Rachitsky (00:51:00):
Well, I've been playing around with it. It is insane. You could just have a little Shire world where you just infinitely walk around middle earth basically, and there's no one there yet, but it's insane. You just go anywhere. There's dystopian world. I'm just looking at all these examples and my favorite part, actually, I don't know if there's a feature or bug, you can see the dots of the world before it actually renders with all the textures. And I just love like, you get a glimpse into what is going on with this model, basically-

Dr. Fei Fei Li (00:51:27):
That is so cool to hear because this is where, as a researcher, I am learning because the dots that lead you into the world was an intentional feature visualization, is not part of the model. The model actually just generates the world. But we were trying to find a way to guide people into the world, and a number of engineers worked on different versions, but we converged on the dot, and so many people, you're not the only one, told us how delightful that experience is, and it was really satisfying for us to hear that this intentional visualization feature that's not just the big hardcore model actually has delighted our users.

Lenny Rachitsky (00:52:19):
Wow. So you add that to make it more, like to have humans understand what's going on-

Dr. Fei Fei Li (00:52:24):
To have fun, yes.

Lenny Rachitsky (00:52:24):
... get more delightful. Wow, that is hilarious. It makes me think about LLMs and the way they, it's not the same thing, but they talk about what they're thinking and what they're doing.

Dr. Fei Fei Li (00:52:32):
Yes, it is. It is.

Lenny Rachitsky (00:52:34):
It also makes me think about just the Matrix. It's exactly the Matrix experience. I don't know if that was your inspiration.

Dr. Fei Fei Li (00:52:42):
Well, like I said, a number of engineers worked on that. It could be their inspiration.

Lenny Rachitsky (00:52:48):
It's in their subconscious. Okay, so just for folks that may want to play around with this, maybe like, what are some applications today that folks can start using today? What's your goal with this launch?

Dr. Fei Fei Li (00:52:59):
Yeah, so we do believe that world modeling is very horizontal, but we're already seeing some really exciting use cases, virtual production for movies, because what they need are 3D worlds that they can align with the camera. So when the actors are acting on it, they can position the camera and shoot the segments really well. And we're already seeing incredible use. In fact, I don't know if you have seen our launch video showing Marble. It was produced by a virtual production company. We collaborated with Sony and they use Marble scenes to shoot those videos. So we were collaborating with those technical artists and directors, and they were saying, this has cut our production time by 40X. In fact, it has to-

Lenny Rachitsky (00:53:00):
40X?

Dr. Fei Fei Li (00:53:59):
Yes, in fact it has to, because we only had one month to work on this project and there were so many things they were trying to shoot. So using Marble really, really significantly accelerated the virtual production for VFX and movies. That's one use cases. We are already seeing our users taking our Marble scene and taking the mesh export and putting games, whether it's games on VR or just fun games that they have developed. We are showing an example of robotic simulation because when I was, I mean I still am a researcher doing robotic training. One of the biggest pain point is to create synthetic data for training robots. And this synthetic data needs to be very diverse. They need to come from different environments with different objects to manipulate. And one path to it is to ask computers to simulate.

(00:55:10):
Otherwise, humans have to build every single asset for robots. That's just going to take a lot longer. So we already have researchers reaching out and wanting to use Marble to create those synthetic environments. We also have unexpected user outreach in terms of how they want to use Marble. For example, a psychologist team called us to use Marble to do psychology research. It turned out some of the psychiatric patients they study, they need to understand how their brain respond to different immersive things of different features. For example, messy scenes or clean scenes or whatever you name it. And it's very hard for researchers to get their hands on these kind of immersive scenes and it will take them too long and too much budget to create. And Marble is a really almost instantaneous way of getting so many of these experimental environments into their hands. So we're seeing multiple use cases at this point. But the VFX, the game developers, the simulation developers as well as designers are very excited.

Lenny Rachitsky (00:56:39):
This is very much the way things work in AI. I've had other AI leaders on the podcast and it's always put things out there early as soon as you can to discover where the big use cases are. The head of ChatGPT told me how, when they first put out ChatGPT, he was just scanning TikTok to see how people were using it and all the things they were talking about, and that's what convinced them where to lean in and help them see how people actually want to use it. I love this last use case for therapy. I'm just imagining heights, people dealing with heights or snakes or spiders, which-

Dr. Fei Fei Li (00:57:11):
It's amazing. A friend of mine last night literally called me and talked about his height scare and asked me if Marble should be used. It's amazing you went straight there.

Lenny Rachitsky (00:57:24):
Because imagining all the exposure therapy stuff, this could be so good for that. That is so cool. Okay, so I should have asked you this before, but I think there's going to be a question of just, how does this differ from things like VO3 and other video generation models? It's pretty clear to me, but I think it might be helpful just to explain how this is different from all the video AI tools people have seen.

Dr. Fei Fei Li (00:57:46):
World Labs' thesis is that spatial intelligence is fundamentally very important, and spatial intelligence is not just about videos. In fact, the world is not passively watching videos passing by. I love, Plato has the allegory of the cave analogy to describe vision. He said that imagine a prisoner tied on his chair, not very humane, but in a cave watching a full life theater in front of him, but the actual life theater that actors are acting is behind his back. It was just lit so that the projection of the action is on a wall of the cave. And then the goal, the task of this prisoner is to figure out what's going on. It's a pretty extreme example, but it really shows, it describes what vision is about, is that to make sense of the 3D world or 4D world out of 2D. So spatial intelligence to me is deeper than only creating that flat 2D world.

(00:59:14):
Spatial intelligence to me is the ability to create, reason, interact, make sense of deeply spatial world, whether it's 2D or 3D or 4D, including dynamics and all that. So World Lab is focusing on that, and of course the ability to create videos per se could be part of this. And in fact, just a couple of weeks ago, we rolled out the world's first real time demoable, real-time video generation on a single H100 GPU. So part of our technology includes that, but I think Marble is very different because we really want creators, designers, developers to have in their hands a model that can give them worlds with 3D structures so they can use it for their work. And that's why Marble is so different.

Lenny Rachitsky (01:00:21):
The way I see it is it's a platform for a ton of opportunity to do stuff. As you described, videos are just like, here's a one-off video that's very fun and cool and you could... And that's it. That's it. And you move on.

Dr. Fei Fei Li (01:00:33):
By the way, we could in Marble, we could allow people to export in video forms. So you could actually, like you said, you go into a world, so let's say it's a hobbit cave. You can actually, especially as a creator, you have such a specific way of moving the camera in a trajectory in the director's mind, and then you can export that from Marble into a video.

Lenny Rachitsky (01:01:02):
What does it take to create something like this? Just how big is the team, how many GPUs you work in? Anything you can share there. I don't know how much of this is private information, but just what does it take to create something like this that you've launched here?

Dr. Fei Fei Li (01:01:12):
It takes a lot of brain power. So we just talk about 20 watts per brain. So from that point of view, it's a small number, but it's actually incredible. It's half billion years of evolution to give us those power. We have a team of 30-ish people now, and we are predominantly researchers and research engineers, but we also have designers and product. We actually really believe that we want to create a company that's anchored in the deep tech of spatial intelligence, but we are actually building serious products. So we have this integration of R&D and productization, and of course, we use a ton of GPUs.

Lenny Rachitsky (01:02:15):
That's the technical thing.

Dr. Fei Fei Li (01:02:17):
Happy to hear.

Lenny Rachitsky (01:02:20):
Well, congrats on the launch. I know this is a huge milestone. I know this took a ton of work.

Dr. Fei Fei Li (01:02:20):
Thank you.

Lenny Rachitsky (01:02:23):
So I just want to say congrats to you and your team. Let me talk about your founder journey for a moment. So you're a founder of this company. You started how many years ago? A couple of years ago, two, three years ago?

Dr. Fei Fei Li (01:02:23):
A year ago.

Lenny Rachitsky (01:02:33):
A year ago?

Dr. Fei Fei Li (01:02:34):
A year plus.

Lenny Rachitsky (01:02:37):
A year? Okay. Wow.

Dr. Fei Fei Li (01:02:37):
Probably, 18 month, yeah.

Lenny Rachitsky (01:02:38):
Okay. What's something you wish you knew before you started this that you wish you could whisper into the ear of Fei-Fei of 18 months ago?

Dr. Fei Fei Li (01:02:46):
Well, I continue to wish I know the future of technology. I think actually that's one of our founding advantage is that we see the future earlier in general than most people. But still, man, this is so exciting and so amazing that what's unknown and what's coming, but I know the reason you're asking me this question is not about the future of technology. Furthermore, look, I did not start a company of this scale at 20-year-old. So I started a dry cleaner when I was 19, but that's a little smaller scale.

Lenny Rachitsky (01:03:30):
We got to talk about that.

Dr. Fei Fei Li (01:03:32):
And then I founded Google Cloud AI and then I founded an institute at Stanford but those are different beasts. I did feel I was a little more prepared as a founder of the grinding journey compared to maybe the 20-year-old founders. But I still, I'm surprised, and it puts me into paranoia sometimes that how intensely competitive AI landscape is from the model, the technology itself, as well as talents. And when I founded the company, we did not have these incredible stories of how much certain talents would cost. So these are things that continue to surprise me and I have to be very alert about.

Lenny Rachitsky (01:04:40):
So the competition you're talking about is the competition for talent, the speed at which just how things are moving.

Dr. Fei Fei Li (01:04:46):
Yeah.

Lenny Rachitsky (01:04:47):
Yeah. You mentioned this point that I want to come back to that if you just look over the course of your career, you were at all of the major collections of humans that led to so many of the breakthroughs that are happening today. Obviously, we talk about ImageNet also just SAIL at Stanford is where a lot of the work happened, Google Cloud, which a lot of the breakthroughs happened. What brought you to those places? Like for people looking for how to advance in their career, be at the center of the future, just is there a through line there of just what pulled you from place to place and pulled you into those groups that might be helpful for people to hear?

Dr. Fei Fei Li (01:05:25):
Yeah, this is actually a great question, Lenny, because I do think about it, and obviously we talked about it's curiosity and passion that brought me to AI, that is more a scientific north star, right? I did not care if AI was a thing or not, so that was one part. But how did I end up choosing in the particular places I work in, including starting World Labs, is I think I'm very grateful to myself or maybe to my parents' genes. I'm an intellectually very fearless person, and I have to say when I hire young people, I look for that because I think that's a very important quality if one wants to make a difference, is that when you want to make a difference, you have to accept that you're creating something new or you're diving into something new. People haven't done that. And if you have that self-awareness, you almost have to allow yourself to be fearless and to be courageous.

(01:06:42):
So when I, for example, came to Stanford, in the world of academia, I was very close to this thing called tenure, which is have the job forever at Princeton. But I chose to come to Stanford because... I love Princeton. It's by alma mater. It's just at that moment there are people who are so amazing at Stanford and the Silicon Valley ecosystem was so amazing that I was okay to take a risk of restarting my tenure clock. Becoming the first female director of SAIL, I was actually relatively speaking a very young faculty at that time, and I wanted to do that because I care about that community. I didn't spend too much time thinking about all the failure cases.

(01:07:46):
Obviously, I was very lucky that the more senior faculty supported me, but I just wanted to make a difference. And then going to Google was similar. I wanted to work with people like Jeff Dean, Jeff Hinton, and all these incredible demists, the incredible people. The same with World Labs. I have this passion. And I also believe that people with the same mission can do incredible things. So that's how it guided my through line. I don't overthink of all possible things that can go wrong because that's too many.

Lenny Rachitsky (01:08:33):
I feel like an important element of this is not focusing on the downside, focusing more on the people, the mission. What gets you excited, what do you think, the curiosity.

Dr. Fei Fei Li (01:08:43):
Yeah. I do want to say one thing to all the young talents in AI, the engineers, the researchers out there, because some of you apply to World Labs, I feel very privileged you considered World Labs. I do find many of the young people today think about every single aspect of an equation when they decide on jobs. At some point, maybe that's the way they want to do it, but sometimes I do want to encourage young people to focus on what's important because I find myself constantly in mentoring mode when I talk to job candidates. Not necessarily recruiting or not recruiting, but just in mentoring mode when I see an incredible young talent who is over-focusing on every minute dimension and aspect of considering a job, when maybe the most important thing is where's your passion? Do you align with the mission? Do you believe and have faith in this team? And just focus on the impact and you can make and the kind of work and team you can work with.

Lenny Rachitsky (01:10:05):
Yeah, it's tough. It's tough for people in the AI space. Now there's so much, so much at them, so much new, so much happening, so much FOMO.

Dr. Fei Fei Li (01:10:11):
That's true.

Lenny Rachitsky (01:10:12):
I could see the stress. And so I think that advice is really important. Just like what will actually make you feel fulfilled in what you're doing, not just where's the fastest growing company, where's the... Who's going to win? I don't know. I want to make sure I ask you about the work you're doing today at Stanford, at the HCI. I think it's the-

Dr. Fei Fei Li (01:10:12):
HAI.

Lenny Rachitsky (01:10:30):
HAI, Human-Centered AI Institute. What are you doing there? I know this is a thing you do on the side still.

Dr. Fei Fei Li (01:10:36):
So yes, HAI, Human-Centered AI Institute was co-founded by me and a group of faculty like Professor John Etchemendy, Professor James Landay, Professor Chris Manning back in 2018. I was actually finishing my last sabbatical at Google and it was a very, very important decision for me because I could have stayed in industry, but my time at Google taught me one thing is AI is going to be a civilization of technology. And it dawned on me how important this is to humanity to the point that I actually wrote a piece in New York Times, that year 2018, to talk about the need for a guiding framework to develop and to apply AI. And that framework has to be anchored in human benevolence, in human centeredness. And I felt that Stanford, one of the world's top university in the heart of Silicon Valley that gave birth to important companies from NVIDIA to Google, should be a thought leader to create this human-centered AI framework and to actually embody that in our research education and policy and ecosystem work.

(01:12:10):
So I founded HAI. Fast-forward, after six, seven years, it has become the world's largest AI institute that does human-centered research, education, ecosystem, outreach, and policy impact. It involves hundreds of faculty across all eight schools at Stanford, from medicine to education, to sustainability to business, to engineering, to humanities to law. And we support researchers, especially at the interdisciplinary area from digital economy, to legal studies, to political science, to discovery of new drugs, to new algorithms to that's beyond transformers. We also actually put a very strong focus on policy because when we started HAI, I realized that Silicon Valley did not talk to Washington DC and or Brussels or other parts of the world.

(01:13:27):
And given how important this technology is, we need to bring everybody on board. So we created multiple programs from congressional bootcamp to AI index report to policy briefing, and we especially participated in policymaking including advocating for a national AI research cloud bill that was passed in the first Trump administration and participating in state level regulatory AI discussions. So there's a lot we did, and I continue to be one of the leaders even though I'm much less involved operationally because I care not only we create this technology, but we use it in the right way.

Lenny Rachitsky (01:14:24):
Wow. I was not aware of all that other work you were doing. As you're talking, I was reminded Charlie Munger had this quote, "Take a simple idea and take it very seriously." I feel like you've done that in so many different ways and stayed with it and it's unbelievable the impact that you've had in so many ways over the years. I'm going to skip the lightning round and I'm just looking to ask you one last question. Is there anything else that you wanted to share? Anything else you want to leave listeners with?

Dr. Fei Fei Li (01:14:52):
I am very excited by AI, Lenny. I want to answer one question that when I travel around the world, everybody asks me is that, if I'm a musician, if I'm a teacher, middle school teacher, if I'm a nurse, if I'm an accountant, if I'm a farmer, do I have a role in AI or is AI just going to take over my life or my work? And I think this is the most important question of AI and I find that in Silicon Valley, we tend not to speak heart-to-heart with people, with people like us and not like us in Silicon Valley, but all of us, we tend to just toss around words like infinite productivity or infinite leisure time or infinite power or whatever. But at the end of the day, AI is about people. And when people ask me that question, it's a resounding yes, everybody has a role in AI.

(01:16:03):
It depends on what you do and what you want. But no technology should take away human dignity and the human dignity and agency should be at the heart of the development, the deployment, as well as the governance of every technology. So if you are a young artist and your passion is storytelling, embrace AI as a tool. In fact, embrace Marble. I hope it becomes a tool for you because the way you tell your story is unique and the world still needs it. But how you tell your story, how do you use the most incredible tool to tell your story in the most unique way is important. And that voice needs to be heard. If you are a farmer near retirement, AI still matters because you are a citizen. You can participate in your community, you should have a voice in how AI is used, how AI is applied.

(01:17:14):
You work with people that you can encourage all of you to use AI to make life easier for you. If you are a nurse, I hope you know that at least in my career, I have worked so much in healthcare research because I feel our healthcare workers should be greatly augmented and helped by AI technology, whether it's smart cameras to feed more information or robotic assistance because our nurses are overworked, overfatigued, and as our society ages, we need more help for people to be taken care of. So AI can play that role. So I just want to say that it's so important that even a technologist like me are sincere about that everybody has a role in AI.

Lenny Rachitsky (01:18:17):
What a beautiful way to end it. Such a tie back to where we started about how it's up to us and take individual responsibility for what AI will do in our lives. Final question, where can folks find Marble? Where can they go, maybe try to join World Labs if they want to? What's the website? Where do people go?

Dr. Fei Fei Li (01:18:34):
Well, World Labs website is www.worldlabs.ai and you can find our research progress there. We have technical blogs. You can find Marble, the product there. You can sign in there. You can find our job posts link there. We're in San Francisco. We love to work with the world's best talents.

Lenny Rachitsky (01:19:02):
Amazing. Fei-Fei, thank you so much for being here.

Dr. Fei Fei Li (01:19:04):
Thank you, Lenny.

Lenny Rachitsky (01:19:06):
Bye everyone.

(01:19:09):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

